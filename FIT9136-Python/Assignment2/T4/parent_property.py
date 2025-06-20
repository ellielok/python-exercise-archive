from abc import ABC, abstractmethod
from typing import Tuple, List, Union

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

    @abstractmethod
    def get_floor_number(self) -> int:
        """Get the floor number of the property"""
        pass

    @abstractmethod
    def set_floor_number(self, floor_number: int) -> None:
        """Set the floor number of the property"""
        pass

    @abstractmethod
    def get_land_area(self) -> int:
        """Get the land area of the property"""
        pass

    @abstractmethod
    def set_land_area(self, land_area: int) -> None:
        """Set the land area of the property"""
        pass

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

if __name__ == '__main__':
    pass
