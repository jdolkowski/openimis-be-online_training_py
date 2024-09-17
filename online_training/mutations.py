import graphene

from core.gql.gql_mutations.base_mutation import BaseMutation, BaseHistoryModelCreateMutationMixin
from core.schema import OpenIMISMutation
from online_training.gql_queries import EncryptedMessageGQLType


class CreateEncryptedMessageInputType(OpenIMISMutation.Input):
    encrypted_message = graphene.String(required=True)

class CreateEncryptedMessageMutation(BaseHistoryModelCreateMutationMixin, BaseMutation):
    _mutation_class = "CreateEncryptedMessageMutation"
    _mutation_module = "online_training"
    _model=EncryptedMessageGQLType
    # should already work because of BaseHistoryModelCreateMutationMixin but it will save a plain text
    # think on how to modify it so it will save encrypted messages