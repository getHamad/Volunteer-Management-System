from datetime import date, datetime
from index import *


class Save:
    
    def __init__(self) -> None:
        self.saveNo = 1
    def load(self):
        # 10 Tasks
        Food_Distribution= Task(
            "Food Distribution","Team Work,Communication",5,8)
        Tutoring = Task(
            "Tutoring","Communication,Active Listening",4,5)
        Enviromental_Cleanup = Task(
            "Enviromental cleanup","Team Work,Safety Awareness",5,12)
        Disaster_Response = Task(
            "Disaster Response","Crisis Management,Adaptability",3,7)
        Animal_Shelter = Task(
            "Animal Shelter", "Animal Care Knowledge,Physical Stamina", 5, 10)
        Health_Awareness_Campaigns = Task(
            "Health Awareness Campaigns", "Public Speaking,Knowledge of Health Topics", 4, 5)
        Building_Homes = Task(
            "Building Homes", "Construction Skills,Teamwork", 6, 15)
        Community_Gardening = Task(
            "Community Gardening", "Gardening Knowledge,Physical Fitness", 3, 8)
        Local_Festival_Volunteer = Task(
            "Local Festival Volunteer", "Customer Service,Adaptability", 2, 20)
        Iftar_Preparation = Task(
            "Iftar Preparation Assistance", "Cooking Skills,Teamwork", 4, 20)



        # 10 Volunteers
        Ahmed_Hamad = Volunteer(
            "Ahmed Hamad Naser", "0501221844", "ahmed@zu.ac.ae", "PhD", date(2020, 4, 12), date(2000, 2, 2), "Team Work, Communication")
        Fatima_Ali = Volunteer(
            "Fatima Ali Hassan", "0502334455", "fatima@zu.ac.ae", "Master's", date(2021, 5, 15), date(1998, 3, 10), "Communication,Active Listening")
        Salem_AlMansoori = Volunteer(
            "Salem AlMansoori", "0503445566", "salem@zu.ac.ae", "Bachelor", date(2019, 1, 20), date(1997, 7, 8), "Team Work,Safety Awareness")
        Nora_AlFarsi = Volunteer(
            "Nora AlFarsi", "0504556677", "nora@zu.ac.ae", "Bachelor", date(2021, 6, 5), date(1999, 8, 15), "Crisis Management,Adaptability")
        Mohammed_AlRashid = Volunteer(
            "Mohammed AlRashid", "0505667788", "mohammed@zu.ac.ae", "PhD", date(2020, 7, 22), date(1995, 12, 1), "Animal Care Knowledge,Physical Stamina")
        Laila_AlHashemi = Volunteer(
            "Laila AlHashemi", "0506778899", "laila@zu.ac.ae", "Master's", date(2022, 2, 28), date(1996, 4, 20), "Public Speaking,Knowledge of Health Topics")
        Khalid_AlNajjar = Volunteer(
            "Khalid AlNajjar", "0507889900", "khalid@zu.ac.ae", "Bachelor", date(2018, 8, 30), date(1994, 9, 25), "Construction Skills,Teamwork")
        Aisha_AlZarooni = Volunteer(
            "Aisha AlZarooni", "0508990011", "aisha@zu.ac.ae", "Bachelor", date(2021, 3, 14), date(1998, 5, 30), "Gardening Knowledge,Physical Fitness")
        Omar_AlFahim = Volunteer(
            "Omar AlFahim", "0509001122", "omar@zu.ac.ae", "Master's", date(2022, 4, 19), date(1997, 6, 22), "Customer Service,Adaptability")
        Mariam_AlSayed = Volunteer(
            "Mariam AlSayed", "0500112233", "mariam@zu.ac.ae", "PhD", date(2019, 9, 9), date(1996, 11, 11), "Cooking Skills,Teamwork")
        


        # 6 Representatives
        Khalid_Alzaabi = Organization_Representative(
            "Khalid Al Mazroui", "0501234567", "khalid.alm@org.ae", "Master's", date(2023, 1, 10), date(1985, 5, 25))
        Saeed_AlZaabi = Organization_Representative(
            "Saeed Al Zaabi", "0502345678", "saeed.alz@org.ae", "Bachelor", date(2022, 2, 20), date(1987, 8, 15))
        Noora_AlAhbabi = Organization_Representative(
            "Noora Al Ahbabi", "0503456789", "noora.ala@org.ae", "PhD", date(2021, 3, 15), date(1990, 12, 1))
        Ahmed_AlFahim = Organization_Representative(
            "Ahmed Al Fahim", "0504567890", "ahmed.alf@org.ae", "Bachelor", date(2024, 4, 5), date(1988, 10, 20))
        Mariam_AlHashimi = Organization_Representative(
            "Mariam Al Hashimi", "0505678901", "mariam.alh@org.ae", "Master's", date(2020, 5, 25), date(1986, 4, 30))
        Fatima_AlKetbi = Organization_Representative(
            "Fatima Al Ketbi", "0506789012", "fatima.alk@org.ae", "Bachelor", date(2019, 6, 10), date(1989, 9, 10))


        # 5 Organizations
        Emirates_Red_Crescent = Organization(
            "Emirates Red Crescent",
            "A volunteer organization that plays a leading role in humanitarian work at both local and international levels.",
            100)
        Beit_Al_Khair_Society = Organization(
            "Beit Al Khair Society",
            "Focuses on providing support to the needy within the UAE community, including food distribution and financial aid.",
            201)
        Dubai_Cares = Organization(
            "Dubai Cares",
            "Part of Mohammed bin Rashid Al Maktoum Global Initiatives, it aims to improve children's access to quality primary education in developing countries.",
            307)
        Emirates_Environmental_Group = Organization(
            "Emirates Environmental Group",
            "A professional working group devoted to protecting the environment through the means of education, action programs, and community involvement.",
            404)
        Emirates_Animal_Welfare_Society = Organization(
            "Emirates Animal Welfare Society",
            "Dedicated to the welfare of animals and works to improve public awareness about the importance of animal welfare and protection.",
            512)


        # 3 Admins
        Khalid_Al_Futtaim = Administrator(
            "Khalid Al Futtaim", "0501234567", "khalid.alfuttaim@admin.com", "Master's", date(2023, 1, 10), date(1985, 5, 25))

        Sara_Al_Zaabi = Administrator(
            "Sara Al Zaabi", "0502345678", "sara.alzaabi@admin.com", "PhD", date(2022, 2, 20), date(1983, 8, 15))

        Omar_Al_Suwaidi = Administrator(
            "Omar Al Suwaidi", "0503456789", "omar.alsuwaidi@admin.com", "Bachelor", date(2024, 3, 15), date(1987, 12, 1))
        
        
        # Inserting opportunities
        Emirates_Red_Crescent.createOpportunity("Ramadan Food Distribution", date(2024, 4, 1), "Morning", "Afternoon", "Abu Dhabi")
        Emirates_Red_Crescent.createOpportunity("Youth Tutoring and Education", date(2024, 9, 15), "Afternoon", "Evening", "Dubai")
        Emirates_Red_Crescent.createOpportunity("Disaster Recovery and Support", date(2024, 11, 10), "Noon", "Evening", "Sharjah")


        Beit_Al_Khair_Society.createOpportunity("Food Pantry Organization", date(2024, 5, 25), "Morning", "Noon", "Ajman")
        Beit_Al_Khair_Society.createOpportunity("Eid Meal Preparation", date(2024, 4, 20), "Morning", "Afternoon", "Ras Al Khaimah")
        Beit_Al_Khair_Society.createOpportunity("Community Gardening Initiative", date(2024, 3, 15), "Morning", "Noon", "Fujairah")

        Dubai_Cares.createOpportunity("Academic Tutoring Support", date(2024, 10, 30), "Morning", "Afternoon", "Dubai")
        Dubai_Cares.createOpportunity("School Supplies Drive", date(2024, 8, 25), "Morning", "Noon", "Al Ain")
        Dubai_Cares.createOpportunity("Educational Workshops for Children", date(2024, 7, 20), "Afternoon", "Evening", "Abu Dhabi")

        Emirates_Environmental_Group.createOpportunity("Beach and Coastal Cleanup", date(2024, 6, 15), "Morning", "Noon", "Dubai")
        Emirates_Environmental_Group.createOpportunity("Community Tree Planting Day", date(2024, 12, 30), "Morning", "Afternoon", "Sharjah")
        Emirates_Environmental_Group.createOpportunity("Environmental Awareness Campaign", date(2024, 11, 5), "Noon", "Afternoon", "Ajman")

        Emirates_Animal_Welfare_Society.createOpportunity("Pet Adoption and Care Day", date(2024, 2, 10), "Morning", "Afternoon", "Dubai")
        Emirates_Animal_Welfare_Society.createOpportunity("Animal Shelter Support", date(2024, 1, 5), "Noon", "Evening", "Ras Al Khaimah")
        Emirates_Animal_Welfare_Society.createOpportunity("Disaster Recovery and Support", date(2024, 11, 10), "Noon", "Evening", "Sharjah")
        
        
        """
        add task to opportunity
        ....
        """
        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Food_Distribution, 30)
        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Tutoring, 30)

        Emirates_Environmental_Group.addTaskToOpportunity(Enviromental_Cleanup,10)
        Emirates_Environmental_Group.addTaskToOpportunity(Disaster_Response,10)

        Dubai_Cares.addTaskToOpportunity(Animal_Shelter,7)
        Dubai_Cares.addTaskToOpportunity(Health_Awareness_Campaigns,7)

        Beit_Al_Khair_Society.addTaskToOpportunity(Building_Homes,4)
        Beit_Al_Khair_Society.addTaskToOpportunity(Community_Gardening,4)

        Emirates_Red_Crescent.addTaskToOpportunity(Local_Festival_Volunteer,1)
        Emirates_Red_Crescent.addTaskToOpportunity(Iftar_Preparation,1)

        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Food_Distribution,2)
        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Tutoring,2)

        Emirates_Environmental_Group.addTaskToOpportunity(Enviromental_Cleanup,3)
        Emirates_Environmental_Group.addTaskToOpportunity(Animal_Shelter,3)

        Dubai_Cares.addTaskToOpportunity(Iftar_Preparation,5)
        Dubai_Cares.addTaskToOpportunity(Community_Gardening,5)

        Beit_Al_Khair_Society.addTaskToOpportunity(Disaster_Response,6)
        Beit_Al_Khair_Society.addTaskToOpportunity(Building_Homes,6)

        Emirates_Red_Crescent.addTaskToOpportunity(Animal_Shelter,8)
        Emirates_Red_Crescent.addTaskToOpportunity(Local_Festival_Volunteer,8)

        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Community_Gardening,9)
        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Health_Awareness_Campaigns,9)

        Emirates_Environmental_Group.addTaskToOpportunity(Disaster_Response,11)
        Emirates_Environmental_Group.addTaskToOpportunity(Tutoring,11)

        Dubai_Cares.addTaskToOpportunity(Local_Festival_Volunteer,12)
        Dubai_Cares.addTaskToOpportunity(Health_Awareness_Campaigns,12)

        Beit_Al_Khair_Society.addTaskToOpportunity(Building_Homes,13)
        Beit_Al_Khair_Society.addTaskToOpportunity(Animal_Shelter,13)

        Dubai_Cares.addTaskToOpportunity(Iftar_Preparation,14)
        Dubai_Cares.addTaskToOpportunity(Tutoring,14)

        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Local_Festival_Volunteer,15)
        Emirates_Animal_Welfare_Society.addTaskToOpportunity(Enviromental_Cleanup,15)


        #Emirates-Red-Crescent O100 - Opportunitiy codes - 1 , 2 , 3
        #Beit-Al-Khair-Society O201 - Opportunity codes - 4 , 5 , 6
        #Dubai-Cares O307 - Opportunity codes - 7 , 8 , 9
        #Emirates-Enviromental-Group - O404 - Opportunity codes - 10 , 11 , 12
        #Emirates-Animal-Walfare-Society - O512 - Opportunity codes - 13, 14, 15

    
        """
        add representatives to all organizations
    
        ....
        """
        Emirates_Red_Crescent.setRepresentatives(Khalid_Alzaabi)
        Beit_Al_Khair_Society.setRepresentatives(Saeed_AlZaabi)
        Dubai_Cares.setRepresentatives(Noora_AlAhbabi)
        Emirates_Animal_Welfare_Society.setRepresentatives(Ahmed_AlFahim)
        Emirates_Environmental_Group.setRepresentatives(Fatima_AlKetbi)
        Emirates_Red_Crescent.setRepresentatives(Mariam_AlHashimi)







        """
        
        ....
        """






        
        return f"Done" 


"""for obj in Volunteer.volunteerRecord:
    print(obj, "\n")

print(Task.getTasks())"""

"""# I NEED THIS
# adding a task
x = input("enter task name: ")
y = input("enter task skills separated by ,: ")
u = str(input("enter credit hour amount: "))
z = input("enter task required number of vol: ")

Task(x, y, u, z)  # type: ignore


for task in Task.tasksRecord:
    print(task)

x = input("enter task name: ")
y = input("enter task skills separated by ,: ")
u = input("enter credit hour amount: ")
z = input("enter task required number of vol: ")

Task(x, y, u, z)


for task in Task.tasksRecord:
    print(task)"""

