#ricevuti in input:
# un carattere da utilizzare
# l'ampiezza della base
# rappresentare l'albero
carattere = str(input("Inserisci il carattere da utilizzare: "))
base = int(input("Inserisci la base da utilizzare: "))
i = 1
while i <= base :
  print(" "  * ((base - i) // 2) +
        char  * (i + 1 - (base % 2)))
  i += 2
