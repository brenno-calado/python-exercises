def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    secret_word = "banana"
    acertos = len(secret_word) * ['_']
    enforcou = False
    acertou = False
    print(acertos)
    while(not enforcou or not acertou):
        falta = acertos.count('_')
        print('Tentativa {} de {}...')
        print('Faltam {} letras para acertar a palavra'.format(falta))
        chute = input('Digite uma letra:')
        chute = chute.strip()
        index = 0
        for letra in secret_word:
            if(chute.upper() == letra.upper()):
                acertos[index] = letra
            index += 1
        print('palavra: ',''.join(acertos),'\n')
        

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
