#Desenvolva uma função que calcule a divisão de uma conta de consumo 
#(conta de restaurante ou bar), em reais, considerando o número de pessoas
# que estavam consumindo e a taxa de serviço que será paga ao garçom.
#Ao usuário do programa serão solicitados o valor total do consumo, em reais, 
# o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.

def calc(percentage, bill_value, people_number):
    new_percentage = (percentage / 100) + 1
    new_bill_value = (bill_value * new_percentage) / people_number
    final_value = str(round(new_bill_value,2))            
    print(f"o valor para cada um é R${final_value.replace('.', ',')}")
    control = False     

def bill_calc():
    control = True
    while control == True:
        bill_value = float(input('Qual o valor da conta em R$? '))
        if bill_value <0:
            print ("Valor Invalido, digite um numero inteiro")
            break
        percentage = int(input('Qual a porcentagem do atendente? '))
        if percentage < 0:
            print ("Valor Invalido, digite um numero inteiro")
            break
        people_number = int(input('Qual o numero de pessoas? '))
        if people_number < 0:
            print ("Valor Invalido, digite um numero inteiro")
            break
        else:
            calc(percentage, bill_value, people_number)
        
bill_calc()