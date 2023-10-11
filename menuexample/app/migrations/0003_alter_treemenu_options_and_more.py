# Generated by Django 4.2 on 2023-05-29 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_insertdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treemenu',
            options={'verbose_name': 'Menu item', 'verbose_name_plural': 'Menu items'},
        ),
        migrations.AlterModelOptions(
            name='treemenucategory',
            options={'verbose_name': 'Menu category', 'verbose_name_plural': 'Menu categories'},
        ),
        migrations.AlterField(
            model_name='treemenu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.treemenucategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='treemenu',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='treemenu',
            name='parent',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.treemenu', verbose_name='Parent element'),
        ),
        migrations.AlterField(
            model_name='treemenu',
            name='path',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='treemenucategory',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='treemenucategory',
            name='verbose_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Verbose name'),
        ),
    ]