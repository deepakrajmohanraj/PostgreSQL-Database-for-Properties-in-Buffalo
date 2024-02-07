deed_columns = {
    "deed_book": ("deed", ""),
    "deed_page": ("deed", ""),
    "deed_date": ("deed", ""),
    "deed_type_code": ("deed", "")
}

house_location_columns = {
    "house_number": ("house_location", ""),
    "street": ("house_location", ""),
    "zipcode": ("house_location", ""),
    "zipcode_extension": ("house_location", ""),
    "council_district": ("house_location", ""),
    "police_district": ("house_location", ""),
    "census_tract": ("house_location", ""),
    "census_block_group": ("house_location", ""),
    "census_block": ("house_location", ""),
    "neighborhood": ("house_location", ""),
    "latitude": ("house_location", ""),
    "longitude": ("house_location", "")

}

owner_details_columns = {
    "owner1": ("owner_details", ""),
    "owner2": ("owner_details", ""),
    "previous_owner": ("owner_details", ""),
    "owner_mail": ("owner_details", "")
}

building_style_columns = {
    "building_style_description": ("building_style", "main")
}

construction_grade_columns = {
    "construction_grade_description": ("construction_grade", "main")
}

construction_quality_columns = {
    "construction_quality_description": ("construction_quality", "main")
}

exterior_wall_columns = {
    "exterior_wall_description": ("exterior_wall", "main")
}

heat_type_columns = {
    "heat_type_description": ("heat_type", "main")
}

overall_condition_columns = {
    "overall_condition_description": ("overall_condition", "main")
}

main_columns = {
    "story_height": ("main", ""),
    "wall_a": ("main", ""),
    "wall_b": ("main", ""),
    "wall_c": ("main", ""),
    "property_class_code": ("main", ""),
    "front": ("main", "")
}
main_missing_columns = {
    "sbl": ("main", ""),
    "tax_district": ("main", ""),
    "depth": ("main", ""),
    "property_class_description": ("main", ""),
    "roll": ("main", ""),
    "total_value": ("main", ""),
    "land_value": ("main", ""),
    "number_of_units": ("main", ""),
    "sale_price": ("main", ""),
    "year_built": ("main", ""),
    "first_story_area": ("main", ""),
    "second_story_area": ("main", ""),
    "total_living_area": ("main", ""),
    "overall_condition": ("main", ""),
    "heat_type": ("main", ""),
    "no_of_stories": ("main", ""),
    "no_of_fireplaces": ("main", ""),
    "no_of_beds": ("main", ""),
    "no_of_baths": ("main", ""),
    "no_of_kitchens": ("main", ""),
    "acres": ("main", ""),
    "add_area": ("main", ""),
    "attic_area": ("main", ""),
    "bill_number": ("main", ""),
    "building_style_code": ("main", ""),
    "central_air": ("main", ""),
    "construction_quality_code": ("main", ""),
    "construction_grade": ("main", ""),
    "council_district_1": ("main", ""),
    "exterior_wall_code": ("main", ""),
    "homestead_code": ("main", ""),
    "geoid20_block": ("main", "")
}

# Combine dictionaries with previous ones
all_columns = {
    **deed_columns,
    **house_location_columns,
    **owner_details_columns,
    **building_style_columns,
    **construction_grade_columns,
    **construction_quality_columns,
    **exterior_wall_columns,
    **heat_type_columns,
    **overall_condition_columns,
    **main_columns,
    **main_missing_columns
}



column_names = ['sbl', 'overall_condition', 'heat_type', 'exterior_wall_code', 'construction_quality_code', 'construction_grade', 'building_style_code', 'front', 'depth', 'prop_class_description', 'roll', 'total_value', 'land_value', 'number_of_units', 'sale_price', 'year_built', 'first_story_area', 'second_story_area', 'total_living_area', 'no_of_stories', 'no_of_fireplaces', 'no_of_beds', 'no_of_baths', 'no_of_kitchens', 'census_tract', 'census_block_group', 'census_block', 'acres', 'add_area', 'attic_area', 'bill_number', 'central_air', 'homestead_code', 'story_height', 'wall_a', 'wall_b', 'wall_c', 'property_class_code', 'tractce20', 'geoid20_tract', 'geoid20_blockgroup', 'geoid20_block', 'building_style_description', 'construction_grade_description', 'construction_quality_description', 'deed_book', 'deed_page', 'deed_date', 'deed_type_code', 'exterior_wall_description', 'heat_type_description', 'house_number', 'street', 'zipcode', 'zipcode_extension', 'latitude', 'longitude', 'tax_district', 'council_district', 'council_district_1', 'police_district', 'neighborhood', 'overall_condition_description', 'owner1', 'owner2', 'previous_owner', 'owner_mail']


column_dict = {i: col for i, col in enumerate(column_names)}


# if __name__ == "__main__":
#     for i in column_names:
#         try:
#             all_columns[i]
#         except:
#             print("missing " + i)



