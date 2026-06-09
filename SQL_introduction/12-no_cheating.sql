-- Script that updates the score of Bob to 10 in the table second_table
-- Updates the row filtering exclusively by the name column instead of an ID
UPDATE second_table SET score = 10 WHERE name = 'Bob';
