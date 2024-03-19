from datetime import datetime, date


"""


"""
class Task:
      """
      """

      taskRecord = {}      
      
      def __init__(self) -> None:
            print("Enter the following information")
            self.__taskNo = str(input("Task number: "))
            self.__title = str(input("Task title: "))
            self.__requiredSkills = str(input("Skills (separated by comma): ").split(","))
            self.__creditHour = int(input("Credit Hours: "))
            self.__numOfVolunteersNeeded = int(input("Number of Volunteers: "))
            self.__status = "Newly Added"
            Task.taskRecord [self.__taskNo] = {
                  # missing values
            }
            
            # getters & setters
      
            



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
            
      def test(self): 
            return self.__userID
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

class Certificate:
      """
      """
      def __init__(self) -> None:
            self.__certificateID #add id here
            self.__volunteer = "" # get volunteer name using
            self.__issueDate = datetime.today().date()  # printing the date of creation    
            
      # functions - getters & setters
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

#Hi