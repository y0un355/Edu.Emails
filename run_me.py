from pages.accountDetails import AccountDetail
from pages.costa import Costa
print('''
                                                                                                    
Welcome, Hope you are having a good day.
By: Anwar MEQOR
                                                                                                                                          
''')

print("|=================================|")
print("|                                 |")
print("|    PLEASE USE 'USA' VPN         |")
print("|                                 |")
print("|=================================|")

email = input("Enter your email (do not enter Fake) : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
costa = Costa(info, email)
costa.start_process()
