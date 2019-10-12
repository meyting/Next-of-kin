from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Period1(Page):
    form_model = 'player'
    form_fields = ['is_donor']

    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period2(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period3(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period4(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period5(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period6(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period7(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period8(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period9(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period10(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period11(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period12(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period13(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period14(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period15(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period16(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period17(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period18(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period19(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Period20(Page):
    def is_displayed(self):
        if self.group.deaths_in_group < 12:
            return True

    def before_next_page(self):
        self.group.collect_organs()
        self.group.count_how_many_need_organs()
        self.player.death()
        self.player.organ_need()
        self.player.get_organs()
        self.player.count_living_periods()
        self.player.reward_for_health()
        self.player.add_payoffs()

class Wait(WaitPage):
    pass

page_sequence = [
    Period1,
    Wait,
    Period2,
    Wait,
    Period3,
    Wait,
    Period4,
    Wait,
    Period5,
    Wait,
    Period6,
    Wait,
    Period7,
    Wait,
    Period8,
    Wait,
    Period9,
    Wait,
    Period10,
    Wait,
    Period11,
    Wait,
    Period12,
    Wait,
    Period13,
    Wait,
    Period14,
    Wait,
    Period15,
    Wait,
    Period16,
    Wait,
    Period17,
    Wait,
    Period18,
    Wait,
    Period19,
    Wait,
    Period20,
    Wait,
]
