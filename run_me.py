from pages.accountDetails import AccountDetail
from pages.costa import Costa

print('''
                                                                                                    
    88     ,a8888a,        ,a8888a,         88            88888888888  88888888ba,    88        88  
  ,d88   ,8P"'  `"Y8,    ,8P"'  `"Y8,     ,d88            88           88      `"8b   88        88  
888888  ,8P        Y8,  ,8P        Y8,  888888            88           88        `8b  88        88  
    88  88          88  88          88      88            88aaaaa      88         88  88        88  
    88  88          88  88          88      88            88"""""      88         88  88        88  
    88  `8b        d8'  `8b        d8'      88            88           88         8P  88        88  
    88   `8ba,  ,ad8'    `8ba,  ,ad8'       88            88           88      .a8P   Y8a.    .a8P  
    88     "Y8888P"        "Y8888P"         88            88888888888  88888888Y"'     `"Y8888Y"'   
                                                                                                    
                                              888888888888                                                                                                                                                                                      
                                                                                                                                          
''')

print("|=================================|")
print("|                                 |")
print("|    PLEASE USE 'USA' VPN         |")
print("|                                 |")
print("|                                 |")
print("|                                 |")
print("|                                 |")
print("|=================================|")

email = input("Enter your email (do not enter Fake) : ")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(info)
costa = Costa(info, email)
costa.start_process()
