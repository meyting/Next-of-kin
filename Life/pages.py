from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Default(Page):
    form_model = 'player'
    form_fields = ['decide']
    def vars_for_template(self):
        return {'treatment': self.session.config['treatment'],}

    def before_next_page(self):
        if self.session.config['treatment'] == 'opt-out':
            if self.player.decide == False:
                for player in self.player.in_rounds(self.round_number, Constants.num_rounds):
                    player.is_donor = True

    def is_displayed(self):
        return self.player.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['is_donor']
    def vars_for_template(self):
        return {'treatment': self.session.config['treatment'],
                'image_path1': 'img/yes.PNG',
                'image_path2': 'img/no.PNG',
                'yes_optout': '<input name="is_donor" type="radio" id="yes" value="True" checked=checked/>',
                'no_optout': '<input name="is_donor" type="radio" id="no" value="False"/>',
                'yes_activechoice': '<input name="is_donor" type="radio" id="yes" value="True"/>',
                'no_activechoice': '<input name="is_donor" type="radio" id="no" value="False"/>',
                }

    def is_displayed(self):
        return self.player.round_number == 1 and self.player.decide == True

    def before_next_page(self):
        for player in self.player.in_rounds(self.round_number, Constants.num_rounds):
            player.is_donor = self.player.is_donor



class Individual(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        for p in self.subsession.get_players():
            if p.round_number >= 2:
                p.is_dead = p.in_round(p.round_number - 1).is_dead
                p.is_donor = p.in_round(1).is_donor
                p.need_organ = p.in_round(p.round_number - 1).need_organ
                p.periods_lived = p.in_round(p.round_number - 1).periods_lived
                p.periods_waiting = p.in_round(p.round_number - 1).periods_waiting
                p.died_of_A = p.in_round(p.round_number - 1).died_of_A
                p.died_of_B = p.in_round(p.round_number - 1).died_of_B
                p.got_organ = p.in_round(p.round_number - 1).got_organ
            p.death_from_A()
            print('DEATH FROM A', p.is_dead, p.participant.id_in_session)
            p.organ_need()
        for p in self.subsession.get_players():
            p.nok_asked()
    def is_displayed(self):
        return self.participant.vars['is_dead'] == False

class Nok(Page):
    form_model = 'player'
    form_fields = ['nok_decision']
    def vars_for_template(self):
        return {'treatment': self.session.config['treatment'],
                'image_path1': 'img/nokyes.PNG',
                'image_path2': 'img/nokno.PNG',
                'nokyes_optout': '<input name="nok_decision" type="radio" id="yes" value="True" checked=checked/>',
                'nokno_optout': '<input name="nok_decision" type="radio" id="no" value="False"/>',
                'nokyes_activechoice': '<input name="nok_decision" type="radio" id="yes" value="True"/>',
                'nokno_activechoice': '<input name="nok_decision" type="radio" id="no" value="False"/>',
                }

    def before_next_page(self):
        self.player.make_nok_decision()

    def is_displayed(self):
        return self.player.asked == True

class Allocate(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.collect_organs()
        print(self.subsession.available_organs_pre_alloc)
        self.subsession.count_how_many_need_organs()
        self.subsession.allocate_organs()
        for p in self.subsession.get_players():
            p.count_waiting_periods()
            print('WAITING PERIODS', p.periods_waiting, p.participant.id_in_session)
            p.death_from_B()
            print('DEATH FROM B', p.is_dead, p.participant.id_in_session)
            p.count_living_periods()
            print('LIVING PERIODS', p.periods_lived, p.participant.id_in_session)
            p.reward_for_health()
            p.add_payoff()
        self.subsession.count_deaths()
    def is_displayed(self):
            return self.participant.vars['is_dead'] == False

class Liferesults(Page):
    def is_displayed(self):
        return self.participant.vars['is_dead'] == False

    def vars_for_template(self):
        if self.player.round_number > 1:
            return {'needed_organ_last_period': self.player.in_round(self.player.round_number-1).need_organ,
                }

'''
class Post_allocation(WaitPage):
    def vars_for_template(self):


    def is_displayed(self):
        return self.player.round_number == self.player.periods_lived+1

class Liferesults(Page):
    def vars_for_template(self):

    def is_displayed(self):
        return self.participant.vars['is_dead'] == False

class Wait(WaitPage):
    def after_all_players_arrive(self):
        self.subsession.count_deaths()

    def is_displayed(self):
        return self.participant.vars['is_dead'] == False
'''
class End(WaitPage):
    wait_for_all_groups = True
    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if self.participant.vars['is_dead']:
            return "Finish"
    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

page_sequence = [
    Default,
    Decision,
    Individual,
    Nok,
    Allocate,
    Liferesults,
    End,
#    Allocation,
#    Post_allocation,
#    Liferesults,
#    Wait,
#    End,
]

# In models die variablen ab jetzt für bis ende bestimmen und dann immer überschreiben lassen
# auf einer seite: erst tod von a? need? collect! allocate! tod von b? update living, update waiting, update payoff
# nächste seite: ergebnisse leben oder ergebnisse tod (und dann warteseite für nächste runde)
# ...