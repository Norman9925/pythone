# identificare i caratteri unicode che rappresentano i 4 semi del poker (cuori, quadri, fiori, picche) nella variante solo bordo.
#creare una stringa con i 4 semi nell'ordine scritto sopra
solo_bytes = b"\xe2\x99\xa1\xe2\x99\xa2\xe2\x99\xa7\xe2\x99\xa4"
stringa = solo_bytes.decode()
print(stringa)
