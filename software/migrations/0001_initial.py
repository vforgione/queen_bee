# Generated by Django 2.1.7 on 2019-02-28 14:18

from django.db import migrations, models
import software.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('version', models.TextField()),
                ('type', models.TextField(choices=[('image', 'image'), ('firmware', 'firmware'), ('driver', 'driver'), ('plugin', 'plugin')])),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('source_url', models.TextField(blank=True, default=None, null=True)),
                ('docs_url', models.TextField(blank=True, default=None, null=True)),
                ('source_tarball', models.FileField(blank=True, default=None, null=True, upload_to=software.models.software_upload_path)),
            ],
            options={
                'verbose_name_plural': 'Software',
                'db_table': 'software',
                'ordering': ('name', '-version'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='software',
            unique_together={('name', 'version')},
        ),
    ]
