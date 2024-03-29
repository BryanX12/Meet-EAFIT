# Generated by Django 4.1.6 on 2023-03-23 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='social.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='social.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
