from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['is_donor']

    def is_displayed(self):
        return self.player.round_number == 1


class Life(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def vars_for_template(self):
        if self.player.round_number >= 2:
            self.player.is_donor = self.player.in_round(self.round_number - 1).is_donor
            self.player.is_dead = self.player.in_round(self.round_number - 1).is_dead
            self.player.need_organ = self.player.in_round(self.round_number - 1).need_organ
            self.player.periods_lived = self.player.in_round(self.round_number - 1).periods_lived
            self.player.periods_waiting = self.player.in_round(self.round_number - 1).periods_waiting
            self.player.got_organ = self.player.in_round(self.round_number - 1).got_organ
            self.player.died_of_A = self.player.in_round(self.round_number - 1).died_of_A
            self.player.died_of_B = self.player.in_round(self.round_number - 1).died_of_B

    def before_next_page(self):
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class End(Page):
    def is_displayed(self):
        return self.group.deaths_in_group == 12

class Wait(WaitPage):
    def after_all_players_arrive(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()

    def is_displayed(self):
        return self.group.deaths_in_group < 12

page_sequence = [
    Decision,
    Wait,
    Life,
    Wait,
    End,
]
