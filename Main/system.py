from index import *
from datetime import datetime, date

currentUser = []

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
                volunteer = Volunteer(
                    fullname, mobile, email, educationLevel, DOJ, DOB, skills
                )
                currentUser.append(volunteer)
                print("Your account has been created successfully!")
                # append the user ????
        finally:
            print("Returning to Previous Menu...")
                
        break


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
            userActualID= user_id.strip(user_id[0])
            x = ""
            if user_id.startswith('V'):
                for volunteer in Volunteer.volunteerRecord:
                    if volunteer.getUserID() == userActualID:
                        currentUser.append(volunteer)
                        x = "V"
                    print(x, volunteer)
            elif user_id.startswith('O'):
                for organizer in Organization_Representative.organizersRecord:
                    if organizer.getUserID() == userActualID:
                        currentUser.append(organizer)
                        x = "O"
                print(x)
            elif user_id.startswith('A'):
                for admin in Administrator.administratorsRecord:
                    if admin.getUserID() == userActualID:
                        currentUser.append(admin)
                        x = "A"
                print(x)
            else:
                print("Invalid ID")
                
        except:
            print("Invalid Request: something went wrong, try again later.")
        else:
            print(x)


    
    
def startPanel():
    
    while True:
        print(" ")
        print("⎧ Volunteer Management System")
        print("⎩      Authorization       ")
        print("  ")
        
        print("- Select your login method\n")
        print("1 • Existing Account")
        print("2 • Create Volunteer Account")
        print("3 • Return to Previous Menu")
        
        try:
            userInput = int(input("Login method ‣ "))
        except:
            print("Invalid Input: your input must be a number in range of 1 - 2")
    
        try:
            if userInput == 1:
                login()
            elif userInput == 2:
                createVolAccount()
            elif userInput == 3: 
                break
            else:
                raise Exception
        except Exception:
            print("Error")
        finally:
            print("Returning to Previous Menu...")
            

VOL1 = Volunteer("awdawdad", "234234234", "dwadadaw", "wadadad", date(2001, 12, 12), date.today(), "awdawd,dawd")
print(VOL1.getUserID())
startPanel()

"""
    Volunteer Functions & Panel
"""
def viewOpportunities():
    pass

def viewAssignedTasks():
    pass

def viewCompletedTasks():
    pass

def viewVolunteeringHours():
    pass




def volunteerPanel():
    pass

"""
    Representative Functions & Panel
"""
def representativePanel():
    pass

"""
    Administrators Functions & Panel
"""
def administratorPanel():
    pass
    











def login():
    """
    login is going to contain the login of volunteer, representative, and administrator
    """
    pass    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def system():
    # While the function is called print the options and ask the user to select from 1-6
    while True:
        print(" ")
        print("  Electronic Coffee System")
        print("|__________________________|")
        print("1. Add a New Order")
        print("2. List All Orders")
        print("3. Find an Order")
        print("4. Delete an Order")
        print("5. Save and Display Result")
        print("6. Exit")
        print("|__________________________|")

        userIn = int(input("Enter your request from the list above (1-6): "))

        # Creating if statements that calls function depending on the user input that the system function received
        if userIn == 1:
            add_order()
        elif userIn == 2:
            list_orders()
        elif userIn == 3:
            find_order()
        elif userIn == 4:
            del_orders()
        elif userIn == 5:
            save()
        elif userIn == 6:
            print("Exiting system, goodbye!")
            break
        else:
            print("Invalid input, please select an option between 1 and 6 ..")


#