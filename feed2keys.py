#######################################
#
# feed2keys.py v1.0.0
# ActivityPub @kaori@cal.vino.blue
#
#######################################

import feedparser
import textwrap
import time
from misskey import Misskey

#mk = Misskey("yourdomain.ltd", i="API_Key")
d = feedparser.parse('https://www,domain.ltd/rss')

for e in d['entries']:
   string = textwrap.dedent('''
   【{titles}】
   {summaries}
   
   {links}
   ''').format(titles=e['title'], summaries=e['summary'], links=e['link']).strip()
#   mk.notes_create(text=string, visibility='followers')
   print(string)