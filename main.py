#nome = input("Come ti chiami? ")
#print("ciao " + nome + "! prepariamoci a contare i danni! ")
#hamburger = input("quanti hamburger hai mangiato oggi? non mentire! ")
#patatine = input("e le patatine invece, quante porzioni ne hai mangiate? ")
#hamburger_numero = int(hamburger)
#patatine_numero = int(patatine)
#totali_sgarri = hamburger_numero + patatine_numero
#print(nome + " oggi hai mangiato la bellezza di: " + str(totali_sgarri) + " Sgarri!")
#-----------------------------------------------------------------------------------------------------------------------
#eta_numero = int(eta_testo)
#eta_futura = eta_numero + 5
#print("la tua età tra 5 anni sarà: " + str(eta_futura) + " Anni!")
#-----------------------------------------------------------------------------------------------------------------------
#password = "renatino"
#tentativo = ""
#tentativi = 0
#while tentativo.lower() != password and tentativi < 3:
#    tentativo = input("Inserisci la password: ")
#    tentativi = tentativi+1
#if tentativo.lower() == password:
#    print("Bingo! sei dentro al Mainframe")
#else:
#    print("Tentativi esauriti, esci.")
#-----------------------------------------------------------------------------------------------------------------------
#blacklist = ["hacker99", "mrrobot", "er_gala", "wrench"]
#username = input("Inserisci il Nome Utente: ")
#username = username.lower()
#if username in blacklist:
#    print("Beccato il furbetto, rimani fuori.")
#else:
#    print("Benvenuto " + username + "!")
#-----------------------------------------------------------------------------------------------------------------------
#password = "renny"
#dizionario = ["renatino", "renno", "1234", "renny", "bau"]
#for tentativo in dizionario:
#    print("Sto scansionando: " + tentativo)
#    if tentativo == password:
#        print("Password individuata!" + "\n" + tentativo + " è la password!")
#        break
#-----------------------------------------------------------------------------------------------------------------------
#VERIFICA
file_server = ["sistema.sys", "config.ini", "malware.exe", "dati.db", "log.txt"]
password_corretta = "admin"
tentativo = ""
tentativi = 0
while tentativo.lower() != password_corretta and tentativi < 3:
    tentativo = input("Inserisci la password: ")
    tentativi = tentativi+1
if tentativo.lower() == password_corretta:
    print("ACCESSO CONSENTITO.")
    for file in file_server:
        print("Analisi in corso: " + file)
        if file.endswith(".exe"):
            print(file + " RILEVATO, DISTRUZIONE TRA 3...2...1.... MALWARE DISTRUTTO.")
            break
else:
    print("ACCESSO NEGATO.")

 
