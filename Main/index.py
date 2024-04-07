from datetime import datetime, date

"""


"""

class Task:
    """
    Task class that contains attributes including task number,title, required skills, credit hours, number of volunteers, and status.
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

        # getters & setters

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
        """
            Global functions 
            """

    def getNumOfVolunteerNeeded(taskNo):
        for task in Task.tasksRecord:
            if task.getTaskNo() == taskNo:
                return f"This task requires {task.__numOfVolunteersNeeded} persons to be accomplished"

    # Exception Handling, task number not found!!!

    def updateStatus(self, status):
        self.__status = status

    # Exception Handling, task number not found!!!

    def getStatus(self):
        """
        getStatus: this function returns the status of the task either "Newly added" or "Completed"

        Returns:
            str: the function returns a string data type
        """
        return self.__status

    # Exception Handling, task number not found!!!

    def getTasks():
        """
        getTasks: this function returns a list of tasks that are already registered in the system

        Returns:
            str: the output will be "string" to print the full detail of the task as in __str__ function
        """
        data = ""
        for obj in Task.tasksRecord:
            if obj.getTitle() == "":
                pass
            else:
                data += "\t" + str(obj) + "\n"
        return data
    
    def __str__(self):
        return f"Task No: {self.__taskNo}\nTitle: {self.__title}\nSkills: {self.__requiredSkills}\nCredit Hours: {self.__creditHour}\nVolunteers Needed: {self.__numOfVolunteersNeeded}\nStatus: {self.__status}\n===================="


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
        self, fullname="", mobile="", email="", educationLevel="", DOJ=date, DOB=date
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
        User.userRecord.append(self)

        # getters & setters

    def setUserID(self, id):
        self.__userID = id

    #def getUserID(self):
        #  return self.__userID

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
        DOJ=date,
        DOB=date,
        skills="",
    ) -> None:
        super().__init__(fullname, mobile, email, educationLevel, DOJ, DOB)
        self.__userID = "V" + str(self._User__userID)
        self.__skills = skills.split(",")
        self.__tasks = []
        self.__completedTasks = []
        self.__totalVolunteeringHrs = 0
        Volunteer.volunteerRecord.append(self)

        # getters & setters

    def setUserID(self, inID):
        self.__userID = inID

    def getUserID(self):
        return self.__userID

    def setSkills(self, skills):
        self.__skills = skills.split(",")

    def getSkills(self):
        
        data = ""
        for skill in self.__skills:
            data += "\t" + str(skill) + "\n"
        return data

    def addTask(self, task=Task()):
        self.__tasks.append(task)

    def getTasks(self):
        """
        getTasks: this function returns the tasks assigned to a volunteer

        Returns:
            list: the list contains the tasks that the volunteer should accomplished
        """
        return self.__tasks

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

    def getCompletedTasks(self):
        """
        getCompletedTasks _summary_

        Returns:
            _type_: _description_
        """
        return self.__completedTasks

    def getTotalVolunteerHours(self):
        return self.__totalVolunteeringHrs

        """
        Global functions 
        """
    def getAllVolunteers():
        """
        getAllVolunteers: returns all existing volunteers in the system

        Returns:
            String: returns a string of volunteer information
        """
        
        data = ""
        for obj in Volunteer.volunteerRecord:
            data += "\t" + str(obj) + "\n"
        return data
    
    
    def __str__(self):
        return super().__str__()


class Volunteer_Opportunity:
    """
    Opportunity class contains opportunities for volunteers.
    The class has attributes including title, date, starting time, ending time, location, list of tasks, list of assigned volunteers, and list of interested volunteers.
    """

    randomCounter = 0

    def __init__(self, title, date, startingTime, endingTime, location) -> None:
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

        # getters & setters

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

    def addToAssignedVolunteers(self,volunteer=Volunteer()):
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
        
        data = ""
        for obj in self.__assignedVolunteers:
            data += "\t" + {str(obj)} + "\n"
        return data

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
        getInterest: this funcion provides a list of interested volunteers

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
            status (str, optional): _description_. Defaults to "".

        Returns:
            _type_: _description_
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

    def __str__(self):
        return f"⎡ Code: {self.__opportunityCode}\n├ Title: {self.getTitle()}\n├ Date: {self.getDate()}\n├ Location: {self.getLocation()}\n├ Starting Time: {self.getStartingTime()}\n⎣ End Time: {self.getEndTime()}"


class Organization_Representative(User):
    """
    Child class of User, with attributes including user Id.
    """
    
    organizersRecord = []

    def __init__(
        self, fullname="", mobile="", email="", educationLevel="", DOJ=date, DOB=date
    ) -> None:
        super().__init__(fullname, mobile, email, educationLevel, DOJ, DOB)
        self.__userID = "O" + str(self._User__userID)

        Organization_Representative.organizersRecord.append(self)

        # getters & setters

    def getUserID(self):
        return self.__userID
    


class Organization:
    """
    Organization class with attributes including organization name, description, list of opportunities, and list of representatives.
    """

    organizationRecord = []

    def __init__(self, organization_name=" ", description="", orgCode=0) -> None:
        self.__organization_name = organization_name.replace(" ", "-")
        self.__organizationCode = "O" + str(orgCode)
        self.__description = description
        self.__opportunities = []
        self.__representatives = []

        Organization.organizationRecord.append(self)

        # getters & setters

    def setOrganizationName(self, name):
        self.__organization_name = name

    def getOrganizationName(self):
        return self.__organization_name

    def setDescription(self, desc):
        self.__description = desc

    def getDescription(self):
        return self.__description

    def createOpportunity(
        self, title, date, startingTime, endingTime, location  # update this function
    ):
        """
        createOpportunity _summary_

        Args:
            title (_type_): _description_
            date (_type_): _description_
            startingTime (_type_): _description_
            endingTime (_type_): _description_
            location (_type_): _description_
        """
        
        opportunity = Volunteer_Opportunity(
            title, date, startingTime, endingTime, location
        )
        self.__opportunities.append(opportunity)

    def deleteOpportunity(self, opportunityCode):
        """
        deleteOpportunity _summary_

        Args:
            opportunityCode (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        try:
            for op in self.__opportunities:
                if op.getOpportunityCode() == opportunityCode:
                    del op
        except:
            return f"Failed to delete {self.__organization_name}"

    def getOpportunities(self):
        """
        getOpportunities _summary_

        Returns:
            _type_: _description_
        """
        return self.__opportunities

    def setRepresentatives(self, rep=Organization_Representative()):
        """
        setRepresentatives _summary_

        Args:
            rep (_type_, optional): _description_. Defaults to Organization_Representative().
        """
        self.__representatives.append(rep)

    def getRepresentatives(self):
        """
        getRepresentatives _summary_

        Returns:
            _type_: _description_
        """
        return self.__representatives

    def setOrgCode(self, code):
        self.__organizationCode = code

    def getOrgCode(self):
        return self.__organizationCode

    def addOpportunityToOrg(
        orgCode, otitle, odate, ostartingTime, oendingTime, olocation
    ) -> str:
        """
        addOpportunityToOrg _summary_

        Args:
            orgCode (_type_): _description_
            otitle (_type_): _description_
            odate (_type_): _description_
            ostartingTime (_type_): _description_
            oendingTime (_type_): _description_
            olocation (_type_): _description_

        Returns:
            _type_: _description_
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
    
    def addTaskToOpportunity(self, task = Task(), opportunityCode = 0):
        for opportunity in self.getOpportunities():
            if opportunity.getOpportunityCode() == opportunityCode:
                opportunity.addTask(task)
            else: 
                continue
    
    def updateTaskStatus(self, opportunityCode = int, task = Task(), status = str )-> str:
        for opportunity in self.getOpportunities():
            if opportunity.getOpportunityCode() == opportunityCode:
                return opportunity.updateTaskStatus(task, status)
            else:
                continue
        else: 
            return f"Opportunity not found, try again later.."
            
    def __str__(self) -> str:
        return f"Organization name: {self.__organization_name}"


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
        self.__issueDate = datetime.today().date()  # printing the date of creation

    # functions - getters & setters

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
        self, fullname="", mobile="", email="", educationLevel="", DOJ=date, DOB=date
    ) -> None:
        super().__init__(fullname, mobile, email, educationLevel, DOJ, DOB)
        self.__userID = "A" + str(self._User__userID)

        # getters & setters

    def setUserID(self, inID):
        self.__userID = inID

    def getUserID(self):
        return self.__userID

    def registerOrganizations(self, name, description, code):
        """
        registerOrganizations _summary_

        Args:
            name (_type_): _description_
            description (_type_): _description_
            code (_type_): _description_


        Returns:
            _type_: _description_
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
        assignRepresentative _summary_

        Args:
            org (_type_, optional): _description_. Defaults to Organization().
            rep (_type_, optional): _description_. Defaults to Organization_Representative().

        Returns:
            _type_: _description_
        """
        if org:
            org.setRepresentatives(rep)
        else:
            return f"Invalid Entry"

    def generateCertificate(self, certificate=Certificate(), vol=Volunteer()):
        """
        generateCertificate _summary_

        Args:
            certificate (_type_, optional): _description_. Defaults to Certificate().
            vol (_type_, optional): _description_. Defaults to Volunteer().

        Returns:
            _type_: _description_
        """
        certificate.setVolunteer(vol)
        toPrint = f"====  -Certificate-  ====\n\tCID: {certificate.getCertificateID()}\n\tVolunteer: {self.getFullName()}\n\tIssue Date: {certificate.getIssueDate()}"

        return toPrint

