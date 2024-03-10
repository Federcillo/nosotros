dizionario_moderno = {
    "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
    "LOL": "Una risposta comune a qualcosa di divertente",
}

parola = input("Scrivi una parola che non capisci:")

if parola.upper() in dizionario_moderno.keys():
    print(parola.upper(), dizionario_moderno[parola.upper()])
else:
    print("La parola inserita non esiste!")
