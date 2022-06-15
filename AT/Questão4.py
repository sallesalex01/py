def calculoJurosCompostos(valorInicial, valorMensal, jurosMensais, periodo):
    total = valorInicial
    for i in range(periodo):
        total += (total * jurosMensais) / 100
        total += valorMensal
        print(f'Após {i+1} períodos(s), o montante será de R${round(total,2)}')
    

def main():
    valorInicial = float(input('Valor inicial: R$ '))
    rendimentoPeriodo = float(input('Rendimento periodo(%): '))
    valorMensal = float(input('Aporte a cada periodo: R$ '))
    periodo = int(input('Total de Periodos: '))
    calculoJurosCompostos(valorInicial, valorMensal, rendimentoPeriodo, periodo)
    
    
main()    

