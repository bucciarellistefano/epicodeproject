--query di ricerca

--query per restituire allo user il nome dei titoli che possiede in libreria (immaginando che ci sia uno script di qualche genere che modifica il nome dell username sul WHERE in base allo user che sta facendo richiesta)

SELECT videogiochi.nome AS titolo FROM libreria 
INNER JOIN utenti ON libreria.id_utente = utenti.id_utente 
INNER JOIN videogiochi ON libreria.id_videogioco = videogiochi.id_videogioco
WHERE utenti.username ='user1';

--query per visualizzare i primi cinque giochi per tempo giocato tra tutti gli utenti
SELECT videogiochi.nome AS titolo, SEC_TO_TIME(SUM(TIME_TO_SEC(tempo_di_gioco))) --questa serie di funzioni serve per avere come output il formato di nuovo temporale 
FROM videogiochi INNER JOIN libreria
ON videogiochi.id_videogioco = libreria.id_videogioco
GROUP BY videogiochi.id_videogioco ORDER BY SEC_TO_TIME(SUM(TIME_TO_SEC(tempo_di_gioco))) DESC LIMIT 5;

--query per visualizzare i giochi in ordine di rating descresente

SELECT videogiochi.nome, AVG(libreria.recensione_numerica) AS 'Media Recensioni' FROM videogiochi 
INNER JOIN libreria
ON videogiochi.id_videogioco = libreria.id_videogioco
GROUP BY videogiochi.nome
ORDER BY AVG(libreria.recensione_numerica) DESC;

--query per vedere il totale incassato dalle transazioni
SELECT SUM(prezzo_acquisto) AS 'totale incasso' FROM transazioni;

--vedere i primi 10 utenti per spesa
SELECT utenti.username, SUM(prezzo_acquisto) AS "Totale speso dall'utente"
FROM utenti RIGHT JOIN transazioni ON utenti.id_utente=transazioni.id_utente
GROUP BY utenti.username
ORDER BY SUM(prezzo_acquisto) DESC
LIMIT 10;

--query per visualizzare le entrate mensili
SELECT SUM(prezzo_acquisto) AS 'Entrata Mensile', MONTHNAME(data_di_acquisto) AS Mese, YEAR(data_di_acquisto) AS Anno FROM transazioni
GROUP BY Mese, Anno
ORDER BY STR_TO_DATE(CONCAT('1 ', Mese, Anno), '%d %M %Y'); --Questa parte serve fondamentalmente per riavere il mese che era stato trasformato in forma testuale in maniera numerica in modo da poterlo ordinare
--per verificare la correttezza della query ho aggiunto successivamente delle righe in 'transazioni' in modo da poter verificare che ordinasse correttamente in anni diversi e mesi diversi

--query per visualizzare le amicizie tra gli utenti e ordinate per longevita'
SELECT * FROM amicizia ORDER BY data_di_inizio ASC;

--query per visualizzare i post pubblicati dagli utenti ordinati in base alla lunghezza del post
SELECT utenti.username AS 'Pubblicato da', blog.articolo, blog.data_pubblicazione AS 'Data di pubblicazione' 
FROM utenti INNER JOIN blog ON utenti.id_utente=blog.id_utente
ORDER BY CHAR_LENGTH(blog.articolo) ASC; --diciamo che logicamente avrebbe piu senso un ordinamento per data di pubblicazione, ho scelto di ordinarlo per numero di caratteri per far vedere l'uso di un'altra funzione


--query per avere l'età media degli utenti approssimata all'intero più vicino
SELECT ROUND((YEAR(NOW())- AVG(YEAR(data_di_nascita))), 0) AS 'Età media' FROM utenti;
/*è un approccio un pò approssimativo poichè considera solo l'anno di nascita degli utenti e non effettivamente se abbiano compiuto gli anni (una persona nata nel 01/01/2000 e o nel 31/12/2000 avrà 
sempre 23 anni nel 2023)*/

--Query per visualizzare i titoli più 'popolari' (cioè presenti in maggior numero nelle librerie degli utenti) in ordine decrescente
SELECT videogiochi.nome AS titolo, COUNT(utenti.id_utente) AS 'Numero di utenti che hanno il titolo in libreria' FROM libreria 
INNER JOIN utenti ON libreria.id_utente = utenti.id_utente 
INNER JOIN videogiochi ON libreria.id_videogioco = videogiochi.id_videogioco
GROUP BY videogiochi.nome
ORDER BY COUNT(utenti.id_utente) DESC;
