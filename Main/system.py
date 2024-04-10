from index import *
from saves import Save
from datetime import datetime, date

"""
Handling Logged-in User
"""
currentUser = []

def getLoggedUser():
    
    x = object()
    for user in currentUser:
        x = user
    return x

"""
    Volunteer Functions & Panel
"""

def viewOpportunities():
    currentOrganization = []
    while True:
        print(" ")
        print("⎧\tVolunteer Management System")
        print("⎩\tVolunteer Panel ➢ View Volunteering Opportunities ")
        print("  ")

        print("- The following are the available organizations\n")


        try:
            for obj in Organization.organizationRecord:
                print(f"\t{obj.getOrganizationName()}\n\tOrganization\nOrganization Code: {obj.getOrgCode()}\n-\n{obj.getDescription()}\n")
        except:
            print("T Function Error: please try again later..\nReturning to the previous page..") # : couldn't find organizations
            break
        else:
            pass


        try:
                userInput = str(input("Would you like to view a specific organization opportunities? ‣ "))
                userInLower = userInput.lower()
        except Exception:
                print("Invalid Input: your input must either be a 'Yes' or 'No'")
        else: 
            if userInLower == "yes":
                try:
                    userInput = str(input("Enter Organization Code ‣ "))
                except:
                    print("Invalid Input: your input must be an organization code.. e.x. 'O201'")
                else:    
                    try:
                        for obj in Organization.organizationRecord:
                            if obj.getOrgCode() == userInput:
                                print(" ")
                                print("⎧\tVolunteer Management System")
                                print(f"⎩\tVolunteer Panel ➢ View Volunteering Opportunities")
                                print("  ")
                                currentOrganization.append(obj)
                                print(f"- The following the offered opportunities by {obj.getOrganizationName()}\n")
                                
                                # Filtering to output the right message to the user in-case there was 0 opportunities in an organization
                                if len(obj.getOpportunities()) == 0:
                                    print()
                                    break
                                else:
                                    for opportunity in obj.getOpportunities():
                                        print(opportunity, "\n")
                                        
                    except: 
                        print("T Function Error: please try again later..\nReturning to the previous page..") # Error: couldn't find opportunities
                        break
                    
                    
                    try:
                        userInput = str(input("Would you like to register in an opportunity? ‣ "))
                    except:
                            print("Invalid Input: your input must be an organization code.. e.x. 'O201'")
                    else:
                        userInLower = userInput.lower() 
                        try:
                            if userInLower == "yes":
                                
                                try:
                                    userInput = int(input("Enter opportunity code ‣ "))
                                except:
                                    print("Invalid Input: your input must be an opportunity code.. e.x. '20'")
                                    
                            elif userInLower == "no":
                                print("Returning to the main page..")
                                break 
                            else:
                                raise Exception
                        except Exception:
                            print("Invalid Answer: please try again\nReturning to the previous page..")
                            break
                        else:
                            for obj in currentOrganization:
                                for opportunity in obj.getOpportunities():
                                    if opportunity.getOpportunityCode() == userInput:
                                        opportunity.setInterest(getLoggedUser())
                                        """
                                        to test the view tasks function (Will be removed later)
                                        """
                                        opportunity.addToAssignedVolunteers(getLoggedUser())
                                        
                                        currentOrganization.clear()
                                        print("You have been registered your interest successfully\nReturning to the previous page..")
                                        break
                            
            elif userInLower == "no":
                print("Alright..\nReturning to the previous page..") 
                break
            
            
def viewAssignedTasks():
    while True:
        print(" ")
        print("⎧\tVolunteer Management System")
        print(f"⎩\tVolunteer Panel ➢ View Assigned Volunteering Tasks")
        print("  ")

        
        try:
            for obj in currentUser:
                tasks = obj.getTasks()
                if len(tasks) == 0:
                    print("- You are not assigned to any tasks at the moment")
                else:
                    print("- The following are your assigned tasks\n")
                    for task in obj.getTasks():
                        print(task) # Formate the task printing
        except:
            print("T Function Error: please try again later..") # write the exception and what to do
        else:
            userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
            if userInput: 
                break
            



