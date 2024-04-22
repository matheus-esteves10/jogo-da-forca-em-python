print("------------------------------")
print("Bem vindo ao jogo da forca")
print("------------------------------")



sorteada = "frango assado"
erros = 0


segredo = ""
for caractere in sorteada:
    if caractere == " ":
        segredo = segredo + "   "
    else:
        segredo = segredo + "_ " 
    


print(f'{segredo} \n Número de erros: {erros}') #_ _ _ _ _   _ _ _ _ _ _

letra_usuario = str(input('Chute uma letra: ')).lower().strip()

if letra_usuario in sorteada:
    segredo = ""
    for caractere in sorteada:
        if caractere == letra_usuario:
            segredo = segredo + letra_usuario + " "
        elif caractere == " ":
            segredo = segredo + "   "
        else:
            segredo = segredo + "_ "
    
else:
    erros = erros + 1

print(f'{segredo} \n Número de erros: {erros}')