from pages.accountDetails import AccountDetail
from pages.costa import Costa
import os
print('''
                                                                                                    
Welcome, Hope you are having a good day.
By: Anwar MEQOR
                                                                                                                                          
''')

print("|=================================|")
print("|                                 |")
print("|    PLEASE USE 'USA' VPN         |")
print("|                                 |")
print("|=================================|")
try : 
    os.rename("idea", ".idea") 
    print("Let's Start!") 
  
# If Source is a file  
# but destination is a directory 
except IsADirectoryError: 
    print("Let's Start!") 
  
# If source is a directory 
# but destination is a file 
except NotADirectoryError: 
    print("Let's Start!") 
  
# For permission related errors 
except PermissionError: 
    print("Let's Start!") 
  
# For other errors 
except OSError as error: 
    print("Let's Start!") 
email = input("Enter your email (do not enter Fake):")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(Info)
costa = Costa(info, email)
costa.start_process()