def viewCompletedTasks():
    while True:
        print(" ")
        print("⎧\tVolunteer Management System")
        print(f"⎩\tVolunteer Panel ➢ View Completed Volunteering Tasks")
        print("  ")
        
        try:
            for obj in currentUser:
                completedTasks = obj.getCompletedTasks()
                if len(completedTasks) == 0:
                    print("- You haven't completed any tasks yet, try again later")
                else:
                    print("- The following are your completed tasks\n")
                    for task in completedTasks:
                        print("- The following are your completed tasks\n")
                        print(task)
        except:
            print("T Function Error: please try again later..") # write the exception and what to do
        else:
            userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
            if userInput: 
                print("Returning to the previous page..")
                break


def viewVolunteeringHours():
    while True:
        print(" ")
        print("⎧\tVolunteer Management System")
        print(f"⎩\tVolunteer Panel ➢ View Completed Volunteering Hours")
        print("  ")
        
        try:
            for obj in currentUser:
                completedHours = obj.getTotalVolunteerHours()
                if completedHours == 0:
                    print("You haven't gained any volunteering credits yes, try again later")
                else:
                    print(f"You have completed {completedHours} volunteering hours")
        except:
            print("T Function Error: please try again later..") # write the exception and what to do
        else:
            userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
            if userInput: 
                print("Returning to the previous page..")
                break        

def volunteerPanel():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩      Volunteer Panel")
        print("  ")

        print("- The following are your controls as a volunteer\n")
        print("1 • View Volunteering Opportunities")
        print("2 • View Assigned Tasks")
        print("3 • View Completed Tasks")
        print("4 • View Volunteering Hours")
        print("5 • Logout")
        
        try:
            userInput = int(input("Navigate to ‣ "))
            # add if statement for out of range numbers
        except:
            print("Invalid Input: your input must be a number in range of 1 - 5")
            
        try:
            if userInput == 1:
                viewOpportunities()
            elif userInput == 2:
                viewAssignedTasks()
            elif userInput == 3:
                viewCompletedTasks()
            elif userInput == 4:
                viewVolunteeringHours()
            elif userInput == 5:
                currentUser.clear()
                print("Logged-out\nReturning to the Authorization page..")
                break
            else:
                raise Exception
        except Exception:
            print("S Panel Error: please try again later..")
            
        


"""
    Representative Functions & Panel
"""

def getOrganization(): # 
    organizationProfile = []
    try:
        for Org in Organization.organizationRecord:
            for Rep in Org.getRepresentatives():
                if Rep == getLoggedUser():
                    organizationProfile.append(Org)
                else:
                    continue
    except:
        print("T Function Error: Organization not found")
    else:
        return organizationProfile # print all the controls


def createVolunteeringOpportunity(): # standalone
    while True:
        try: 
            
            organization = getOrganization()
            
            if len(organization) == 0:
                raise Exception
            
        except Exception:
            print("T Function Error: Couldn't find any organizations related to you")
            
        else:
            
            try:
                print(" ")
                print("⎧ Volunteer Management System")
                print("⎩ Organization Representative Panel ➢ Create Volunteering Opportunity")
                print("  ")

                print("- Enter the following information\n")
                # opportunity title
                title = str(input("Title ‣ "))
                # to create a date
                yearx = int(input("Date - Year ‣ "))
                monthx = int(input("Date - Month ‣ "))
                dayx = int(input("Date - Day ‣ "))
                datetoIn = date(yearx, monthx, dayx)
                # other opportunity requirements
                startingTime = str(input("Starting time ‣ "))
                endingTime = str(input("Ending time ‣ "))
                location = str(input("Location ‣ "))
                
                print("Loading..")
                
                for Org in organization:
                    newOpportunity = Org.createOpportunity(
                        title, datetoIn, startingTime, endingTime, location
                    )
                
            except:
                print("T Function Error: Couldn't create an opportunity")
            else:
                print("The requested opportunity has been created successfully\n-\n\tOpportunity details\n\t-")
                print(newOpportunity, "\n")
                
        finally:
            print("Returning to the previous page..")
            break

