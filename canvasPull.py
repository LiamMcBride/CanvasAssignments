from canvasapi import Canvas
import newCanvasAPIFunctions as duedate
import datetime
import csv

#Ok so this reads the time in 'z' or zulu time aka UTC time. So if something is due at 11:59 my time, it is 04:59 the next day
#according to zulu time. So I need to detect the computers time zone, and work out a function that converts the time AND date to 
#the correct one. Because it doesn't just change the time it will push it forward a day, that's why all my design things are labelled
#as due a day early.

def DMY(time):
    day = time[-2:]
    month = time[5:7]
    year = time[:4]
    return(int(month), int(day), int(year))

def TodayValue(year, month, day):
    test = str(year)
    temp = test[2:] + str(month) + str(day)
        
    temp = int(temp)
    
        
    return temp

def sortDate(assignments):

    temp = []
    final = []
    useMe = []
    # try looking for lowest year and lowest month then comparing days
    for ass in assignments:
        dateParse = duedate.Due(ass)
        temp.append(dateParse.value)
    temp.sort()

    for ass in assignments:
        dateParse = duedate.Due(ass)
        useMe.append(dateParse)

    for mem in temp:
        i = 0
        for use in useMe:
            if(use.value == mem):
                final.append(assignments[i])
                assignments[i] = ' '
            i += 1
    
    return final

URL = "https://canvas.vt.edu/"

KEY = "Joimarie5302"

TOKEN = "4511~brX8DDeJfqE4lK77HHrzfPLu0bj0kEARSTZILbYrhXrJXLOF3kpVRBpHEoioDq6D"

canvas = Canvas(URL, TOKEN)

courses = canvas.get_courses()

user = canvas.get_current_user()

cDateTime = datetime.datetime.now()


month, day, year = DMY(str(cDateTime)[:10])

lines = []

for course in courses:
    line = []
    line.append(str(course))
    lines.append(line)

    assignments = course.get_assignments()

    usedAsses = []

    for ass in assignments:
        line = [""]
        dateParse = duedate.Due(ass)
        if(dateParse.year != False and int(dateParse.value) >= TodayValue(year, month, day)):
            usedAsses.append(ass)
            
    usedAsses = sortDate(usedAsses)

    for ass in usedAsses:
        try:
            dateParse = duedate.Due(ass)
            line.append(str(ass))
            line.append(str(dateParse.getCorrectDate()))
            lines.append(line)
            line = [""]
        except:
            x = 0

with open('test3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lines)

        #Have it sorted off of date. Also make sure to check quizes as well not just assignments. 
        #Do something about it saying 11/10/2020 when its really due 11/09/2020 at 11:59pm
        #Possibly include the time it's due as well for the classes that have stuff due at weird times.
