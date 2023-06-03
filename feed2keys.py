#######################################
#
# feed2keys.py v1.0.0-1
# ActivityPub @kaori@cal.vino.blue
#
#######################################

import feedparser
import textwrap
import time
import re
from misskey import Misskey

#mk = Misskey("yourdomain.ltd", i="API_Key")
#d = feedparser.parse('https://www,domain.ltd/rss')
d = feedparser.parse('https://feed.mdpr.jp/rss/export/mdpr-entertainment.xml')
#print(d.keys())

for e in d['entries']:
   string = textwrap.dedent('''
   {update}
   【{titles}】
   {summaries}
   
   {links}
   ''').format(update=e['published'], titles=e['title'], summaries=e['summary'], links=e['link']).strip()
#   mk.notes_create(text=string, visibility='followers')
   print(string)
