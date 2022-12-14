# Generated by Django 2.2.28 on 2022-11-05 03:52

from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.slugfield


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_auto_20200724_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', oscar.models.fields.slugfield.SlugField(max_length=255, verbose_name='Slug')),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners', to='partner.PartnerType'),
        ),
    ]
