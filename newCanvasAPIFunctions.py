from canvasapi import Canvas
import datetime

class Due:
    def __init__(self,assign):
        self.assignment = assign
        self.day = 0
        self.month = 0
        self.year = 0
        self.cDay = 0
        self.cMonth = 0
        self.cYear = 0
        self.cHour = 0
        self.cMinute = 0
        self.cSecond = 0
        self.value = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.getDMY()
        self.getMachineDMY()
        
        
        
    def timeCorrect(self):
        hour = int(self.hour)
        day = int(self.day)
        month = int(self.month)
        year = int(self.year)
        change = 5

        tHour, tMinute, tSecond = self.getHMS(str(datetime.datetime.now())[11:-1])

        change = int(self.cHour) - int(tHour)

        #corrects days months and year based off if the time change moves it back a minute
        if(hour - change < 0):
            if(day - 1 == 0):
                if(month - 1 == 0):
                    year -= 1
                month -= 1
            day -= 1
        hour -= change
        if(hour < 0):
            hour = 12 + hour

        self.hour = str(hour)
        self.day = str(day)
        self.month = str(month)
        self.year = str(year)
        
        if(len(self.month) < 2):
            self.month = "0" + self.month
        if(len(self.day) < 2):
            self.day = "0" + self.day
        

    def getHMS(self, time):
        #input hr:mn:sc.mili
        #      0123456789
        hour = time[:2]
        minute = time[3:5]
        second = time[6:8]
        
        return hour,minute,second

    def getMachineDMY(self):
        time = str(datetime.datetime.utcnow())[:10]
        self.cDay = time[-2:]
        self.cMonth = time[5:7]
        self.cYear = time[:4]
        
    

    def getDMY(self):
        if(self.getDate() != False):
            time = 0
            self.day = self.getDate()
            time = self.getTime()
            self.day = self.day[-2:]          
            self.month = self.getDate()
            self.month = self.month[5:7]
            self.year = self.getDate()
            self.year = self.year[:4]
            
            self.hour, self.minute, self.second = self.getHMS(time)
            self.cHour, self.cMinute, self.cSecond = self.getHMS(str(datetime.datetime.utcnow())[11:-1])
            self.timeCorrect()
            self.value = self.getValue()

        else:
            self.year = False
        
    def getValue(self):
        temp = str(self.year[2:]) + str(self.month) + str(self.day)
        
        temp = int(temp)
        
        return temp



    def getData(self):
        
        #return self.assignment.due
        #print(self.assignment.oooh)
        return self.assignment.oooh

    def getDate(self):
        test = str(self.getData())
        

        index = test.find("due_at=") + 7
        
        
        temp = ""
        while(True):
            if(test[index] != ","):
                temp += test[index]
            else:
                break
            index += 1
        try:
            test = int(temp[:2])
        except:
            return False
        
        return temp[:10]
    
    def getCorrectDate(self):
        month = self.month
        day = self.day
        
        if(len(month) < 2):
            month = "0" + month
        if(len(day) < 2):
            day = "0" + day

        return month + "/" + day + "/" + self.year
    

    def getTime(self):
        
        test = str(self.getData())

        index = test.find("due_at=") + 7
        
        
        temp = ""
        while(True):
            if(test[index] != ","):
                temp += test[index]
            else:
                break
            index += 1
        return temp[11:-1]
    


    



