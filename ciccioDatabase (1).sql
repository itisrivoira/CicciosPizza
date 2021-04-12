create database CiccioOF;
use CiccioOF;

create table Giocatore(
	nomeUt varchar(26) not null,
	password varchar(30) not null,
	email varchar(30) not null,
	stelleTot int(4)null,
	primary key (nomeUt)
);

create table Livello(
	TempoLim int(4) not null,
	numLvl varchar(4) not null,
	numOrd varchar(4) not null,
	primary key (numLvl)
);

create table PartitaGiro(
	nomeUtt varchar(26) not null,
	dataPar date null,
	puntiTot varchar(4) not null,
	codPar char(8) not null,
	ordComp varchar(4) null,
	primary key (codPar),
	FOREIGN KEY (nomeUtt) REFERENCES Giocatore(nomeUt)
);

create table Ordine(
	numOrd char(8) not null,
	tempLim char(4) not null,
	puntOrd char(4) not null,
	primary key (numOrd)
);

create table GiocaCar(
	stelle char(3) null,
	data date not null,
	nomeUttt varchar(26) not null,
	numLvll varchar(4) not null,
	primary key (nomeUttt,numLvll),
	FOREIGN KEY (nomeUttt) REFERENCES Giocatore(nomeUt),
	FOREIGN KEY (numLvll) REFERENCES Livello(numLvl)
);

create table Contiene(
	codParr char(8) not null,
	numOrdd char(8) not null,
	primary key (numOrdd,codParr),
	FOREIGN KEY (codParr) REFERENCES PartitaGiro(codPar),
	FOREIGN KEY (numOrdd) REFERENCES Ordine(numOrd)
);






