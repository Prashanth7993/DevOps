# import datetime
# dir(datetime)


from datetime import datetime
import pytz
# now = datetime.now()
        #"Or"
# now = datetime(2026,10,1)
# now.strftime("%m/%d/%Y") #Chaning format of datetime.
now = datetime.now(pytz.timezone('Asia/Tokyo'))
day = now.day
month = now.month
year = now.year
hr = now.hour
mn = now.minute
sc = now.second
# print("Day:"day,+"Month:"month,"Year:"year,"hour:"hr,"min:"mn,sc)
print(f'Day={day}/Month={month}/Year={year}/hour={hr}/Minute={mn}/Second={sc}')