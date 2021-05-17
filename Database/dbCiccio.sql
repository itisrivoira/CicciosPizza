CREATE DATABASE cicciosPizza;

use cicciosPizza;

CREATE TABLE IF NOT EXISTS Giocatori(
	username VARCHAR(25) NOT NULL primary key,
	password VARCHAR(64) NOT NULL,
	email VARCHAR(25) NOT NULL,
	punteggioMax INT NULL);
	
CREATE TABLE IF NOT EXISTS Livelli(
	id_Livello INT NOT NULL primary key,
	stelleOtt INT NOT NULL,

	username VARCHAR(25) NOT NULL,

	FOREIGN KEY (username) REFERENCES Giocatori (username));
	
