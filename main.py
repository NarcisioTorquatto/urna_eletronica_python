def pedir_numero_titulo():
    # Esta função solicita o número do título de eleitor e valida o comprimento do número inserido
    while True:
        titulo_de_eleitor = input('Informe seu título de eleitor: ')
        if len(titulo_de_eleitor) == 10:
            return titulo_de_eleitor  # Retorna o número do título se estiver correto
        else:
            print('Erro: o número do documento precisa ter 10 dígitos')

# Loop principal do programa
while True:
    print('\nEscolha uma Opção:\n')
    print('[1] - Novo Voto')
    print('[2] - Resultado')
    print('[3] - Sair\n')

    # Solicitação da opção do menu
    opcao_menu = int(input('Informe a opção desejada: '))

    if opcao_menu == 1:
        nome_do_eleitor = input('Informe o nome do eleitor: ')
        data_de_nascimento = input('Informe a sua data de nascimento: ')
        numero_do_titulo = pedir_numero_titulo()  # Chama a função para obter o número do título

        print('Escolha o número do Candidato que deseja votar: ')
        print('[1] - Bolsonaro')
        print('[2] - Lula')

        # Solicitação do voto do eleitor
        candidato = int(input('Informe o número do candidato que deseja votar: '))

        # Confirmação do voto
        if candidato == 1:
            print('Deseja votar em Bolsonaro?')
        elif candidato == 2:
            print('Deseja votar em Lula?')

        # Opções para confirmar, cancelar ou sair
        opcao = input('[1] - Sim  [2] - Não  [3] - Sair')

        if opcao == '1':
            print('VOTO CONFIRMADO')
        elif opcao == '2':
            continue  # Retorna ao início do loop principal
        elif opcao == '3':
            break  # Sai do loop principal

    elif opcao_menu == 2:
        print('Mostrando resultados...')

    elif opcao_menu == 3:
        break  # Sai do loop principal

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')  # Mensagem de erro para opções inválidas
