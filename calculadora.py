#Projeto Calculadora em Python


while True:

    afirmar = input("Deseja sair da calculadora: [s]im ou [n]ão? ")
    if afirmar == "s":
        print("Obrigado por utilizar a calculadora em Python, volte sempre")        
        break

    print("*****Calculadora******")

    num = input("> ")
    fator = input("+, -, x, /, -%, +%:>  ")
    num2 = input("> ")

    if num.isnumeric() and num2.isnumeric():
        num = int(num)
        num2 = int(num2)
    else:
        print("Somente número inteiro!")
        continue

    soma = 0
    if fator == "+":
       soma = num + num2
       print(f"{num} {fator} {num2} = {soma}")
    else:
    
     if fator == "-":
        soma = num - num2
        print(f"{num} {fator} {num2} = {soma}")
     else:
        if fator == "*":
            soma = num * num2
            print(f"{num} {fator} {num2} = {soma}") 
        else:
            if fator == "/":
                soma = num / num2
                print(f"{num} {fator} {num2} = {soma}")
            else:
                if fator == "-%":                     
                   soma = num - (num * (num2/100))
                   print(f"{num} {fator} {num2} = {soma}")
                else:
                    if fator == "+%":
                        soma = num + (num * (num2/100))
                        print(f"{num} {fator} {num2} = {soma}")
                    else:        
                     print("Dados Invalidos")
            continue

