# Generated by Django 4.1.7 on 2023-04-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('number_guests', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('10:00', '10:00 AM'), ('11:00', '11:00 AM'), ('12:00', '12:00 PM'), ('13:00', '01:00 PM'), ('14:00', '02:00 PM'), ('15:00', '03:00 PM'), ('16:00', '04:00 PM'), ('17:00', '05:00 PM'), ('18:00', '06:00 PM'), ('19:00', '07:00 PM')], max_length=15)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.TextField(max_length=240)),
                ('price', models.IntegerField()),
                ('available', models.CharField(choices=[('avaible', 'Disponoble'), ('not avaible', 'No disponible')], max_length=15)),
                ('veggie_option', models.CharField(choices=[('avaible', 'Disponoble'), ('not avaible', 'No disponible')], max_length=15)),
                ('image', models.ImageField(blank=True, default='image', null=True, upload_to='product/')),
            ],
        ),
        migrations.CreateModel(
            name='Promo_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.TextField(max_length=240)),
                ('price', models.IntegerField()),
                ('available', models.CharField(choices=[('avaible', 'Disponoble'), ('not avaible', 'No disponible')], max_length=15)),
                ('veggie_option', models.CharField(choices=[('avaible', 'Disponoble'), ('not avaible', 'No disponible')], max_length=15)),
                ('image', models.ImageField(blank=True, default='image', null=True, upload_to='promo/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('job', models.CharField(max_length=40)),
                ('workshift', models.CharField(choices=[('morning', 'Mañana'), ('evening', 'Tarde')], max_length=15)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='image', null=True, upload_to='staff/')),
            ],
        ),
    ]
