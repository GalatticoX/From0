#import requests
#bersagli = ["https://www.google.com", "https://httpbin.org/status/404", "https://sito-finto-999.com"]
#for sito in bersagli:
#    try:
#        risposta = requests.get(sito)
#        if risposta.status_code == 200:
#            print("🟢 ONLINE: " + sito)
#        else:
#            print("🔴 PROBLEMA:(CODICE: " + str(risposta.status_code) + "): " + sito)
#    except:
#        print("⚫ IRRAGGIUNGIBILE: " + sito)
#-----------------------------------------------------------------------------------------------------------------------
#import requests
#risposta = requests.get("http://example.com")
#sorgente = risposta.text
#if "Domain" in sorgente:
#    print("Parola 'Domain' trovata!")
#else:
#    print("Parola 'Domain' non trovata")
#-----------------------------------------------------------------------------------------------------------------------
#import requests
#risposta = requests.get("https://jsonplaceholder.typicode.com/users")
#dati_utenti = risposta.json()
#with open("Dati_utenti.txt", "w") as file:
#    for singolo_utente in dati_utenti:
#        file.write("Dati utente: \n" + "Nome: " + singolo_utente["name"] + "\n" + "Email: " + singolo_utente["email"] + "\n---------------------------\n")
#-----------------------------------------------------------------------------------------------------------------------
#VERIFICA
import requests
id = input("Inserisci l'ID 'da 1 a 10' da cercare: ")
try:
    risposta = requests.get("https://jsonplaceholder.typicode.com/users/" + id)
    if risposta.status_code == 200:
        dati = risposta.json()
        with open("Dati.txt", "a") as file:
            file.write("Dati utente: \n" + "Nome: " + dati["name"] + "\n" + "Numero di telefono: " + dati["phone"] + "\n--------------------------------------------\n")
    else:
        print("Errore: Bersaglio inesistente")
except:
    print("Errore di connessione.")

