
def fibonaccinum(a):
    if a == 0 or a == 1:
        return a
    
    return fibonaccinum(a-1) + fibonaccinum(a-2)

try:
   num = int(input())
   assert num > 0
except ValueError:
    print('Номер должно быть целочисленный')
except AssertionError:
    print('Номер отрицательный')

print(fibonaccinum(num))


