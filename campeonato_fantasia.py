#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas,
# variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.
#Fluxo de exceção: 
#O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

def show_winner(participants):
    winner_name = max(participants, key=participants.get)
    all_grades = participants.values()
    max_grade = max(all_grades)

    print (f'(a) vencedor(a) foi {winner_name}, com nota {max_grade}')

def convert_to_float(grade):
    return float(grade.replace(',','.'))

def is_invalid(grade):
    return grade < 0 or grade > 10

def collect_participants_info():
    participants = {}
    for i in range(5):
        name = input(f"Informe nome do {i+1}º participante: ")
        grade = input (f"Informe nota do {i+1}º participante: ")
        grade =  convert_to_float(grade)
            
        if is_invalid(grade):
            print("Nota invalida")
            break    
        participants[name] = grade
    return participants

def main():
    show_winner(collect_participants_info())
    
main()