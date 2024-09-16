import base64
from online_training.apps import OnlineTrainingConfig
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext as _


def encrypt(message):
    key = get_key()
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key))
    return base64.b64encode(encrypted.encode()).decode()


def decrypt(encrypted_message):
    key = get_key()
    encrypted_message = base64.b64decode(encrypted_message).decode()
    decrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_message, key))
    return decrypted


def get_key():
    key = OnlineTrainingConfig.key
    if not key:
        raise ImproperlyConfigured(_("encryption_key_not_set_in_configuration"))
    return key.ljust(256)[:256]