import datetime
from misskey import Misskey

time_now = datetime.datetime.now()
time_str = time_now.strftime("%H:%M")
message = "---------------- "+time_str+" ----------------"

mk = Misskey("yourdomain.ltd", i="API_Key")
mk.notes_create(text=message, visibility='followers')
