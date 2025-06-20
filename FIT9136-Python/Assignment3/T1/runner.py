from custom_errors import CustomValueError, CustomTypeError
import csv


# A new Class for read Countries.csv
def read_countries():
    """
    Reads the 'name' column from 'countries.csv' and returns a list of country names.
    
    Returns:
        list: A list containing the names of countries.
    """
    countries = []
    with open("countries.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            countries.append(row["name"])
    return countries


class Runner:
    """
    Represents an Runner who participates in races, managing their attributes and performance.

    Attributes:
        name (str): The name of the runner.
        age (int): The age of the runner.
        country (str): The country of the runner.
        sprint_speed (float): The sprint speed of the runner in meters per second.
        endurance_speed (float): The marathon speed of the runner in meters per second.
        energy (int): The current energy level of the runner, initialized to max_energy.
    """

    max_energy = 1000 # Maximum energy level for all runners

    def __init__(
        self,
        name: str,
        age: int,
        country: str,
        sprint_speed: float,
        endurance_speed: float,
    ) -> None:
    
        """
        Initializes a new Runner instance with specified attributes, validating each input.
        
        Raises:
            CustomTypeError: If incorrect types are provided for any attribute.
            CustomValueError: If any attribute value is out of allowed range.
        """
        # Validate and initialize instance variables
        if not isinstance(name, str):
            raise CustomTypeError("Name must be a string.")

        if not name.replace(" ", "").isalnum():
            raise CustomValueError("Name must be an alphanumeric string.")

        if not isinstance(age, int):
            raise CustomTypeError("Age must be an integer.")

        if not (5 <= age <= 120):
            raise CustomValueError("Age must be an integer between 5 and 120.")

        if not isinstance(country, str):
            raise CustomTypeError("Country must be a string.")

        countries = read_countries()
        if country not in countries:
            raise CustomValueError("Country must be in countries.csv.")

        if not isinstance(sprint_speed, float):
            raise CustomTypeError("Sprint speed must be a float.")

        if not (2.2 <= sprint_speed <= 6.9):
            raise CustomValueError("Sprint speed must lie between 2.2 and 6.8 m/s.")

        if not isinstance(endurance_speed, float):
            raise CustomTypeError("Endurance speed must be a float.")

        if not (1.8 <= endurance_speed <= 5.4):
            raise CustomValueError("Endurance speed must lie between 1.8 and 5.4 m/s.")

        # Variables
        self.name = name
        self.age = age
        self.country = country
        self.sprint_speed = sprint_speed
        self.endurance_speed = endurance_speed
        
        self.energy = self.max_energy # Initialize energy to maximum

    def drain_energy(self, drain_points: int) -> None:
        """
        Drains a specified amount of energy from the runner, ensuring it does not drop below zero.
        
        Args:
            drain_points (int): The amount of energy to drain from the runner.

        Raises:
            CustomTypeError: If drain_points is not an integer.
            CustomValueError: If drain_points is out of the valid range.
        """

        if not isinstance(drain_points, int):
            raise CustomTypeError("Drain points must be an integer.")

        if not (0 <= drain_points <= self.max_energy):
            raise CustomValueError(
                "Drain points cannot be less than 0 or more than the maximum energy."
            )
        self.energy = max(0, self.energy - drain_points) # Ensure energy does not go negative

    def recover_energy(self, recovery_amount: int) -> None:
        """
        Recovers a specified amount of energy for the runner, ensuring it does not exceed max_energy.
        
        Args:
            recovery_amount (int): The amount of energy to recover.

        Raises:
            CustomTypeError: If recovery_amount is not an integer.
            CustomValueError: If recovery_amount is out of the valid range.
        """
        if not isinstance(recovery_amount, int):
            raise CustomTypeError("Recovery amount must be an integer.")
        if not (0 <= recovery_amount <= self.max_energy):
            raise CustomValueError(
                "Recovery amount cannot exceed the maximum energy."
            )
        self.energy = min(self.max_energy, self.energy + recovery_amount) # Ensure energy does not exceed maximum

    def run_race(self, race_type: str, distance: float) -> float:
        """
        Calculates the time taken to complete a race based on the race type and distance.

        Args:
            race_type (str): The type of race, either 'short' or 'long'.
            distance (float): The distance of the race in kilometers.

        Returns:
            float: The time taken to complete the race in seconds, rounded to two decimal places.

        Raises:
            CustomTypeError: If incorrect types are provided for race_type or distance.
            CustomValueError: If the distance is non-positive or the race_type is invalid.
        """
        if not isinstance(race_type, str):
            raise CustomTypeError("Run type must be a string.")

        if not isinstance(distance, float):
            raise CustomTypeError("Distance must be a float.")

        if distance <= 0:
            raise CustomValueError("Distance must be greater than zero.")

        if race_type == "short":
            speed = self.sprint_speed
        elif race_type == "long":
            speed = self.endurance_speed
        else:
            raise CustomValueError("Race type must be 'short or 'long'.")

        time_taken_calculate = (distance * 1000) / speed # Convert distance from km to meters
        time_taken = round(time_taken_calculate, 2) # Round the time taken.
        return time_taken

    def __str__(self) -> str:
        """
        Returns a string representation of the Runner instance.

        Returns:
            str: A formatted string displaying the runner's name, age, and country.
        """
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"


if __name__ == "__main__":
    runner = Runner("Elijah", 18, "Australia", 5.8, 4.4)

    # running a short race
    time_taken = runner.run_race("short", 2)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")

