# Generated by Django 3.0.4 on 2020-04-11 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.IntegerField(choices=[(1, 'CETAKAN'), (2, 'ATK'), (3, 'CONSUMABLE')])),
                ('nama', models.CharField(max_length=50)),
                ('jumlah', models.IntegerField()),
                ('satuan', models.IntegerField(choices=[(1, 'RIM'), (2, 'BLK'), (3, 'KBLK'), (4, 'BKS'), (5, 'BH'), (6, 'KTK'), (7, 'PAK'), (8, 'PS')])),
                ('harga', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SisaStok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockopname.Produk')),
            ],
        ),
        migrations.CreateModel(
            name='Permintaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('tgl', models.DateTimeField(auto_now_add=True)),
                ('produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockopname.Produk')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
