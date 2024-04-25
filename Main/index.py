from datetime import datetime, date

"""

Title: Volunteer Management System
File: index.py
Imports: datetime
Use of File: back-end of the different functions in system.py, called as the "base structure" of the overall system
Author(s): Hamad Almazrouei, Abdullah Alzaabi, Tahnoon Alzaabi

"""


class Task:
    """
    Task class that contains attributes including task number, title, required skills, credit hours, number of volunteers, and status
    """
    
    tasksRecord = []
    taskIdCounter = 0
    def __init__(self, title="", skills="", creditHours=0, numOfVol=0):
        Task.taskIdCounter += 1
        self.__taskNo = Task.taskIdCounter
        self.__title = title
        self.__requiredSkills = skills.split(",")
        self.__creditHour = creditHours
        self.__numOfVolunteersNeeded = numOfVol
        self.__status = "Newly Added"
        Task.tasksRecord.append(self)

    def setTaskNo(self, taskNo):
        self.__taskNo = taskNo

    def getTaskNo(self):
        return self.__taskNo

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setRequiredSkills(self, skills):
        self.__requiredSkills = skills

    def getRequiredSkills(self):
        return self.__requiredSkills

    def setCreditHour(self, hour):
        self.__creditHour = hour

    def getCreditHour(self):
        return self.__creditHour

    def setNumOfVolunteerNeeded(self, num):
        self.__numOfVolunteersNeeded = num

    def updateStatus(self, status):
        self.__status = status

    def getStatus(self):
        """
        getStatus: this function returns the status of the task either "Newly added" or "Completed"

        Returns:
            str: the function returns a string data type
        """
        return self.__status

    """
    Global functions 
    """

    def getNumOfVolunteerNeeded(taskNo):
        for task in Task.tasksRecord:
            if task.getTaskNo() == taskNo:
                return f"This task requires {task.__numOfVolunteersNeeded} persons to be accomplished"

    def __str__(self):
        return f"⎡ Task No: {self.__taskNo}\n├ Title: {self.__title}\n├ Skills: {self.__requiredSkills}\n├ Credit Hours: {self.__creditHour}\n├ Volunteers Needed: {self.__numOfVolunteersNeeded}\n⎣ Status: {self.__status}\n"


class User:
    """
    Super class of three other classes (Administrator, Organization Representative, and Volunteer)
    User class contains attributes : user id, full name, mobile number, email, education level, date of birth, and date of join.
    """

    userRecord = []
    today = datetime.now()
    year = str(today.year)
    month = str(today.month)
    nums = str("000")
    strOfID = str(year + "0" + month + nums)
    randomID = int(strOfID)

    def __init__(
            self, fullname="", mobile="", email="", educationLevel="", DOB=date
    ) -> None:
        User.randomID += 1
        self.__userID = User.randomID
        self.__fullName = fullname
        self.__mobile = mobile
        self.__email = email
        self.__educationLevel = educationLevel
        self.__DOB = DOB
        self.__DOJ = datetime.today()

    def setUserID(self, id):
        self.__userID = id

    def getUserID(self):
        return self.__userID

    def setFullName(self, name):
        self.__fullName = name

    def getFullName(self):
        return self.__fullName

    def setMobile(self, mobile):
        self.__mobile = mobile

    def getMobile(self):
        return self.__mobile

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setEducationLevel(self, level):
        """
        setEducationLevel: this function allows to edit the current education level of a user
        to a new one

        Args:
            str: the new education level
        """
        self.__educationLevel = level

    def getEducationLevel(self):
        """
        getEducationLevel: this function returns the current education level of the user

        Returns:
            str: the current education level of the user
        """
        return self.__educationLevel

    def setDOB(self, date):
        self.__DOB = date

    def getDOB(self):
        return self.__DOB

    def setDOJ(self, date):
        self.__DOJ = date

    def getDOJ(self):
        return self.__DOJ

    """
    Global functions 
    """

    def __str__(self):
        return f"User ID: {self.__userID}\nName: {self.__fullName}\nMobile: {self.__mobile}\nEamil: {self.__email}\nEducation Level: {self.__educationLevel}\nDate of Birth: {self.__DOB}\nDate of Join: {self.__DOJ}"


