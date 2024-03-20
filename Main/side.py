from datetime import datetime, date


"""


"""
class Task:
      """
      """      
      taskIdCounter = 0
      
      def __init__(self, title = "", skills = "", creditHours=0, numOfVol=0):
            Task.taskIdCounter +=1
                        
            self.__taskNo = Task.taskIdCounter
            self.__title = title
            self.__requiredSkills = skills.split(",")
            self.__creditHour = creditHours
            self.__numOfVolunteersNeeded = numOfVol
            self.__status = "Newly Added"
            
            # getters & setters
      def setTaskNo(self,
                    taskNo):
            self.__taskNo = taskNo
      
      def getTaskNo(self):
            return self.__taskNo
      
      def setTitle(self,
                   title):
            self.__title = title
      
      def getTitle(self):
            return self.__title
      
      def setRequiredSkills(self,
                            skills):
            self.__requiredSkills = skills
      
      def getRequiredSkills(self):
            return self.__requiredSkills
      
      def setCreditHour(self,
                        hour):
            self.__creditHour = hour
      
      def getCreditHour(self):
            return self.__creditHour
      
      def setNumOfVolunteerNeeded(self,
                                  num):
            self.__numOfVolunteersNeeded = num
      
      def getNumOfVolunteerNeeded(self):
            return self.__numOfVolunteersNeeded
      
      def updateStatus(self,
                       status):
            self.__status = status
                 
      def getStatus(self):
            return self.__status
      
            



    
         
      

      
            
      

