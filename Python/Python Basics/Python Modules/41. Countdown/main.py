import datetime, bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2024, 10, 25)

days_away = next_birthday - today

if today == next_birthday:
   print(bday_messages.random_message)
else:
   print(f'My next birthday is {days_away.days} days away!')