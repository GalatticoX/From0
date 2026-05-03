import requests
import time
maschera = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
nome_file = input("Digita il file da scansionare: ")
with open(nome_file, "r")as file_bersagli:
    for riga in file_bersagli:
        parola = riga.strip()
        try:
            risposta = requests.get(parola + "robots.txt", headers=maschera)
            if risposta.status_code == 200:
                print("🟢 TROVATO: " + parola + "robots.txt")
                with open("report_vulnerabili", "a") as file_report:
                    file_report.write("Breccia individuata: " + parola + "robots.txt\n")
            else:
                print("🔴 CHIUSO: " + parola + "robots.txt")
            time.sleep(1)
        except:
            print("⚫ERRORE: " + parola + "robots.txt")
THE END....?

