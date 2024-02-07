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
natural join owner_details
limit 100;

