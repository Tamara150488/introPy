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
    for numero in range(fim):       #repetir o bloco de zero até  fim
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1,'-', nome)

def brimcar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))


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
    resultado = calcular_area_do_retangulo(2,4)
    print(f'A área do triangulo é de {resultado} m²')

    # executar uma contagem progressiva
    contagem_progressiva(10)

    # exibir o  nome do candidato varias vezes
    apoiar_candidato('Fake', 100)

    #brincar de Plim
    brimcar_de_plim(101)