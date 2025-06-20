from ingestion import ingest_files

if __name__ == '__main__':
    props, amens = ingest_files('sample_properties.csv', 'sample_melbourne_medical.csv', 'sample_melbourne_schools.csv', 'train_stations.csv', 'sample_sport_facilities.csv')
    nearest_station, distance = props[0].nearest_amenity(amens, 'train_station', None)

    print(f"The nearest station to {props[0].get_full_address()} is {nearest_station.get_amenity_name()} and it is {round(distance,2)}km away")

    print(f"The property at {props[1].get_full_address()} has the following features: {props[1].get_property_features()}")

    print(f"We are going to add 'tennis court' as a feature to this property")

    props[1].add_feature('tennis court')

    print(f"Now the property at {props[1].get_full_address()} has the following features: {props[1].get_property_features()}")
    
