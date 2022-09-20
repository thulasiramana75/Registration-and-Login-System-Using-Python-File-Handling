# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:57:21 2022

@author: THULASIRAMAN AYYAMUTHU
"""


           # Registration and Login System Using Python, File Handling

# Database Reading 

def Reading_Data(Read):
    file_data = open("Database.txt","r")
    data_lines = file_data.read()
    print(data_lines)
    
#Reading_Data(1)
    

# Email_Validation Process

import re
def Email_Validate(email):
    formula = "^[a-zA-Z]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.fullmatch(formula,email):
        return True
    else:
        return False

#email = input(" Enter Your Email ID: ")
#Email_Validate(email)


# Password_Validation Process

def Password_Validate(password):
    
    if (5 < len(password) < 16 and re.search(r'\d+', password) and re.search(r'[a-z]+', password) and
            re.search(r'[A-Z]+', password) and re.search(r'\W+', password) and not re.search(r'\s+', password)):
        return True
    else:
        return False

#password = input(" Enter Your Password: ")
#Password_Validate(password)


# Password Rule Display

def Password_Rule(Rule):
    print(" \nPassword must be with following conditions password length should be (5 < password < 16) Must have minimum one special character,one digit,one uppercase, one lowercase character\n\n")


# New User Registration process
       
def New_Registrtaion(New_User):
    Email_ID = input("\nEnter Your Email ID : ")
    Mail_Validate = Email_Validate(Email_ID)
    if Mail_Validate == True:
        print("\n")
        Password_Rule(1)
        Password = input("\n\nEnter Your Email Password : ")
        Password_Validation = Password_Validate(Password)
        if Password_Validation == True:
            my_files = open("Database.txt","a")
            my_files.write(Email_ID)
            my_files.write(" ")
            my_files.write(Password)
            my_files.write("\n")
            my_files.close()
            print("\nRegistration Successfully Completed")
            #Main_Display(1)
        else:
            print("\nEntered Passsword is not meet the Criteria.... Please Try Again !!! \n\n")
            Password_Rule(1)
            #Main_Display(1)
    else:
        print("\n\nEntered Email ID is Incorrect.... Please Try Again !!!")
        #Main_Display(1)

        
# Forget Password process

def Forget_Password(mail):
    Password1 = ""
    file_data = open("Database.txt","r")
    data_lines = file_data.readlines()
    for data in data_lines:
       data_info = data.split()
       #print(data_info[0])
       #print(data_info[1])
       if data_info[0] == mail:
           Password1 = data_info[1]
    print("\nYour Password is : " , Password1)
    #Main_Display(mail)
 
    
# Password Reset process

def Reset_Password(Mail):
    Password_Rule(Mail)
    New_Password = input("\nEnter Your New Password : ")
    Password_Check = Password_Validate(New_Password)
    if Password_Check == True:
        my_files = open("Database.txt","w")
        my_files.write(Mail)
        my_files.write(" ")
        my_files.write(New_Password)
        my_files.write("\n")
        my_files.close()
        #with open("Database.txt","r") as f:
         #       data_lines = f.read()
         #       print("\n",data_lines)
    print("\nPassword Reset Successfully Completed")
    #Main_Display(Mail)
           

# login process

def Login_Process(Login):
    Email_ID = input("Enter Your Email ID : ")
    Password = input("\nEnter Your Email Password : ")
    temp_storage = ""
    file_data = open("Database.txt","r")
    data_lines = file_data.readlines()
    for data in data_lines:
        data_info = data.split()
        #print(data_info[0])
        #print(data_info[1])
        if data_info[0]== Email_ID:
            temp_storage = data_info[0]
            if data_info[0]== Email_ID and (data_info[1] == Password):  
                print("You have Successfully Logged In !!! ")
                #Main_Display(Login)
                break
            else: 
                print("\nYour " + temp_storage + " is exist in the database. But, Your have entered Incorrect password. Please Try with Below Options...!!!")
                print("\n1. Forget Password" + "\n2. Reset Password")
                User_Choice = int(input("\nEnter Your Choice : "))
                if User_Choice ==  1:
                    Forget_Password(temp_storage)
                elif User_Choice == 2:
                    Reset_Password(temp_storage)
                else: 
                    print("\n Invalid Option Choosed and Try Again... !!!")
                    #Main_Display(Login)
                break
    else:
            print("Your Email ID is not exist in the database. Please go ahead with New Registration...")
            
            User_response = input("\nPlease provide your response if you want to proceed respectively (Y or N) :  ")
            if User_response == "Y":
                print("\nWelcome to New Registration :)")
                New_Registrtaion(1)
            else:
                print("\nThanks for your time. Please try Again Later !!!")
                #Main_Display(Login)
                
#Login_Process(1)


# Main Display Function....

def Main_Display(Menu):
    
    print("\n Welcome.... !!!!") 
    print("\n" + "1. New Registration" + "\n" + "2. Login")
    User_choice = int(input("\nEnter Your Choice : "))
    if User_choice ==1:
        New_Registrtaion(1)
    elif User_choice ==2:
        Login_Process(2)
    else:
        print("Invalid Selection") 
        
Main_Display(1)  





















