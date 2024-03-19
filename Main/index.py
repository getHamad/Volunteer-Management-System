from datetime import datetime



"""


"""
class Task:
      """
      """
      def __init__(self,title = "",taskNO = "",requiredSkills = [],creditHour = 0,numOfVolunteersNeeded = 0, status = "") -> None:
            self.__title = title
            self.__taskNo = taskNO
            self.__requiredSkills = requiredSkills
            self.__creditHour = creditHour
            self.__numOfVolunteersNeeded = numOfVolunteersNeeded
            self.__status = status

            



class Volunteer_Opportunity:
      """
      """
      def __init__(self,title,data,startingTime,endingTime,location) -> None:
            self.__title = title
            self.__data = data
            self.__startingTime = startingTime
            self.__endingTime = endingTime
            self.__location = location
            
            
      
      
      
class Organization:
      """
      """
      def __init__(self,organization_name,description,organizationID) -> None:
            self.__organization_name = organization_name
            self.__description = description
            self.__organizationID = organizationID
            
            
      

class User:
      """
      Super class of three other classes (Administrator, Organization Representative, and Volunteer)
      """
      userRecord = []
      
      today = datetime.now()
      year = str(today.year)
      month = str(today.month)
      nums = str("000")
      strOfID = str(year + "0" + month + nums)
      randomID = int(strOfID)
      
      def __init__(self,userID, fullName, mobile,email,educationLevel, DOJ,DOB) -> None:
            User.randomID += 1
            self.__userID = User.randomID
            self.__fullName = fullName
            self.__mobile = mobile
            self.__email = email
            self.__educationLevel = educationLevel
            self.__DOJ = DOJ
            self.__DOB = DOB
            


 
 
class Volunteer(User):
      """
      """
      volunteerRecord = []     
      
      
      def __init__(self) -> None: 
            pass # add super().__init__ after fixing user attributes
class Organization_Representative(User):
      """
      """
      organizationRepRecord = []

      
      def __init__(self) -> None:
            pass # add super().__init__ after fixing user attributes
      
class Administrator(User):
      """
      """
      administratorRecord = []
      
      def __init__(self) -> None:
            pass # add super().__init__ after fixing user attributes      