from datetime import date, datetime
from index import *

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
Khalid_AlMazroui = Organization_Representative(
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

    # 15 Opportunities (3 in each)

# 3 Admins








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

