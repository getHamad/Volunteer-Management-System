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