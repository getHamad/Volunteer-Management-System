from datetime import datetime, date


"""


"""
class Task:
      """
      """

      taskRecord = {}      
      taskIdCounter = 0
      
      def __init__(self) -> None:
            Task.taskIdCounter +=1
            
            print("Enter the following information to create your task")
            self.__taskNo = Task.taskIdCounter
            self.__title = str(input("Task title: "))
            self.__requiredSkills = str(input("Skills (separated by comma): ").split(","))
            self.__creditHour = int(input("Credit Hours: "))
            self.__numOfVolunteersNeeded = int(input("Number of Volunteers: "))
            self.__status = "Newly Added"
            
            
            
            Task.taskRecord [self.__taskNo] = {
                  "taskNo": self.__taskNo,
                  "title": self.__title,
                  "required skills": self.__requiredSkills,
                  "credit hour": self.__creditHour,
                  "number of volunteers needed": self.__numOfVolunteersNeeded,
                  "status": self.__status
            }
            
            # getters & setters
      def setTaskNo(self,taskNo):
            self.__taskNo = taskNo
      
      def getTaskNo(self):
            return self.__taskNo
      
      def setTitle(self,title):
            self.__title = title
      
      def getTitle(self):
            return self.__title
      
      def setRequiredSkills(self,skills):
            self.__requiredSkills = skills
      
      def getRequiredSkills(self):
            return self.__requiredSkills
      
      def setCreditHour(self,hour):
            self.__creditHour = hour
      
      def getCreditHour(self):
            return self.__creditHour
      
      def setNumOfVolunteerNeeded(self,num):
            self.__numOfVolunteersNeeded = num
      
      def getNumOfVolunteerNeeded(self):
            return self.__numOfVolunteersNeeded
      
     
      def getStatus(self, taskNo):
            infoOfStatus = ""
            for task, data in Task.taskRecord.items(): 
                  if task == taskNo:
                        infoOfStatus = data['status']
            return infoOfStatus
      
      def updateStatus(self,taskno ,status):
            if taskno in Task.taskRecord:
                  for task, data in Task.taskRecord.items(): 
                        if task == taskno:
                              data['status'] = status
                              print(f"Status has been updated for task {taskno}")
                        else: 
                              print("Loading..")
            else:
                  print(f"Id {taskno} not found in the dictionary")
            



class Volunteer_Opportunity:
      """
      """
      opportunityDict = {}
      opportunityCounter = 0
      
      
      def __init__(self) -> None:
            Volunteer_Opportunity.opportunityCounter += 1
            self.__title = str(input("Volunteer Opportunity: "))
            self.__date = input("date of birth (yyyy-mm-dd): ").split("-")
            self.__date = date(int(self.__DOJ[0]), int(self.__DOJ[1]), int(self.__DOJ[2]))
            self.__startingTime = str(input("Starting Time (00:00): "))
            self.__endingTime = str(input("Ending Time (00:00): "))
            self.__location = str(input("Location: "))
            self.__tasks = []
            self.__assignedVolunteers = []
            self.__interest = []
            
            Volunteer_Opportunity.opportunityDict [Volunteer_Opportunity.opportunityCounter] = {
                  "title":self.__title,
                  "date":self.__date,
                  "starting time":self.__startingTime,
                  "ending time": self.__endingTime,
                  "location":self.__location,
                  "tasks": self.__tasks,
                  "assignedVolunteers": self.__assignedVolunteers,
                  "interest": self.__interest
            }
            
            # getters & setters
      def setTitle(self, title):
            self.__title = title

      def getTitle(self):
            return self.__title
      
      def setDate(self,date):
            self.__date = date

      def getDate(self):
            return self.__date
      
      def setStartingTime(self,time):
            self.__startingTime = time

      def getStartingTime(self):
            return self.__startingTime
      
      def setEndTime(self,time):
            self.__endingTime = time

      def getEndTime(self):
            return self.__endingTime
      
      def setLocation(self,location):
            self.__location = location
      
      def getLocation(self):
            return self.__location
      
      def setTasks(self,tasks):
            self.__tasks = tasks
      
      def getTasks(self):
            return self.__tasks
      
      def setAssignedVolunteers(self,volunteer):
            self.__assignedVolunteers = volunteer

      def getAssignedVolunteers(self):
            return self.__assignedVolunteers
      
      def setInterest(self,interest):
            self.__interest = interest
      
      def getInterest(self):
            return self.__interest
      

            
      
            
         
      
