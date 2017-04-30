Schedule Keeper
===============

Sends emails at regular times to keep you on track with your schedules.

Sample config file
------------------

```
name          : 'Cryptopals'
username      : 'Robert'
email         : 'me@here.com'
start_date    : datetime.date(2017, 04, 27)
end_date      : datetime.date(2017, 06, 1)
num_reminders : 10
get_progress  : lambda x: "challenge {}".format(x + 21)
```
