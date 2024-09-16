import graphene
from graphene_django import DjangoObjectType

from core import ExtendedConnection


class EncryptedMessageGQLType(DjangoObjectType):
    class Meta:
        # interfaces = (graphene.relay.Node,): Implements the Relay Node interface, allowing the object type to use Relay’s global object identification system.
        # Relay Integration: Facilitates standardized fetching and querying of objects by ID, supporting features like pagination and global IDs.
        interfaces = (graphene.relay.Node,)
        connection_class = ExtendedConnection