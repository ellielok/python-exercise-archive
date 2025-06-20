import os
import json
from typing import List, Tuple, Dict
from parent_property import Property
from child_properties import House, Apartment
from amenity import Amenity
from ingestion import ingest_files
from score import *

def read_request(request_filename: str) -> Tuple[dict, dict]:
    """
    This method reads a request file in json format
    and returns two dictionaries; one containing the
    house_importance features and one containing the 
    amenity_importance features.
    """
    # TODO: Step 1 - Define this method to read a JSON request and return 2 dictionaries
    with open(request_filename, "r",) as f:
        text:string = f.read()
        request: dict = json.loads(text)
        house_importance = request['request']['house_importance']
        amenities_accessibility = request['request']['amenities_accessibility']
        return house_importance, amenities_accessibility

def find_matching_properties(props: List[Property], house_importance: dict) -> List[Property]:
    """
    THis method recevied a list of all properties and a dictionary that
    contains the house importance criteria from a user's request 
    and returns a list of Property objects that match the user's request
    """
    # TODO: Step 2 - Define this method to return a list of matching properties
    return [prop for prop in props if check_property(prop, house_importance)]

def check_property(prop: Property, house_importance: dict) -> bool:
    """
    Check if the given property match the user's request
    """
    if "suburb" in house_importance:
        expected_suburb: str = house_importance["suburb"]
        if prop.get_suburb() != expected_suburb:
            return False
    if "prop_type" in house_importance:
        expected_prop_type: str = house_importance["prop_type"]
        if prop.get_prop_type() != expected_prop_type:
            return False
    if "property_features" in house_importance:
        expected_property_features: List[str] = house_importance["property_features"].split(";")
        for feature in expected_property_features:
            if feature not in prop.get_property_features():
                return False
    if "floor_area" in house_importance:
        min_floor_area: int = house_importance["floor_area"]
        if prop.get_floor_area() < min_floor_area:
            return False
    if "land_area" in house_importance:
        min_land_area: int = house_importance["land_area"]
        if prop.get_land_area() < min_land_area:
            return False
    
    if "bedrooms" in house_importance:
        min_bedrooms: int = house_importance["bedrooms"]
        if prop.get_bedrooms() < min_bedrooms:
            return False

    if "bathrooms" in house_importance:
        min_bathrooms: int = house_importance["bathrooms"]
        if prop.get_bathrooms() < min_bathrooms:
            return False

    if "parking_spaces" in house_importance:
        min_parking_spaces: int = house_importance["parking_spaces"]
        if prop.get_parking_spaces() < min_parking_spaces:
            return False

    if "floor_number" in house_importance:
        max_floor_number: int = house_importance["floor_number"]
        if prop.get_floor_number() > max_floor_number:
            return False
        
    if "price" in house_importance:
        max_price: int = house_importance["price"]
        if prop.get_price() > max_price:
            return False
    
    return True

def create_response_dict(scored_properties: dict) -> dict:
    """
    This method takes in a dictionary that has the property objects 
    and their star scores and creates a dictionary in JSON format 
    that can be written into a file
    """
    # TODO: Step 3 - Define this method to create a response dictionary
    properties = []
    for score, prop in scored_properties.items():
        prop_id = prop.get_prop_id()
        properties.append({"property_id": prop_id, "star_score":score})
    return{"properties":properties}


def produce_star_scores(request_filename: str, properties_file: str, amenities_files: List[str]) -> dict:
    # Read the properties and amenities
    medical_file, schools_file, train_stations, sport_facilities = amenities_files
    props, amenities = ingest_files(properties_file, medical_file, schools_file, train_stations, sport_facilities)

    # Read the request and get the dictionaries of house_importance and amenity_accessibility
    house_importance, amenity_accessibility = read_request(request_filename)

    # Collect properties that match the property criteria
    matched_props = find_matching_properties(props, house_importance)

    # Score properties using the amenity amenity_accessibility dictionary
    prop_scores = [score_property(x, amenities, amenity_accessibility) for x in matched_props]

    # Now, we can normalise the scores that we just got
    norm_scores = normalise_scores(prop_scores)

    # Create a collection matching property object to Score
    prop_scored = dict(zip(norm_scores, matched_props))

    # Create a response dictionary
    response_dict = create_response_dict(prop_scored)
    
    # Return the response dictionary from step 3 and the list of matching property family objects
    return response_dict, matched_props

def respond(response_dict: dict) -> None:
    """
    This function reads a response dictionary and creates a JSON 
    file based on the content of the response dictionary
    """
    properties: List[dict] = response_dict['properties']
    sorted_properties = sorted(properties, reverse = True, key = lambda p: p['star_score'])
    sorted_response_dict = {"properties": sorted_properties}

    output_filename = "response.json"
    text = json.dumps(sorted_response_dict, indent=2)
    with open(output_filename, "w") as f:
        f.write(text)


if __name__ == '__main__':
    response_dict, matched_props = produce_star_scores('request.json', 'melbourne_properties.csv', ['melbourne_medical.csv', 'melbourne_schools.csv', 'train_stations.csv', 'sport_facilities.csv'])
    print(f"{len(matched_props)} properties matched with the user's request")
    respond(response_dict)
    # Check if response.json exists in the current directory
    if os.path.exists("/home/response.json"):
        print("File created successfully")
    else:
        print("File not created. Some Error occurred")
