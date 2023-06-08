WITH RECURSIVE temp1 (id, parent_id, name) AS (
	SELECT t_1.*, cast (t_1.name as varchar(200)) as path
	FROM table_1 t_1
	UNION
	SELECT t_2.*, CAST (temp1.path || ',' || t_2.name AS varchar(200) ) as path 
	FROM table_1 t_2
	JOIN temp1 ON (temp1.parent_id = t_2.id)
)
SELECT * INTO table_2 FROM (
	SELECT * FROM temp1
) t;
SELECT * FROM table_2;