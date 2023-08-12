from posixpath import split
import re
regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"

user_input = input("Enter time: ")
validate_time = re.match(regex, user_input)
if validate_time or user_input == 'bye':
   if user_input !='bye':
       get_time = user_input.split(":")
       if int(get_time[0]) <12:
           print("good m.")
       elif int(get_time[0]) >=12 and int(get_time[0]) <24:
           print('good af.')
   else:
       print('goood b.')       
else:
    print(False)
# name = input ("Enter name: ")
# time = input ("Enter time: ")
# if time in "12:00, 1:00, 2:00, 3:00, 4:00, 5:00, 6:00, 7:00, 8:00, 9:00, 10:00, 11:00":
#     print("Good morning " + name)
# elif time in "13:00,14:00,15:00,16:00,17:00,18:00,19:00,20:00,21:00,22:00,23:00,24:00":
#     print("Good afternoon " + name)
# elif time == "bye":
#     print("Goodnight " + name)
# else:
#     print("wrong input")
    
    