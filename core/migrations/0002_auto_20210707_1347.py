# Generated by Django 3.2.4 on 2021-07-07 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewDish', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='dish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.viewdish'),
        ),
    ]
