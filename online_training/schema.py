import graphene
import graphene_django_optimizer as gql_optimizer

from core.schema import signal_mutation_module_validate
from online_training.apps import MODULE_NAME


# class Query(graphene.ObjectType):
#     encrypted_message =
#
#
#     def resolve_
#         return gql_optimizer.query()
#
#
# class Mutation(graphene.ObjectType):
#     create_encrypted_message =


# reminder that we could use signals, but we are not using them during the practice
# def bind_signals():
#     signal_mutation_module_validate[MODULE_NAME].connect(define_what_should_happen_on_mutation_validation)