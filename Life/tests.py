from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.round_number in Constants.start_rounds:
            if self.player.id_in_subsession in[1,2,3,4,5,6]:
                yield pages.Default, dict(decide = False)
            elif self.player.id_in_subsession in [7,8,9,10,11,12]:
                yield pages.Default, dict(decide= True)
#            if self.player.id_in_subsession in[1,2,3,4,5,6]:
#                yield pages.Decision, dict(is_donor='False')
            if self.player.id_in_subsession in [7,8,9]:
                yield pages.Decision, dict(is_donor= False)
            elif self.player.id_in_subsession in [10,11,12]:
                yield pages.Decision, dict(is_donor= True)
        if self.participant.vars['is_dead'] == False and self.player.asked == True:
            yield pages.Nok, dict(nok_decision = False)
        if self.participant.vars['is_dead'] == False:
            yield pages.Liferesults
        if self.subsession.round_number in Constants.finish_rounds:
            yield pages.End


