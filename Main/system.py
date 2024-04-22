from index import *
from saves import Save
from datetime import datetime, date
"""

Title: Volunteer Management System
File: system.py
Imports: index.py / saves.py / datetime
Use of File: front-end of the system, called as the "Panel" of the overall system
and used to execute different set of actions, and tasks throughout the system
Author(s): Hamad Almazrouei, Abdullah Alzaabi, Tahnoon Alzaabi

"""


"""
    Handling Logged-in User & its related functions
"""

currentUser = []

def getLoggedUser() -> object:
    
    x = object()
    for user in currentUser:
        x = user
        
    return x

def getLoggedUserName() -> str:
    
    x = ""
    for user in currentUser:
        x = user.getFullName()
        
    return x

def getLoggedUserID() -> str:
    
    x = ""
    for user in currentUser:
        x = user.getUserID()
        
    return x


"""
    Activity logging
"""
# logins activity
system_logins = 0
system_f_logins = 0
system_s_logins = 0
# new users, and opportunities view requests
system_op_views = 0
system_new_users = 0


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
                if obj.getOrganizationName() == "":
                    continue
                else:
                    print(f"\t{obj.getOrganizationName()}\n\tOrganization\nOrganization Code: {obj.getOrgCode()}\n-\n{obj.getDescription()}\n")
        except:
            print("T Function Error: failure in accessing organizations..\nReturning to the previous page..") # : couldn't find organizations
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
                    userInput = str(input("Organization Code ‣ "))
                    userInput = userInput.upper()
                except:
                    print("Invalid Input: your input must be an organization code.. e.x. 'O201'")
                else:   
                    
                    try:
                        xFilter = ""
                        
                        for obj in Organization.organizationRecord:
                            if obj.getOrgCode() == userInput:
                                xFilter = "0"
                                print(" ")
                                print("⎧\tVolunteer Management System")
                                print(f"⎩\tVolunteer Panel ➢ View Volunteering Opportunities")
                                print("  ")
                                currentOrganization.append(obj)
                                print(f"- The following the offered opportunities by {obj.getOrganizationName()}\n")
                                
                                # Filtering to output the right message to the user in-case there was 0 opportunities in an organization
                                if len(obj.getOpportunities()) == 0:
                                    print("The requested organization is not offering any opportunities, try again later..")
                                    break
                                else:
                                    global system_op_views
                                    system_op_views += 1
                                    for opportunity in obj.getOpportunities():
                                        print(opportunity, "\n")
                        
                        if xFilter != "0":
                            raise Exception

                    except Exception : 
                        print("T Function Error: failure in accessing organization opportunities..\nReturning to the previous page..") # Error: couldn't find opportunities
                        break
                    
                    
                    try:
                        userInput = str(input("Would you like to register in an opportunity? ‣ "))
                    except:
                            print("Invalid Input: your input must be a 'Yes' or 'No'")
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
                            print("Invalid Answer: please try again later..\nReturning to the previous page..")
                            break
                        else:
                            for obj in currentOrganization:
                                for opportunity in obj.getOpportunities():
                                    if opportunity.getOpportunityCode() == userInput:
                                        
                                        opportunity.setInterest(getLoggedUser())
                                        currentOrganization.clear() # Cleared cache of the selected organization
                                        print("You have been registered your interest successfully\nReturning to the previous page..")
                                        break
                            
            elif userInLower == "no":
                print("Returning to the previous page..") 
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
                    print("\n")
                else:
                    print("- The following are your assigned tasks\n")
                    for task in obj.getTasks():
                        print(task) # Formate the task printing
        except:
            print("T Function Error: failure in accessing user tasks, please try again later..") # write the exception and what to do
        else:
            userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
            if userInput: 
                print("Returning to the previous page..")
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
                    print("\n")
                else:
                    print("- The following are your completed tasks\n")
                    for task in completedTasks:
                        print(task)
        except:
            print("T Function Error: failure in accessing user completed tasks, please try again later..") # write the exception and what to do
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
                    print("You haven't been credited with any volunteering hours yet, try again later")
                    print("\n")
                else:
                    print(f"You have completed {completedHours} volunteering hours")
                    print("\n")
        except:
            print("T Function Error: failure in accessing user completed volunteering hours, please try again later..") # write the exception and what to do
        else:
            userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
            if userInput: 
                print("Returning to the previous page..")
                break        

