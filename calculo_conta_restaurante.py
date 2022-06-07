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

def bill_validation(bill_value):
    value_error = False
    if bill_value < 0: 
        value_error = True
    while value_error == True:                
        print ("Valor Invalido, digite um numero inteiro")
        bill_value = float(input('Qual o valor da conta em R$? '))
        if bill_value >= 0:
            value_error = False
    return float(bill_value)
        
def percentage_validation(percentage):
    value_error = False
    if percentage < 0: 
        value_error = True
    while value_error == True:                
        print ("Valor Invalido, digite um numero inteiro")
        percentage = float(input('Qual a porcentagem do atendente '))
        if percentage >= 0:
            value_error = False
    return float(percentage)

def people_validation(people_number):
    value_error = False
    if people_number < 0:
        value_error = True
    while value_error == True:
        print ("Valor Invalido, digite um numero inteiro")
        people_number = int(input('Qual o numero de pessoas? '))
        if people_number >= 0:
            value_error = False
    return int(people_number)

def bill_calc():
    control = True
    while control == True:
        bill_value = float(input('Qual o valor da conta em R$? '))
        valid_bill = bill_validation(bill_value)
        
        percentage = float(input('Qual a porcentagem do atendente '))
        valid_percentage = percentage_validation(percentage)
        
        people_number = int(input('Qual o numero de pessoas? '))
        valid_people_number = people_validation(people_number)
        
        calc(valid_percentage, valid_bill, valid_people_number)
        break
        
bill_calc()