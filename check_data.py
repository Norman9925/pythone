#acquisire l'input da utente controllando se il contenuto della stringa può essere interpretato come una data. Restituirlo ('print') in un formato standard
# 3/3/25   => 03-03-2025
# 7-5-24   => 07-05-2024
# 29/3     => 29-03-2025
# 2 2 25   => 02-02-2025
#5 maggio  => 05-05-2025

valore_stringa = input("passami una data da verificare: ")
passami una data da verificare: 3/3/25
len(valore_stringa)
indice = 0
ANNO_DEFAULT = 2025
giorno = ""
mese = ""
anno = ""
fase = "G" # "M", "A"
while indice < len(valore_stringa):
  current = valore_stringa[indice]
 # print(current)
  if not current.isdigit():
  if fase == "G":
    fase = "M"
     indice += 1
    continue
   if fase == "M"
    fase = "A"
    indice += 1
    continue
   if fase == "A":
      break
    else:
      if fase == "G":
         giorno += current
      if fase == "M":
         mese += current
      if fase == "A":
         anno += current
        
       indice += 1     
      giorno = int(giorno)
      mese = int(mese)
      anno = int(anno)
     if anno < 50:
       anno += 2000
     if anno < 100:
       anno += 1900
    #  print(giorno, mese, anno, sep= "-")
  print(f"{giorno:02d}-{mese:02d}-{anno:04d}")
  