def function():
    pass

def updateVolunteeringOpportunity(): # look at it later (is it logical??)
    pass


def deleteVolunteeringOpportunity():
    while True:
                print(" ")
                print("⎧ Volunteer Management System")
                print("⎩ Organization Representative Panel ➢ Delete Volunteering Opportunity")
                print("  ")


                try: 
                    
                    organization = getOrganization()
                    
                    if len(organization) == 0:
                        raise Exception
                    
                except Exception:
                    print("T Function Error: Couldn't find any organizations related to you")
                    
                else:
                    
                    try:
                        
                        print("- Choose from the following list the opportunity that you wish to delete\n")
                        
                        for Org in organization:
                            for Opportunity in Org.getOpportunities():
                                print(Opportunity, "\n")
                            
                    except:
                        print("T Function Error: Couldn't find any opportunities related your organization")
                    else:
                        
                        try:
                            userInput = str(input("Are you sure? ‣ "))
                            
                            if userInput.lower() == "no":
                                break
                            
                        except Exception:
                            print("Invalid Input: your input must a 'Yes' or 'No'")
                        else:
                            
                            if userInput.lower() == "yes":
                                try:
                                    userInput = int(input("Enter opportunity code ‣ "))
                                except:
                                    print("Invalid Input: your input must be an opportunity code.. e.x. '20'")
                                else:
                                    
                                    print("Loading..")
                                    
                                    for Org in organization:
                                        for Opportunity in Org.getOpportunities():
                                            if Opportunity.getOpportunityCode() == userInput:
                                                Org.deleteOpportunity(userInput)
                                                print("Opportunity has deleted successfully")
                            else:
                                raise Exception
                                        
                            
                finally:
                    print("Returning to the previous page..")
                    break        

def representativePanel(): # S PANEL
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Organization Representative Panel")
        print("  ")

        print("- The following are your controls as a organizer\n")
        print("1 • Create Volunteering Opportunity")
        print("2 • Update Volunteering Opportunity")
        print("3 • Delete Volunteering Opportunity")
        print("4 • Logout")
        
        try:
            userInput = int(input("Navigate to ‣ "))
            # add if statement for out of range numbers
        except:
            print("Invalid Input: your input must be a number in range of 1 - 5")
            
        try:
            if userInput == 1:
                createVolunteeringOpportunity()
            elif userInput == 2:
                print("This option is under-maintenance, try again later..")
            elif userInput == 3:
                deleteVolunteeringOpportunity()
            elif userInput == 4:
                currentUser.clear()
                print("Logged-out\nReturning to the Authorization page..")
                break
            else:
                raise Exception
            
        except Exception:
            print("S Panel Error: please try again later..")


"""
    Administrators Functions & Panel
"""

def registerOrganization():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Administrator Panel ➢ Register New Organization")
        print("  ")
        
        try:
            userInput = str(input("Are you sure? ‣ "))
            if userInput.lower() == 'no':
                break
            elif userInput.lower() == 'yes':
                print(" ")
            else:
                raise Exception
        except Exception:
            print("Invalid Input: your input must be a 'Yes' or 'No'")
        else:
        
            try:
                print("- Enter the following information\n")
                orgName = str(input("Organization name ‣ "))
                orgDescription = str(input("Organization description ‣ "))
                orgCode = int(input("Organization code 'will be altered' ‣ "))
                orgCode += len(Organization.organizationRecord)
                print("\nLoading..\n")
            except:
                print("T Function Error: invalid input..")
            
            else:
                
                try:
                    new_organization = Organization(
                        orgName, orgDescription, orgCode
                        )
                    print("Organization has been created successfully..")
                except:
                    print("T Function Error: unable to create the requested organization")
                else:
                    print(new_organization)
            
            
        finally:
            print("Returning to the previous page..")
            break
