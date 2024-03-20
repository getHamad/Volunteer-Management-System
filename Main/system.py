from index import *



def administrator_panel():
    # Implement administrator panel functionality here
    print("Administrator Panel")

def organization_rep_panel():
    # Implement organization representative panel functionality here
    print("Organization Representative Panel")

def otherSysFunc():
      while True:
    # Implement volunteer panel functionality here
            print("Other system functions")
            break
    
def userControls():
      print("⎡ Volunteer Management System ")
      print("├ User Controls")
      print("⎣\n")
      print("1 - Administrator Panel 👤")
      print("2 - Organization Representative Panel 🔧")
      print("3 - Volunteer Panel 👨🏻‍🔧")
      print("4 - Back to Menu ")
      
      secondInput = int(input("Select your panel: "))      

                    
def main(): 
      while True:
            print("Volunteer Management System")
            print("")
            print("")
            print("")
            print("")
            print("") 
            
            mainInput = int(input("Select your menu: "))
            
            if mainInput == 1: 
                  
                  
                  if secondInput == 1:
                        otherSysFunc()
                  elif secondInput == 2:
                        pass
                  elif secondInput == 3: break
            
            
                  


# Start the system
main()