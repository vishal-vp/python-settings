"""
Module init which exports the correct settings.

The settings file to be used must be specified in the environment variable 
SETTINGS_MODULE.
"""
import importlib
import os

SETTINGS_MODULE = os.environ['SETTINGS_MODULE']


class Settings:
    def __init__(self, settings_module):
        """Import settings file."""
        self.SETTINGS_MODULE = settings_module
        settings_module = importlib.import_module(SETTINGS_MODULE)
        # Parse settings.
        for setting in dir(settings_module):
            setting_value = getattr(settings_module, setting)
            setattr(self, setting, setting_value)

    def __getattr__(self, name):
        """Return the value of setting or None."""
        return getattr(self, name, None)

    def __setattr__(self, name, value):
        """Set the value of setting."""
        self.__dict__[name] = value


settings = Settings(SETTINGS_MODULE)
