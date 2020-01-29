# Generated by Django 3.0 on 2019-12-13 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_auto_20191213_0643'),
        ('deck', '0006_deck_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='cards',
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.Deck')),
            ],
        ),
        migrations.AddField(
            model_name='deck',
            name='card',
            field=models.ManyToManyField(through='deck.Membership', to='card.Card'),
        ),
    ]