import base64
from django.db import models
from online_training.apps import OnlineTrainingConfig
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext as _

from core.models.history_model import HistoryModel


class EncryptedMessage(HistoryModel):
    encrypted_message = models.TextField()
