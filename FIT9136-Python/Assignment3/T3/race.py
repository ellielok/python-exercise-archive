from custom_errors import CustomTypeError, CustomValueError, RunnerAlreadyExistsError, RunnerDoesntExistError, RaceIsFullError
from abc import ABC, abstractmethod
from runner import Runner
import math
from typing import List, Tuple, Union


class Race(ABC):
    """
    Abstract base class representing a generic race.

    Attributes:
        distance (float): The distance of the race in kilometers.
        runners (list): List of Runner objects participating in the race.
    """
    def __init__(self, distance: float, runners:list=None) -> None:
        """
        Initializes the Race with a given distance and optional list of runners.

        Args:
            distance (float): The distance of the race in kilometers.
            runners (list, optional): Initial list of runners. Defaults to None.

        Raises:
            CustomTypeError: If the distance is not a float or runners is not a list of Runner instances.
        """
        if not isinstance(distance, float):
            raise CustomTypeError("Distance must be a float.")
        
        if runners is not None:
            if not isinstance(runners, list):
                raise CustomTypeError("Runners must be a list.")
        
            for runner in runners:
                if not isinstance(runner, Runner):
                    raise CustomTypeError("Runner must be a instance of Runner class.")
        
        
        self.distance = distance
        self.runners = runners if runners is not None else []

    def add_runner(self, runner: Runner)->None:
        """
        Adds a runner to the race.

        Args:
            runner (Runner): The runner to add.

        Raises:
            RunnerAlreadyExistsError: If the runner already exists in the race.
            RaceIsFullError: If adding the runner would exceed the maximum participants.
        """
        if runner in self.runners:
            raise RunnerAlreadyExistsError("Runner already exists.")
        if len(self.runners) >= self.maximum_participants:
            raise RaceIsFullError("The face is already full.")
        self.runners.append(runner)

    def remove_runner(self, runner: Runner)->None:
        """
        Removes a runner from the race.

        Args:
            runner (Runner): The runner to remove.

        Raises:
            RunnerDoesntExistError: If the runner does not exist in the race.
        """
        if runner not in self.runners:
            raise RunnerDoesntExistError("This runner is not in the race.")
        self.runners.remove(runner)
    
    @abstractmethod
    def conduct_race(self):
        """
        Conducts the race and calculates the results. Must be implemented by subclasses.
        """
        pass

    @property
    @abstractmethod
    def maximum_participants(self) -> int:
        """
        Abstract property that must be implemented by subclasses.
        """
        pass

class ShortRace(Race):
    """
    Represents a short race.

    Class Attributes:
        race_type (str): Identifier for the type of race.
        maximum_participants (int): Maximum number of runners allowed.
        time_multiplier (float): Multiplier to adjust calculated race times.
    """
    race_type = "short"
    maximum_participants = 8
    time_multiplier = 1.2
        

    def conduct_race(self) -> List[Tuple[Runner, float]]:
        """
        Conducts a short race and calculates the time taken for each runner.

        Returns:
            list: A list of tuples containing each runner and their race time.
        """
        result = []
        for runner in self.runners:
            time_taken = runner.run_race(self.race_type, self.distance) * self.time_multiplier
            result.append((runner, time_taken))
        return result
    

class MarathonRace(Race):
    """
    Represents a marathon race.

    Class Attributes:
        race_type (str): Identifier for the type of race.
        maximum_participants (int): Maximum number of runners allowed.
        energy_per_km (int): Energy consumed per kilometer by each runner.
    """
    race_type = "long"
    maximum_participants = 16
    energy_per_km = 100
    

    def conduct_race(self)->List[Tuple[Runner, Union[float, str]]]:
        """
        Conducts a marathon race and calculates the time taken or DNF status for each runner.

        Returns:
            list: A list of tuples containing each runner and their race time or 'DNF' status.
        """
        result = []
        for runner in self.runners:
            time_taken = 0
            for km in range(math.ceil(self.distance)):
                if runner.energy > 0:
                    time_taken += runner.run_race(self.race_type, self.distance)
                    runner.drain_energy(self.energy_per_km)
                else:
                    time_taken = "DNF"
                    break
            result.append((runner, time_taken))
        return result


if __name__ == "__main__":
    short_race = ShortRace(0.5)
    long_race = MarathonRace(5.0)

    # Add a Runner
    eli = Runner("Elijah", 18, "Australia", 5.8, 4.4)
    rup = Runner("Rupert", 23, "Australia", 2.3, 1.9)

    long_race.add_runner(eli)
    long_race.add_runner(rup)

    results = long_race.conduct_race()
    for runner, time in results:
        print(runner.name, time)

