# Generated by Django 4.0.2 on 2022-03-14 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_main_post_header_mainitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gabon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PCP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WPD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('header', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='main',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='main',
            name='header',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='WPDItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wpd_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.wpd')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='ThreatItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threat_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.threat')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='ResourceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.resource')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='PCPItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pcp_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pcp')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='PartnerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.partner')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='NewItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.new')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='MeetItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meet_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meet')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='HelpItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.help')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='GabonItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gabon_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.gabon')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='FundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fund_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fund')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='FAQItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.faq')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='ConservationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conservation_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.conservation')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ouraction_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.action')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.CreateModel(
            name='AboutItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_posts', to=settings.AUTH_USER_MODEL)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.about')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
    ]