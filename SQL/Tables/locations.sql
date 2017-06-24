CREATE TABLE locations(
	pk_location_id integer PRIMARY KEY NOT NULL,
	fk_parent_location_id integer NULL,
	name text NULL,
	FIPS_cd text NULL,
	fips_code_int text NULL,
	state_fips_cd text NULL,
	county_fips_cd text NULL,
	FIPS_type text NULL,
	state_cd text NULL,
	parent_FIPS_cd text NULL,
	state text NULL,
	nation text NULL,
	active bit NULL
 )