class Volunteer(User):
    """
    Child class of User with attributes : user id, skills, list of tasks, list of completed tasks, and total volunteering hours.
    """

    volunteerRecord = []
    
    def __init__(
            self,
            fullname="",
            mobile="",
            email="",
            educationLevel="",
            DOB=date,
            skills="",
    ):
        super().__init__(fullname, mobile, email, educationLevel, DOB)
        self.__userID = "V" + str(self._User__userID)
        self.__skills = skills.split(",")
        self.__tasks = []
        self.__completedTasks = []
        self.__totalVolunteeringHrs = 0
        Volunteer.volunteerRecord.append(self)    

    def setUserID(self, inID):
        self.__userID = inID

    def getUserID(self):
        return self.__userID

    def setSkills(self, skills):
        self.__skills = skills.split(",")

    def getTasks(self):
        """
        getTasks: this function returns the tasks assigned to a volunteer

        Returns:
            list: the list contains the tasks that the volunteer should accomplished
        """
        return self.__tasks

    def getTotalVolunteerHours(self):
        return self.__totalVolunteeringHrs

    def getCompletedTasks(self):
        """
        getCompletedTasks: this function provides the completed tasks by the user

        Returns:
            int: this function provides the integer of the total volunteering hours
        """
        return self.__completedTasks

    def addTask(self, task=Task()):
        self.__tasks.append(task)

    def setTotalVolunteerHours(self, sign="", amount=0):
        """
        setTotalVolunteerHours: this function adds the volunteering hour of a task to the total volunteering hour of the 
        user

        Args:
            sign (str): the sign specifies if the amount will be added or subtracted form the total volunteering 
            hours. Defaults to "".
            amount (int): the amount is the number of hours to add or subtract to the total volunteering hour. Defaults to 0.

        Returns:
            int : the new total volunteering hours after adding or subtracting
            
        Notes: 
            This function is only used in the backend of the code, you may consider it 
            as a part of a whole process (which is marking a task as completed and crediting volunteers)
        """
        if sign == "+":
            self.__totalVolunteeringHrs += amount
        elif sign == "-":
            self.__totalVolunteeringHrs -= amount
        else:
            return f"Error, check your inputs again"
        
    def addCompletedTasks(self, task=Task()):
        """
        addCompletedTasks: this function appends an existing task in the assigned task to the completed tasks list.
        the function changes the status of the task to be 'completed' and removes the task from the assigned tasks.

        Args:
            task (object, Task()): this represents an object of the Task class. Defaults to Task().
        """
        task.updateStatus("Completed")
        self.setTotalVolunteerHours("+", task.getCreditHour())
        self.__completedTasks.append(task)
        self.__tasks.remove(task)

    def __str__(self):
        return f"{super().__str__()}\nTotal Volunteering Hours: {self.__totalVolunteeringHrs}\nSkills: {self.__skills}"


class Volunteer_Opportunity:
    """
    Opportunity class contains opportunities for volunteers.
    The class has attributes including title, date, starting time, ending time, location, list of tasks, list of assigned volunteers, and list of interested volunteers.
    """

    randomCounter = 0

    def __init__(self, title=str, date=date, startingTime=str, endingTime=str, location=str) -> None:
        Volunteer_Opportunity.randomCounter += 1
        self.__opportunityCode = Volunteer_Opportunity.randomCounter
        self.__title = title
        self.__date = date
        self.__startingTime = startingTime
        self.__endingTime = endingTime
        self.__location = location
        self.__tasks = []
        self.__assignedVolunteers = []
        self.__interest = []

    def setOpportunityCode(self, code):
        self.__opportunityCode = code

    def getOpportunityCode(self):
        return self.__opportunityCode

    def setTitle(self, title):
        self.__title = title

    def getTitle(self):
        return self.__title

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date

    def setStartingTime(self, time):
        self.__startingTime = time

    def getStartingTime(self):
        return self.__startingTime

    def setEndTime(self, time):
        self.__endingTime = time

    def getEndTime(self):
        return self.__endingTime

    def setLocation(self, location):
        self.__location = location

    def getLocation(self):
        return self.__location

    def addTask(self, inTask=Task()):
        self.__tasks.append(inTask)

    def getTasks(self):
        return self.__tasks

    def addToAssignedVolunteers(self, volunteer=Volunteer()):
        """
        addToAssignedVolunteers: this function adds a volunteer to a list of assigned volunteers.

        Args:
            volunteer (object, Volunteer()): this takes a volunteer from interest list and append it to assigned volunteer list by removing
            the volunteer from the interest list. Defaults to Volunteer().
        """
        if volunteer in self.__interest:
            self.__interest.remove(volunteer)
            self.__assignedVolunteers.append(volunteer)
            for task in self.__tasks:
                volunteer.addTask(task)
        else:
            return f"Invalid Request: {volunteer} has not been in interest list"

    def getAssignedVolunteers(self):
        return self.__assignedVolunteers

    """
    Global functions 
    """

    def setInterest(self, interest=Volunteer()):
        """
        setInterest: this function adds a volunteer to the list of interested volunteers

        Args:
            interest (object, Volunteer()): this object refers to an object in the Volunteer class. Defaults to Volunteer().
        """
        self.__interest.append(interest)

    def getInterest(self):
        """
        getInterest: this function provides a list of interested volunteers

        Returns:
            list: this list contains all volunteers willing to take the opportunity
        """
        return self.__interest

    def updateTaskStatus(self, task=Task(), status=""):
        """
        updateTaskStatus: this function updates the status by taking two attributes. The task itself and the
        new status for that task

        Args:
            task (object, Task()): the task refers to an object in the T. Defaults to Task().
            status (str, optional): the status of the task that will be updated.

        Returns:
            None: if the 'if' condition is met
            String: if the 'else' condition is met
        """
        lowerStatus = status.lower()
        if task in self.__tasks:
            if lowerStatus == "completed":
                for vol in self.__assignedVolunteers:
                    vol.addCompletedTasks(task)
            else:
                task.updateStatus(status)
        else:
            return f"{task}, is not assigned to this opportunity"

    def registerInterest(self, vol=Volunteer()):
        """
        registerInterest _summary_

        Args:
            vol (_type_, optional): _description_. Defaults to Volunteer().
        """
        self.__interest.append(vol)

    def __del__(self):
        className = self.__class__.__name__
        return f"{className}, has been destroyed"

    def __str__(self):
        return f"⎡ Code: {self.__opportunityCode}\n├ Title: {self.getTitle()}\n├ Date: {self.getDate()}\n├ Location: {self.getLocation()}\n├ Starting Time: {self.getStartingTime()}\n⎣ Ending Time: {self.getEndTime()}"


