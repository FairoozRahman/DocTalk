# Generated by Django 3.2.9 on 2021-12-20 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('feet', models.CharField(blank=True, max_length=5, null=True)),
                ('inch', models.CharField(blank=True, max_length=5, null=True)),
                ('weight', models.CharField(blank=True, max_length=5, null=True)),
                ('dob', models.DateTimeField()),
                ('asthma', models.BooleanField()),
                ('is_diabetic', models.BooleanField(default=False)),
                ('bs_before', models.CharField(blank=True, max_length=5, null=True)),
                ('bs_after', models.CharField(blank=True, max_length=5, null=True)),
                ('systole', models.CharField(blank=True, max_length=5, null=True)),
                ('diastole', models.CharField(blank=True, max_length=5, null=True)),
                ('patient_image', models.ImageField(blank=True, default='patients/patient-default.png', null=True, upload_to='patients/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('allergic', models.ManyToManyField(blank=True, to='Profile.Allergies')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('c_address', models.TextField(blank=True, max_length=1024, null=True)),
                ('reg_num', models.CharField(blank=True, max_length=10, null=True)),
                ('bkash_no', models.CharField(blank=True, max_length=11, null=True)),
                ('fees_new', models.IntegerField(blank=True, null=True)),
                ('fees_old', models.IntegerField(blank=True, null=True)),
                ('fees_report', models.IntegerField(blank=True, null=True)),
                ('doc_image', models.ImageField(blank=True, default='doctors/doctor-default.jpg', null=True, upload_to='doctors/')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('specializations', models.ManyToManyField(to='Profile.Specialization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=500)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.doctor')),
            ],
        ),
    ]
