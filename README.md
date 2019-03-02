# python-settings
Django like settings management for any python application.

Allows you to have multiple settings for different environments like development, staging and production. You can have multiple settings file in the conf folder and during runtime you choose the settings file to use by settings the environment variable SETTINGS_MODULE to whichever settings file you prefer.

## Install
1. Download the conf folder and place it in the source code directory.
2. Set the SETTINGS_MODULE environment variable to the setting you want to use.
   `export SETTINGS_MODULE="conf.develop"
3. Then from the main module you can import the settings.
   `from conf import settings`
