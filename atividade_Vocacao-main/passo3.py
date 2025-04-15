nome = str(input("\nDigite o seu nome: "))
print("\nOperações:\n1 - Adição.\n2 - Subtração.\n3 - Multiplicação.\n4 - Divisão.\n")
calc = int(input(f"{nome}, informe a operação desejada: "))
x = 0
y = 0

if (calc == 1):
    x = float(input(f"{nome}, digite o valor de X: "))
    y = float(input(f"{nome}, digite o valor de Y: "))
    resp1 = x + y
    print(f"{nome}, O resultado de",x,"+",y,"=",resp1)

elif (calc == 2):
    x = float(input(f"{nome}, digite o valor de X: "))
    y = float(input(f"{nome}, digite o valor de Y: "))
    resp2 = x - y
    print(f"{nome}, O resultado de",x,"-",y,"=",resp2)

elif (calc == 3):
    x = float(input(f"{nome}, digite o valor de X: "))
    y = float(input(f"{nome}, digite o valor de Y: "))
    resp3 = x * y
    print(f"{nome}, O resultado de",x,"X",y,"=",resp3)

elif (calc == 4):
    x = float(input(f"{nome}, digite o valor de X: "))
    y = float(input(f"{nome}, digite o valor de Y: "))
    resp4 = x / y
    print(f"{nome}, O resultado de",x,"÷",y,"=",resp4)

else:
    print(f"{nome}, esse número não está na lista de operações!")
    print("Tente rodar o código novamente.")
