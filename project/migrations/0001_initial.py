# Generated by Django 3.0.5 on 2020-12-01 15:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('sub_title', models.TextField(blank=True, max_length=100, null=True)),
                ('body', models.TextField(blank=True, max_length=100, null=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 12, 1, 15, 40, 4, 744405, tzinfo=utc))),
                ('hit', models.PositiveIntegerField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 12, 1, 15, 40, 4, 745403, tzinfo=utc))),
                ('comment', models.CharField(max_length=300)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]