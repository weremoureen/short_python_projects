#def login():
    #username = input("Enter username: ")
    #if not user_exists(username):
        #print("user does not exist.")
        #return
    #password = getpass("password: ")
    #if not authenticate_user(username, pasword):
        #print ("Incorrect password.")
        #return
    #print("Login successful.")
            
#login()        




#users = {'users1':'password1', 'user2':'password2', 'user3':'password3'}
#def login():
    #username = input("Enter your user name:")
    #password = input("Enter your password:")
    
            
    #if username in users and users[username] == password:
        #print("Login successful!")
    
    #else:
        #print("Invalid username or password.Please try again.")


#login()







def login():
    username = input("Enter username:")
    password = input("Enter password:")


    valid_users = ["user1", "user2", "user3"]
    valid_passwords = ["password1", "passsword2", "passsword3"]
    
    
    if username in valid_users and password == valid_passwords[valid_users.index(username)]:
        print("Login successful!")
    
    else:
        print("Invalid username or password.")

login()        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

