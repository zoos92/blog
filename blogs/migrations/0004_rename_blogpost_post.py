# Generated by Django 5.1.3 on 2024-11-22 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_postcomment_comment_alter_comment_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Post',
        ),
    ]
