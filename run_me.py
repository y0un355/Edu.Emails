from pages.accountDetails import AccountDetail
from pages.costa import Costa

print('''
                                                                                                    
  010    1       1 1       1     1       1   010    01010         010     0     0  10101010101    000
 0   0   1 0     1  1       1   1       1   0   0   1     1      0   0    1     1       1        0   0
1     1  1  0    1   1       1 1       1   1     1  0    0      1     1   0     0       0       0     0
1     1  1   0   1    1       1       1    1     1  10101       1     1   1     1       1      0       0
1010101  1    0  1     1     1 1     1     1010101  01          1010101   0     0       0      0       0
1     1  1     0 1      1   1   1   1      1     1  1 1         1     1   1     1       1       0     0
1     1  1      01       1 1     1 1       1     1  0  1        1     1   0     0       0        0   0
1     1  1       1        1       1        1     1  1   1       1     1    10101        1         000

                                                                                                                                          
''')

print("|=================================|")
print("|                                 |")
print("|    PLEASE USE 'USA' VPN         |")
print("|                                 |")
print("|=================================|")

email = input("Enter your email (do not enter Fake):")
accountdetails = AccountDetail()
info = accountdetails.getInfo()
print(Info)
costa = Costa(info, email)
costa.start_process()