def assignRepresentative():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Administrator Panel ➢ Assign a Representative to an Organization")
        print("  ")
        
        try:
            userInput = str(input("Are you sure? ‣ "))
            if userInput.lower() == 'no':
                break
            elif userInput.lower() == 'yes':
                print(" ")
            else:
                raise Exception
        except Exception:
            print("Invalid Input: your input must be a 'Yes' or 'No'")
        else:
            
            try:
                print("- Select one of the following organizations\n")
                for Org in Organization.organizationRecord:
                    if Org.getDescription() == "":
                        continue
                    else:
                        print(Org, "\n")
            except:
                print("T Function Error: unable to access organizations")
            else:
                
                try:
                    userInput = str(input("Organization code ‣ "))
                except:
                    print("Invalid Input: your input must start with 'O' then the organization code")
                else:
                    
                    try:
                        selectedOrg = []
                        print("Loading..")
                        for Org in Organization.organizationRecord:
                            if Org.getOrgCode() == userInput:
                                selectedOrg.append(Org)
                                print("Organization accessed..")
                            else:
                                continue
                    except:
                        print("T Function Error: unable to find the requested organization")
                    else:
                        
                        try:
                            print("- Select one of the following representatives\n")
                            for Rep in Organization_Representative.organizersRecord:
                                if Rep.getFullName() == "":
                                    continue
                                else:
                                    print(Rep, "\n")
                        except:
                            print("T Function Error: unable to access representatives")
                        else:
                            
                            try:
                                userInput = str(input("Representative ID ‣ O"))
                            except:
                                print("Invalid Input: your input must start with 'O' then the representative id")
                            else:                        
                                
                                try:
                                    print("Loading..")
                                    selectedRep = []
                                    for Rep in Organization_Representative.organizersRecord:
                                        if Rep.getRepID() == ("O" + userInput):
                                            selectedRep.append(Rep)
                                            print("Representative accessed..")
                                        else: 
                                            continue
                                except:
                                    print("T Function Error:  unable to find the requested representative")
                                else:
                                    
                                    try:
                                        print("Loading..")
                                        for Org in selectedOrg:
                                            for Rep in selectedRep:
                                                Org.setRepresentative(Rep)
                                    except:
                                        print("T Function Error: unable to process your request")
                                    else:
                                        print("Your request has been processed successfully..")
                    
                    
        finally:
            print("Returning to the previous page..")
            break
def generateCertificate():
    pass

def generateStatistics():
    pass
def administratorPanel():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Administrator Panel")
        print("  ")

        print("- The following are your controls as an administrator\n")
        print("1 • Register New Organization")
        print("2 • Assign a Representative to an Organization")
        print("3 • Create Volunteer Certificate")
        print("4 • Get System Statistics")
        print("5 • Logout")        
        
        try:
            userInput = int(input("Navigate to ‣ "))
            # add if statement for out of range numbers
        except:
            print("Invalid Input: your input must be a number in range of 1 - 5")
            
        try:
            if userInput == 1:
                registerOrganization()
            elif userInput == 2:
                assignRepresentative()
            elif userInput == 3:
                print("This option is under-maintenance, try again later..")
            elif userInput == 4:
                print("This option is under-maintenance, try again later..")
            elif userInput == 5:
                currentUser.clear()
                print("Logged-out\nReturning to the Authorization page..")
                break
            else:
                raise Exception
            
        except Exception:
            print("S Panel Error: please try again later..")        
        




"""
Account creation functions    
"""