class Organization:
      """
      """
      organizationRecord = {}
      def __init__(self) -> None:
            self.__organization_name = str(input("Organization Name: ")).replace(" ","-")
            self.__description = str(input("Description: "))
            self.__opportunities = [ ]
            self.__representatives = [ ]
            
            Organization.organizationRecord [self.__organization_name] = {
                  "description": self.__description,
                  "opportunities": self.__opportunities,
                  "representatives": self.__representatives
            }   
            
            # getters & setters
      def setOrganizationName(self,name):
            self.__organization_name = name
      
      def getOrganizationName(self):
            return self.__organization_name
      
      def setDescription(self,desc):
            self.__description = desc
      
      def getDescription(self):
            return self.__description
      
      def setOpportunities(self,opportunities):
            self.__opportunities = opportunities
      
      def getOpportunities(self):
            return self.__opportunities
      
      def setRepresentatives(self,rep):
            self.__representatives = rep

      def getRepresentatives(self):
            return self.__representatives
      
            
      

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
                   ) -> None:
            User.randomID += 1
            self.__userID = User.randomID
            print("Enter the following information")
            self.__fullName = str(input("full name: "))
            self.__mobile = str(input("mobile number: "))
            self.__email = str(input("email: "))
            self.__educationLevel = str(input("education level: "))
            self.__DOB = input("date of birth (yyyy-mm-dd): ").split("-")
            self.__DOB = date(int(self.__DOJ[0]), int(self.__DOJ[1]), int(self.__DOJ[2]))
            self.__DOJ = datetime.today()
            

            # getters & setters
      def setUserID(self,id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID
      
      def setFullName(self,name):
            self.__fullName = name
      
      def getFullName(self):
            return self.__fullName
      
      def setMobile(self,mobile):
            self.__mobile = mobile
      
      def getMobile(self):
            return self.__mobile
      
      def setEmail(self,email):
            self.__email = email
      
      def getEmail(self):
            return self.__email

      def setEducationLevel(self,level):
            self.__educationLevel = level
      
      def getEducationLevel(self):
            return self.__educationLevel
      
      def setDOB(self, date):
            self.__DOB = date
      
      def getDOB(self):
            return self.__DOB
      
      def setDOJ(self,date):
            self.__DOJ = date
      
      def getDOJ(self):
            return self.__DOJ
 
 


class Volunteer(User):
      """
      """
      volunteerRecord = {}

      def __init__(self,
                   ) -> None:
            super().__init__()
            self.__userID = "V" + str(self._User__userID)
            self.__skills = input("skills separated by comma: ").split(",")
            self.__tasks = []
            self.__completedTasks = []
            self.__totalVolunteeringHrs = 0
            
            
            Volunteer.volunteerRecord [self.__userID] = {
                  "skills": self.__skills,
                  "tasks": self.__tasks,
                  "completedTasks": self.__completedTasks,
                  "totalVolunteeringHrs" : self.__totalVolunteeringHrs
               
            }
            
            
            User.userRecord [self.__userID] = {
                  "fullname": self._User__fullName,
                  "mobile": self._User__mobile,
                  "email": self._User__email,
                  "educationLevel": self._User__educationLevel,
                  "DOJ": self._User__DOJ,
                  "DOB": self._User__DOB      
            }
            
            # getters & setters
      def setUserID(self,id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID
      
      def setSkills(self,skills):
            self.__skills = skills
      
      def getSkills(self):
            return self.__skills
      
      def setTasks(self,tasks):
            self.__tasks = tasks
      
      def getTasks(self):
            return self.__tasks
      
      def setCompletedTasks(self,compTasks):
            self.__completedTasks = compTasks
      
      def getCompletedTasks(self):
            return self.__completedTasks
      
      def setTotalVolunteerHours(self, hrs):
            self.__totalVolunteeringHrs = hrs
      
      def getTotalVolunteerHours(self):
            return self.__totalVolunteeringHrs

            
      

class Organization_Representative(User):
      """
      """
      organizationRepRecord = {}


      
      def __init__(self) -> None:
            super().__init__()
            self.__userID = "O" + str(self._User__userID)
      
            Organization_Representative.organizationRepRecord [self.__userID] = {
                  "User ID": self.__userID
            }

            User.userRecord [self.__userID] = {
                  "fullname": self._User__fullName,
                  "mobile": self._User__mobile,
                  "email": self._User__email,
                  "educationLevel": self._User__educationLevel,
                  "DOJ": self._User__DOJ,
                  "DOB": self._User__DOB      
            }
            
            # getters & setters
      def setUserID(self,id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID
      



class Certificate:
      """
      """
      today = datetime.now()
      year = str(today.year)
      nums = str("0000")
      strOfID = str(year + "0" + nums)
      randomID = int(strOfID)      
      
      def __init__(self) -> None:
            randomID += 1
            self.__certificateID = randomID
            self.__volunteer = "" # get volunteer name using volunteer ID
            self.__issueDate = datetime.today().date()  # printing the date of creation    
            
      # functions - getters & setters
      def setCertificateID(self,id):
            self.__certificateID = id
      
      def getCertificateID(self):
            return self.__certificateID
      
      def setVolunteer(self,volunteer):
            self.__volunteer = volunteer
      
      def getVolunteer(self):
            return self.__volunteer
      
      def setIssueDate(self,date):
            self.__issueDate = date
      
      def getIssueDate(self):
            return self.__issueDate
      



class Administrator(User):
      """
      """
      administratorRecord = []
      
      def __init__(self)-> None:
            super().__init__()
            self.__userID = "A" + str(self._User__userID)

            Administrator.administratorRecord [self.__userID] = {
                  "User ID": self.__userID
            }
            
            User.userRecord [self.__userID] = {
                  "fullname": self._User__fullName,
                  "mobile": self._User__mobile,
                  "email": self._User__email,
                  "educationLevel": self._User__educationLevel,
                  "DOJ": self._User__DOJ,
                  "DOB": self._User__DOB      
            }

            # getters & setters
      def setUserID(self, id):
            self.__userID = id
      
      def getUserID(self):
            return self.__userID



#tests
t = Task()
e = Task()
print(t.updateStatus(3, "completed"))
print(Task.taskRecord)