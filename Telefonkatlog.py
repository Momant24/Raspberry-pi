telefonkatalog = []

def printMeny():
    print("-------------------Telfonkatalog-------------------")
    print("| 1. Legg til ny person                           |")
    print("| 2. Søk opp person eller telefonnummer           |")
    print("| 3. Vis alle personer                            |")
    print("| 4. Avslutt                                      |")
    print("| 5. Slett oppføring                              |")
    print("| 6. Rediger person                               |")
    print("---------------------------------------------------")
    menyvalg =input("Skriv inn for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
        printMeny()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "4":
        bekreftelse = input("Er du sikker på at du vil avslutte J/N ")
        if (bekreftelse == "J" or bekreftelse == "j"):
            exit()
    elif valgtTall == "5":
        Slettbruker()
    elif valgtTall == "6":
        redigerPerson()
    else:
        nyttForsok = input("Ugyldig valg. Velg et tall mellom 1-6: ")
        utfoerMenyvalg(nyttForsok)
    
def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")

    nyRegistrering = [fornavn, etternavn, telefonnummer]
    telefonkatalog.append(nyRegistrering)

    print("{0} {1} er registrert med telefonnummer {2}"
        .format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

def visAllePersoner():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()
    else:
        print("*******************************************"
              "*******************************************")
        for personer in telefonkatalog:
            print("* Fornavn: {:15s} Etternavn: {:15s} Telefonnummer: {:8s}"
                  .format(personer[0], personer[1], personer[2]))
        print("*******************************************"
                  "*******************************************")
        input("Trykk en tast for å gå tilbake til menyen")
        printMeny()

def sokPerson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
        printMeny()
    else:
        print("1. Søk på fornavn")
        print("2. Søk på etternavn")
        print("3. Søk på telefonnummer")
        print("4. Tilbake til hovedmeny")
        sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
        if sokefelt == "1":
            navn = input("Fornavn: ")
            finnPerson("fornavn", navn)
        elif sokefelt == "2":
            navn = input("Etternavn: ")
            finnPerson("etternavn", navn)
        elif sokefelt == "3":
            tlfonnummer = input("Telefonnummer: ")
            finnPerson("telefonnummer", tlfonnummer)    
        elif sokefelt == "4":
            printMeny()
        else:
            print("Feil du har ikke klart å skrive et tal som er gyldig") 
            sokPerson()


def Slettbruker():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
    else:
        navn = input("Skriv inn fornavn eller etternavn på personen du vil slette: ")
        funnet = False
        for person in telefonkatalog:
            if navn in person:
                telefonkatalog.remove(person)
                print(f"{person[0]} {person[1]} er slettet fra katalogen")
                funnet = True
                break
        if not funnet:
            print("Ingen heter det i katalogen")
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()


def finnPerson(typeSok, sokeTekst):
    svar = []
    for personer in telefonkatalog:
        if typeSok == "fornavn":
            if personer[0] == sokeTekst:
               svar.append(personer)
            elif typeSok == "etternavn":
                svar.append(personer)
            elif typeSok == "telefonnummer":
                svar.append(personer)
    if not svar:
        print("finner ingen personer")
    else:
        for personer in svar:
            print("{0} {1} har telefonnummer {2}"
                    .format(personer[0], personer[1], personer[2]))
        
def redigerPerson():
    if not telefonkatalog:
        print("Det er ingen registrerte personer i katalogen")
    else:
        navn = input("Skriv inn fornavn eller etternavn på personen du vil redigere: ")
        funnet = False
        for person in telefonkatalog:
            if navn in person:
                funnet = True
                print(f"Du redigerer nå {person[0]} {person[1]} med telefonnummer {person[2]}")
                
                nyFornavn = input(f"Oppdater fornavn (eller trykk Enter for å beholde '{person[0]}'): ")
                nyEtternavn = input(f"Oppdater etternavn (eller trykk Enter for å beholde '{person[1]}'): ")
                nyTelefonnummer = input(f"Oppdater telefonnummer (eller trykk Enter for å beholde '{person[2]}'): ")

                if nyFornavn:
                    person[0] = nyFornavn
                if nyEtternavn:
                    person[1] = nyEtternavn
                if nyTelefonnummer:
                    person[2] = nyTelefonnummer

                print(f"Oppdatert informasjon: {person[0]} {person[1]} med telefonnummer {person[2]}")
                break

        if not funnet:
            print("Ingen person med dette navnet funnet i katalogen.")
    
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()           


printMeny()