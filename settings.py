import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
#    DEBUG = True
	DEBUG = True # wieder löschen wenn Umgebungsvariable gesetzt					!!!!!!!!!!!!!!!

ADMIN_USERNAME = 'meyting_nok'
# for security, best to set admin password in an environment variable
# ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'nok' # wieder löschen wenn Umgebungsvariable gesetzt 			!!!!!!!!!!!!!!!

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME


# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

# AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
AUTH_LEVEL = 'STUDY' # wieder löschen wenn Umgebungsvariable gesetzt			!!!!!!!!!!!!!!!

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'de'

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = \
    [
    {
        'name': 'Organ_Donation_Game_Opt_Out',
        'display_name': "Next-of-kin o-o",
        'num_demo_participants': 12,
        'app_sequence': ['Instructions_Nokgame','Life'],
        'use_browser_bots' : False,
        'treatment': 'opt-out',
        'participation_fee': 5,
    },
    {
        'name': 'Organ_Donation_Game_Active_Choice',
        'display_name': "Next-of-kin a-c",
        'num_demo_participants': 12,
        'app_sequence': ['Instructions_Nokgame','Life'],
        'use_browser_bots' : False,
        'treatment': 'active-choice',
        'participation_fee': 5
    },
    ]

ROOMS = \
    [
    {
        'name': 'FLEX_room',
        'display_name': 'FLEX Laboratory',
        'participant_label_file': 'FLEX_room.txt',
        #'use_secure_urls': True,
    },
    ]

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '&)r_jm3fmd*myk4n#!p-cndswf&=0)9fj)wrif1&*a%o1nx6lp'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
