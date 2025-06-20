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
    

if __name__ == '__main__':
    pass

