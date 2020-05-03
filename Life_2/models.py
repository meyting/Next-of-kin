from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy as np

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Life_2'
    players_per_group = 2
    num_rounds = 20
    a = 0.1
    b = 0.2
    p = 1
    l = 5
    r = 0.6
    startbudget_opt_out = 1.50
    startbudget_active_choice = 2
    thinking_cost = 50
    registration_cost = 50
    nok_yes = 30

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly(fixed_id_in_group=True)
        else:
            self.group_like_round(1)
        print(self.get_group_matrix())
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['is_dead'] = False
                if 'treatment' == 'opt-out' in self.session.config:
                    p.is_donor = True
                    p.participant.vars['is_donor'] = True
                if 'treatment' == 'active-choice' in self.session.config:
                    p.is_donor = None
                    p.participant.vars['is_donor'] = None
                p.treatment = self.session.config['treatment']

    available_organs_pre_alloc = models.IntegerField(initial=0)
    needed_organs_pre_alloc = models.IntegerField(initial=0)
    available_organs_post_alloc = models.IntegerField(initial=0)
    needed_organs_post_alloc = models.IntegerField(initial=0)
    deaths_in_subsession = models.IntegerField(initial=0)

    def collect_organs(self):
        players = self.get_players()
        available = [2 if p.is_dead == True and p.is_donor == True and p.got_organ == False and p.need_organ == False and p.periods_lived +1 == p.round_number else 0 for p in players]
        self.available_organs_pre_alloc = sum(available)
        self.available_organs_post_alloc = sum(available)
      #  print("WHILE COLLECTING - COLLECTED", self.available_organs_pre_alloc)

    def count_how_many_need_organs(self):
        players = self.get_players()
        needed = [1 if p.is_dead == False and p.need_organ == True else 0 for p in players]
        self.needed_organs_pre_alloc = sum(needed)
        self.needed_organs_post_alloc = sum(needed)
        #print("WHILE COLLECTING - NEEDED", self.needed_organs_pre_alloc)

    def count_deaths(self):
        players = self.get_players()
        deaths = [1 if p.is_dead == True else 0 for p in players]
        self.deaths_in_subsession = sum(deaths)

    def allocate_organs(self):
        players = self.get_players()
        for p in players:
            if self.available_organs_pre_alloc >= self.needed_organs_pre_alloc > 0:
                if p.need_organ == True and p.is_dead == False and p.got_organ == False:
                    p.got_organ = True
                    for player in p.in_rounds(p.round_number + 1, Constants.num_rounds):
                        player.got_organ = True
                    p.need_organ = False
                    p.in_round(p.round_number + 1).need_organ = False
                    p.periods_waiting = 0
                    self.available_organs_post_alloc -= 1
                    self.needed_organs_post_alloc -= 1
            waitlist = [p.periods_waiting for p in players]
            waitlist.sort(reverse=True)
           # print('WAITLIST', waitlist)
            for p in players:
                if 0 < self.available_organs_pre_alloc < self.needed_organs_pre_alloc:
                    if p.periods_waiting == waitlist[0] and p.need_organ == True and p.is_dead == False and p.got_organ == False:
                        p.got_organ = True
                        for player in p.in_rounds(p.round_number + 1, Constants.num_rounds):
                            player.got_organ = True
                        p.need_organ = False
                        p.in_round(p.round_number + 1).need_organ = False
                        p.periods_waiting = 0
                        self.available_organs_post_alloc -= 1
                        self.needed_organs_post_alloc -= 1
                del waitlist[0]
        #print("POST ALLOCATION", self.available_organs_post_alloc)
       # print("POST ALLOCATION", self.needed_organs_post_alloc)


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    payoff_period = models.FloatField(initial = 0)
    is_dead = models.BooleanField(initial=False)
    is_donor = models.BooleanField(choices=[[True, 'Organspender'], [False, 'Kein Organspender']])
    need_organ = models.BooleanField(initial = False)
    periods_lived = models.IntegerField(initial = 0)
    periods_waiting = models.IntegerField(initial = 0)
    got_organ = models.BooleanField(initial = False)
    died_of_A = models.BooleanField()
    died_of_B = models.BooleanField()
    asked = models.BooleanField()
    nok_decision = models.BooleanField(blank = True)
    treatment = models.StringField(widget=widgets.HiddenInput(), verbose_name='')
    decide = models.BooleanField()
    other = models.BooleanField(blank = True)

# Execute each period
    def death_from_A(self):
        self.payoff_period = 0
        A_failure_prop = random.random()
        if A_failure_prop > 1 - Constants.a and self.is_dead == False:
            self.is_dead = True
            self.participant.vars["is_dead"] = True
            for player in self.in_rounds(self.round_number+1,Constants.num_rounds):
                player.is_dead = True
            self.died_of_A = True
            self.need_organ = False
            self.payoff_period -= 1

    def death_from_B(self):
        if Constants.num_rounds+1 > self.periods_waiting >= Constants.l:
            self.is_dead = True
            self.participant.vars["is_dead"] = True
            for player in self.in_rounds(self.round_number+1,Constants.num_rounds):
                player.is_dead = True
            self.died_of_B = True
            self.need_organ = False
            self.periods_waiting = Constants.num_rounds
            self.payoff_period -= 1


    def organ_need(self):
        B_failure_prop = random.random()
        #print(B_failure_prop)
        if B_failure_prop > 1-Constants.b and self.is_dead == False and self.need_organ == False:
            self.need_organ = True

    def count_living_periods(self):
        if self.is_dead == False:
            self.periods_lived += 1
            for player in self.in_rounds(self.round_number+1,Constants.num_rounds):
                player.periods_lived += 1

    def count_waiting_periods(self):
        if self.is_dead == False and self.need_organ == True:
            self.periods_waiting += 1

    def reward_for_health(self):
        if self.need_organ == False and self.is_dead == False:
            self.payoff_period += 1

    def add_payoff(self):
        self.payoff = self.payoff + self.payoff_period

    def nok_asked(self):
        groupmember = self.get_others_in_group()
        if self.session.config['treatment'] == 'opt-out':
            asked = [g.is_dead and g.periods_lived+1 == g.round_number and g.is_donor == True for g in groupmember]
            self.asked = asked[0]
        if self.session.config['treatment'] == 'active-choice':
            asked = [g.is_dead and g.periods_lived+1 == g.round_number and g.is_donor == None for g in groupmember]
            self.asked = asked[0]

    def make_nok_decision(self):
        groupmember = self.get_others_in_group()
        for g in groupmember:
            if self.asked == True:
                g.is_donor = self.nok_decision
                for gm in g.in_rounds(self.round_number + 1, Constants.num_rounds):
                    gm.is_donor = self.nok_decision
                g.participant.vars['is_donor'] = self.nok_decision
                if self.session.config["treatment"] == "opt-out" and self.nok_decision == None:
                    g.is_donor = True
                    for gm in g.in_rounds(self.round_number + 1, Constants.num_rounds):
                        gm.is_donor = True
                    g.participant.vars['is_donor'] = True
                if self.session.config["treatment"] == "active-choice" and self.nok_decision == None:
                    g.is_donor = False
                    for gm in g.in_rounds(self.round_number + 1, Constants.num_rounds):
                        gm.is_donor = False
                    g.participant.vars['is_donor'] = False

    def decision_of_partner(self):
        groupmember = self.get_others_in_group()
        other = [g.is_donor for g in groupmember]
        self.other = other[0]