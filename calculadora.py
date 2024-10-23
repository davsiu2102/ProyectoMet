num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe otro número: "))

op =  input("Escribe un + o - para hacer la operación: ")
if op == '-':
    res = num1 - num2
elif op == '+':
    res = num1 - num2

print(f"Tu resultado fue: {res}")