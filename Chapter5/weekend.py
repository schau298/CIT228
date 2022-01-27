import datetime
# weekdays tuple
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday")
# retrieving current date
now = datetime.date.today()
# retrieve the day of the week in integer
dayOfWeek=now.weekday()
# subscript into weekDays using dayOfWeek
today=weekDays[dayOfWeek]
# calculate and print days until weekend
daysToWeekend=6-dayOfWeek
print("There are ", daysToWeekend-1, " days until weekend")
# flag to only print 1 quote in for loop
quotePrinted="false"
# prints week days left until weekend with a quote
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today=="Sunday" and quotePrinted=="false":
        print(left, "Sunday is for relaxation!")
        quotePrinted="true"
    elif (today=="Monday" or today=="Tuesday" or today=="Wednesday") and quotePrinted=="false":
        print(left, "Another day, Another measley dollar")
        quotePrinted="true"
    elif today=="Thursday" and quotePrinted=="false":
        print(left, "Time to do school all day")
        quotePrinted=="true"
    elif quotePrinted=="false":
        print(left, "Yay the weekend is finally here!")
    else:
        print(left)