class Organization_Representative(User):
    """
    Child class of User with its attributes including user Id
    """

    organizersRecord = []

    def __init__(
            self, fullname="", mobile="", email="", educationLevel="", DOB=date
    ) -> None:
        super().__init__(fullname, mobile, email, educationLevel, DOB)
        self.__userID = "O" + str(self._User__userID)
        Organization_Representative.organizersRecord.append(self)

    def getUserID(self):
        return self.__userID

    def getDOB(self):
        return super().getDOB()

    def getRepID(self):
        return self.__userID

    def __str__(self):
        return f"{super().__str__()} id {self.getRepID()}"


class Organization:
    """
    Organization class with attributes including organization name, description, list of opportunities, and list of representatives
    """

    organizationRecord = []

    def __init__(self, organization_name="", description="", orgCode=0) -> None:
        self.__organization_name = organization_name.replace(" ", "-")
        self.__organizationCode = "O" + str(orgCode)
        self.__description = description
        self.__opportunities = []
        self.__representatives = []
        Organization.organizationRecord.append(self)

    def setOrganizationName(self, name):
        self.__organization_name = name

    def getOrganizationName(self):
        return self.__organization_name

    def setDescription(self, desc):
        self.__description = desc

    def getDescription(self):
        return self.__description

    def createOpportunity(
            self, title, date, startingTime, endingTime, location 
    ):
        """
        createOpportunity: this function will allow to create a new opportunity within the organization, which represents a composition relationship

        Args:
            title (str): the title of the opportunity
            date (date): the data of the opportunity
            startingTime (str): the starting time
            endingTime (str): the ending time
            location (str): the location of the opportunity
        """
        opportunity = Volunteer_Opportunity(
            title, date, startingTime, endingTime, location
        )
        self.__opportunities.append(opportunity)

    def deleteOpportunity(self, opportunityCode):
        """
        deleteOpportunity: this function allows to delete a specific opportunity within an organization

        Args:
            opportunityCode (str): the code that will allow to specify a specific opportunity
        """
        for op in self.__opportunities:
            if op.getOpportunityCode() == opportunityCode:
                self.__opportunities.remove(op)

    def getOpportunities(self) -> list:
        """
        getOpportunities returns the list of opportunities that are in the organization

        Returns:
            List: list of opportunity objects
        """
        return self.__opportunities

    def setRepresentative(self, rep=Organization_Representative()) -> None:
        """
        setRepresentatives: allows to set a representative to an organization

        Args:
            rep (Object): this is an object of representative
        """
        self.__representatives.append(rep)

    def getRepresentatives(self) -> list:
        """
        getRepresentatives: this function provides all the representatives in a given organization

        Returns:
            list: the list contains all representatives in the organization
        """
        return self.__representatives

    def setOrgCode(self, code) -> None:
        self.__organizationCode = code

    def getOrgCode(self) -> str:
        return self.__organizationCode

    def addOpportunityToOrg(
            orgCode, otitle, odate, ostartingTime, oendingTime, olocation
    ) -> str:
        """
        addOpportunityToOrg: this function allows to add an opportunitiy to an organization

        Args:
            orgCode(str): this code can be used to specify a specific opportunity
            otitle (str): this represents the title of the opportunity
            odate(date): this represents the date of the opportunity
            ostartingTime (str): the starting time
            oendingTime (str): the ending time
            olocation (str): the location of the opportunity
        """

        orgName = ""

        for org in Organization.organizationRecord:
            if org.getOrgCode() == orgCode:
                orgName = org.getOrganizationName()
                org.createOpportunity(
                    otitle, odate, ostartingTime, oendingTime, olocation
                )
            else:
                return f"Invalid Organization Code"
        return f"Opportunity has been added to {orgName} successfully"

    def addTaskToOpportunity(self, task=Task(), opportunityCode=0):
        for opportunity in self.getOpportunities():
            if opportunity.getOpportunityCode() == opportunityCode:
                opportunity.addTask(task)
            else:
                continue

    def updateTaskStatus(self, opportunityCode=int, task=Task(), status=str) -> str:
        for opportunity in self.getOpportunities():
            if opportunity.getOpportunityCode() == opportunityCode:
                return opportunity.updateTaskStatus(task, status)
            else:
                continue
        else:
            return f"Opportunity not found, try again later.."

    def __str__(self) -> str:
        return f"Organization code: {self.getOrgCode()}\nOrganization name: {self.__organization_name}"


