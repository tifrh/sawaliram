# Generated by Django 2.2.2 on 2019-07-23 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sawaliram_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert', models.BooleanField(default=False)),
                ('writer', models.BooleanField(default=False)),
                ('translator', models.BooleanField(default=False)),
                ('expert_application', models.TextField()),
                ('writer_application', models.TextField()),
                ('translator_application', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='volunteer_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'volunteer_request',
            },
        ),
    ]