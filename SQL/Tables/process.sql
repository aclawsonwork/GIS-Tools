CREATE TABLE process ( 
	pk_process_id integer NOT NULL PRIMARY KEY, 
	fk_process_type_id integer NOT NULL,
	fk_location_id integer NOT NULL, 
	process_date datetime NOT NULL, 
	elapsed_time_seconds float NOT NULL 
);