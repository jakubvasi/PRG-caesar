# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 13:12:35 2018

@author: Kuba
"""

import os

# Abeceda zacina nejcetnejsim znakem E
abeceda = "EFGHIJKLMNOPQRSTUVWXYZABCD"

#__Funkce__________________________________________________________________________________________#

# Kontrola velikosti souboru, vychozi hodnota: 64kB
def size_check(soubor, maxSize = 0xFFFF):
    try:
        statinfo = os.stat(soubor)
    except:
        print("Neplatny nazev")
        return 1
    
    if statinfo.st_size > maxSize:
        print("Prilis velky soubor")
        return 1
    return 0

def ziskej_soubor(hlaska = "Zadejte nazev souboru: "):
    zadejNazev = True
    while zadejNazev:
        soubor = input(hlaska)
        zadejNazev = size_check(soubor)
    return soubor

def ziskej_bool(dotaz = "ANO/NE"):   #Vrací hodnotu True/False dle odpovědi
    x = input(dotaz)
    if x.upper() == 'A' or x.upper() == "ANO":
        return True
    else:
        return False
    
def vytvor_soubor(soubor):
    with open(soubor, "w"):
        pass

def zapis_soubor(soubor, klic, data):
    with open(soubor, "a") as f:
        f.write("Klic:" + klic + "\n")
        f.write(data)
        f.write("\n")
        
# Vraci nejcetnejsi znak
def nej_znak(text):    
    znaky = {}
    text = text.upper()
    
    for znak in text:
        # Ignoruje znaky mimo abecedu
        if not znak in abeceda:
            continue
        # Pokud je pismeno ve slovniku, inkrementuje jeho pocet
        if znak in znaky:
            znaky[znak] += 1
        # Pokud pismeno jeste neni ve slovniku, prida ho
        else:
            znaky[znak] = 1
    
    #Vrati nejcetnejsi znak
    return max(znaky, key=znaky.get)    


def desifruj(text, klic):
    text2 = ""
    
    posun = -abeceda.index(klic)
    sifra = abeceda[posun:] + abeceda[:posun]
    for x in text:
        try:
            text2 += sifra[abeceda.index(x)]
        except ValueError:
            text2 += x
    return(text2)



#__Hlavni program__________________________________________________________________________________#
# Nazev noveho souboru
novySoubor = "desifra.txt"

print("Vita vas program louskacek. Spolecne rozlouskneme cokoli!")
soubor = ziskej_soubor("Zadejte nazev zasifrovaneho souboru: ")

# Vytvori soubor pro zapis vysledku
vytvor_soubor(novySoubor)

# Otevre zasifrovany soubor
with open("sifra.txt", "r") as f:
    sifrovanyText = f.read()

# Najde nejcastejsi znak v textu
klic = nej_znak(sifrovanyText)
desifrovany_text = desifruj(sifrovanyText, klic)

print(desifrovany_text)
odpoved = ziskej_bool("Je text v poradku? A/N: ")

if(odpoved):
    zapis_soubor(novySoubor, klic, desifrovany_text)

else:
    print("Dobra, kdyz to nejde po dobrem, zkusime to silou. Hrubou silou!")
    for klic in abeceda:
        desifrovany_text = desifruj(sifrovanyText, klic)
        zapis_soubor(novySoubor, klic, desifrovany_text)
    print("Hotovo. Ani Caesar neprekona hrubou silu!")

print("Desifrovany text je ulozen v souboru: ", novySoubor)
input("Stisknutim klavesy enter me muzete ukoncit. Tesim se na pristi louskani.")