class User:
      """
      Super class of three other classes (Administrator, Organization Representative, and Volunteer)
      """
      userRecord = {}
      
      today = datetime.now()
      year = str(today.year)
      month = str(today.month)
      nums = str("000")
      strOfID = str(year + "0" + month + nums)
      randomID = int(strOfID)
      
      def __init__(self,
                   fullname = '',mobile = '',email = '',educationLevel = '',DOJ = date, DOB = date
                   ) -> None:
            User.randomID += 1
            self.__userID = User.randomID            
            self.__fullName = fullname
            self.__mobile = mobile
            self.__email = email
            self.__educationLevel = educationLevel
            self.__DOB = DOB
            self.__DOJ = DOJ
            self.__DOJ = datetime.today()

            

            # getters & setters
      def setUserID(self,
                    id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID
      
      def setFullName(self,
                      name):
            self.__fullName = name
      
      def getFullName(self):
            return self.__fullName
      
      def setMobile(self,
                    mobile):
            self.__mobile = mobile
      
      def getMobile(self):
            return self.__mobile
      
      def setEmail(self,
                   email):
            self.__email = email
      
      def getEmail(self):
            return self.__email

      def setEducationLevel(self,
                            level):
            self.__educationLevel = level
      
      def getEducationLevel(self):
            return self.__educationLevel
      
      def setDOB(self,
                 date):
            self.__DOB = date
      
      def getDOB(self):
            return self.__DOB
      
      def setDOJ(self,
                 date):
            self.__DOJ = date
      
      def getDOJ(self):
            return self.__DOJ
 
 


class Volunteer(User):
      """
      """

      def __init__(self,
                   fullname = '',mobile = '',email = '',educationLevel = '',DOJ = date, DOB = date, skills="") -> None:
            super().__init__(fullname,mobile,email ,educationLevel,DOJ , DOB)
            self.__userID = "V" + str(self._User__userID)
            self.__skills = skills.split(",")
            self.__tasks = []
            self.__completedTasks = []
            self.__totalVolunteeringHrs = 0
            
            
            # getters & setters
      def setUserID(self,
                    id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID
      
      def setSkills(self,
                    skills):
            self.__skills = skills.split(",")
      
      def getSkills(self):
            data = ""
            for skill in self.__skills:
                  data += "\t" + str(skill) + "\n"
            return data
      
      
      def getTasks(self):
            data = ""
            for obj in self.__tasks:
                  data += "\t" + str(obj) + "\n"
            return data
      
      
      def setTotalVolunteerHours(self, 
                                 sign = "", amount = 0):
            if sign == "+": 
                  self.__totalVolunteeringHrs += amount
            elif sign == "-":
                  self.__totalVolunteeringHrs -= amount
            else: 
                  return f"Error, check your inputs again"
            
            
      def addCompletedTasks(self,
                            task:Task()): # type: ignore
            if task in self.__tasks: 
                  task.updateStatus("Completed")
                  self.setTotalVolunteerHours("+", task.getCreditHour())
                  self.__completedTasks.append(task)
                  self.__tasks.remove(task)
            else: 
                  return f"{task}, is not in our records"
                  
      
      def getCompletedTasks(self):
            return self.__completedTasks
      

                  
      
      def getTotalVolunteerHours(self):
            return self.__totalVolunteeringHrs
      
      

            

class Volunteer_Opportunity:
      """
      """
      opportunityCounter = 0
      
      
      def __init__(self,
                   title, date, startingTime, endingTime, location) -> None:
            Volunteer_Opportunity.opportunityCounter += 1
            self.__title = title
            self.__date = date
            self.__startingTime = startingTime
            self.__endingTime = endingTime
            self.__location = location
            self.__tasks = []
            self.__assignedVolunteers = []
            self.__interest = []
            
            
            # getters & setters
      def setTitle(self, 
                   title):
            self.__title = title

      def getTitle(self):
            return self.__title
      
      def setDate(self,
                  date):
            self.__date = date

      def getDate(self):
            return self.__date
      
      def setStartingTime(self,
                          time):
            self.__startingTime = time

      def getStartingTime(self):
            return self.__startingTime
      
      def setEndTime(self,
                     time):
            self.__endingTime = time

      def getEndTime(self):
            return self.__endingTime
      
      def setLocation(self,
                      location):
            self.__location = location
      
      def getLocation(self):
            return self.__location
      
      def setTasks(self,
                   tasks):
            self.__tasks = tasks
      
      def getTasks(self):
            return self.__tasks
      
      def addAssignedVolunteers(self,
                                volunteer = Volunteer()):
            self.__assignedVolunteers.append(volunteer)

      def getAssignedVolunteers(self):
            data = ""
            for obj in self.__assignedVolunteers:
                  data += "\t" + {str(obj)} + "\n"
            return data

      def setInterest(self,
                      interest = Volunteer()):
            self.__interest.append(interest)
      
      def getInterest(self):
            data = ""
            for obj in self.__interest:
                  data += "\t" + str(obj) + "\n"
            return data
      
      def addTask(self, 
                  Task = Task()):
            self.__tasks.append(Task)
            
      def updateStatus(self,
                       task = Task(), status = ""):
            if task in self.__tasks: 
                  task.updateStatus(status)
            else:
                  return f"{task}, is not recorded"
                        
    
      def __str__(self):
            return f"⎛ Title: {self.getTitle()} ⎞\n⎡ Date: {self.getDate()}\n├ Location: {self.getLocation()}\n├ Starting Time: {self.getStartingTime()}\n⎣ End Time: {self.getEndTime()}"
        
            
            
      
                    
      

class Organization_Representative(User):
      """
      """

      
      def __init__(self,
                   fullname = '',mobile = '',email = '',educationLevel = '',DOJ = date, DOB = date
                   ) -> None:
            super().__init__(fullname,mobile,email ,educationLevel,DOJ , DOB)
            self.__userID = "O" + str(self._User__userID)
      
            
            # getters & setters
      
      def getUserID(self):
            return self.__userID
      

class Organization:
      """
      """
      def __init__(self,organization_name= " ",description ="") -> None:
            self.__organization_name = organization_name.replace(" ","-")
            self.__description = description
            self.__opportunities = [ ]
            self.__representatives = [ ]
            
            # getters & setters
      def setOrganizationName(self,
                              name):
            self.__organization_name = name
      
      def getOrganizationName(self):
            return self.__organization_name
      
      def setDescription(self,
                         desc):
            self.__description = desc
      
      def getDescription(self):
            return self.__description
      
      def createOpportunities(self,
                              title,date,startingTime,endingTime,location):

            opportunity = Volunteer_Opportunity(title,date,startingTime,endingTime,location)
            self.__opportunities.append(opportunity)
        
      
      def getOpportunities(self):
            data = "⎨Opportunities\n"
            for obj in self.__opportunities:
                  data += "\t" + str(obj) + "\n"
            return data
      
      def setRepresentatives(self,
                             rep = Organization_Representative()):
            self.__representatives.append(rep)

      def getRepresentatives(self):
            data = ""
            for op in self.__representatives:
                  data += "\t" + str(op) + "\n"
            return data
      
      
class Certificate:
      """
      """
      today = datetime.now()
      year = str(today.year)
      nums = str("0000")
      strOfID = str(year + "0" + nums)
      randomID = int(strOfID)      
      
      def __init__(self) -> None:
            Certificate.randomID += 1
            self.__certificateID = Certificate.randomID
            self.__volunteer  =""
            self.__issueDate = datetime.today().date()  # printing the date of creation    
            
      # functions - getters & setters
      
      def getCertificateID(self):
            return self.__certificateID
      
      def setVolunteer(self,
                       volunteer = Volunteer()):
            self.__volunteer = volunteer.getFullName()
      
      def getVolunteer(self):
            return self.__volunteer
      
      def getIssueDate(self):
            return self.__issueDate
      



class Administrator(User):
      """
      """      
      def __init__(self,
                   fullname = '',mobile = '',email = '',educationLevel = '',DOJ = date, DOB = date
                   )-> None:
            super().__init__(fullname,mobile,email ,educationLevel,DOJ , DOB)
            self.__userID = "A" + str(self._User__userID)


            # getters & setters
      def setUserID(self, 
                    id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID

      def assignRepresentative(self, 
                               org = Organization(), rep = Organization_Representative()):
            if org:
                  org.setRepresentatives(rep)
            else:
                  return f"Invalid Entry"
            
      def generateCertificate(self, 
                              certificate = Certificate(), vol = Volunteer()):

            certificate.setVolunteer(vol)
            toPrint = f"====  -Certificate-  ====\n\tCID: {certificate.getCertificateID()}\n\tVolunteer: {self.getFullName()}\n\tIssue Date: {certificate.getIssueDate()}"
            
            return toPrint
            
                  





