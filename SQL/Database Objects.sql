CREATE OR REPLACE PROCEDURE get_main_data()
LANGUAGE plpgsql
AS $$
BEGIN
  -- Drop the temporary table if it already exists
  DROP TABLE IF EXISTS temp_main_data;
  
  -- Create a new temporary table named "temp_main_data"
  CREATE TEMPORARY TABLE temp_main_data AS
  
  -- Select all columns from the "main" table and join it with other tables
  -- using the "natural join" keyword to automatically join on columns with
  -- the same name in both tables
  SELECT *
  FROM main 
  natural join building_style
  natural join construction_grade 
  natural join construction_quality 
  natural join deed
  natural join exterior_wall 
  natural join heat_type 
  natural join house_location
  natural join overall_condition 
  natural join owner_details;
  
  -- End of the stored procedure
END;
$$;

-- This function updates the "total_living_area" column in the "main" table whenever the "first_story_area" or "second_story_area" columns are updated or a new row is inserted.

CREATE OR REPLACE FUNCTION update_total_living_area() RETURNS trigger AS $$
BEGIN
    NEW.total_living_area = NEW.first_story_area + NEW.second_story_area;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- This trigger is created to activate the "update_total_living_area()" function whenever an insert or update occurs on the "first_story_area" or "second_story_area" columns in the "main" table.

CREATE TRIGGER update_total_living_area_trigger
    BEFORE INSERT OR UPDATE OF first_story_area, second_story_area
    ON public.main
    FOR EACH ROW
    EXECUTE FUNCTION update_total_living_area();


update main
set second_story_area = 1000
where sbl = '1114100005012001'

-- Create or replace a function called 'get_zipcode_stats' with a parameter called 'zipcode_val'
-- The function returns a table with three columns called 'total_houses', 'avg_total_value', and 'avg_beds'
-- The data types of the columns are 'bigint', 'numeric(16,0)', and 'numeric(16,0)', respectively
CREATE OR REPLACE FUNCTION get_zipcode_stats(zipcode_val numeric(16,0))
RETURNS TABLE (
    total_houses bigint,
    avg_total_value numeric(16,0),
    avg_beds numeric(16,0)
) AS $$
BEGIN
    -- Return a query that calculates the total number of houses, average total value, and average number of beds
    -- The query performs a join operation between 'house_location' and 'main' tables, based on the 'sbl' column in 'main' and 'zipcode' in 'house_location'
    -- The results are filtered based on the input parameter 'zipcode_val'
    RETURN QUERY
    SELECT
        count(*) as total_houses,
        avg(total_value) as avg_total_value,
        avg(no_of_beds) as avg_beds
    FROM
        house_location hl
        JOIN main m ON m.sbl = hl.sbl
    WHERE
        hl.zipcode = zipcode_val;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_zipcode_stats(14214);