def volunteerPanel():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎪ Volunteer Panel")        
        print(f"⎩ Welcome {getLoggedUserName()}!")
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
                print("You have been logged-out..\nReturning to the Authorization page..")
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
        print("T Function Error: failure in accessing organization of representative")
    else:
        return organizationProfile # print all the controls


def createVolunteeringOpportunity(): # standalone
    while True:
        try: 
            
            organization = getOrganization()
            
            if len(organization) == 0:
                raise Exception
            
        except Exception:
            print("T Function Error: couldn't find any organizations related to you")
            
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
                print("The requested opportunity has been created successfully")
                
        finally:
            print("Returning to the previous page..")
            break


def updateVolunteeringOpportunity(): 
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Organization Representative Panel ➢ Update Volunteering Opportunity")
        print("  ")        
        
        repOrganization = getOrganization() # use loop cause it will return a list
        selectedOpportunity = ""
        taskCache = 0
        try:
            
            try:
                print("- Choose from the following list the opportunity that you wish to update\n")
                        
                for Org in repOrganization:
                    for Opportunity in Org.getOpportunities():
                        print(Opportunity, "\n")                
            except:
                print("T Function Error: failure in accessing organization opportunities")
            else:

                try:
                    # print("- Enter the following information")
                    opCode = int(input("Opportunity Code ‣ "))
                        
                except:
                    print("Invalid Input: your input should be an integer and related to an opportunity")
                else:
                    # try then print all of the update options
                    selectedOpportunity = opCode
                    
                    try:
                        print("\n")
                        print("Loading opportunities..\n")
                        xFilter = ""
                        for Org in repOrganization:
                            for Opportunity in Org.getOpportunities():
                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                    print("Opportunity accessed..\n")
                                    xFilter = "0"
                                else:
                                    continue
                        
                            if xFilter == "0":
                                continue
                            else:
                                raise Exception
                            
                    except Exception:
                        print("T Function Error: failure in accessing organization opportunity ")
                    else:
                        
                        print("- The following are your opportunity controls\n")
                        print(" ")
                        print("1 • Update Title")
                        print("2 • Update Date")
                        print("3 • Update Starting Time")
                        print("4 • Update Ending Time")
                        print("5 • Update Location ")
                        print("6 • Update Task ")
                        print("7 • Control Volunteers ")                                      
                        print("8 • Exit ")        
                        print(" ")
                        try:
                            optionsOfIn = [1,2,3,4,5,6,7,8]
                            
                            user_input = int(input("Selection ‣ "))
                            
                            if user_input not in optionsOfIn:
                                raise Exception
                            
                        except Exception:
                            print("Invalid Input: your input must be an integer in range of 1 - 6")
                            
                        else:
                            print("\n")
                            if user_input == 1:
                                try:
                                    newTitle = str(input("New Title ‣ "))
                                except:
                                    print("Invalid Input: your Title must be string")
                                else:
                                    try:
                                        for Org in repOrganization:
                                            for Opportunity in Org.getOpportunities():
                                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                    Opportunity.setTitle(newTitle)
                                                    print("Your opportunity title has been altered successfully..\n")
                                                else:
                                                    continue
                                    except:
                                        print("T Function Error: unable to alter opportunity title")
                            elif user_input == 2:
                                try:
                                    inYear = int(input("Year ‣ "))
                                    inMonth = int(input("Month ‣ "))
                                    inDay = int(input("Day ‣ "))  
                                    dateIn = date(inYear, inMonth, inDay)
                                    if not dateIn:
                                        raise Exception
                                except Exception:
                                    print("Invalid Input: your input must represent a date")  
                                else:
                                    print("\n")
                                    try:
                                        for Org in repOrganization:
                                            for Opportunity in Org.getOpportunities():
                                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                    Opportunity.setDate(dateIn)
                                                    print("Your opportunity date has been altered successfully..\n")
                                                else:
                                                    continue 
                                    except:
                                        print("T Function Error: unable to alter opportunity date")
                            elif user_input == 3:
                                try:
                                    new_starting_time = str(input("New Starting Time ‣ "))
                                except:
                                    print("Invalid Input: your input must represent a date")
                                else:
                                    print("\n")
                                    try:
                                        for Org in repOrganization:
                                            for Opportunity in Org.getOpportunities():
                                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                    Opportunity.setStartingTime(new_starting_time)
                                                    print("Your opportunity starting time has been altered successfully..\n")
                                                else:
                                                    continue
                                    except:
                                        print("T Function Error: unable to alter opportunity starting date")    
                            elif user_input == 4:
                                try:
                                    new_ending_time = str(input("New Ending Time ‣ "))
                                except:
                                    print("Invalid Input: your input must represent an Ending Time")
                                else:
                                    print("\n")
                                    try:
                                        for Org in repOrganization:
                                            for Opportunity in Org.getOpportunities():
                                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                    Opportunity.setEndTime(new_ending_time)
                                                    print("Your opportunity ending time has been altered successfully..\n")
                                                else:
                                                    continue
                                    except:
                                        print("T Function Error: unable to alter opportunity ending date") 
                            elif user_input == 5:
                                try:
                                    new_Location = str(input("New Location ‣ "))
                                except:
                                    print("Invalid Input: your input must represent a Location")
                                else:
                                    print("\n")
                                    try:
                                        for Org in repOrganization:
                                            for Opportunity in Org.getOpportunities():
                                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                    Opportunity.setLocation (new_Location)
                                                    print("Your opportunity location has been altered successfully..\n")
                                                else:
                                                    continue
                                    except:
                                        print("T Function Error: unable to alter opportunity Location") 
                                        
                            elif user_input == 6:
                                try:
                                    print("\n")
                                    print("Loading tasks..\n")
                                    
                                    for Org in repOrganization:
                                        for Opportunity in Org.getOpportunities():
                                            if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                if len(Opportunity.getTasks()) == 0:
                                                    print(f"'{Opportunity.getTitle()}' opportunity has no tasks assigned to it yet, try again later..")
                                                    raise Exception
                                                else:
                                                    print("Tasks accessed..\n")
                                                    for task in Opportunity.getTasks():
                                                        print(task, "\n")
                                except Exception:
                                    print("T Function Error: unable to access opportunity tasks")
                                else:
                                    
                                    try:
                                        secUserInput = int(input("Task no ‣ "))
                                    except:
                                        print("Invalid Input: your input must be an integer of a task code")
                                    else:
                                        print("\n")
                                        taskCache = secUserInput
                                        xFilter = ""
                                        for Org in repOrganization:
                                            for Opportunity in Org.getOpportunities():
                                                if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                    for task in Opportunity.getTasks():
                                                        if task.getTaskNo() == taskCache:
                                                            try:
                                                                print(f"- The following are your '{task.getTitle()}' task controls\n")
                                                                print("1 • Update Title")
                                                                print("2 • Update Status")
                                                                print("3 • Exit")
                                                                print("\n")
                                                                xFilter = "0"
                                                                try:
                                                                    choices = [1,2,3]
                                                                    thiUserInput = int(input("Selection ‣ "))
                                                                    if thiUserInput not in choices:
                                                                        raise Exception
                                                                except Exception:
                                                                    print("Invalid Input: your input must be an integer") 
                                                                else:
                                                                    print("\n")
                                                                    if thiUserInput == 1:
                                                                        try:
                                                                            forUserInput = str(input("New Title ‣ "))
                                                                        except Exception:
                                                                            print("Invalid Input: your input must be an string") 
                                                                        else:
                                                                            print("\n")
                                                                            try:
                                                                                task.setTitle(forUserInput)
                                                                            except:
                                                                                print("F Function Error: failure in the process of altering task")
                                                                            else:
                                                                                print("Your task title has been altered successfully..\n")
                                                                        
                                                                    elif thiUserInput == 2: 
                                                                        try:
                                                                            print("Recommended Status Selection ☛ 'Pending', 'Paused', 'Ongoing', 'Completed', 'Canceled'")
                                                                            fifUserInput = str(input("New Status ‣ "))
                                                                        except Exception:
                                                                            print("Invalid Input: your input must be an string")
                                                                        else:
                                                                            print("\n")
                                                                            try:
                                                                                print("Loading task status..")  
                                                                                Opportunity.updateTaskStatus(task, fifUserInput)
                                                                            except:
                                                                                print("F Function Error: failure in altering task")
                                                                            else:
                                                                                print("Your task status has been altered successfully..\n")
                                                                    elif thiUserInput == 3:
                                                                        break
                                                            except Exception:
                                                                print("T Function Error: failure in initializing task controls")                                                         
                                                    if xFilter != "0":
                                                        print("Opportunity does not contain any task with the request code, try again later.. ")
                            elif user_input == 7:
                                try:
                                    print(f"- The following are your volunteer controls\n")
                                    print("1 • View Volunteers Interest List")
                                    print("2 • View Assigned Volunteers List")
                                    print("3 • Exit")
                                    print("\n")
                                    
                                    try:
                                        choices = [1,2,3]
                                        user_input = int(input("Selection ‣ "))
                                        if user_input not in choices:
                                            raise Exception
                                    except:
                                        print("Invalid Input: your input must be an integer and a menu selection e.x. '1, 2, or 3 to exit'") 
                                    else:
                                        print("\n")
                                        if user_input == 1:
                                            
                                            print("Loading Volunteers Interest List..\n")
                                            try:
                                                for Org in repOrganization:
                                                    for Opportunity in Org.getOpportunities():
                                                        if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                            if len(Opportunity.getInterest()) == 0:
                                                                print(f"'{Opportunity.getTitle()}' opportunity has no interest at the moment, try again later..\n")
                                                                break
                                                            else:
                                                                print("Volunteers Interest List accessed..\n")
                                                                for interest in Opportunity.getInterest():
                                                                    print(interest, "\n")
                                            except:
                                                print("T Function Error: failure in accessing volunteer interest list")
                                            else:
                                                userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
                                                if userInput: 
                                                    break
                                            
                                        elif user_input == 2:
                                            xFilter = False
                                            try:
                                                for Org in repOrganization:
                                                    for Opportunity in Org.getOpportunities():
                                                        if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                            
                                                            if len(Opportunity.getInterest()) == 0:
                                                                print(f"'{Opportunity.getTitle()}' opportunity has no interest at the moment, try again later..\n")
                                                                xFilter = True
                                                                userInput = str(input("Click 'Space then Enter' to return to the previous page ‣ "))
                                                                if userInput: 
                                                                    break
                                                            else:
                                                                print("Volunteers Interest List accessed..\n")
                                                                print("⏛"*20, "\n")
                                                                for interest in Opportunity.getInterest():
                                                                    print(interest, "\n")

                                                            if len(Opportunity.getAssignedVolunteers()) == 0:
                                                                print("⏛"*20, "\n")
                                                                print(f"'{Opportunity.getTitle()}' opportunity has no assigned volunteers at the moment\n")
                                                            else:
                                                                print("Assigned Volunteers List accessed..\n")
                                                                print("⏛"*20, "\n")
                                                                for assigned in Opportunity.getAssignedVolunteers():
                                                                    print(assigned, "\n")
                                            except:
                                                print("T Function Error: failure in accessing volunteers lists")
                                            else:
                                                if xFilter != True:
                                                    try:
                                                        choices = ["yes", "no"]
                                                        secInput = str(input("Do you wish to assign a volunteer? ‣ "))
                                                        secInput = secInput.lower()
                                                        if secInput not in choices:
                                                            raise Exception
                                                        
                                                    except Exception:
                                                        print("Invalid Input: your input must be 'Yes' or 'No'")
                                                    else:
                                                        
                                                        if secInput == "yes":
                                                            
                                                            try:
                                                                thiInput = int(input("Volunteer ID ‣ V"))
                                                                thiInput = "V" + str(thiInput)
                                                            except:
                                                                print("Invalid Input: your input must be a integer that represent a volunteer ID")
                                                            else:
                                                                
                                                                try:
                                                                    xFilter = ""
                                                                    print("Loading volunteer..\n")
                                                                    volCache = []
                                                                    for volunteer in Volunteer.volunteerRecord:
                                                                        if volunteer.getUserID() == thiInput:
                                                                            volCache.append(volunteer)
                                                                            xFilter = "0"
                                                                            print("Volunteer accessed..\n")
                                                                        else:
                                                                            continue
                                                                    
                                                                    if xFilter != "0":
                                                                        raise Exception
                                                                        
                                                                except Exception:
                                                                    print("F Function Error: failure in accessing the requested volunteer")
                                                                else:
                                                                    
                                                                    print("Processing request..\n")
                                                                    try:
                                                                        for volunteer in volCache:
                                                                            for Org in repOrganization:
                                                                                for Opportunity in Org.getOpportunities():
                                                                                    if Opportunity.getOpportunityCode() == selectedOpportunity:
                                                                                        if volunteer in Opportunity.getInterest():
                                                                                            Opportunity.addToAssignedVolunteers(volunteer)
                                                                                            print(f"Volunteer '{volunteer.getFullName()}' has been added to '{Opportunity.getTitle()}' opportunity successfully..")
                                                                                        else:
                                                                                            print(f"Volunteer '{volunteer.getFullName()}' did not assign his interest for this opportunity..")
                                                                                            raise Exception
                                                                    except:
                                                                        print("F Function Error: failure in processing request")
                                                                    else:
                                                                        volCache.clear()
                                                                        xFilter = ""
                                                                        # Can be used for timers
                                                                    
                                                        elif secInput == "no":
                                                            break
                                                else:
                                                    xFilter = False
                                                    print("")
                                                
                                        elif user_input == 3:
                                            break
                                        
                                except:
                                    print("T Function Error: failure in initializing volunteer controls")
                                else:
                                    pass

                            elif user_input == 8:
                                break    
                                
        except:
            print('Panel Error')
        else:
            pass
        finally:
            print("Returning to the previous page..")
            break


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
                                    userInput = int(input("Enter Opportunity Code ‣ "))
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
        print("⎪ Organization Representative Panel")
        print(f"⎩ Welcome {getLoggedUserName()}!")
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
                updateVolunteeringOpportunity()
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
                                            print("Representative found..")
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
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Administrator Panel ➢ Generate Certificate")
        print("  ")
        print("- Enter the following information\n")
        
        volunteerPointer = []
        
        try:
            userInput = input("Volunteer code ‣ V")
        except:
            print("Invalid Input: your input needs to be an integer")
        else:
            userInput = "V" + str(userInput)
            
            
            try:
                print("Loading..")
                for volunteer in Volunteer.volunteerRecord:
                    if volunteer.getUserID() == userInput:
                        volunteerPointer.append(volunteer)
                        print("Volunteer found..")
                    else:
                        continue
            except:
                print("T Function Error: unable to access volunteer")
            else:
                print("Gathering volunteer details..")
                vName = ""
                vCredits = 0
                cIssueDate = date.today()
                try:
                    for volunteer in volunteerPointer:
                        vName = str(volunteer.getFullName())
                        vCredits = int(volunteer.getTotalVolunteerHours())
                except:
                    print(f"T Function Error: processing failure")
                else:
                    print("Creating certificate..\n")
                    
                    try:                    
                        print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
                        print(f"\t\t\t\t {vName}\n")
                        print(f"\tThis certificate is awarded to the mentioned volunteer in appreciation \n\t     of their invaluable volunteer services and contributions\n\n\t Your selfless dedication, hard work, and generosity have made a \n\t    significant impact, and we are grateful for your support.\n")
                        print("\t  Volunteering Hours\t\t\t\tIssue Date")
                        print(f"\t\t⎯⎯⎯⎯\t\t\t\t\t   ⎯⎯⎯⎯")
                        print(f"\t\t  {vCredits}\t\t\t\t\t{cIssueDate}")
                        print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n")
                    except:
                        print("T Function Error: failed to print certificate") 
                    
                        
        finally:        
            print("Returning to the previous page..")
            break

