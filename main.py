'''
NAME: main.py
AUTHOR: Roger Aragon
DATE: 3/3/19
DESCRIPTION: Sales tax calculator
EMAIL: aragonr87056@student.vvc.edu
'''

purchase = int(input('Purchase price: $'))
s_tax = purchase * 0.05
c_tax = purchase * 0.025
tot_tax = s_tax + c_tax
tot_purch = purchase + tot_tax
    
print('Purchase; $',purchase)
print('State tax: $',s_tax)
print('County tax: $',c_tax)
print('Total tax: $', tot_tax)
print('Grand total: $', tot_purch)
