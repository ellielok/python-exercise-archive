from typing import Tuple, List, Union
from parent_property import Property

class House(Property):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        land_area: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        super().__init__(
            prop_id = prop_id, 
            bedrooms = bedrooms, 
            bathrooms = bathrooms, 
            parking_spaces = parking_spaces, 
            full_address = full_address,
            floor_area = floor_area,
            price = price,
            property_features = property_features,
            coordinates = coordinates
            )
        self.__land_area = land_area
    
    def get_prop_type(self) -> str:
        """Get the type of property: house"""
        return 'house'
    
    def get_land_area(self) -> int:
        """Get the land area of the property"""
        return self.__land_area
    
    def set_land_area(self, land_area: int) -> None:
        """Set the land area of the property"""
        self.__land_area = land_area

    def get_floor_number(self) -> int:
        """Get the floor number of the property"""
        pass
    
    def set_floor_number(self, floor_number: int) -> None:
        """Set the floor number of the property"""
        pass

class Apartment(Property):
    def __init__(self, prop_id: str, 
                        bedrooms: int, 
                        bathrooms: int, 
                        parking_spaces: int, 
                        full_address: str,
                        floor_number: int,
                        floor_area: int,
                        price: int,
                        property_features: List[str],
                        coordinates: Tuple[float, float]):
        super().__init__(
            prop_id = prop_id, 
            bedrooms = bedrooms, 
            bathrooms = bathrooms, 
            parking_spaces = parking_spaces, 
            full_address = full_address,
            floor_area = floor_area,
            price = price,
            property_features = property_features,
            coordinates = coordinates
            )
        self.__floor_number = floor_number
    
    def get_prop_type(self) -> str:
        """Get the type of property: apartment"""
        return 'apartment'
    

    def get_land_area(self) -> int:
        """Get the land area of the property"""
        pass
    
    def set_land_area(self, land_area: int) -> None:
        """Set the land area of the property"""
        pass

    def get_floor_number(self) -> int:
        """Get the floor number of the property"""
        return self.__floor_number
    
    def set_floor_number(self, floor_number: int) -> None:
        """Set the floor number of the property"""
        self.__floor_number = floor_number


if __name__ == '__main__':
    house = House(
        prop_id="A",
        bedrooms=3,
        bathrooms=3,
        parking_spaces=3,
        full_address="A A A A A A A",
        land_area=3,
        floor_area=3,
        price=3,
        property_features="",
        coordinates=(1, 2) ,
    )
    print(house.get_land_area())

