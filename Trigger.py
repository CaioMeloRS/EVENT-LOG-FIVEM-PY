# TROCAR JSOHN PARA LUA E TRANSFORMAR EM TRIGGER
# Solicita a primeira frase ao usuário
frase1 = input("Digite a primeira frase: ")

# Adiciona aspas em torno da primeira frase
frase1 = '"' + frase1 + '"' + ","

# Solicita a segunda frase ao usuário
frase2 = input("Digite a segunda frase: ")

# Substitui os colchetes por chaves na primeira frase
frase1 = frase1.replace("[", "{").replace("]", "}")

# Adiciona aspas no começo da segunda frase
#frase2 = '"' + frase2

# Verifica se o primeiro ou último caractere da segunda frase é um colchete
if frase2[0] == "[":
    frase2 = "" + frase2[1:]
if frase2[-1] == "]":
    frase2 = frase2[:-1] + ""
    
    
    # Verifica se o segundo caractere da segunda frase é um colchete e, nesse caso, o substitui por uma string vazia
#if frase2[1] == "[":
   # frase2 = frase2[0] + "" + frase2[2:]

# Substitui os colchetes restantes na segunda frase por chaves
frase2 = frase2.replace("[", "{").replace("]", "}")

# Junta as duas frases
frase_final = frase1 + frase2

# Adiciona a palavra "TriggerServerEvent" antes da frase final
frase_final = "TriggerServerEvent" + "(" + frase_final + ")" +")"

# Exclui o penúltimo caractere da frase final
frase_final = frase_final[:-1]

# Exibe a frase final para o usuário
print(frase_final)