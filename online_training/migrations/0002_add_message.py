# Generated by Django 4.2.16 on 2024-09-16 22:50
from django.db import migrations
import uuid

from datetime import datetime as py_datetime

def add_message_instance(apps, schema_editor):
    EncryptedMessage = apps.get_model('online_training', 'EncryptedMessage')
    user = apps.get_model('core', 'User').objects.get(username="Admin")

    encrypted_message_instance = EncryptedMessage(
        id=uuid.uuid4(),
        encrypted_message="IQ0TDQ0aFkMUUgtMBgBZQgtOCFUTDAEOQixSFQMFEAcWShIQDkUCHEYgFgsVDgcTAAECWEsxABkPUgsJFgAOABlHERhISw0TCh4ACAAYDhsnGRgJDxcRND0+fzI+PA==",
        user_created=user,
        user_updated=user,
        date_created=py_datetime.now(),
        date_updated=py_datetime.now()
    )

    encrypted_message_instance.save()


class Migration(migrations.Migration):
    dependencies = [
        ('online_training', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_message_instance),
    ]