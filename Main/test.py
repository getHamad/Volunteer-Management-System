from index import *



d = {}
def test( id, name = ""): 
      id = id
      name = name
      d [id] = {
            "name": name
      }
      
      return "done"
      
test(1, "hamad a almazrouei")
test(2, "ahmed")
test(3, "rashid")
print(d)



"""for i in d.items(): 
      print(i) """
      
def update_id(id_to_update, new_id):
    if id_to_update in d:
        d[new_id] = d.pop(id_to_update)  # Update id and preserve associated data
        print(f"Updated id {id_to_update} to {new_id}")
    else:
        print(f"Id {id_to_update} not found in the dictionary")

# Example: Update id 2 to 4
update_id(2, 4)
print(d)     



for i, data, in d.items():
      if i == 1:
            print(data['name'])
      else: 
            pass
            
            
print("\n\n")
v1 = Volunteer()
v2 = Volunteer()

print(Volunteer.volunteerRecord)
print("\ngdfgdgdfg\n")
print(f"{User.userRecord}", )


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


system()