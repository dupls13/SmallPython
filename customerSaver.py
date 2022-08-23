
def organizer():
    
    customers = {}
    run = True
    while run:
        
        
        
        phoneNumber = input("Enter the client's phone number: ")
        if phoneNumber == 'end':
            run = False 
        elif phoneNumber == "clear all":
            customers.clear()
        
        else:
            reason = input("Enter the reason for their visit: ")
            if reason == "end":
                run = False 
        
        
        
        customers[phoneNumber] = reason
        print(customers)
        
    
organizer()