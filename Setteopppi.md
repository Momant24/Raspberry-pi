## Hvordan sette opp rasberry pi
1. Last ned rasberry pi immager fra nettet 
2. Sett inn mikro sd kortet og velg ubunto som opperativ system. Og instaler den på mikro sd kortet.
3. Sett opp pi og velg ditt språk og keyboard layoutn
4. Koble den til wifi eller ethernett.
5. Så sjekker du etter oppdateringer og oppdaterer med komandoene under.

``` console
sudo apt update
sudo apt upgrade
```
6. Så setter du opp brannmuren for å tilatte ssh med komandoene under.
``` console
sudo apt install ufw
sudo ufw enable

sudo ufw allow ssh

sudo ufw status 
```
7. Instaler ssh server og set at den starter opp ved oppstart av maskinen med kodene under.
``` console
sudo apt install openssh-server

sudo systemctl enable ssh

sudo systemctl start ssh
```
8. Instaler all programvare som du trenger
``` console
sudo apt install python3-pip
sudo apt install python3
sudo apt install git
sudo apt install mariadb-server 
sudo mysql_secure_installation
```
#### Oppset av MariaDB
1. Logg inn i mariaDB tryk enter når passor spørsmålet dukker opp.
2. Lag en ny bruker og gi rettigheter til brukeren endre username og passor til det du ønsker
3. Gi rettigheter til din bruker. 
4. Oppdater rettigheter med den 3 kode snutten
``` sql
sudo mariadb –u root -p

CREATE USER 'username'@'localhost'IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'username'@’localhost’ IDENTIFIED BY 'password';

FLUSH PRIVILEGES;
```
### Sette statisk ip adresse
1. Skriv sudo nmtui for å komme inn på en lilla skjerm.
2. Gå inn på Edit  a connection
3. Velg ethernett eller wi fi.
4. Bytt ipv4 til manual
5. Trykk på show vedsinav ipv4
6. Add en adresse som du ønsker
7. 10.0.0.1 til gateway
8. Legg til 10.0.0.10 til dns server og leg til en til under 8.8.8.8
9. Legg til serch domains 255.0.0.0
10. Press ok
``` console
sudo nmtui
```
#### Ta sudo update og sudo upgrade igjen for at alt skal være opptatert

[Åpne dokumentet](Telefonkatlog.py)