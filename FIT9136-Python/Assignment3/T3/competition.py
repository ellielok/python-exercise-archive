from custom_errors import CustomTypeError, CustomValueError
from race import Race, ShortRace, MarathonRace
from runner import Runner
from typing import List, Tuple, Union, Dict


class Competition:
    MAX_ROUNDS = 3
    """
    Manages a competition consisting of multiple rounds of races, maintaining a leaderboard.

    Attributes:
        runners (List[Runner]): List of runners participating in the competition.
        rounds (int): Number of rounds in the competition.
        distances_short (List[float]): Distances for the short races in each round.
        distances_marathon (List[float]): Distances for the marathon races in each round.
        leaderboard (Dict[str, Tuple[str, int]]): Leaderboard tracking runner positions and points.
    """

    def __get_ordinal(self, n):
        # Helper function to return the ordinal string for a given integer
        # NOTE : You can ignore this method, you don't need to comment
        # or do any checks on it whatsoever
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        if 11 <= n % 100 <= 13:
            suffix = "th"
        else:
            suffix = suffixes.get(n % 10, "th")
        return f"{n}{suffix}"

    def __init__(
        self,
        runners: [List],
        rounds: int,
        distances_short: List[float],
        distances_marathon: List[float],
    ):
        """
        Initializes a new Competition instance.

        Args:
            runners (List[Runner]): List of runners.
            rounds (int): Number of competition rounds.
            distances_short (List[float]): Distances for short races.
            distances_marathon (List[float]): Distances for marathon races.

        Raises:
            CustomTypeError: For incorrect type inputs.
            CustomValueError: For invalid value inputs.
        """
        if not isinstance(self.MAX_ROUNDS, int):
            raise CustomTypeError("MAX GROUND must be an integer.")

        if runners is not None:
            if not isinstance(runners, list):
                raise CustomTypeError("Runners must be a list.")

            for runner in runners:
                if not isinstance(runner, Runner):
                    raise CustomTypeError("Runner must be a instance of Runner class.")

        if not isinstance(rounds, int):
            raise CustomTypeError("Rounds must be a positive integer.")

        if rounds <= 0:
            raise CustomValueError("Rounds must be a positive integer.")

        if not isinstance(distances_short, list):
            raise CustomTypeError("Distance shorts must be a list.")

        for distance in distances_short:
            if not isinstance(distance, float):
                raise CustomTypeError("Distance must be a float.")
            if distance <= 0:
                raise CustomValueError("Distance must be a positive floating value.")

        if not isinstance(distances_marathon, list):
            raise CustomTypeError("Distance shorts must be a list")

        for distance in distances_marathon:
            if not isinstance(distance, float):
                raise CustomTypeError("Distance must be a float.")
            if distance <= 0:
                raise CustomValueError("Distance must be a positive floating value.")

        if len(distances_short) != rounds or len(distances_marathon) != rounds:
            raise CustomValueError(
                "The length of both distances lists should be the same as rounds."
            )

        self.runners = runners
        self.rounds = rounds
        self.distances_short = distances_short
        self.distances_marathon = distances_marathon

        self.leaderboard = {}

        for i in range(1, len(self.runners) + 1):
            self.leaderboard[self.__get_ordinal(i)] = None

    def conduct_competition(self) -> Dict[str, Union[Tuple[str, int], None]]:
        """
        Conducts the competition through all rounds, updating the leaderboard after each race.

        Returns:
            Dict[str, Union[Tuple[str, int], None]]: The final leaderboard after all rounds.
        """
        current_round = 1
        i = 0
        while current_round <= self.rounds:
            # Conduct the short race with all runners
            short_race = ShortRace(self.distances_short[i], runners=self.runners)
            short_result = self.conduct_race(short_race)

            # Conduct the Marathon race with all runners
            marathon = MarathonRace(self.distances_marathon[i], runners=self.runners)
            marathon_result = self.conduct_race(marathon)

            # Recover energy for all DNF runners
            for runner, time_taken in marathon_result:
                if time_taken == "DNF":
                    runner.recover_energy(runner.max_energy)

            current_round += 1
            i += 1
            self.update_leaderboard(short_result)
            self.update_leaderboard(marathon_result)

        return self.leaderboard

    def conduct_race(self, race: Race)  -> List[Tuple[Runner, Union[float, str]]]:
        """
        Conducts a race and returns the results.

        Args:
            race (Race): The race to be conducted.

        Returns:
            List[Tuple[Runner, Union[float, str]]]: The results of the race.
        """
        if not isinstance(race, Race):
            raise CustomTypeError("Race should be race class.")
        return race.conduct_race()

    def get_point(self, name: str) -> int:
        for value in self.leaderboard.values():
            if value is not None:
                value_name = value[0]
                if value_name == name:
                    return value[1]
        return 0

    def update_leaderboard(
        self, results: List[Tuple[Runner, Union[float, str]]]
    ) -> None:
        """
       Updates the leaderboard based on the results of a race.

        Args:
            results (List[Tuple[Runner, Union[float, str]]]): The results of the race, each being a tuple of a Runner and their time or 'DNF'.

        Raises:
            CustomTypeError: If results are not in the expected format.
            CustomValueError: If the time taken is not positive or not 'DNF'.
        """
        if not isinstance(results, list):
            raise CustomTypeError("Results must be a list.")

        for item in results:
            if not isinstance(item, tuple):
                raise CustomTypeError("Item must be a tuple.")
            if len(item) != 2:
                raise CustomValueError("Length of the tuple must be 2.")
            if not isinstance(item[0], Runner):
                raise CustomTypeError("Must be runner.")
            time_taken = item[1]
            if not isinstance(time_taken, (float, str)):
                raise CustomTypeError("Point must be a float or str.")
            if isinstance(time_taken, float):
                if time_taken <= 0:
                    raise CustomValueError("Time taken must be a positive float.")
            if isinstance(time_taken, str):
                if time_taken != "DNF":
                    raise CustomValueError(
                        "If time taken is a string, it only can be 'DNF'."
                    )

        valid_results = []
        invalid_results = []

        for item in results:
            runner = item[0]
            time_taken = item[1]
            is_valid: bool = time_taken != "DNF"
            if is_valid:
                valid_results.append(item)
            else:
                invalid_results.append(item)
        sorted_results = sorted(valid_results, key=lambda x: x[1])

        runner_points: List[Tuple[str, int]] = []
        for item in invalid_results:
            runner: Runner = item[0]
            tpl = (runner.name, self.get_point(runner.name))
            runner_points.append(tpl)

        max_point = len(results)
        for i, item in enumerate(sorted_results):
            round_point = max_point - 1 - i
            runner: Runner = item[0]
            tpl = (runner.name, self.get_point(runner.name) + round_point)
            runner_points.append(tpl)

        sorted_runner_points = sorted(runner_points, key=lambda x: x[1], reverse=True)
        leaderboard = {}
        for n, item in enumerate(sorted_runner_points):
            key = self.__get_ordinal(n + 1)
            value = item
            self.leaderboard[key] = value

    def print_leaderboard(self) -> None:
        """
        Prints the current leaderboard in a formatted manner.
        """
        print(self.leaderboard)
        print("Leaderboard\n\n")
        for key, value in self.leaderboard.items():
            print(f"{key} - {value[0]} ({value[1]})")


if __name__ == "__main__":
    # Example usage
    runners = [
        Runner("Elijah", 19, "Australia", 6.4, 5.2),
        Runner("Rupert", 67, "Botswana", 2.2, 1.8),
        Runner("Phoebe", 12, "France", 3.4, 2.8),
        Runner("Lauren", 13, "Iceland", 4.4, 5.1),
        Runner("Chloe", 21, "Timor-Leste", 5.2, 1.9),
    ]

    competition = Competition(runners, 3, [0.5, 0.6, 1.2], [4.0, 11.0, 4.5])
    _ = competition.conduct_competition()
    competition.print_leaderboard()

