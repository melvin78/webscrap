# Generated by Django 3.2 on 2021-12-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('idimage', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('subcateoryid', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'image',
                'managed': True,
            },
        ),
    ]
