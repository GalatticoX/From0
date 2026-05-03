#import requests
#bersaglio = "https://www.google.com/"
#wordlist = ["admin", "login", "robots.txt", "area-riservata"]
#for parola in wordlist:
#    url_attacco = bersaglio + parola
#    risposta = requests.get(url_attacco)
#    if risposta.status_code == 200:
#        print("🟢 TROVATO: " + url_attacco)
#    else:
#        print("🔴 CHIUSO: " + url_attacco)
#-----------------------------------------------------------------------------------------------------------------------
import requests
import time
maschera = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
bersaglio = input("Inserisci l'URL da attaccare: 'RICORDA https:// !' ")
with open("wordlist.txt", "r") as file:
    for riga in file:
        parola = riga.strip()
        url_attacco = bersaglio + parola
        try:
            risposta = requests.get(url_attacco, headers=maschera)
            if risposta.status_code == 200:
                print("🟢 TROVATO: " + url_attacco)
            else:
                print("🔴 CHIUSO: " + url_attacco)
            time.sleep(1)
        except:
            print("⚫ ERRORE: IMPOSSIBILE RAGGIUNGERE: " + url_attacco)
#-----------------------------------------------------------------------------------------------------------------------
#import requests
#maschera = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#}
#bersaglio = "https://httpbin.org/user-agent"
#risposta = requests.get(bersaglio, headers=maschera)
#print(risposta.text)