def jogar():
    from getpass import getpass
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************"'\n\n')
    secret_word = ''
    while(secret_word == ''):
        game_mode = input('Digite o modo do jogo: (1) jogador OU (2) jogadores: ')
        if(game_mode == '2'):
            secret_word = getpass("coloque uma palavra secreta para o amigo adivinhar: ").upper()
        elif(game_mode == '1'):
            secret_word = 'jazz'.upper()
        else:
            print('Por favor, Digite o número 1 ou 2...')
    acertos = len(secret_word) * [' _ ']
    tentativa = 0
    chances = 6
    print('palavra: ',''.join(acertos),'\n')
    while(True):
        print('Tentativa {} de {}...'.format(tentativa + 1,chances))
        print('Faltam {} letras para acertar a palavra'.format(acertos.count(' _ ')))
        chute = input('Digite uma letra:')
        chute = chute.strip().upper()
        print('*******************************************************')
        if(chute in secret_word):
            index = 0
            for letra in secret_word:
                if(chute == letra.upper()):
                    acertos[index] = " {} ".format(letra)
                index += 1
            print('\033[32m','Acertou!')
            print('\033[39m')
        else:
            tentativa += 1
            print('\033[31m','Ops! Você errou!')
            print('\033[39m')
        print('palavra: ',''.join(acertos),'\n')
        if(acertos.count(' _ ') == 0):
            print('Parabéns!')
            break
        elif(tentativa == chances):
            print('Tente outra vez!')
            break

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
