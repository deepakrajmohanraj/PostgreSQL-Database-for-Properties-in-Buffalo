-- Create an index called house_location_zipcode_idx on the house_location table, specifically on the zipcode column.
CREATE INDEX house_location_zipcode_idx ON house_location (zipcode);

-- Explain and analyze the performance of a SELECT statement on the house_location table, specifically retrieving all columns for rows where the zipcode column equals 14214.
EXPLAIN ANALYZE
SELECT *
FROM house_location
WHERE zipcode = 14214;

-- Drop the house_location_zipcode_idx index from the house_location table.
DROP INDEX house_location_zipcode_idx;
