import random

print("------------------------------")
print("Bem vindo ao jogo da forca")
print("------------------------------")



lista_de_palavras = ["frango assado", "maça", "banana", "amendoim", "batata frita", "chocolate", "carne assada", "arroz", "feijao", "abobrinha", "couve flor", "alface", "tomate"]
sorteada = random.choice(lista_de_palavras)
erros = 0
chutadas = " "

segredo = ""

for caractere in sorteada:
    if caractere in chutadas:
            segredo = segredo + caractere + " "
    else:
            segredo = segredo + "_ "


while erros < 6 and "_" in segredo:
    print(f'{segredo} \n Número de erros: {erros}') 
    print(f"Letras chutadas: {', '.join(chutadas[1:])}")
    letra_usuario = str(input('Chute uma letra: ')).lower().strip()
    chutadas = chutadas + letra_usuario

    segredo = ""
    for caractere in sorteada:
        if caractere in chutadas:
            segredo = segredo + caractere + " "
        else:
            segredo = segredo + "_ "
    
    if not letra_usuario in sorteada:
         erros = erros + 1

if erros == 6:
     print(f"Você foi enforcado. A palavra era {sorteada}")
else:
     print(f"Parabéns, você acertou a palavra {sorteada}")
