from email import message
from django.test import TestCase
from django.db import models
from datetime import datetime
# Create your tests here.


def checkInput(data):
   message = ""
   if data['FirstName'] == "":
      message = "The First Name MUST be filled"

   elif data['LastName'] == "":
      message = "The Last Name MUST be filled"

   elif data['Address'] == "":
      message = "The Address MUST be filled"

   elif data['City'] == "":
      message = "The City MUST be filled"

   elif not data['ZipCode'].strip().isdigit():
      message = "The Zip Code MUST be a number"

   elif not data['LandLine'].strip().isdigit():
      message = "The LandLine MUST be a number"

   elif not data['Phone'].strip().isdigit():
      message = "The cellular MUST be a number"

   elif data['BirthDay'] == "": 
      message = "The BirthDay MUST be filled" 
      
   else:
      
      newDate = data['BirthDay'].split('-')
      if int(newDate[0]) > 2022 or int(newDate[1]) > 12 or int (newDate[2]) > 31:
         message = "The Birth Day is not allowed" 
      today = datetime.now()
      if today < datetime.strptime(data['BirthDay'] ,"%Y-%m-%d"):
         message = "The Birth Day is in the future" 
         
   return message
