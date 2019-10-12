from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.round_number == 1:
            if self.player.id_in_group in[1,2,3,4,5,6]:
                yield pages.Period1, dict(is_donor='True')
                yield pages.Period2
                yield pages.Period3
                yield pages.Period4
                yield pages.Period5
                yield pages.Period6
                yield pages.Period7
                yield pages.Period8
                yield pages.Period9
                yield pages.Period10
                yield pages.Period11
                yield pages.Period12
                yield pages.Period13
                yield pages.Period14
                yield pages.Period15
                yield pages.Period16
                yield pages.Period17
                yield pages.Period18
                yield pages.Period19
                yield pages.Period20

            if self.player.id_in_group in[7,8,9,10,11,12]:
                yield pages.Period1, dict(is_donor='False')
                yield pages.Period2
                yield pages.Period3
                yield pages.Period4
                yield pages.Period5
                yield pages.Period6
                yield pages.Period7
                yield pages.Period8
                yield pages.Period9
                yield pages.Period10
                yield pages.Period11
                yield pages.Period12
                yield pages.Period13
                yield pages.Period14
                yield pages.Period15
                yield pages.Period16
                yield pages.Period17
                yield pages.Period18
                yield pages.Period19
                yield pages.Period20


