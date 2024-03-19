from datetime import datetime, date


"""


"""
class Task:
      """
      """

      taskRecord = {}      
      def __init__(self) -> None:
            self.__title = str(input("Task title: "))
            self.__taskNo = str(input("Task number: "))
            self.__requiredSkills = str(input("skills separated by comma: ").split(","))
            self.__creditHour = int(input("Credit Hours: "))
            self.__numOfVolunteersNeeded = int(input("Number of Volunteers: "))
            self.__status = str(input("Status"))
            Task.taskRecord [self.__taskNo] = {
                  
            }
            



class Volunteer_Opportunity:
      """
      """
      opportunityDict = {}
      opportunityCounter = 0
      def __init__(self,
                   title = '', date = date, startingTime = '', endingTime = '', location = ''
                   ) -> None:
            Volunteer_Opportunity.opportunityCounter += 1
            self.__title = title
            self.__date = date
            self.__startingTime = startingTime
            self.__endingTime = endingTime
            self.__location = location
            
            
      
      
      
class Organization:
      """
      """
      def __init__(self,
                   organization_name = '', description = '', organizationID = ''
                   ) -> None:
            self.__organization_name = organization_name
            self.__description = description
            self.__organizationID = organizationID
            
            
      

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
               
            }
            
            
            User.userRecord [self.__userID] = {
                  "fullname": self._User__fullName,
                  "mobile": self._User__mobile,
                  "email": self._User__email,
                  "educationLevel": self._User__educationLevel,
                  "DOJ": self._User__DOJ,
                  "DOB": self._User__DOB      
            }
            
            
      def test(self): 
            return self.__userID
class Organization_Representative(User):
      """
      """
      organizationRepRecord = {}

      
      def __init__(self, 
                   fullName, mobile, email, educationLevel, DOJ, DOB
                   ) -> None:
            super().__init__( fullName, mobile, email, educationLevel, DOJ, DOB)
            self.__userID = "O" + str(self._User__userID)

            
class Administrator(User):
      """
      """
      administratorRecord = []
      
      def __init__(self, 
                   userID, fullName, mobile, email, educationLevel, DOJ, DOB
                   )-> None:
            super().__init__(userID, fullName, mobile, email, educationLevel, DOJ, DOB)
            self.__userID = "A" + str(self._User__userID)




