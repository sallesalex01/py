#Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
#Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
#Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
#Não tem direito a voto (menor de 16 anos).
#Fluxo de exceção: 
#O programa deve verificar se a idade da pessoa é maior do que zero.
def validation():
    control = True
    print("Para sair do programa digite 0")
    while control == True:
        age = float(input('Informe sua idade: '))
        if age > 0:
            if age >= 18 and age < 70:
                print("Voto Obrigatorio")
            elif age == 16 and age < 18 or age >= 70: 
                print("Não tem obrigação de votar")
            elif age < 16 and age > 0:
                print ("Não tem direito de votar")
        if age < 0:
                print("Idade invalida")
        if age == 0:
            print("Tchau :D")
            control = False
    return

def age_to_vote():
    validation()
    
age_to_vote()