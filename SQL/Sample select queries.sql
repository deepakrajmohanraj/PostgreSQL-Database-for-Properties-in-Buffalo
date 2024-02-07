--It calculates the count of houses, average total value, and year-built statistics for each building style and construction grade combination, then filters and sorts the results to show only those with more than 10 houses and an average total value greater than 50000, ordered by the count of houses in descending order.
SELECT bs.building_style_description, cg.construction_grade_description, COUNT(*) AS total_houses,
  AVG(m.total_value) AS avg_total_value, MIN(m.year_built) AS min_year_built, MAX(m.year_built) AS max_year_built
FROM main m
JOIN building_style bs ON m.building_style_code = bs.building_style_code
JOIN construction_grade cg ON m.construction_grade = cg.construction_grade
GROUP BY bs.building_style_description, cg.construction_grade_description
HAVING COUNT(*) > 10 AND AVG(m.total_value) > 50000
ORDER BY total_houses DESC;

--This SQL query retrieves the sbl, total living area, building style description, and construction grade description from the public.main table, joined with the public.building_style and public.construction_grade tables. It filters the results to only include rows where the total living area is greater than the average total living area in the main table and sorts the results by total living area in descending order.
SELECT 
    sbl, 
    total_living_area, 
    building_style_description, 
    construction_grade_description
FROM 
    main 
    JOIN building_style ON main.building_style_code = building_style.building_style_code 
    JOIN construction_grade ON main.construction_grade = construction_grade.construction_grade 
WHERE 
    total_living_area > (SELECT AVG(total_living_area) FROM main)
ORDER BY 
    total_living_area DESC;

--This SQL query retrieves information about houses in the 14214 zipcode area, groups the data by neighborhood, calculates averages, and ranks neighborhoods based on average total value, displaying only the top 10.
WITH location_info AS (
    SELECT
        h.sbl, h.house_number, h.street, h.zipcode, h.latitude, h.longitude, h.neighborhood, m.year_built, m.total_value, m.land_value, 
		m.number_of_units, m.no_of_stories, m.total_living_area, bs.building_style_description, cg.construction_grade_description,
 		cq.construction_quality_description, ew.exterior_wall_description
    FROM
        house_location h JOIN main m ON h.sbl = m.sbl JOIN building_style bs ON m.building_style_code = bs.building_style_code
        JOIN construction_grade cg ON m.construction_grade = cg.construction_grade
        JOIN construction_quality cq ON m.construction_quality_code = cq.construction_quality_code
        JOIN exterior_wall ew ON m.exterior_wall_code = ew.exterior_wall_code WHERE h.zipcode = 14214
),
grouped_info AS (
    SELECT
        li.neighborhood, AVG(li.year_built) AS avg_year_built, AVG(li.total_value) AS avg_total_value, AVG(li.land_value) AS avg_land_value,
        SUM(li.number_of_units) AS total_units, AVG(li.no_of_stories) AS avg_no_of_stories, AVG(li.total_living_area) AS avg_total_living_area,
        COUNT(*) AS num_buildings FROM location_info li GROUP BY li.neighborhood
),
ordered_info AS (
    SELECT
        gi.neighborhood, gi.avg_year_built, gi.avg_total_value, gi.avg_land_value, gi.total_units, gi.avg_no_of_stories, gi.avg_total_living_area,
        gi.num_buildings, ROW_NUMBER() OVER (ORDER BY gi.avg_total_value DESC) AS rank FROM grouped_info gi
)
SELECT * FROM ordered_info WHERE rank <= 10;
	
--Here's an example of a simple select query using recursive CTE that fetches all the houses located in a particular neighborhood along with their property class description and total living area:	
WITH RECURSIVE house_list AS (
  SELECT main.sbl, prop_class_description, total_living_area
  FROM main
  JOIN house_location ON main.sbl = house_location.sbl
  WHERE neighborhood = 'Riverside'
  
  UNION
  
  SELECT main.sbl, main.prop_class_description, main.total_living_area
  FROM main
  JOIN house_list ON main.sbl = house_list.sbl
)

SELECT *
FROM house_list;



