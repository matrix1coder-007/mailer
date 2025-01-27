# Generated by Django 3.2.3 on 2021-05-20 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='name of the company', max_length=150)),
                ('bic', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='mailer.companymodel')),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(max_length=150)),
                ('total', models.DecimalField(decimal_places=9, max_digits=18)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='mailer.companymodel')),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='mailer.contactmodel')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