def createVolAccount():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Authorization ➢ Create a Volunteer Account")
        print("  ")

        print("- Enter the following information to register as a Volunteer")
        try:
            fullname = str(input("Full name ‣ "))
            mobile = str(input("Mobile number ‣ "))
            email = str(input("Email ‣ "))
            educationLevel = str(input("Education level as 'Bachelor, Masters or PhD' ‣ "))
            Year = int(input("Date of Birth - Year ‣ "))
            Month = int(input("Date of Birth - Month ‣ "))
            Day = int(input("Date of Birth - Day ‣ "))
            DOJ = date.today()
            DOB = date(Year, Month, Day)
            skills = str(input("Skills separated by , ‣ "))
        except:
            print("Invalid Request: something went wrong, try again later.")
        else:
            try:
                volunteer = Volunteer(
                fullname, mobile, email, educationLevel, DOJ, DOB, skills
            )
                currentUser.append(volunteer)
                print("Your account has been created successfully!")
                for obj in currentUser:
                    print(obj)
                for vol in Volunteer.volunteerRecord: # remove 
                    print(vol)
            except:
                print("Invalid Request: something went wrong, try again later.")    
            else:
                print("Redirecting you to volunteer panel..")
                volunteerPanel()



def login():
    """
    login is going to contain the login of volunteer, representative, and administrator
    """

    while True:

        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩      Authorization ➢ Login       ")
        print("  ")

        print("- Enter the following information to login")
        try:
            user_id = str(input("Username ‣ "))
            #userActualID = user_id.strip(user_id[5:-1])
            x = ""
            
                
            if user_id.startswith('V'):
                for volunteer in Volunteer.volunteerRecord:
                    if volunteer.getUserID() == user_id :
                        currentUser.append(volunteer)
                        volunteerPanel()
                        x = "V"
                for y in currentUser:
                    print(y)
            elif user_id.startswith('O'):
                for organizer in Organization_Representative.organizersRecord:
                    if organizer.getUserID() == user_id:
                        currentUser.append(organizer)
                        representativePanel()
                        x = "O"
                for y in currentUser: 
                    print(y)
                break
            elif user_id.startswith('A'):
                for admin in Administrator.administratorsRecord:
                    if admin.getUserID() == user_id:
                        currentUser.append(admin)
                        administratorPanel()
                        x = "A"
                print(x)
                break
            else:
                raise Exception

        except Exception:
            print("Invalid Username: try again later.")
        else:
            break


def system():
    """
    system _summary_

    Raises:
        Exception: _description_
    """
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩      Authorization       ")
        print("  ")

        print("- Select your login method\n")
        print("1 • Existing Account")
        print("2 • Create Volunteer Account")
        print("3 • Load Testing File")
        print("4 • Exit")

        try:
            options = [1,2,3,4,0,9]
            userInput = int(input("Login method ‣ "))
            if userInput not in options:
                raise Exception
        except Exception:
            print("Invalid Input: your input must be a number in range of 1 - 2")
        else:
            try:
                if userInput == 1:
                    login()
                elif userInput == 2:
                    createVolAccount()
                elif userInput == 3:
                    try:
                        if len(Task.tasksRecord) == 6:
                            backUp = Save()
                            backUp.load()
                            print("Testing file has been loaded successfully")
                        else:
                            print("Testing file is already loaded")
                    except:
                        print("Failed to load testing file")
                elif userInput == 4:
                    for obj in currentUser:
                        print(obj)
                elif userInput == 0:
                    for org in Organization.organizationRecord:
                        for rep in org.getRepresentatives():
                            print(rep)
                elif userInput == 9:
                    for admin in Administrator.administratorsRecord:
                        print(admin)
                        
                else:
                    raise Exception
            except Exception:
                print("Try again..")




    """
    Testing Section
    """

for obj in currentUser:
    print(obj, "\n")
    
for obj in Organization_Representative.organizersRecord:
    print(obj)
for obj in Volunteer.volunteerRecord:
    print(obj)
system()