def generateStatistics():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩ Administrator Panel ➢ System Statistics")
        print("  ")
        
        admins = 0
        representatives = 0
        volunteers = 0
        
        t_tasks = 0
        
        organizations = 0
        opportunities = 0
        
        try:
            # USER STATS
            try:
                print("Loading volunteers..")
                for vol in Volunteer.volunteerRecord:
                    if vol.getFullName() == "":
                        continue
                    else:
                        volunteers += 1
                print("Loading representatives..")                        
                for rep in Organization_Representative.organizersRecord:
                    if rep.getFullName() == "":
                        continue
                    else:
                        representatives += 1
                print("Loading administrators..")                        
                for adm in Administrator.administratorsRecord:
                    if adm.getFullName() == "":
                        continue
                    else:
                        admins += 1
            except:
                print("T Function Error: failure in processing users")
            else:
                # TASKS STATS
                try:
                    print("Loading tasks..")
                    for task in Task.tasksRecord:
                        if task.getTitle() == "":
                            continue
                        else:
                            t_tasks += 1
                except:
                    print("T Function Error: failure in processing tasks")
                else:
                    # ORGANIZATIONS STATS
                    try:
                        print("Loading organizations & opportunities..")
                        for org in Organization.organizationRecord:
                            if org.getOrganizationName() == "":
                                continue
                            else:
                                organizations += 1
                                for op in org.getOpportunities():                        
                                    if op.getTitle() == "":
                                        continue
                                    else:
                                        opportunities += 1
                    except:
                        print("T Function Error: failure in processing organizations & opportunities")
                    else:
                        # SYSTEM STATS           
                        try:
                            print("Loading final report..")
                            users_text = f"\n\t⎝ USERS STATISTICS ⎠\n \nVolunteers: {volunteers}\nOrganization Representatives: {representatives}\nAdministrators: {admins}\nTotal of Users: {(volunteers+representatives+admins)}\n"
                            task_text = f"\n\t⎝ TASKS STATISTICS ⎠\n \nTasks: {t_tasks}\n"
                            org_text = f"\n\t⎝ ORGANIZATIONS STATISTICS ⎠\n\nOrganizations: {organizations}\nOpportunities: {opportunities}\n"
                            system_text = f"\n\t⎝ SYSTEM STATISTICS ⎠\n \nSuccessful Logins: {system_s_logins}\nFailed Logins: {system_f_logins}\nTotal Login Attempts: {system_logins}\n\t-\nOpportunities View Requests: {system_op_views}\nTotal New Volunteers: {system_new_users}\n"
                            print(users_text, task_text, org_text, system_text)
                        except:
                            print("T Function Error: failure in final processing")
                        else:
                            print(" ")             
            
        except:
            print("S Panel Error: try again later")
        else:
            pass # MAY ADD "DO YOU WANT TO EXIT THIS PAGE?" TO GIVE THEM A CHANCE TO VIEW DATA
        finally:
            print("Returning to the previous page..")
            break

