
def jogar():

    welcome_message()
    load_words()
    secret_word = load_game_mode()
    acertos = load_acertos(secret_word)

    tentativa = 0
    chances = 6
    print('palavra: ',''.join(acertos),'\n')
    while(True):
        print('Tentativa {} de {}...'.format(tentativa + 1,chances))
        print('Faltam {} letras para acertar a palavra'.format(acertos.count(' _ ')))
        
        guess = try_guess()
        print('*******************************************************')
        if(guess in secret_word):
            find_match()
        else:
            tentativa += 1
            print('\033[31m','Ops! Você errou!')
            print('\033[39m')
        
        print('palavra: ',''.join(acertos),'\n')
        if(acertos.count(' _ ') == 0):
            print('Você ganhou! Parabéns!')
            break
        elif(tentativa == chances):
            print('Tente outra vez!')
            break

    bye_message()

def welcome_message():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************"'\n\n')

def load_words():
    words = []
    with open('palavras.txt') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    return words

def load_game_mode():
    from getpass import getpass
    import random

    words = load_words()

    secret_word = ''
    while(secret_word == ''):
        game_mode = input('Digite o modo do jogo: (1) jogador OU (2) jogadores: ')
        if(game_mode == '2'):
            secret_word = getpass("coloque uma palavra secreta para o amigo adivinhar: ").upper()
        elif(game_mode == '1'):
            random_index = random.randrange(0, len(words))
            secret_word = words[random_index].upper()
        else:
            print('Por favor, Digite o número 1 ou 2...')
    return secret_word

def load_acertos(secret_word):
        return [' _ ' for letra in secret_word]

def try_guess():
    guess = input('Digite uma letra:').strip().upper()
    return guess

def find_match(secret_word, guess, acertos):
    index = 0
    for letra in secret_word:
        if(guess == letra.upper()):
            acertos[index] = " {} ".format(letra)
        index += 1
    print('\033[32m','Acertou!')
    print('\033[39m')

def bye_message():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~Fim do jogo!~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if(__name__ == "__main__"):
    jogar()
