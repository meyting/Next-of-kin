from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions1(Page):
    pass

class Instructions2(Page):
    def vars_for_template(self):
        return {'treatment': self.session.config['treatment'],}

class Instructions3(Page):
    pass

class Instructions4(Page):
    def vars_for_template(self):
        return {'treatment': self.session.config['treatment'],}

class Instructions5(Page):
    def vars_for_template(self):
        return {'treatment': self.session.config['treatment'],}

page_sequence = [
    Instructions1,
    Instructions2,
    Instructions3,
    Instructions4,
    Instructions5,
]
