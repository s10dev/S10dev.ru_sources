# Generated by Django 3.1.7 on 2021-03-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, help_text='Текст комменатрия', max_length=100, null=True),
        ),
    ]
