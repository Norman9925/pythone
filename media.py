# acquisire tramite input una sequenza di valori numerici fino a che l'utente non scriva **exit**.
# in tal caso stampare la media dei valori letti
somma_numeri = 0
numeri_letti = 0
valore_stringa = input("inserisci il prossimo valore oppure 'exit': ")
while valore_stringa != "exit" :
  numeri_letti += 1
  somma_numeri += int(valore_stringa)
  valore_stringa = input("inserisci il prossimo valore oppure 'exit': ")
  #print("i numeri_letti sono: ", numeri_letti)
  #print("la somma dei numeri è: ", somma_numeri)
 print("la media dei numeri letti è: ", somma / numeri_letti)
