from django.apps import AppConfig

MODULE_NAME = "online_training"

DEFAULT_CFG = {
    "key": "very-secure-key-mniuwerfberfkjekrjfbwekrfbwerbfwerjgkbewkrjgewkrjgewrkgwerkgwkergjwekrgQQQQQQQQQQQQ",
}

class OnlineTrainingConfig(AppConfig):
    name = MODULE_NAME

    key = None

    def __load_config(self, cfg):
        for field in cfg:
            if hasattr(OnlineTrainingConfig, field):
                setattr(OnlineTrainingConfig, field, cfg[field])

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CFG)
        self.__load_config(cfg)