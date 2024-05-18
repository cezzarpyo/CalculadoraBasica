def soma(a, b):
    resultado = a + b
    print(f"O resultado da soma é: {resultado}")

def sub(a, b):
    resultado = a - b
    print(f"O resultado da subtração é: {resultado}")

def div(a, b):
    if b == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = a / b
        print(f"O resultado da divisão é: {resultado}")

def mul(a, b):
    resultado = a * b
    print(f"O resultado da multiplicação é: {resultado}")

a = int(input("FALE O PRIMEIRO NUMERO: "))
b = int(input("FALE O SEGUNDO NUMERO: "))
c = input("FALE UM TIPO DE OPERAÇÃO (+, -, /, *): ")

if c == "+":
    soma(a, b)
elif c == "-":
    sub(a, b)
elif c == "/":
    div(a, b)
elif c == "*":
    mul(a, b)
else:
    print("Operação Inválida")
    