def administratorPanel():
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎪ Administrator Panel")
        print(f"⎩ Welcome {getLoggedUserName()}!")
        print("  ")

        print("- The following are your controls as an administrator\n")
        print("1 • Register New Organization")
        print("2 • Assign a Representative to an Organization")
        print("3 • Generate Volunteer Certificate")
        print("4 • Get System Statistics")
        print("5 • Logout")        
        print(" ")
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
                generateCertificate()
            elif userInput == 4:
                generateStatistics()
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

createVxFilter = False # Created here as a static variable to prevent function conflict

def createVolAccount():
    while True:
        global createVxFilter
        try:
            if createVxFilter == True:
                print(" ")
                print("Restriction: You have already been registered as a volunteer")
            else:
                print(" ")
                print("⎧ Volunteer Management System")
                print("⎩ Authorization ➢ Create a Volunteer Account")
                print("  ")                
                print("- Enter the following information to register as a Volunteer")
                
                fullname = str(input("Full name ‣ "))
                mobile = str(input("Mobile number ‣ "))
                email = str(input("Email ‣ "))
                educationLevel = str(input("Education level as 'Bachelor, Masters or PhD' ‣ "))
                Year = int(input("Date of Birth - Year ‣ "))
                Month = int(input("Date of Birth - Month ‣ "))
                Day = int(input("Date of Birth - Day ‣ "))
                DOB = date(Year, Month, Day)
                skills = str(input("Skills separated by , ‣ "))
                
        except:
            print("Invalid Request: something went wrong, try again later.")
        else:
            if createVxFilter == True:
                print(" ")
                system()
            else:
                try:
                    volunteer = Volunteer(
                    fullname, mobile, email, educationLevel,  DOB, skills
                )
                    currentUser.append(volunteer)
                    print("Your account has been created successfully!")
                    createVxFilter = True
                    
                    for obj in currentUser:
                        print(obj,"\n")
                except:
                    print("Invalid Request: something went wrong, try again later.")    
                else:
                    global system_new_users
                    system_new_users += 1
                    print("Redirecting you to volunteer panel..")
                    login()



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
        global system_logins, system_s_logins
        system_logins += 1

        try:
            user_id = str(input("Username ‣ "))
            user_id = user_id.upper()
            #userActualID = user_id.strip(user_id[5:-1])
            x = ""
            global system_s_logins, system_f_logins
            xFilter = False
            
            if user_id.startswith('V'):
                for volunteer in Volunteer.volunteerRecord:
                    if volunteer.getUserID() == user_id :
                        currentUser.append(volunteer)
                        system_s_logins += 1
                        xFilter = True
                        volunteerPanel()
                else:
                    if xFilter == False:
                        system_f_logins += 1
                        print("Invalid Username: the entered username doesn't match any user in our records, try again later..")
                    else:
                        xFilter = False
                    

            elif user_id.startswith('O'):
                for organizer in Organization_Representative.organizersRecord:
                    if organizer.getUserID() == user_id:
                        system_s_logins += 1
                        xFilter = True
                        currentUser.append(organizer)
                        representativePanel()
                        
                else:
                    if xFilter == False:
                        system_f_logins += 1
                        print("Invalid Username: the entered username doesn't match any user in our records, try again later..")
                    else:
                        xFilter = False

            elif user_id.startswith('A'):
                for admin in Administrator.administratorsRecord:
                    if admin.getUserID() == user_id:
                        system_s_logins += 1
                        xFilter = True
                        currentUser.append(admin)
                        administratorPanel()
                        
                else:
                    if xFilter == False:
                        system_f_logins += 1
                        print("Invalid Username: the entered username doesn't match any user in our records, try again later..")
                    else:
                        xFilter = False
                    

            else:
                raise Exception

        except Exception:
            print("Invalid Input: your input formate is incorrect, try again later..")
        else:
            break


def system():
    """
    system _summary_

    Raises:
        Exception: _description_
    """
    while True:
        print("  ")
        print("⎧ Volunteer Management System")
        print("⎩      Authorization       ")
        print("  ")
        print("- Select your login method\n")
        print("1 • Existing Account")
        print("2 • Create Volunteer Account")
        print("3 • Load Testing File")
        print("4 • Exit")
        
        createAccount = False
        
        try:
            options = [1,2,3,4,0,8,9]
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
                    try:
                        createVolAccount()
                        createAccount = True
                    except:
                        print("Error xFilter: unable to run create volunteer xFilter in sys..")
                    else:
                        if createAccount == True:
                            createAccount = False
                            print(" ")
                            break
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
                    print("Shutting Down..")
                    print("System Down")
                    break
                elif userInput == 9:
                    for org in Organization.organizationRecord:
                        for rep in org.getRepresentatives():
                            print(rep)
                elif userInput == 0:
                    for admin in Administrator.administratorsRecord:
                        print(admin)
                elif userInput == 8:
                    for vol in Volunteer.volunteerRecord:
                        print(vol)        
                else:
                    raise Exception
            except Exception:
                print("Try again..")
system()