abcdario = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"}

print("dime un texto")
texto = input()

if (len(abcdario.difference(texto))) == 0:
    print("estan todas las letras del abecedario")

if (len(abcdario.difference(texto))) > 0:
    print("te faltan letras")



