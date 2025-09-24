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



print(displayAllContact())