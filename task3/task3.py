import sys

def sum_cash(self):
    n = 0
    for num in self:
        cash_total[n] += float(num)
        n += 1

cash_total = []
with open(sys.argv[1]+'\Cash1.txt', 'r') as cash1:
    for num in cash1:
        cash_total.append(float(num))
        
with open(sys.argv[1]+'\Cash2.txt', 'r') as cash2:
    sum_cash(cash2)

with open(sys.argv[1]+'\Cash3.txt', 'r') as cash3:
    sum_cash(cash3)

with open(sys.argv[1]+'\Cash4.txt', 'r') as cash4:
    sum_cash(cash4)

with open(sys.argv[1]+'\Cash5.txt', 'r') as cash5:
    sum_cash(cash5)

max_cash=max(cash_total)

for cash in range(len(cash_total)): 
    if cash_total[cash] == max_cash:
        print(cash+1)
        break
        
  