reddito=int(input("Inserisci il reddito: "))
ALIQUOTA_1 = 0.23
ALIQUOTA_2 = 0.35
ALIQUOTA_3 = 0.43
SCAGLIONE_1 = 28000
SCAGLIONE_2 = 50000
imposta = 0
if reddito <= SCAGLIONE_1:
  imposta = reddito * ALIQUOTA_1
else:
  if reddito > SCAGLIONE_1 and reddito <= SCAGLIONE_2:
    imposta = (SCAGLIONE_1 * ALIQUOTA_1 + (reddito - SCAGLIONE_1) * ALIQUOTA_2
  else:
    imposta = (SCAGLIONE_1 * ALIQUOTA_1 + 
              (SCAGLIONE_2 - SCAGLIONE_1) * ALIQUOTA_2 +
              ( reddito - SCAGLIONE_2) * ALIQUOTA_3)
    print("l'imposta da pagare è: ", imposta)
