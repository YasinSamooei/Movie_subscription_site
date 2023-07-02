# Generated by Django 4.2.2 on 2023-06-30 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='آدرس ایمیل')),
                ('full_name', models.CharField(max_length=55, verbose_name='نام و نام خانوادگی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/users', verbose_name='تصویر')),
                ('gender', models.CharField(blank=True, choices=[('man', 'مرد'), ('woman', 'زن')], max_length=10, null=True, verbose_name='جنسیت')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('language', models.CharField(blank=True, choices=[('Persian', 'فارسی'), ('English', 'انگلیسی'), ('German', 'آلمانی')], max_length=10, null=True, verbose_name='زبان')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کارمند')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='ادمین')),
                ('Subscription_plan', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Subscription', to='accounts.subscription')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
            },
        ),
    ]