# Generated by Django 5.0.3 on 2024-09-12 14:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=350)),
                ('date_created', models.DateTimeField()),
                ('real_estate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=350)),
                ('date_and_time', models.DateTimeField()),
                ('image', models.ImageField(upload_to='advertisements/')),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('F', 'Fixed price'), ('S', 'Accepts suggestions for price'), ('N', 'The price is not fixed')], max_length=1)),
                ('new', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement_app.category')),
            ],
        ),
    ]