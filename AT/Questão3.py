#se alguem algum dia ler esse codigo, eu sei que era pra separar tudo em função ok?
#concatenar string? também, criar variavel pros numeros magicos flutuantes? também
#PREGUIÇA MANO, TRABALHO DA FACULDADE


def dados_usuarios():
    try:
        renda_usuario = float(input("Renda mensal total: R$ "))
        if renda_usuario < 0:
            raise Exception('Insira um valor valido na renda do usuario e abra o pograma de novo MUWHAUWHUAWHUAHWUHAUWHAUA')
        
        gastos_moradia = float(input("Gastos totais com moradia: R$ "))
        if gastos_moradia < 0:
            raise Exception('Insira um valor valido nos gastos da moradia e abra o programa de novo MUWHAUWHUAWHUAHWUHAUWHAUA')
                            
        gastos_educação = float(input("Gastos totais com educação: R$ "))
        if gastos_educação < 0:
            raise Exception('Insira um valor valido gastos da educação e abra o programa de novo MUWHAUWHUAWHUAHWUHAUWHAUA')
        
        gastos_transporte = float(input("Gastos totais com transporte: R$ "))
        if gastos_transporte < 0:
            raise Exception('Insira um valor valido nos gastos de transporte e abra o programa de novo MUWHAUWHUAWHUAHWUHAUWHAUA')
        return {
            "renda_usuario": renda_usuario,
            "gastos_moradia": gastos_moradia,
            "gastos_educação": gastos_educação,
            "gastos_transporte": gastos_transporte,
        }
    except Exception as e:
        print(e)
        return None    

def validacoes(data):
    #gastos moradia > renda usuario 
    if data.get('gastos_moradia') > data.get('renda_usuario') * 0.30:    
        print(f"Seus gastos totais com moradia comprometem {round(data.get('gastos_moradia') / data.get('renda_usuario') * 100, 2)}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R${round(data.get('renda_usuario') * 0.30, 2)}")
    #gastos moradia < renda usuario
    elif data.get('gastos_moradia') <= data.get('renda_usuario') * 0.30:
        print(f"Seus gastos totais com moradia comprometem {round(data.get('gastos_moradia') / data.get('renda_usuario') * 100, 2)}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.")
        
    #gastos educação > renda usuario
    if data.get('gastos_educação') > data.get('renda_usuario') * 0.20:
        print(f"Seus gastos totais com educação comprometem {round(data.get('gastos_educação') / data.get('renda_usuario') * 100, 2)} de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {round(data.get('renda_usuario') * 0.20, 2)}")
    #gastos educação < renda usuario
    elif data.get('gastos_educação') <= data.get('renda_usuario') * 0.20:
        print(f"Seus gastos totais com educação comprometem {round(data.get('gastos_educação') / data.get('renda_usuario') * 100, 2)}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendado")
       
    #gastos transporte > renda usuario    
    if data.get('gastos_transporte') > data.get('renda_usuario') * 0.10:
        print(f"Seus gastos totais com transporte comprometem {round(data.get('gastos_transporte') / data.get('renda_usuario') * 100, 2)}% de sua renda total. O máximo recomendado é de 10%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R${round(data.get('renda_usuario') * 0.10, 2)}")
    #gastos transporte < renda usuario
    elif data.get('gastos_transporte') <= data.get('renda_usuario') * 0.10:
        print(f"Seus gastos totais com transporte comprometem {round(data.get('gastos_transporte') / data.get('renda_usuario') * 100, 2)}% de sua renda total. Seus gastos estão dentro da margem recomendado")
        
def main():
   user_data = dados_usuarios()
   if user_data != None:
    validacoes(user_data)

main()