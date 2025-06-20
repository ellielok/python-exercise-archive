from abc import ABC, abstractmethod
from typing import Tuple, List, Union
from amenity import Amenity

import math


class Property(ABC):
    """
    Define a Property class that holds variables and methods common to child classes 
    """
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        self.__prop_id = prop_id
        self.__full_address = full_address
        self.__suburb = full_address.split(" ")[3]
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__parking_spaces = parking_spaces
        self.__coordinates = coordinates
        self.__floor_area = floor_area
        self.__price = price
        self.__property_features = property_features

    
    def get_prop_id(self) -> str:
        """Get the property's ID"""
        return self.__prop_id

    def get_full_address(self) -> str:
        """Get the property's address"""
        return self.__full_address

    def get_suburb(self) -> str:
        """Get the property's suburb"""
        return self.__suburb
    
    @abstractmethod
    def get_prop_type(self) -> str:
        """Define an abstract method of getting the type of property"""
        pass
    
    def set_bedrooms(self, bedrooms: int) -> None:
        """Set the number of bedrooms the property has"""
        self.__bedrooms = bedrooms
    
    def get_bedrooms(self) -> int:
        """Get the number of bedrooms the property has"""
        return self.__bedrooms
    
    def set_bathrooms(self, bathrooms: int) -> None:
        """Set the number of bathrooms the property has"""
        self.__bathrooms = bathrooms
    
    def get_bathrooms(self) -> int:
        """Get the number of bathrooms the property has"""
        return self.__bathrooms
    
    def set_parking_spaces(self, parking_spaces: int) -> None:
        """Set the number of parking spaces the property has"""
        self.__parking_spaces = parking_spaces

    def get_parking_spaces(self) -> int:
        """Get the number of parking spaces the property has"""
        return self.__parking_spaces
    
    def get_coordinates(self) -> Tuple[float, float]:
        """Get a tuple containing latitude and longitude of the property"""
        return self.__coordinates

    def get_floor_number(self) -> int:
        """Get the floor number of the property"""
        return self.__floor_number
    
    def set_floor_number(self, floor_number: int) -> None:
        """Set the floor number of the property"""
        self.__floor_number = floor_number

    def get_land_area(self) -> int:
        """Get the land area of the property"""
        return self.__land_area
    
    def set_land_area(self, land_area: int) -> None:
        """Set the land area of the property"""
        self.__land_area = land_area

    def set_floor_area(self, floor_area: int) -> None:
        """Set the floor number of the property"""
        self.__floor_area = floor_area
    
    def get_floor_area(self) -> int:
        """Get the floor number of the property"""
        return self.__floor_area

    def set_price(self, price: int) -> None:
        """Set the price of the property"""
        self.__price = price
    
    def get_price(self) -> int:
        """Get the price of the property"""
        return self.__price
    
    def set_property_features(self, property_features: List[str]) -> None:
        """Set a list of the features of the property"""
        self.__property_features = property_features
    
    def get_property_features(self) -> List[str]:
        """Get a list of the features of the property"""
        return self.__property_features

    def add_feature(self, feature: str) -> None:
        """Add features into the property"""
        if feature not in self.get_property_features():
            self.get_property_features().append(feature)
    
    def remove_feature(self, feature: str) -> None:
        """Remove features from the property"""
        if feature in self.get_property_features():
            self.get_property_features().remove(feature)

    def __check_amenity(self, amenity: Amenity, amenity_type: str, amenity_subtype: str = None) -> bool:
        """
        Check if the amenity match to the type required
        """
        # If the amenity doesn't match to the type required, return False
        if amenity.get_amenity_type() != amenity_type:
            return False
        if amenity_subtype == None:
            return True
        # Exceptional circumstance: if the subtype is Pri/Sec school
        if amenity_subtype == "Pri/Sec":
            if amenity.get_amenity_subtype() == "Primary":
                return True
            if amenity.get_amenity_subtype() == "Secondary":
                return True
        if amenity_subtype == "Secondary":
            if amenity.get_amenity_subtype() == "Pri/Sec":
                return True
        if amenity_subtype == "Primary":
            if amenity.get_amenity_subtype() == "Pri/Sec":
                return True
        # If the amenity match to the subtype required, return True
        if amenity.get_amenity_subtype() == amenity_subtype:
            return True
        return False
        

    def nearest_amenity(self, amenities: List[Amenity], amenity_type: str, amenity_subtype: str = None) -> Tuple[Amenity, float]:
        """
        Finding the Nearest Amenity
        """
        nearest_amenity = None
        min_distance = float('inf')

        prop_lat = self.get_coordinates()[0]
        prop_lon = self.get_coordinates()[1]
        
        # Use for in loop to get the nearest amenity
        for amenity in amenities:
            # Use check_amenity function to check if the amenity match to the type required 
            if self.__check_amenity(amenity, amenity_type, amenity_subtype) == True:
                amenity_lat = amenity.get_amenity_coords()[0]
                amenity_lon = amenity.get_amenity_coords()[1]

                distance = self.__haversine_distance(prop_lat, prop_lon, amenity_lat, amenity_lon)

                if distance < min_distance:
                    nearest_amenity = amenity
                    min_distance = distance
        
        return nearest_amenity, min_distance

    def __haversine_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Copy the function from the previous task
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # Convert decimal degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        radius_of_earth = 6371  # Radius of the earth in kilometers.
        distance = radius_of_earth * c

        return distance

if __name__ == '__main__':
    pass
