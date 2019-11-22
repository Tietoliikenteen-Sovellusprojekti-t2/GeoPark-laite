CREATE PROCEDURE `Insert_GPS` (
IN Aikaleima LONG,
IN Lattitude DOUBLE,
IN Longitude DOUBLE
)

Aliohjelma:BEGIN

INSERT INTO GPS VALUES (NULL,Aikaleima,Lattitude,Longitude);

END