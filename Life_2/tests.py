from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.round_number == 1:
            if self.player.id_in_subsession in[1,2,3,4,5,6]:
                yield pages.Decision, dict(is_donor='False')
            if self.player.id_in_subsession in [7, 8, 9, 10, 11, 12]:
                yield pages.Decision, dict(is_donor='True')
        if self.participant.vars['is_dead'] == False and self.is_asked == True:
            yield pages.Liferesults, dict(nok_decision ='False')
        if self.participant.vars['is_dead']:
            yield pages.Liferesults


