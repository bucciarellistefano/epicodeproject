#Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video

nome_scuola = 'Epicode' 
print(nome_scuola)

#Abbiamo la stringa : nome_scuola "Epicode" Stampare l'iniziale

print(nome_scuola[0])

#Abbiamo la stringa : nome_scuola = "Epicode" Stampare le prime tre lettere, utilizzare le parentesi quadre [] e l'operatore ':' per accedere agli elementi della stringa mediante slicing

print(nome_scuola[0:3])

#Stampare la stringa trasformando tutte le lettere in maiuscole utilizzanda il metodo .upper()

print(nome_scuola.upper(), "\n")

#Abbiamo la variabile x = 10 incrementarla di 2 e poi moltiplicarla per 3, Usando due metodi diversi

#Metodo 1
"""
x = 10
numero_incrementi = 2
i = 0
while i < numero_incrementi:
    x += 1
    i += 1
x = x * 3
print(x)
"""
#Metodo 2
"""
x = 10
x = (x+2)*3
print(x)
"""

#Scriviamo un programma che chiede all'utente in input: i litri di benzina nel serbatoio, l'efficienza espressa in km per litro, il prezzo della benzina per litro e visualizza il costo per 100km

def costo_viaggio():
    litri = float(input("Inserisci i litri presenti nel serbatoio: \n")) #dato inutile
    efficienza = float(input("Inserisci l'efficienza della macchina espressa in km/l: \n"))
    prezzo = float(input("Inserisci il prezzo in euro della benzina per litro: \n"))
    print("Il costo per 100 km del tuo viaggio sarà:", (prezzo / efficienza * 100), "Euro")

#costo_viaggio()

#Scriviamo un programma che chidere in input all'utente una stringa e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri
def manipolazione_stringa():
    stringa = input("Inserisci la stringa che vuoi manipolare:\n")
    print(stringa[0:3] + "..." + stringa [-3:])

#manipolazione_stringa()

#Verificare, Per ognuna delle seguenti stringhe se il numero di caratteri è compreso tra 5 e 8: Epicode, Windows, Excel, Powerpoint, Word
lista_stringhe= ['Epicode', 'Windows', 'Excel', 'Powerpoint', 'Word']

for i in range(len(lista_stringhe)):
    print("La lunghezza della parola '", lista_stringhe[i], "' è :", len(lista_stringhe[i]))
    if 5 <=len(lista_stringhe[i]) <= 8:
        print("Compreso\n")
    else:
        print("Non compreso\n")


#Abbiamo la seguente lista di codici prodotto: codici = ["knt-S1", "cba-G9", "qtr-z8"] Per ognuno dei codici, estrarre la parte finale (gli ultimi tre caratteri, quindi trattino incluso) e memorizzarlo in tre variabili
codici = ["knt-S1", "cba-G9", "qtr-z8"]
for i in range(len(codici)):
    variable_name = f"cod{i}"
    exec(f"{variable_name} = '{codici[i][-3:]}'")
    
for i in range(len(codici)):
    variable_name = f"cod{i}"
    print(f"{variable_name}", "è", eval(variable_name), "\n")
#Il codice qui sopra è una overcomplicazione di qualcosa che poteva essere molto più semplice però ho cercato di automatizzare il processo in modo che venissero create automaticamente variabili numerate in base al numero degli elementi presenti sulla lista

#Abbiamo un insieme(set) di titoli di azioni 'growth') di titoli di azioni "growth" (ciow  che hanno una cescita dei ricavi maggiore della media):
growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre", "Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}

#Abbiamo un insieme di titoli "value" (cioè titolii che offrono agli investitori un elevato ritorno sull'investimento, garantendo al contempo stabilità e sicurezza):
value = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.", "Wells Fargo & Co,", "Verizon Communications", "BP PLC", "LyondellBasell Industries", "MetLife", "Interactive Broker Group", "Intel"}

#Abbiamo un insieme di titoli di aziende ad alta tecnologia:
tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platform", "Tesla", "Alibaba", "Salesforce", "Advances Micro Devices", "Intel", "Paypal", "Activision Blizzard", "Electronic Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}

#Abbiamo un insieme di titoli di aziende nell'healthcare:
healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lily & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer", "Thermo Fisher Scientific", "Abbott Laboratories"}

#Si vuole diversificare l'investimento, investendo in aziende growth e value, quali sono le aziende?
#growth_or_value =  growth | value 
print("Le aziende che comprendono titoli di tipo 'Growth' u 'Value' sono :\n", growth | value , "\n")   

#Quali sono le aziende tecnologiche growth?
#tech_and_growth = tech & growth
print("Le aziende che fanno parte sia del campo 'Tech' e del campo 'Growth' sono :\n", tech & growth, "\n")

#Si vuole investire sia in aziende tecnologiche che value, quali si devono considerare?
#tech_or_growth = tech | value
print("Le aziende facendi parte del gruppo sia 'Tech' che 'Value' sono:\n", tech | value, "\n")

#Quali sono i titoli healthcare che non sono value
#healthcare_but_not_value = healthcare - value
print("I titoli che fanno parte del gruppo 'Healthcare' ma non fanno parte di 'Value' sono:\n", healthcare - value, "\n")

#In quali deve investire se vuole azioni tech ma solo se siano growth o value?
#tech_in_growth_or_value = tech & (growth | value)
print("I Titoli che sono 'Tech' ma che fanno parte di 'Growth' o 'Value':\n", tech & (growth | value), "\n")