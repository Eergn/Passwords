from getpass import getpass
import pickle
import os

os.system("clear")
def etable():
    print('enter table to edit')
    table=raw_input()+".data"
    print('enter username')
    us = raw_input()
    print('enter password')
    password = raw_input()
    t="\n"+us+" : "+password
    pickle.dump(t, open(table, "wb"))
    app()
def ctable():
    print('enter table name')
    table=raw_input()
    print ('you created '+table+' table \n click enter to continue')
    x=''
    td=table+".data"
    pickle.dump(x, open(td, "wb"))
    con = raw_input()
    if con=='':
        etable()
    else:
        etable()

def dtable():
    t=raw_input('table name')+".data"
    con=raw_input('do you want to delete')
    if con=='yes' or con=='y':
        os.remove(t)
    else:
        inputp()

def menu():
    os.system("clear")
    print ("1.Register")
    print ("2.Login")
    print ("3.To change password")
    print ("4.To delete account")
    choose = raw_input ('Choose your number : ')
    if choose =='1':
        register()
    elif choose =='2':
        login()
    elif choose == '3':
        os.system("clear")
        print('Login to change password')
        username = pickle.load(open("usernames.data", "rb"))
        password = pickle.load(open("pass.data", "rb"))
        account = pickle.load(open("account.data", "rb"))
        logusername = raw_input ('username : ')
        logpassword = getpass('password : ')
        if account ==logusername+logpassword:
            if logusername==username:
                if logpassword==password:
                    newpassword = raw_input ("New Password : ")
                    print ("password changed!")
                    pickle.dump(newpassword, open("pass.data", "wb"))
                    account = logusername+newpassword
                    pickle.dump(account, open("account.data", "wb"))
    elif choose =='4':
        os.system("clear")
        username = pickle.load(open("usernames.data", "rb"))
        password = pickle.load(open("pass.data", "rb"))
        account = pickle.load(open("account.data", "rb"))
        logusername = raw_input ('username : ')
        logpassword = getpass('password : ')
        if account ==logusername+logpassword:
            if logusername==username:
                if logpassword==password:
                    os.system("clear")
                    print ("Do you want to delete the account[yes/no]\nAnd it will delete all datas")
                    Choice = raw_input()
                    if Choice =='yes':
                        print ('deleted succesfully')
                        x = ''
                        os.remove("pass.data")
                        os.remove("account.data")
                        os.remove("usernames.data")
                        re=raw_input('do you want to Register[y,n]')
                        if re=='y':
                            register()
                        else:
                            menu()
        else:
            menu()   

def inputp():
    os.system("clear")
    print ('1.create table\n2.edit table\n3.delte table\nchoose a number.')
    lol=raw_input()
    if lol=='1':
        ctable()
    elif lol=='2':
        etable()
    elif lol=='3':
        dtable()

def passwords():
    os.system("clear")
    table = raw_input('which table you want to open')+".data"
    hacc = pickle.load(open(table, "rb"))
    print ('usernames : passwords')
    print (hacc)
    fn=raw_input('press enter to continue')
    if fn=='':
        inputp()
    else:
        inputp()
def app():
    os.system("clear")
    print('Do you want to show password[y/n]')
    answer= raw_input ()
    if answer=='y':
        passwords()
    elif answer=='n':
        inputp()
def login():
    os.system("clear")
    print("Login")
    username = pickle.load(open("usernames.data", "rb"))
    password = pickle.load(open("pass.data", "rb"))
    account = pickle.load(open("account.data", "rb"))
    logusername = raw_input ('username : ')
    logpassword = getpass('password : ')
    if account ==logusername+logpassword:
        if logusername==username:
            if logpassword==password:
                    app()
    else:
        print("Login Failed")
        ls=raw_input('click enter to register')
        if ls=='':
            register()
        else:
            login()
            
def register():
    os.system("clear")
    print("Register")
    username = raw_input ("New Username : ")
    password = getpass("New Password : ")
    repass  = getpass("Retype Password : ")
    if password==repass:
        account = username + password
        print ('your username is : '+username+'\nyour password is : '+password)
        #saving things
        pickle.dump(username, open("usernames.data", "wb"))
        pickle.dump(password, open("pass.data", "wb"))
        pickle.dump(account, open("account.data", "wb"))
        x_re=raw_input()
        if x_re=='':
            login()
        else:
            login()
    else:
        print("you didn't retype correctlly\n{enter} totry again")
        rere=raw_input()
        if rere=='':
            register()
        else:
            register()
menu()
                    
        
        
                
    
   
