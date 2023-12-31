# Generated by Django 4.2.4 on 2023-09-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(db_column='store type -> google, apple', max_length=50)),
                ('product_id', models.TextField(db_column='ID issued by provider')),
                ('purchase_id', models.TextField(db_column='ID issued by the store(google, apple)')),
                ('localverificationdata', models.TextField()),
                ('serververificationdata', models.TextField()),
                ('purchace_date', models.DateTimeField(auto_now_add=True)),
                ('purchace_price', models.CharField(max_length=50)),
            ],
        ),
    ]
