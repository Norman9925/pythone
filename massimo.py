#acquisire una serie di numeri interi adottando un valore sentinella per terminare la lettura (input()). Quindi stampare il valore massimo. Adottare **q** come valore sentinella.

prova = []
userInput = input("Inserisci un numero: ")
while userInput != "q":
    prova.append(int(userInput))
    userInput = input("Inserisci un numero: ")
temp = None
for v in prova:
    if temp == None:
        temp = v
    else:
        if temp < v:
            temp = v
print("valore max", temp)
