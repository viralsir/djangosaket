# Generated by Django 3.2.9 on 2021-11-21 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival', to='airline.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='airline.airport'),
        ),
    ]