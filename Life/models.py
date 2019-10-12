from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Life'
    players_per_group = 12
    num_rounds = 1
    a = 0.1
    b = 0.2
    p = 1
    l = 5
    r = 0.6

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly(fixed_id_in_group=True)
        else:
            self.group_like_round(1)
        print(self.get_group_matrix())

class Group(BaseGroup):
    available_organs = models.IntegerField(initial=0)
    needed_organs = models.IntegerField(initial=0)
    deaths_in_group = models.IntegerField(initial=0)

# Execute each period
    def collect_organs(self):
        self.available_organs = 0
        for p in self.get_players():
            if p.is_dead == True and p.is_donor == True and p.got_organ == False and p.need_organ == False:
                self.available_organs += 2

    def count_how_many_need_organs(self):
        for p in self.get_players():
            if p.is_dead == False and p.need_organ == True and p.got_organ == False:
                self.needed_organs += 1

    def count_deaths(self):
        for p in self.get_players():
            if p.is_dead == True:
                self.deaths_in_group += 1



class Player(BasePlayer):
'''
for i in range(1, 50):
    Player.add_to_class("payoff_period_{}".format(i),
                        models.FloatField(initial=0))
    Player.add_to_class("is_donor_{}".format(i),
                        models.BooleanField(initial=False))
    Player.add_to_class("is_dead_{}".format(i),
                        models.BooleanField(initial=False))
    Player.add_to_class("need_organ_{}".format(i),
                        models.BooleanField(initial=False))
    Player.add_to_class("periods_lived_{}".format(i),
                        models.IntegerField(initial=0))
    Player.add_to_class("periods_waiting_{}".format(i),
                        models.IntegerField(initial=0))
    Player.add_to_class("got_organ_{}".format(i),
                        models.BooleanField(initial=False))
'''

    payoff_period = models.FloatField(initial = 0)
    is_donor = models.BooleanField(initial = False)
    is_dead = models.BooleanField(initial = False)
    need_organ = models.BooleanField(initial = False)
    periods_lived = models.IntegerField(initial = 0)
    periods_waiting = models.IntegerField(initial = 0)
    got_organ = models.BooleanField(initial = False)
    died_of_A = models.BooleanField()
    died_of_B = models.BooleanField()

# Execute each period
    def death(self):
        self.payoff_period = 0
        A_failure_prop = random.random()
        if A_failure_prop > 1 - Constants.a and self.is_dead == False:
            self.is_dead = True
            self.died_of_A = True
            self.need_organ = False
            self.payoff_period -= 1
        if self.need_organ == True:
            self.periods_waiting += 1
        if 100 > self.periods_waiting > Constants.l + 1 :
            self.is_dead = True
            self.died_of_B = True
            self.need_organ = False
            self.periods_waiting = 100
            self.payoff_period -= 1

    def organ_need(self):
        B_failure_prop = random.random()
        if B_failure_prop > 1-Constants.b and self.is_dead == False and self.need_organ == False:
            self.need_organ = True

    def get_organs(self):
        for k in range(0,Constants.l+1):
            if self.periods_waiting == 5-k:
                if self.need_organ == True and self.is_dead == False and self.group.available_organs > 0 and self.group.needed_organs <= self.group.available_organs:
                    self.got_organ = False
                    self.need_organ = False
                    self.group.available_organs -= 1
                    self.group.needed_organs =- 1

    def count_living_periods(self):
        if self.is_dead == False:
            self.periods_lived += 1

    def reward_for_health(self):
        if self.need_organ == False and self.is_dead == False:
            self.payoff_period += 1

    def add_payoffs(self):
        self.payoff = self.payoff + self.payoff_period


