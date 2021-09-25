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


def sair():
    print('Obrigada e Volte Sempre!!!')


def exibir_menu(escolha):
    opcao = {
        1: print_hi('Tamara'),
        2: calcular_area_do_retangulo(3, 6),
        3: calcular_area_do_quadrado(5),
        4: calcular_area_do_tringlo(3, 9),
        5: contagem_progressiva(10),
        6: apoiar_candidato('Sábado', 20),
        7: brincar_de_plim(20),
        8: sair()
    }
    return opcao.get(escolha, 'Opção Inválida')


# estrutura de identificação / execução do script
if __name__ == '__main__':

    resposta = 'C'

    while resposta.upper() != 'Z':
        print('##################################')
        print('#                                #')
        print('#   M E N U   D E  O P Ç Õ E S   #')
        print('#                                #')
        print('#     1 - Olá Mundo              #')
        print('#     2 - Área do Retangulo      #')
        print('#     3 - Área do Quadrado       #')
        print('#     4 - Área do Triangulo      #')
        print('#     5 - Contagem Progressiva   #')
        print('#     6 - Apoiar Candidato       #')
        print('#     7 - Brincar de Plim        #')
        print('#                                #')
        print('#     Z - Sair                   #')
        print('#                                #')
        print('##################################')

        resposta = input('Escolha sua Opção')
        print(f'A sua escolha foi: {resposta}')


        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Tamara')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(3, 6)
                print(f'A área do retangulo é de {resultado} m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(5)
                print(f'A área do quadrado é de {resultado} m²')
            elif resposta == '4':
                resultado == calcular_area_do_tringlo(3, 9)
                print(f'A área do triangulo é de {resultado} m²')
            elif resposta == '5':
                contagem_progressiva(10),
            elif resposta == '6':
                apoiar_candidato('Sábado', 20)
            elif resposta == '7':
                brincar_de_plim(20),
            else:
                print('Voçê digitpu uma opção inválida. Escolha uma opção de 1 a 7.')


    print('Obrigada e Volte Sempre!!!')