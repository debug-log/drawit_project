# Generated by Django 2.1.5 on 2019-01-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogStage',
            fields=[
                ('stage_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('try_count', models.IntegerField(blank=True, default=0)),
                ('success_count', models.IntegerField(blank=True, default=0)),
                ('types', models.CharField(choices=[('success', 'success'), ('fail', 'fail')], default='fail', max_length=20)),
            ],
            options={
                'ordering': ('stage_id',),
            },
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
