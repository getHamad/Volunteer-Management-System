from Main.Index import *



task1 = Task("Car cleaning","communication, accuracy",3,2)
task2 = Task("Car cleaning","strength, accuracy",3,2)
vol1 = Volunteer("Abdulla","0501221433","as@zu.ac.ae",'phd',date(2024,2,12),date(2003,4,27))

Organization1 = Organization("ADNOC", "ADNOC Cleaning Services")

volOpp = Organization1.createOpportunities("Clean",date(2023,2,2),"Afternoon","Night","AD")

rep1 = Organization_Representative("Ali","0501221433","as@zu.ac.ae",'Masters',date(2024,2,12),date(2003,4,27))

admin1 = Administrator("Ahmed","0501221433","as@zu.ac.ae",'Bachelor',date(2024,2,12),date(2003,4,27))

arep1 = admin1.assignRepresentative(Organization1, rep1)
print(Task.getNumOfVolunteerNeeded(4)
)


# adding a task 
x = input("enter task name: ")
y = input("enter task skills separated by ,: ")
u = input('enter credit hour amount: ')
z = input('enter task required number of vol: ')

Task(x,y,u,z)


for task in Task.tasksRecord: 
      print(task)
      
x = input("enter task name: ")
y = input("enter task skills separated by ,: ")
u = input('enter credit hour amount: ')
z = input('enter task required number of vol: ')

Task(x,y,u,z)


for task in Task.tasksRecord: 
      print(task)
      
      
