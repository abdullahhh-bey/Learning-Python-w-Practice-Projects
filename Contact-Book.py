contact = [{
    "name" : "Alex",
    "email" : "a@gmail.com",
    "phone" : "0302321121"
},
           {
    "name" : "Pingu",
    "email" : "a1@gmail.com",
    "phone" : "030232121"
}]


def addContact():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    
    #validation
    if name == "" or email == "" or phone == "":
        print("Incomplete Information")
        return
        
    global contact
    
    for v in contact:
        if email == v["email"] or phone == v["phone"]:
            print("Info already exist")
            return
        
    #add at the end  of the list
    contact.append({
        "name" : name,
        "email" : email,
        "phone" : phone
    })
    print("Added in Contact Book")
    
  

def searchByName(name): 
    n = name.strip()
    foundList = []
    
    if n == "":
        raise Exception("Cannot pass a null value")
    found = False
    
    global contact
    for v in contact:
        if n == v["name"]:
            found = True
            foundList.append(v)
        else:
            continue
        
    if found is False:
        return f"No Contact with the Name:{n}"
    else:
        return foundList
    
    
def searchByEmail(email): 
    e = email.strip()
    foundList = []
    
    if e == "":
        raise Exception("Cannot pass a null value")
    found = False
    global contact
    for v in contact:
        if e == v["email"]:
            found = True
            foundList.append(v)
        else:
            continue
        
    if found is False:
        return f"No Contact with the Email:{e}"
    else:
        return foundList
    

def displayAllContact():
    global contact 
    allContacts = []
    
    for v in contact:
        allContacts.append(v)
    return allContacts


def removeContact(email):
    global contact
    found = False
    for v in contact:
        if email == v["email"]:
            contact.remove(v)
            found = True
            return "Removed"
        else:
            continue
    
    if found is False:
        return f"No Contact with this Email: {email}"
    
    

print("Welcome to FindMe.COM")
choice = True

while choice is True:
    try:
        print("1 -> Add Contact ( Name, Email, Phone Number )")
        print("2 -> Search Contact ")
        print("3 -> Display All Contacts ")
        print("4 -> Remove Contact by Email")
        print("5 -> Exit")
        userInput = int(input("Enter option no: "))
        
        match userInput:
            case 1:
                addContact()
            case 2:
                print("1 -> By Email ( recommended )")
                print("2 -> By Name")
                opt = int(input("Enter options for search (1 or 2): "))
                match opt:
                    case 1:
                        email = input("Enter Email to search: ")
                        print(searchByEmail(email))
                    case 2: 
                        name = input("Enter Name to search: ")
                        print(searchByName(name))
            case 3:
                print(displayAllContact())
            case 4: 
                e = input("Enter Email to remove: ")
                print(removeContact(e))
            case 5:
                break
    except:
        print("Invalid Exception")

    select = input("Do you want to continue: (Yes/No) ")
    if select == 'No' or select ==  'no':
        print("GoodBye!")
        choice = False
    else:
        continue