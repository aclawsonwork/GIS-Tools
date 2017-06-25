select
	p.pk_process_id as process_id,
	p.process_date as process_date,
	l.state_cd as state_cd,
	t.name as process_name,
	p.elapsed_time_seconds as elapsed_time
	
from
	process p inner join process_types t on p.fk_process_type_id = t.pk_process_type_id
	inner join locations l on p.fk_location_id = l.pk_location_id
where
	p.fk_location_id IN (2,11,12)
order by l.state_cd