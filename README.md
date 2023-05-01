# Aluas-AP-Biblioteca

LAB 7-9:

CERINTE:
- Folosiți dezvoltarea iterativă bazat pe funcționalități
- Identificați și planificați funcționalități pe 3 iterații
- Folosiți dezvoltare dirijate de teste. Toate funcțiile trebuie testate și specificate
- Folosiți arhitectură stratificată (UI, Controller, Domain, Repository)
- Validați datele – pentru intrări invalide, aplicația sa tipărescă mesaje de eroare corespunzătoare – folosiți
excepții.
- Documentația conține: Enunț, lista de funcționalități, planul de iterații. Pentru fiecare funcționalitate: scenariu de
rulare

Scrieți o aplicație pentru o bibliotecă.

Aplicația stochează:
  - cărți: id, titlu, descriere, autor etc
  - clienți: iod, nume, CNP etc
  
Creați o aplicație care permite:
  - gestiunea listei de cărți și clienți.
  - adaugă, șterge, modifică, lista de cărți, lista de clienți
  - căutare carte, căutare clienți.
  - Închiriere/returnare carte
  - Rapoarte:
    - Cele mai inchiriate cărți.
    - Clienți cu cărți închiriate ordonat dupa: nume, după numărul de cărți închiriate
    - Primi 20% dintre cei mai activi clienți (nume client si numărul de cărți închiriate)

LAB 10: Extindeți proiectul de la laboratorul precedent prin adăugarea de clase repository care salvează
datele în fișiere text, astfel încat: modificand numai în application coordinator (e.g. main.py),
aplicația trebuie să poată funcționa alternativ fie cu date salvate in memorie, fie cu date salvate
in fișiere.


LAB 11: Extindeți proiectul de la laboratorul precedent prin adăugarea de teste folosind framework-ul
unittest. Trebuie testate toate functiile (exceptand cele de ui) astfel incat sa se atingă un grad de
acoperie (coverage) de 100% la nivel de linii de cod. Gradul de acoperire va fi demonstrat prin
rularea tool-ului de Code Coverage disponibil in PyCharm.


LAB 12: Modificați proiectul de la laboratorul precedent prin implementarea functionalitatilor legate de
statistici/rapoarte utilizând obiecte de tip DTO (Data Transfer Object), acolo unde este cazul. Ar
trebui sa fie implementate cel puțin doua functionalitati utilizând DTO-uri (se pot introduce noi
functionalitati in proiect dacă este cazul).
