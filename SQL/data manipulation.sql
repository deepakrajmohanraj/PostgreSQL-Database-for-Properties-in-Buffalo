--Inserting
INSERT INTO building_style (building_style_code, building_style_description) VALUES (16, 'Cottage');

INSERT INTO main (sbl, front, depth, prop_class_description, roll, total_value, land_value, number_of_units, sale_price, year_built, 
				  first_story_area, second_story_area, total_living_area, overall_condition, heat_type, no_of_stories, no_of_fireplaces, 
				  no_of_beds, no_of_baths, no_of_kitchens, census_tract, census_block, acres, add_area, attic_area, building_style_code, 
				  central_air, construction_quality_code, construction_grade, exterior_wall_code, homestead_code, 
				  story_height, wall_a, wall_b, wall_c, property_class_code, geoid20_block) 
VALUES ('1114100005012001', 30, 80, 'COM VAC W/IMP', 8, 5000, 2500, 11, 480000, 2000, 
		1500, 0, 1500, 3, 2, 1, 3, 2, 1, 2,
		'25.02','2012', 0.5, 0, 0, 10, 1, 1, 'UNKNOWN', 0, 
		'N', 8, 100, 200, 300, 331, '360290025022012');

--Delete
DELETE FROM construction_grade WHERE construction_grade = 'UNKNOWN';

DELETE FROM house_location WHERE zipcode IS NULL;

--Updating
UPDATE construction_quality SET construction_quality_description = 'Above average' WHERE construction_quality_code = 2.8;

UPDATE main SET total_value = 5500 WHERE sbl = '0658200002007000';

select * from main where sbl = '1114100005012001'



