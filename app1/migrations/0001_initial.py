# Generated by Django 3.1.7 on 2021-03-28 05:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('mobile_number', models.IntegerField()),
                ('age', models.IntegerField(max_length=3)),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'others')])),
                ('pincode', models.IntegerField(max_length=6)),
                ('country', models.CharField(max_length=50)),
                ('instragram_link', models.URLField(max_length=2000, null=True)),
                ('Facbook_link', models.URLField(max_length=2000, null=True)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_action', models.BooleanField()),
                ('m_drama', models.BooleanField()),
                ('m_romance', models.BooleanField()),
                ('m_comedy', models.BooleanField()),
                ('m_horror', models.BooleanField()),
                ('m_musical', models.BooleanField()),
                ('m_science_fiction', models.BooleanField()),
                ('m_documentary', models.BooleanField()),
                ('m_adventure', models.BooleanField()),
                ('m_thriller', models.BooleanField()),
                ('m_fiction', models.BooleanField()),
                ('m_fantasy', models.BooleanField()),
                ('m_animations', models.BooleanField()),
                ('b_action', models.BooleanField()),
                ('b_drama', models.BooleanField()),
                ('b_romance', models.BooleanField()),
                ('b_horror', models.BooleanField()),
                ('b_Sci_Fi', models.BooleanField()),
                ('b_informative', models.BooleanField()),
                ('b_adventure', models.BooleanField()),
                ('b_thriller', models.BooleanField()),
                ('b_fictional', models.BooleanField()),
                ('b_fantasy', models.BooleanField()),
                ('b_inspirational', models.BooleanField()),
                ('b_biographies', models.BooleanField()),
                ('mail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user_table', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'not_accepted'), (1, 'accepted'), (2, 'pending')], default=2)),
                ('match', models.IntegerField(max_length=3)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user_table', unique=True)),
            ],
        ),
    ]
