bal = int(input('Begining Balance: '))
interest = int(input('Interest expense(?%): '))
pay = int(input('Payment: '))
year = int(input('number of year: '))
bgbal=bal
int_total=pay*year-bal
print(bal,interest,pay,year)
print('Period Ending Day|Begining Balance|Debit Interest Expense|+|Debit Notes Payable|=|Credit Cash|Ending Balance')
for i in range(year):
    if i==(year-1):
        print('year',i+1,end='|')
        print('{:>10}'.format(bal),end='|')
        print('{:>10}'.format(pay-bal),end='|')
        print('{:>10}'.format(bal),end='|')
        print('{:>10}'.format(pay),end='|')
        print('{:>10}'.format(0),end='|')
        print()
    elif i==0:
        print('year',i+1,end='|')
        print('${:>9}'.format(bal),end='|')
        B=round(bal*interest/100)
        print('${:>9}'.format(B),end='|')
        C=pay-B
        print('${:>9}'.format(C),end='|')
        print('${:>9}'.format(pay),end='|')
        bal=bal-C
        print('${:>9}'.format(bal),end='|')
        print()
    else:
        print('year',i+1,end='|')
        print('{:>10}'.format(bal),end='|')
        B=round(bal*interest/100)
        print('{:>10}'.format(B),end='|')
        C=pay-B
        print('{:>10}'.format(C),end='|')
        print('{:>10}'.format(pay),end='|')
        bal=bal-C
        print('{:>10}'.format(bal),end='|')
        print()
print('                 |${:>9}'.format(int_total),end='|')
print('${:>9}'.format(bgbal),end='|')
print('${:>9}'.format(pay*year),end='|')
print()
input("PRESS ANY KEY TO EXIT")

    

    
