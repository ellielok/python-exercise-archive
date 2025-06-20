from haversine import haversine_distance
from typing import List 

def extract_information(property_string: str) -> dict:
    """
    Extract property information from the given string 
    """
    # Converts the given string into a list
    values:List[str] = property_string.split(",")

    # Assign different substring values to corresponding variables
    prop_id, full_address, bedrooms, bathrooms, parking_spaces, latitude, longitude, floor_number, land_areas, floor_area, price, property_features = values

    # Extract the suburb value from full_address
    suburb = full_address.split(" ")[3]

    # Get property tpye
    if "/" in full_address.split(" ")[0]:
        prop_type = "apartment"

    else:
        prop_type = "house"

    # Add needed values into a dict according to the property type
    property_dict = {}

    property_dict['prop_id'] = prop_id
    property_dict['prop_type'] = prop_type
    property_dict['full_address'] = full_address
    property_dict['suburb'] = suburb
    property_dict['bedrooms'] = int(bedrooms)
    property_dict['bathrooms'] = int(bathrooms)
    property_dict['parking_spaces'] = int(parking_spaces)
    property_dict['latitude'] = float(latitude)
    property_dict['longitude'] = float(longitude)

    if prop_type == "house":
        property_dict['land_area'] = int(land_areas)
    else:
        property_dict['floor_number'] = int(floor_number)
    
    property_dict['floor_area'] = int(floor_area)
    property_dict['price'] = int(price)
    property_dict['property_features'] = property_features.split(";")

    return property_dict


def process_properties(file_name: str) -> dict:
    """
    Extract property information from the given CSV file. 
    """    
    
    properties = {}
    
    with open (file_name, "r") as f:
        # Convert the data into a list of lines
        lines:List[str] = (f.read()).split('\n')
        for line in lines[1:]:
            # If the value of line is True(not empty), add values into the dict
            if line:
                property = extract_information(line)
                properties[property['prop_id']] = property
    return properties


def process_stations(file_name: str) -> dict:
    """
    Extract station information from the given string.
    """     
    stations = {}

    # Convert the data into a list of lines
    with open (file_name, "r") as f:
        lines:List[str] = (f.read()).split('\n')
        # If the value of line is not empty, add values into the dict
        for line in lines[1:]:
            if line:
                values = line.split(',')
                stop_id,stop_name,stop_lat,stop_lon = values
                station = {}
                station['stop_id'] = stop_id
                station['stop_name'] = stop_name
                station['stop_lat'] = float(stop_lat)
                station['stop_lon'] = float(stop_lon)
            stations[station['stop_id']] = station
    return stations


def nearest_station(properties: dict, stations: dict, prop_id: str) -> str:
    """
    Find the nearest station name of the give property
    """
    # Define latitude and longitude for the property
    prop_lat = properties[prop_id]['latitude']
    prop_lon = properties[prop_id]['longitude']
    
    # Create variables of the nearest station and distance
    min_distance = float('inf')
    nearest_station = ''

    # Use for in loop to get the nearest station
    for station in stations.values():
        station_lat = station['stop_lat']
        station_lon = station['stop_lon']
        
        distance = haversine_distance(prop_lat, prop_lon, station_lat, station_lon)
        
        if distance < min_distance:
            min_distance = distance
            nearest_station = station['stop_name']
        
    return nearest_station


def main():
    """
    You need not touch this function, if your 
    code is correct, this function will work as intended 
    """
    # Process the properties
    properties_file = 'sample_properties.csv'
    properties = process_properties(properties_file)

    # Process the train stations
    stations_file = 'train_stations.csv'
    stations = process_stations(stations_file)

    # Check the validity of stations
    sample_prop = 'P10001'
    print(f"The nearest station for property {sample_prop} is {nearest_station(properties, stations, sample_prop)}")
    


if __name__ == '__main__':
    main()
