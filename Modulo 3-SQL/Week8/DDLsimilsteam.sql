CREATE DATABASE similsteam;

CREATE TABLE utenti(id_utente INT NOT NULL primary key, username VARCHAR(30) UNIQUE NOT NULL, email VARCHAR(100) UNIQUE NOT NULL, telefono VARCHAR(20), data_di_nascita DATE);
CREATE TABLE videogiochi(id_videogioco INT NOT NULL primary key, nome VARCHAR(100), prezzo FLOAT(8,2), data_di_rilascio DATE);
CREATE TABLE transazioni(id_transazioni INT NOT NULL primary key, id_utente INT NOT NULL, id_videogioco INT NOT NULL, prezzo_acquisto FLOAT(8,2), data_di_acquisto DATE); 
CREATE TABLE libreria(id_elemento_libreria INT NOT NULL primary key, id_utente INT NOT NULL, id_videogioco INT NOT NULL, tempo_di_gioco TIME NOT NULL, recensione_numerica FLOAT(2,1), recensione_scritta TEXT);
CREATE TABLE amicizia(id_amico1 INT NOT NULL, id_amico2 INT NOT NULL, PRIMARY KEY(id_amico1, id_amico2), data_di_inizio DATE);
CREATE TABLE blog(id_post INT NOT NULL primary key, id_utente INT NOT NULL, articolo TEXT, data_pubblicazione DATE); 

ALTER TABLE transazioni ADD FOREIGN KEY(id_utente) REFERENCES utenti(id_utente);
ALTER TABLE transazioni ADD FOREIGN KEY(id_videogioco) REFERENCES videogiochi(id_videogioco);

ALTER TABLE libreria ADD FOREIGN KEY(id_utente) REFERENCES utenti(id_utente);
ALTER TABLE libreria ADD FOREIGN KEY(id_videogioco) REFERENCES videogiochi(id_videogioco);

ALTER TABLE amicizia ADD FOREIGN KEY(id_amico1) REFERENCES utenti(id_utente);
ALTER TABLE amicizia ADD FOREIGN KEY(id_amico2) REFERENCES utenti(id_utente);

ALTER TABLE blog ADD FOREIGN KEY(id_utente) REFERENCES utenti(id_utente);
