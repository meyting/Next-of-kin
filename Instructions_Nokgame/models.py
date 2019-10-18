from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Instructions_Nokgame'
    players_per_group = None
    num_rounds = 1
    gamerounds = 30
    gamerounds_part = int(gamerounds/2)
    number_payout_gamerounds = 4
    startbudget_opt_out = 1.50
    startbudget_active_choice = 2
    thinking_cost = 50
    registration_cost = 50
    nok_yes = 30

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
