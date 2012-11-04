###
# Copyright (c) 2012, xo
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import re

class GoodJobOpers(callbacks.Plugin):
    """LONG LIVE SABU GREATEST HACKER ALIVE"""

    oper_nick = "DaPrivateer"

    def doQuit(self, irc, msg):
        if ircmsgs.isSplit(msg):
            irc.reply("GOOD JOB OPERS!", prefixNick=False)
            if msg.nick == self.oper_nick:
                irc.queueMsg(ircmsgs.nick(self.oper_nick))

Class = GoodJobOpers


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
