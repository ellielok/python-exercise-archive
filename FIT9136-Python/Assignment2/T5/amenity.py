from typing import Tuple, List, Union

class Amenity():
    def __init__(self, amenity_code: str, 
                        amenity_name: str,
                        amenity_type: str, 
                        amenity_subtype: str,
                        coordinates: Tuple[float, float]):
        self.__amenity_code = amenity_code
        self.__amenity_name = amenity_name
        self.__amenity_type = amenity_type
        self.__amenity_subtype = amenity_subtype
        self.__amenity_coordinates = coordinates

    def get_amenity_code(self) -> str:
        """Get the code of the amenity"""
        return self.__amenity_code
    
    def set_amenity_name(self, amenity_name: str) -> None:
        """Set the name of the amenity"""
        self.__amenity_name = amenity_name
    
    def get_amenity_name(self) -> str:
        """Get the code of the amenity"""
        return self.__amenity_name
    
    def get_amenity_coords(self) -> Tuple[float, float]:
        """Get the latitude and longitude of the amenity"""
        return self.__amenity_coordinates
    
    def get_amenity_type(self) -> str:
        """Get the type of the amenity"""
        return self.__amenity_type
    
    def set_amenity_subtype(self, amenity_subtype: Union[str,None]) -> None:
        """Set the subtype of the amenity"""
        self.__amenity_subtype = amenity_subtype
    
    def get_amenity_subtype(self) -> Union[str,None]:
        """Get the subtype of the amenity"""
        return self.__amenity_subtype

if __name__ == '__main__':
    a = Amenity('1001')
    

    
