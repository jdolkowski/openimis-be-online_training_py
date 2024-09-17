import graphene
from graphene_django import DjangoObjectType

from core import ExtendedConnection


class EncryptedMessageGQLType(DjangoObjectType):
    class Meta:
        # something missing here
        interfaces = (graphene.relay.Node,)
        connection_class = ExtendedConnection