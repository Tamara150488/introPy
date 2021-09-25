# 1 - imports / bibliotecas

# 2 - Classes

# 3 - Métodos e Funções
# def = definition = definição
def print_hi(name):
    print(f'Oi, {name}')


def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2


def calcular_area_do_tringlo(largura, comprimento):
    return largura * comprimento / 2


def contagem_progressiva(fim):
    for numero in range(fim):  # repetir o bloco de zero até  fim
        print(numero)


def apoiar_candidato(nome, vezes):
    for numero in range(vezes):

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)


def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))


def exibir_dia_da_semana_if(numero):
    if numero == 1:
        print('O dia é segunda')
    elif numero == 2:
        print('O dia é terça')
    elif numero == 3:
        print('O dia é quarta')
    elif numero == 4:
        print('O dia é quinta')
    elif numero == 5:
        print('O dia é sexta')
    elif numero == 6:
        print('O dia é sábado')
    elif numero == 7:
        print('O dia é domingo')
    else:
        print('Número inválido, Digite o número 1 a 7')

'''
def exibir_dia_da_semana_match(numero):
    print('Execução com MATCH')

    match numero:
        case 1:
            print('O dia é segunda')
            exit()
        case 2:
            print('O dia é terça')
            exit()
        case 3:
            print('O dia é quarta')
            exit()
        case 4:
            print('O dia é quinta')
            exit()
        case 5:
            print('O dia é sexta')
            exit()
        case 6:
            print('O dia é sábado')
            exit()
        case 7:
            print('O dia é domingo')
            exit()
    case_:
    print('Número inválido, Digite o número 1 a 7')
'''
def brincar_de_para_ou_continua():
    resposta = 'C'     #C aqui significa que continua

    #while resposta== 'C' or resposta == 'c':
    while resposta.upper() == 'C':
        resposta = input('Digite Cc para continuar ou qualquer caracter para parar')

    print('Você decidiu parar a brincadeira')


# estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Tamara')

    # chamar a função de calulo da area do retangulo
    resultado = calcular_area_do_retangulo(5, 3)
    print(f'A área do retângulo é de {resultado} m²')

    # chamar a função de calulo da area do quadrado
    resultado = calcular_area_do_quadrado(4)
    print(f'A área do qudrado é de {resultado} m²')

    # chamar a função de calulo da area do retangulo
    resultado = calcular_area_do_retangulo(2, 4)
    print(f'A área do triangulo é de {resultado} m²')

    # executar uma contagem progressiva
    contagem_progressiva(10)

    # exibir o  nome do candidato varias vezes
    apoiar_candidato('Fake', 100)

    # brincar de Plim
    brincar_de_plim(101)

    # exemplo de dia da semana co if - elif  - else
    exibir_dia_da_semana_if(' ')

    # exemplo de dia da semana com if - elif  - else
    #exibir_dia_da_semana_match(1)

    #exemplo com while - para ou continua
    brincar_de_para_ou_continua(' ')

