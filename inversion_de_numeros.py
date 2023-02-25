# programa para inveritr un numero de tres digitos

print("------------------------------------")
print("----------invertir numeros----------")
print("------------------------------------")

#input

n = int(input("digite elnumero de tres cifras: "))

#procesing

mod = n % 10      #3cer digito
de  = n  // 10
mod2 =  de % 10   #2do digito
de2 = de // 10    #1er digito

ni = mod*100 + mod2*10 + de2
#output

print("------------------------------------")
print("----------RESULTADO-----------------")
print("------------------------------------")
print("numero invertido:" + str(ni))