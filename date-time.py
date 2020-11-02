# Youtube author: Corey Schafer Python Tutorial
# Datetime Module - How to work with Dates, Times, Timedeltas and Timezones (tz)

import datetime
# Naive dates/times - less informative (lacks information about timezone (tz))
# Aware dates/times - higher level of detail to avoid confusion
# datetime.date - working with year / months / days
d = datetime.date(2016, 7, 24)  # (pass with no leading zero)
today = datetime.date.today()   # datetime.date(2020, 11, 02)
print(today.day)                # 2
print(datetime.datetime.now())  # 2020-11-02 18:37:23.362332
print(today.weekday())     # Monday is 0 / Sunday is 6 (Indexing starts from 0)
print(today.isoweekday())  # Monday is 1 / Sunday is 7
tdelta = datetime.timedelta(days=7)  # Create timedelta (Diff) object
print(today + tdelta)      # 2020-11-09
print(today - tdelta)      # 2020-10-26
christmas = datetime.date(2020, 12, 24)
till_christmas = christmas - today
print(till_christmas.days)             # 52
print(till_christmas.total_seconds())  # 4492800.0

# datetime.time - working with hours / minutes / sec / microsec (naive)
t = datetime.time(9, 30, 45, 1000)
print(t.hour)       # 9
# datetime.datetime - includes (date + time)
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)           # 2016-07-26 12:30:45.100000
print(dt.date())    # 2016-07-26
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)  # 2016-07-27 00:30:45.100000
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)     # 2020-11-02 22:17:28.373760 # timezone (tz) = None
print(dt_now)       # 2020-11-02 22:17:28.373762 # timezone as an option
print(dt_utcnow)    # 2020-11-02 20:17:28.373764 # current UTC time (TZ = None)

# create a timezone aware datetime using UTC (use: tzinfo=pytz.UTC)
import pytz  # pytz library is recommended to use by docs.python.org
# It is recommended to always work with UTC when dealing with timezones (tz)
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)           # 2020-11-02 19:13:59+00:00  # "+00:00" - offset
dt_now = datetime.datetime.now
print(dt_now)  # 2020-11-02 19:23:53.982032
dt_now = datetime.datetime.now(tz=pytz.UTC)  # make aware / UTC timezone
# 2020-11-02 17:24:57.250772+00:00
dt_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)  # same as prev
# Convert timezone of dt_utcnow
dt_local = dt_utcnow.astimezone(pytz.timezone('Europe/Copenhagen'))
print(dt_local)
# Print all available TimeZones in pytz:
# for tz in pytz.all_timezones:
#     print(tz)

# Convert naive to aware and set Copenhagen timezone:
dt_local = datetime.datetime.now()
print(dt_local)                 # 2020-11-02 17:54:04.199754
dt_copenhagen = dt_local.astimezone(pytz.timezone('Europe/Copenhagen'))
print(dt_copenhagen)            # 2020-11-02 16:54:04.199754+01:00

# Get current aware datetime and set timezone to Copenhagen:
dt_copen = datetime.datetime.now(tz=pytz.timezone('Europe/Copenhagen'))
# Use ISO format to display the datetimes, save, and parse them around
print(dt_copen.isoformat())     # 2020-11-02T17:59:11 # ISO Format
print(dt_copen.strftime('%B %d, %Y'))  # November 02, 2020 # string from time
# to use datetime operations, string should be converted first to datetime obj
dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)                       # 2016-07-26 00:00:00
# strftime - Datetime to string
# strptime - String to Datetime object


############################################################################
# Youtube: Kyle Monson
# Python Dateutil Library - Feb 8, 2019
# creating datetime object from strings without setting format
from dateutil import parser, relativedelta, rrule
# * relativedelta: Handling of "calendar" offsets
# * rrule: Generation of RFC(2445) recurrence relations
# * tz: Time zone Handling
# * parser: Parsing arbitrary datetimes
# better recognition of date strings compare to builtin datetime module
# downside is - dateutil.parser is 30 times slower then builtin datetime.strptime
print(parser.parse("2012-01-19 17:21:00")) # 2012-01-19 17:21:00
print(parser.parse("19-01-12 17:21:00", dayfirst=True)) # 2012-01-19 17:21:00
print(parser.parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)) # 2047-01-01 08:21:00
print(parser.parse("Sunday May 17 8:12:34 PM")) # 2021-05-17 20:12:34
# reccurence rule (create datetime objects at whatever recurrence specified)
start_date = datetime.datetime(2014, 12, 31)
list(rrule.rrule(freq=rrule.MONTHLY, count=4, dtstart=start_date))
list(rrule.rrule(freq=rrule.MONTHLY, count=4, dtstart=start_date))
# datetime.datetime(2014, 12, 31, 0, 0),
#  datetime.datetime(2015, 1, 31, 0, 0),
#  datetime.datetime(2015, 3, 31, 0, 0),
#  datetime.datetime(2015, 5, 31, 0, 0)
# 2,4 months skipped as those doesn't have 31st day, that's how rrule handles edge cases
list(rrule.rrule(freq=rrule.MONTHLY, count=4, dtstart=start_date, interval=2))
#  datetime.datetime(2014, 12, 25, 0, 0),
#  datetime.datetime(2015, 2, 25, 0, 0),
#  datetime.datetime(2015, 4, 25, 0, 0),
#  datetime.datetime(2015, 6, 25, 0, 0)
# Same as above but every 2 months
# pprint(list(rrule.rrule(rrule.YEARLY, bymonth=1, byweekday=range(7), dtstart=parser.parse("19980101T090000"), until=parser.parse("20000131T090000"))))
# (3 year of recurrence of days in January (every day in January from 1999 to 2001)) 

rset = rrule.rruleset()  # enables to combine multiple recurrence rules and put them together
# Get the previous month:
a = datetime.datetime(1997, 2, 1)
print(a.replace(month=a.month-1))  # datetime.datetime(1997, 1, 1, 0, 0)
rd = relativedelta.relativedelta
a - rd(months=1)  # datetime.datetime(1997, 1, 1, 0, 0)
