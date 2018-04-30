#Glicemix outline

Interfaccia principale:

- Visualizza dati
- Importa dati
  - da backup
  - da uright (txt o csv malformato)
- Esporta dati
  - formato csv (corretto)
  - formato backup (da definire)
- Impostazioni
- Modifica dati
- Esci
		

Ciclo principale:
 - Mostra menu
 - attendi input
   - se giusto ritorna valore
   - se sbagliato messaggio e ritorna in attesa






------------------
Avvio:
	* Carica impostazioni
		- Check impostazioni
			- Se primo avvio o impostazioni TOFU -> rifare configurazione
	* Apri database
		- Check database
			- Se database inesistente -> crea database
			- Se database TOFU -> avviso + ricrea database vuoto (con opzione per ripristino da backup)
		- Prompt (interfaccia principale)
		
