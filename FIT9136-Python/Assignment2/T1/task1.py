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


def add_feature(property_dict: dict, feature: str) -> None:
    """
    Add new feature to property
    """
    property_features = property_dict['property_features']
    if feature not in property_features:
        property_features.append(feature)

def remove_feature(property_dict: dict, feature: str) -> None:
    """
    Remove existing feature from property
    """
    property_features = property_dict['property_features']
    if feature in property_features:
        property_features.remove(feature)

def main():
    sample_string = "P10001,3 Antrim Place Langwarrin VIC 3910,4,2,2,-38.16655678,145.1838435,,608,257,870000,dishwasher;central heating"
    property_dict = extract_information(sample_string)
    print(f"The first property is at {property_dict['full_address']} and is valued at ${property_dict['price']}")

    sample_string_2 = "P10002,G01/7 Rugby Road Hughesdale VIC 3166,2,1,1,-37.89342337,145.0862616,1,,125,645000,dishwasher;air conditioning;balcony"
    property_dict_2 = extract_information(sample_string_2)

    print(f"The second property is in {property_dict_2['suburb']} and is located on floor {property_dict_2['floor_number']}")

    add_feature(property_dict, 'electric hot water')
    print(f"Property {property_dict['prop_id']} has the following features: {property_dict['property_features']}")

if __name__ == '__main__':
    main()
