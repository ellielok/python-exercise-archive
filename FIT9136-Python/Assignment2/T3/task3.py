import csv
import json

def process_schools(file_name: str) -> dict:
    """
    Extract school information from a CSV file
    """
    # Read the file
    with open(file_name, "r", encoding='utf-8-sig') as f:
        school_dict = {}
        lines = csv.DictReader(f)

        # Add values of each school into the dict
        for line in lines:
            # Ignore empty rows 
            if not line['school_lon']: 
                continue
            if not line['school_lat']:
                continue
            school = {
                'school_no' : line['school_no'],
                'school_name' : line['school_name'],
                'school_type' : line['school_type'],
                'school_lat' : float(line['school_lat']),
                'school_lon' : float(line['school_lon'])
            }
            
            school_dict[school['school_no']] = school

        return school_dict


def process_medicals(file_name: str) -> dict:
    """
    Extract medical information from a CSV file
    """
    # Read the file
    with open(file_name, "r", encoding='utf-8-sig') as f:
        medical_dict = {}
        lines = csv.DictReader(f)

        # Add values of each gp into the dict
        for line in lines:
            location_string = line['location']
            # Ignore rows marking with NA 
            if not location_string or location_string == 'NA': 
                continue
            
            location_dict = json.loads(location_string)
            gp = {
                'gp_code' : line['gp_code'],
                'gp_name' : line['gp_name'],
                'gp_lat' : float(location_dict['lat']),
                'gp_lon' : float(location_dict['lng'])
            }
            
            medical_dict[gp['gp_code']] = gp

        return medical_dict


def process_sport(file_name: str) -> dict:
    """
    Extract sport facilities information from a CSV file
    """

    sport_dict = {}

    # Read the file
    with open(file_name, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        # Add values of each school into the dict
        for row in reader:
            # Ignore empty rows 
            if not row["sport_lat"]:
                continue
            if not row["sport_lon"]:
                continue 

            sport = {
                "facility_id": row["facility_id"],
                "facility_name": row["facility_name"],
                "sport_lat": float(row["sport_lat"]),
                "sport_lon": float(row["sport_lon"]),
                "sport_played": row["sport_played"],
            }

            sport_dict[sport["facility_id"]] = sport
    return sport_dict


def main():
    school_dict = process_schools('sample_melbourne_schools.csv')
    medical_dict = process_medicals('sample_melbourne_medical.csv')
    sport_dict = process_sport('sample_sport_facilities.csv')

    sample_medical_code = 'mgp0041'
    print(f"There are {len(school_dict)} schools and {len(sport_dict)} sport facilities in our dataset")
    print(f"The location for {medical_dict[sample_medical_code]['gp_name']} is {medical_dict[sample_medical_code]['gp_lat']}, {medical_dict[sample_medical_code]['gp_lon']}")

if __name__ == '__main__':
    main()

