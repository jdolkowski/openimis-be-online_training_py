import logging
import warnings

from core.services import BaseService
from online_training.models import EncryptedMessage
from online_training.utils import encrypt

logger = logging.getLogger(__name__)

# implement base service for EncodedMessage

class EncryptedMessageService(BaseService):
    OBJECT_TYPE = EncryptedMessage

    def create(self, obj_data):
        message = obj_data.pop("encrypted_message")
        if message:
            encrypted_message = encrypt(message)
            obj_data["encrypted_message"] = encrypted_message
        return super().create(obj_data)