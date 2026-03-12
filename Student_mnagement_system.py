"""
Store customer information, including name, contact details, and purchase history.
1) add new records
2) update existing records
3) delete records
4) retrieve records based on specific criteria by id
5) search records

"""


def add():
  s_name = input("Enter your name: ")
  s_id = input("Enter your S_Id: ")
  address = input("Enter your address: ")
  phone_no = input("Enter your phone number")

  with open("student.txt","a") as f:
    f.write(f"{s_name},{s_id},{address},{phone_no}\n")

  print("You have registered. ")  

def Display_():
  try:
    with open("student.txt","r") as f:
      data = f.readlines()
      
      if not data:
        print("No records found.\n")
        return
      print("\n\t--- Student record ---")
      for line in data:
        s_name, s_id, address, phone_no = line.strip().split(",")
        print(f"Name:\t{s_name}\tID:\t{s_id}\tAddress:\t{address}\tPhone:\t{phone_no}")
      print()
  except FileNotFoundError:      
    print("File not found.\n")
    
def update_():
  try:
    with open("student.txt","r") as f:
      data = f.readlines()

    customer_id = input("Enter your id to edit content:")
    found = False
    for i in range(len(data)):
      c_name,c_id,address,phone = data[i].strip().split(",")

      if c_id == customer_id:
        new_name = input("Enter your new name:")
        new_addres = input("Enter your new address:")
        new_phone_no = input("Enter your new phono number:")

        data[i] = c_id,new_name,new_addres,new_phone_no
        found = True
        break
      if found:
        with open("student.txt","w") as f:
          f.writelines(data)

        print("update sucessfullyy!!!!!!")

      else:
        print("ID not found")

  except FileNotFoundError:
    print("File not exisst") 


def search():
    s_id=input("Enter the id of student:\n")
    with open("student.txt","r") as f:
        id_data=f.readline()
        if not id_data:
            print("No records found.\n")
            return
        
def delete_():
    with open("student.txt","r") as f:
       lines = f.readlines()




    while True:
        print("1.Add Student")
        print("2.View Students")
        print("3.Search Student")
        print("4.Update Student")
        print("5.Delete Student")
        print("6.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            Display_()
        elif choice == "3":
            search()
        elif choice == "4":
            update_()
        elif choice == "5":
            delete_()
        elif choice == "6":
            print("See you later!!!!!!!!")
            break
        else:
            print("!!!!!!!!!!!---invalid choice-----!!!!!!")
        

            
