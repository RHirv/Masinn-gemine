def sisendi_kontroll(sisend):
    while True:
        #Muudame sisendi ujukomaarvuks ja ümardame selle lähima täisarvuni
        value = float(input(sisend))
        value = round(value)
            
        #Kontrollime, kas number on mõistlikus vahemikus (1 kuni 50)
        if 1 <= value <= 50:
            return value
        else:
            print("Palun sisestage number vahemikus 1 kuni 50.")


def loo_muster(muster, rida, tulp):
    #Loome mustri ja prindime seda ridade ja tulpade arvu järgi
    for _ in range(rida):
        # Iga rea puhul prindime mustri 'tulp' korda
        print(muster * tulp)

#Kuvame kasutajale juhised
print("Programm genereerib mustri.")
print("Palun sisestage ridade ja tulpade arv (vahemikus 1 kuni 50).")

#Küsime kasutajalt ridade ja tulpade arvu ning valideerime sisendi
rida = sisendi_kontroll("Mitu rida: ")
tulp = sisendi_kontroll("Mitu tulpa: ")

#Määrame mustri
muster = "/*/*/*/*/*/*/"

#Genereerime mustri
loo_muster(muster, rida, tulp)
