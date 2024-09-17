import graphene
import graphene_django_optimizer as gql_optimizer

from core.schema import signal_mutation_module_validate, OrderedDjangoFilterConnectionField
from online_training.apps import MODULE_NAME
from online_training.gql_queries import EncryptedMessageGQLType
from online_training.models import EncryptedMessage
from online_training.mutations import CreateEncryptedMessageMutation


class Query(graphene.ObjectType):
    encrypted_message = OrderedDjangoFilterConnectionField(
        EncryptedMessageGQLType,
        orderBy=graphene.List(of_type=graphene.String)
    )

    def resolve_encrypted_messages(self, info):
        query = EncryptedMessage.objects.all()
        return gql_optimizer.query(query, info)


class Mutation(graphene.ObjectType):
    create_encrypted_message = CreateEncryptedMessageMutation.Field()


# reminder that we could use signals, but we are not using them during the practice
# def bind_signals():
#     signal_mutation_module_validate[MODULE_NAME].connect(define_what_should_happen_on_mutation_validation)