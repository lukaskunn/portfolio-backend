# Generated by Django 4.2.4 on 2023-09-01 01:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lang_code', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sect_title', models.CharField(max_length=100)),
                ('content', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='landing', to='content.content')),
            ],
        ),
        migrations.CreateModel(
            name='SectSubtitle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=50)),
                ('test', models.CharField(max_length=50)),
                ('landing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sect_subtitle', to='content.landing')),
            ],
        ),
    ]
