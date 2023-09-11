#Abbiamo la stringa: nome_scuola = "Epicode". Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while.

nome_scuola = "Epicode"
x = 0
while x < len(nome_scuola):
    print(nome_scuola[x])
    x += 1
print("\n")
#Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while

x = 0
while x <= 20:
    print(x)
    x += 1

#Calcolare e stampare tutte le prime 10 potenza di 2(e.g., 2^0, 2^1, 2^2,...) utilizzando un ciclo while

x = 0
while x <= 10:
    print(2 ** x)
    x += 1

#calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while domandando all'utente di inserire N
x = 0
while True:
    try:
        n = int(input("Inserisci N, ovvero il numero di elevazione a potenza di 2 che si vuole ottenere : "))
        break
    except:
        print("Inserisci un numero intero")

while x <= n :
    print(2 ** x)
    x += 1

#Abbiamo due liste, una di studenti e una di corsi:

studenti = [ 'Alex', 'Bob', 'Cyndy', 'Dan', 'Emma', 'Faith', 'Grace', 'Henry']
corsi = ['Cybersecurity', 'Data Analyst', 'Backend', 'Frontend', 'Data Analyst', 'Backend', 'Frontend']
#Verificare che entrambe le liste abbiano la stessa lunghezza e stampare a video una frase che ci dica se è cosi o meno
if len(studenti) == len(corsi) :
    print("Le liste hanno la stessa lunghezza")
else :
    print('Le liste non hanno la stessa lunghezza')

#Abbiamo due liste una di studenti e una di corsi (studenti è uguale alla precedente), aggiungere i danti mancanti alla lista corsi sapendo che
"""
Emma segue data analyst
Faith segue Backend
Grace segue Frontend
Henry segue Cybersecurity
"""
corsi2 = ['Cybersecurity', 'Data Analyst', 'Backend', 'Frontend', 'Data Analyst', 'Backend' ]
#Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in coda alle liste, poi verificheremo che sono della stessa lunghezza e se lo sono stamperermo la lista corsi


#Scriviamo un  programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri. Attenzioni a tutti i casi particolari, ovvero implementare soluzioni ad hoc per stringhe di lunghezza inferiori a 6 caratteri
ciao = input("Inserisci la stringa da trasformare: ")
if len(ciao) >= 6 :
    print(ciao[0:3] + "..." + ciao[-3:])
else :
    print(ciao[0 : (int(len(ciao)/2) + len(ciao)%2)] + "..." + ciao[- (int(len(ciao)/2)) : ])

#Memorizza e stampa tutti i fattori di un numero dato in input

def numero_primo(numero):
    i = 2
    while i < (numero/2):
        if numero%i == 0:
            return False
        i += 1
    return True

def fattori_primi(numero) :
    lista_fattori = [1]
    i = 2
    while i <= numero/2 :
        if numero%i == 0 and numero_primo(i):
            lista_fattori.append(i)
        i += 1
    return lista_fattori

def fattori_primi_ripetuti(numero):
    lista_fattori_primi = fattori_primi(numero)
    lista_fattori_ripetuti = []
    while numero > 1 :
        for i in lista_fattori_primi :
            if numero % i == 0 :
                lista_fattori_ripetuti.append(i)
                numero = numero / i
    return lista_fattori_ripetuti

        
    
        
    