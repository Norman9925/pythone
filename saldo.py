# scrivete una funzione che calcoli il saldo di un conto bancario dopo che siano trascorsi un dato numero di anni,
# a partire da un dato saldo iniziale e con un dato tasso di interesse annuo, accreditando gli interessi annualmente.

def saldo(saldo_iniziale, tasso, numero_di_anni = None) :
  if numero_di_anni == None :
    # stampare 20 valori del saldo anno dopo anno
    saldo_corrente = saldo_iniziale
    for I in range(20) :
      print(saldo_corrente += (1 + tasso)
    saldo_iniziale *= tasso
   else :
      return saldo_finale = saldo_iniziale * (1 + tasso) ** numero_di_anni 
      # restituisco (return) il saldo richiesto
  print(saldo_finale)
saldo(10000, 0.04, 10)
