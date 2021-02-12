# Bruteforce-Password-Generator
In diesem Repository finden Sie den Code zu unserem Passwort Sicherheit Basis Guide. Mit dem Skript wird demonstriert, wie sich Zeichensatz und Passwort Länge auf die Generierung einer Brute Force Liste auswirken. 

Den gesamten Passwort Basis Sicherheit Guide finden Sie auf unserem Blog: 

https://www.inmodis.de/basis-security-guides/der-passwort-basis-sicherheit-guide/ 

# Achtung
Wenn Sie die Wort Länge (Variable repeat) zu sehr erhöhen, steigt die Zahl der generierten Passwörter exponentiell an und die Ausführung des Skripts wird irgendwann mit einem Memory Error abbrechen. 

Wenn Sie tatsächlich eine Brute Force Liste generieren wollen, müssen Sie den Code so abändern, dass die Passwörter eines nach dem anderen generiert und dann in ein Textfile geschrieben werden. 
