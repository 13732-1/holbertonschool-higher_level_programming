-- Script that lists all records of the table second_table with a name value
-- Filters out rows without names and lists rows by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
