# import this  #The Zen of Python
import os

restaurantes = [{'nome':'Okazam Sushishow', 'categoria':'Japonesa','ativo' :False},
                {'nome':'OXinxei', 'categoria':'Japonesa','ativo' :True},
                {'nome':'Kynuin', 'categoria':'Japonesa','ativo' :False}]

def exibir_nome():
    print ('Sabor Express')

def opcoes():
    print ('1 - Cadastrar Restaurante')
    print ('2 - Listar Restaurante')
    print ('3 - Alternar Status Restaurante')
    print ('4 - Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu  ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print (linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurante')
    nome_restaurante = input('Digite o nome do restaurante:  ')
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")
    dados_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!!!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print ('Restaurante não encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
