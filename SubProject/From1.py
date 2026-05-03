#def scansiona_ip(indirizzo):
#    print("Inizio scansione sul bersaglio " + indirizzo)
#    print("Ricerca porte aperte.........\nNessuna vulnerabilità trovata.\n")
#bersagli = ["192.168.1.1","10.0.0.5","255.168.1.0" ]
#for ip in bersagli:
#    scansiona_ip(ip)
#-----------------------------------------------------------------------------------------------------------------------
#mappa_rete = {
#"admin":"192.168.1.1",
#"boss":"10.0.0.5",
#"me":"255.168.1.0"
#}
#ricerca = input("Seleziona quale IP vuoi cercare: ")
#try:
#    print("Risultato trovato " + mappa_rete[ricerca])
#except:
#    print("Errore, Utente non presente nel Database.")
#-----------------------------------------------------------------------------------------------------------------------
#lista_ip = ["192.168.1.1","10.0.0.5","255.168.1.0"]
#with open("Scansiona_IP.txt", "w")as file:
#    for ip in lista_ip:
#        file.write("Sto scansionando l'IP di: " + str(ip) + "\n")
#-----------------------------------------------------------------------------------------------------------------------
#with open("Scansiona_IP.txt", "r") as file:
#    dati_estratti = file.read()
#print(dati_estratti)
#-----------------------------------------------------------------------------------------------------------------------
#VERIFICA
database_segreto = {
"admin":"supersegreta"
}
def verifica_accesso(utente, password):
    try:
        if password == database_segreto[utente]:
            print("Accesso consentito a: " + utente)
        else:
            print("Password errata.")
    except:
        print("Allarme: Utente sconosciuto.")
        with open("log_intrusi.txt", "a") as file:
            file.write("Tentativo di intrusione da: " + utente + "\n")
nome_utente = input("Inserisci il nome utente: ")
password_utente = input("Inserisci la password: ")
verifica_accesso(nome_utente, password_utente)
nome_utente = ()
password_utente = ()
