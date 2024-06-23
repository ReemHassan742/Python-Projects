def load_key ():
    file = open("key.key", "rb")
    key = file.read ()
    file.close()
    return key 
 

key = load_key()

def view():
    with open ('passwords.txt','r') as f :
        for line in f.readlines():
            date = line.rstrip()
            user, passw = date.split("|") 
        
        
def add():
    name = input ("Account Name :")
    pwd = input ("password:")       
    
    with open ('passwords.txt', 'a') as f :
     
      
      
      
      
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue     