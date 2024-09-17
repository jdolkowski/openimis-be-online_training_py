

import graphene
from graphene_django import DjangoObjectType

from core import ExtendedConnection
from online_training.models import EncryptedMessage
from online_training.utils import decrypt


class EncryptedMessageGQLType(DjangoObjectType):
    decrypted_message = graphene.String()

    class Meta:
        model = EncryptedMessage
        filter_fields = {}
        interfaces = (graphene.relay.Node,)
        connection_class = ExtendedConnection


    def resolve_decrypted_message(self, info):
        return decrypt(self.encrypted_message)