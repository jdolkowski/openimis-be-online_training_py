import graphene

from core.gql.gql_mutations.base_mutation import BaseMutation, BaseHistoryModelCreateMutationMixin
from core.schema import OpenIMISMutation
from online_training.gql_queries import EncryptedMessageGQLType
from online_training.services import EncryptedMessageService


class CreateEncryptedMessageInputType(OpenIMISMutation.Input):
    encrypted_message = graphene.String(required=True)

class CreateEncryptedMessageMutation(BaseHistoryModelCreateMutationMixin, BaseMutation):
    _mutation_class = "CreateEncryptedMessageMutation"
    _mutation_module = "online_training"
    _model=EncryptedMessageGQLType

    @classmethod
    def _mutate(cls, user, **data):
        if "client_mutation_id" in data:
            data.pop('client_mutation_id')
        if "client_mutation_label" in data:
            data.pop('client_mutation_label')

        service = EncryptedMessageService(user)
        service.create(data)

    class Input(CreateEncryptedMessageInputType):
        pass