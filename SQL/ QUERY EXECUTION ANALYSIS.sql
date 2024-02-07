-- Remove foreign key constraints to main table from other tables
ALTER TABLE deed DROP CONSTRAINT fk_deed_main;
ALTER TABLE house_location DROP CONSTRAINT fk_house_location_main;
ALTER TABLE owner_details DROP CONSTRAINT fk_owner_details_main;
ALTER TABLE main DROP CONSTRAINT main_pkey;

-- Retrieve all data from main table and house_location table based on sbl values
-- Analyze the execution plan and provide timing information
EXPLAIN ANALYZE
SELECT *
FROM main
JOIN house_location
ON main.sbl = house_location.sbl;

-- Add primary key constraint to main table on sbl column
ALTER TABLE main
ADD CONSTRAINT main_pkey PRIMARY KEY (sbl);

-- Add foreign key constraints to main table from other tables on sbl column
ALTER TABLE deed
ADD FOREIGN KEY (sbl) REFERENCES main(sbl);
ALTER TABLE owner_details
ADD FOREIGN KEY (sbl) REFERENCES main(sbl);
ALTER TABLE house_location
ADD FOREIGN KEY (sbl) REFERENCES main(sbl);

-- Retrieve all data from main table and house_location table based on sbl values
-- Analyze the execution plan and provide timing information
EXPLAIN ANALYZE
SELECT *
FROM main
JOIN house_location
ON main.sbl = house_location.sbl;


-- Use EXPLAIN ANALYZE to analyze the execution plan and performance of the SELECT query
EXPLAIN ANALYZE
-- Select all columns from the "main" table in the "public" schema where year_built is greater than 1900, no_of_beds is greater than or equal to 3, and no_of_baths is greater than or equal to 2
SELECT * FROM public.main 
WHERE year_built > 1900 
AND no_of_beds >=3
AND no_of_baths >=2;

-- Create an index named "main_yearbuilt_noofbeds_noofbaths_idx" on the "public.main" table for the columns "year_built", "no_of_beds", and "no_of_baths"
CREATE INDEX main_yearbuilt_noofbeds_noofbaths_idx 
ON public.main(year_built,no_of_beds,no_of_baths);

-- Use EXPLAIN ANALYZE to analyze the execution plan and performance of the SELECT query after creating the index
EXPLAIN ANALYZE
-- Select all columns from the "main" table in the "public" schema where year_built is greater than 1900, no_of_beds is greater than or equal to 3, and no_of_baths is greater than or equal to 2
SELECT * FROM public.main 
WHERE year_built > 1900 
AND no_of_beds >=3
AND no_of_baths >=2;

-- This code drops an existing index named "main_yearbuilt_noofbeds_noofbaths_idx"
DROP INDEX main_yearbuilt_noofbeds_noofbaths_idx;

-- The EXPLAIN ANALYZE command is used to analyze the query plan and execution time of the subsequent UPDATE statement.
EXPLAIN ANALYZE 
-- The UPDATE statement modifies the "total_value" column in the "main" table by increasing the value by 10% for rows where the "year_built" column is greater than 2000.
UPDATE public.main 
SET total_value = total_value*1.1 
WHERE year_built>2000;

-- This CREATE INDEX statement creates an index on the "year_built" column in the "main" table to speed up queries that involve filtering by this column.
CREATE INDEX main_year_built_idx 
ON public.main(year_built);

-- The EXPLAIN ANALYZE command is used again to analyze the query plan and execution time of the subsequent UPDATE statement, which is identical to the first one.
EXPLAIN ANALYZE 
UPDATE public.main 
SET total_value = total_value*1.1 
WHERE year_built>2000;
