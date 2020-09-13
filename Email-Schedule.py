import smtplib
import sys
from datetime import date, timedelta, datetime
import calendar
import random

i = 0
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
today = date.today()
my_date = date.today()
DayOfWeek = calendar.day_name[my_date.weekday()]
To = "alex.diker@email.com"
From = "alex.diker@email.com"
# smtpserver = smtplib.SMTP("SMTP.GMAIL.COM", 500)
OnCallList = {'User1': ['User1.User@email.com'],
              'User2': ['User1.User@email.com'],
              'User3': ['User1.User@email.com'],
              'User4': ['User1.User@email.com'],
              'User5': ['User1.User@email.com'],
              'User6': ['User1.User@email.com']}

OCL = ['User1', 'User2', 'User3', 'User4', 'User5', 'User6']

ListOfUsers = random.sample(OCL, len(OCL))


def allmondays(month):
    d = date(year, month, day)
    d += timedelta(days=0 - d.weekday())
    while d.month == month:
        yield d
        d += timedelta(days=7)


for d in allmondays(month):
    d2 = (d + timedelta(6))
    i += 1
    print(ListOfUsers[i] + " " + str(d) + " - " + str(d2))


def read_schedule(x):
    global email
    username = getpass.getuser()
    e = "C;\User." + username + "/Desktop/" + "call.csv"
    csvfiler = open(e, 'r')
    csvFileArray = []
    for row in csv.reader(csvfiler):
        csvFileArray.append(row)
    person = csvFileArray[0][0]
    if name in OnCallList:
        email = OnCallList.get(name)
        print(email)

# def send_email():
#    smtpserver.ehlo()
#    smtpserver.starttls()
#    smtpserver.ehlo()
#    header = 'To: ' + To + '\n' + 'From: ' + From + '\n' + 'Subject: ' + ListOfUsers[0] + ' is on call this week \n'
#    print(header)
#    msg = header + '\n This list rotates every monday morning. \n' + \
#          '\n An Email is generated every monday morning. Script last ran at ' + \
#          today.strftime("%d/%m/%y") + '\n\n' + ListOfUsers[0] + '\n' + ListOfUsers[1] + \
#          '\n' + ListOfUsers[2] + '\n' + ListOfUsers[3] + '\n' + ListOfUsers[4]
#    smtpserver.sendmail(From, To, msg)
#    print('done!')
#    smtpserver.close()


# send_email()