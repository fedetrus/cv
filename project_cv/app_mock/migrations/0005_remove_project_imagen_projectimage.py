# Generated by Django 4.2 on 2025-02-19 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mock', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='imagen',
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app_mock.project')),
            ],
        ),
    ]
