
frase1 = input("Digite a primeira frase: ")

frase1 = '"' + frase1 + '"' + ","

frase2 = input("Digite a segunda frase: ")

frase1 = frase1.replace("[", "{").replace("]", "}")

if frase2[0] == "[":
    frase2 = "" + frase2[1:]
if frase2[-1] == "]":
    frase2 = frase2[:-1] + ""

frase2 = frase2.replace("[", "{").replace("]", "}")

frase_final = frase1 + frase2

frase_final = "TriggerServerEvent" + "(" + frase_final + ")" +")"

frase_final = frase_final[:-1]

print(frase_final)
