# Generated by Django 3.1.1 on 2020-10-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0015_remove_order_handicrafts'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='handicrafts',
            field=models.ManyToManyField(to='gallery.OrderArt'),
        ),
    ]