class Certificate:
    """
    Certificate class with attributes including certificate ID, volunteer name, and issue date
    """

    today = datetime.now()
    year = str(today.year)
    nums = str("0000")
    strOfID = str(year + "0" + nums)
    randomID = int(strOfID)

    def __init__(self) -> None:
        Certificate.randomID += 1
        self.__certificateID = Certificate.randomID
        self.__volunteer = ""
        self.__issueDate = datetime.today().date()

    def getCertificateID(self):
        return self.__certificateID

    def setVolunteer(self, volunteer=Volunteer()):
        self.__volunteer = volunteer.getFullName()

    def getVolunteer(self):
        return self.__volunteer

    def getIssueDate(self):
        return self.__issueDate


class Administrator(User):
    """
    Child class of User with attributes including user
    """

    administratorsRecord = []

    def __init__(
            self, fullname="", mobile="", email="", educationLevel="", DOB=date
    ) -> None:
        super().__init__(fullname, mobile, email, educationLevel, DOB)
        self.__userID = "A" + str(self._User__userID)
        Administrator.administratorsRecord.append(self)

    def setUserID(self, inID):
        self.__userID = inID

    def getUserID(self):
        return self.__userID

    def registerOrganizations(self, name, description, code):
        """
        registerOrganizations: this function allows the Admin to register organizations using the attributes of organization "Composition"

        Args:
            name (str): the name of the organization
            description (str): the description of the organization
            code (str): the code of the organization


        Returns:
            str: massage
        """
        try:
            org = Organization(name, description, code)
            return f"Organization registered"
        except:
            return f"Failed to register organization"

    def assignRepresentative(
            self, org=Organization(), rep=Organization_Representative()
    ):
        """
        assignRepresentative: this function allows to assign a representative to an organization

        Args:
            org (Object): this is an object from organization class. 
            rep (Object): this is an object from representative class.

        Returns:
            str: massage 
        """
        if org:
            org.setRepresentatives(rep)
        else:
            return f"Invalid Entry"

    def generateCertificate(self, certificate=Certificate(), vol=Volunteer()):
        """
        generateCertificate: this function allow to generate a certificate for a volunteer

        Args:
            certificate (Object): this is an object from class Certificate. Defaults to Certificate().
            vol (Object): this is an object from class Volunteer. Defaults to Volunteer().

        Returns:
            String: certificate string with all of the needed content
        """
        certificate.setVolunteer(vol)
        toPrint = f"====  -Certificate-  ====\n\tCID: {certificate.getCertificateID()}\n\tVolunteer: {self.getFullName()}\n\tIssue Date: {certificate.getIssueDate()}"

        return toPrint

    def __str__(self):
        return super().__str__()