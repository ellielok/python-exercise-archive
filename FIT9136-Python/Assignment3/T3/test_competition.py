import unittest
from competition import Competition
from runner import Runner
from custom_errors import CustomTypeError, CustomValueError
from race import ShortRace, MarathonRace


class SimpleShortRace(ShortRace):
    """A simple race implementation to simulate ShortRace"""

    def __init__(self, distance, runners):
        super().__init__(distance, runners)

    def conduct_race(self):
        # Return a sorted list of runners based on a simple criterion (e.g., speed)
        return sorted(
            [(runner, self.distance / runner.sprint_speed) for runner in self.runners],
            key=lambda x: x[1],
        )


class SimpleMarathonRace(MarathonRace):
    """A simple race implementation to simulate MarathonRace"""

    def __init__(self, distance, runners):
        super().__init__(distance, runners)

    def conduct_race(self):
        # Return a sorted list of runners based on a simple criterion (e.g., speed)
        return sorted(
            [
                (runner, self.distance / runner.endurance_speed)
                for runner in self.runners
            ],
            key=lambda x: x[1],
        )


class TestCompetition(unittest.TestCase):
    def setUp(self):
        # Create some runner instances for testing
        self.runners = [
            Runner("Elijah", 19, "Australia", 6.4, 5.2),
            Runner("Rupert", 67, "Botswana", 2.2, 1.8),
            Runner("Phoebe", 12, "France", 3.4, 2.8),
            Runner("Lauren", 13, "Iceland", 4.4, 5.1),
            Runner("Chloe", 21, "Timor-Leste", 5.2, 1.9),
        ]

        # Set up a competition instance
        self.distances_short = [0.5, 0.6, 1.2]
        self.distances_marathon = [4.0, 11.0, 4.5]
        self.competition = Competition(
            self.runners, 3, self.distances_short, self.distances_marathon
        )

    def test_init_valid_input(self):
        # Assert that the competition instance is properly initialized
        self.assertEqual(self.competition.runners, self.runners)
        self.assertEqual(self.competition.rounds, 3)
        self.assertEqual(self.competition.distances_short, self.distances_short)
        self.assertEqual(self.competition.distances_marathon, self.distances_marathon)
        self.assertIsNotNone(self.competition.leaderboard)
        self.assertEqual(
            self.competition.leaderboard,
            {"1st": None, "2nd": None, "3rd": None, "4th": None, "5th": None},
        )

    def test_init_invalid_input(self):
        # Test invalid runners list
        with self.assertRaises(CustomTypeError):
            Competition("not a list", 3, self.distances_short, self.distances_marathon)

        # Test invalid rounds (less than 1)
        with self.assertRaises(CustomValueError):
            Competition(
                self.runners,
                0,
                self.distances_short,
                self.distances_marathon,
            )
        with self.assertRaises(CustomValueError):
            Competition(
                self.runners,
                -1,
                self.distances_short,
                self.distances_marathon,
            )
        # Test invalid rounds (more than MAX_ROUNDS)
        with self.assertRaises(CustomValueError):
            Competition(
                self.runners,
                6,
                self.distances_short,
                self.distances_marathon,
            )
        # Test invalid rounds (not an int)
        with self.assertRaises(CustomTypeError):
            Competition(
                self.runners,
                2.5,
                self.distances_short,
                self.distances_marathon,
            )
        # Test invalid rounds (not an int)
        with self.assertRaises(CustomTypeError):
            Competition(
                self.runners,
                2.0,
                self.distances_short,
                self.distances_marathon,
            )

        # Test invalid distances_short
        with self.assertRaises(CustomTypeError, msg="`distances_short` is not a list"):
            Competition(self.runners, 3, "not a list", self.distances_marathon)
        with self.assertRaises(
            CustomValueError, msg="`distances_short` contains negative values"
        ):
            Competition(self.runners, 3, [1.1, 2.2, -1.1], self.distances_marathon)
        with self.assertRaises(
            CustomTypeError, msg="`distances_short` contains non-float values"
        ):
            Competition(self.runners, 3, [1.1, 2.2, 4], self.distances_marathon)
        with self.assertRaises(
            CustomValueError,
            msg="`distances_short` does not have the same length as `runners`",
        ):
            Competition(self.runners, 3, [1.1, 2.2], self.distances_marathon)

        # Test invalid distances_marathon
        with self.assertRaises(
            CustomTypeError, msg="`distances_marathon` is not a list"
        ):
            Competition(self.runners, 3, self.distances_short, "not a list")
        with self.assertRaises(
            CustomValueError, msg="`distances_marathon` contains negative values"
        ):
            Competition(self.runners, 3, self.distances_short, [1.1, 2.2, -1.1])
        with self.assertRaises(
            CustomTypeError, msg="`distances_marathon` contains non-float values"
        ):
            Competition(self.runners, 3, self.distances_short, [1.1, 2.2, 4])
        with self.assertRaises(
            CustomValueError,
            msg="`distances_marathon` does not have the same length as `runners`",
        ):
            Competition(self.runners, 3, self.distances_short, [1.1, 2.2])

    def test_conduct_competition_dnf(self):
        # Only run 1 round
        self.competition.rounds = 1

        # Before the competition, all runners should have max_energy
        for runner in self.runners:
            self.assertEqual(runner.energy, runner.max_energy)

        # Set energy of runners[0] to a very low value
        self.runners[0].energy = 1

        # Conduct the competition
        self.competition.conduct_competition()

        # Energy of runners[0] should be max_energy
        self.assertEqual(self.runners[0].energy, self.runners[0].max_energy)

        # Other runners should have energy less than max_energy
        for runner in self.runners[1:]:
            self.assertLess(runner.energy, runner.max_energy)

    def test_conduct_competition(self):
        # Conduct the competition
        leaderboard = self.competition.conduct_competition()

        # Assert the leaderboard is updated correctly
        # This will depend on the input results and implementation of update_leaderboard
        # Example expected leaderboard assuming input data and round outcomes
        expected_leaderboard = {
            "1st": ("Elijah", 12),
            "2nd": ("Chloe", 9),
            "3rd": ("Lauren", 6),
            "4th": ("Phoebe", 3),
            "5th": ("Rupert", 0),
        }
        self.assertEqual(
            leaderboard,
            expected_leaderboard,
            f"Invalid leaderboard. Check points logic {expected_leaderboard}",
        )

    def test_conduct_race(self):
        # Use real race classes for testing
        short_race = SimpleShortRace(0.5, self.runners)
        marathon_race = SimpleMarathonRace(4.0, self.runners)

        # Conduct races
        short_result = self.competition.conduct_race(short_race)
        marathon_result = self.competition.conduct_race(marathon_race)

        # Verify that results are sorted by time correctly
        # Assuming lower times indicate higher rank
        self.assertLess(
            short_result[0][1], short_result[1][1]
        )  # 1st should be faster than 2nd
        self.assertLess(
            marathon_result[0][1], marathon_result[1][1]
        )  # 1st should be faster than 2nd

    def test_conduct_race_invalid_input(self):
        with self.assertRaises(CustomTypeError):
            self.competition.conduct_race("not a race")
        with self.assertRaises(CustomTypeError):
            self.competition.conduct_race(234)
        with self.assertRaises(CustomTypeError):
            self.competition.conduct_race(None)

    def test_update_leaderboard(self):
        # Define test results for updating the leaderboard
        self.competition.update_leaderboard(
            [
                (self.runners[0], 10.0),
                (self.runners[1], 12.0),
                (self.runners[2], 14.0),
            ]
        )
        self.assertEqual(
            self.competition.leaderboard,
            {
                "1st": ("Elijah", 2),
                "2nd": ("Rupert", 1),
                "3rd": ("Phoebe", 0),
                "4th": None,
                "5th": None,
            },
        )

    def test_update_leaderboard_dnf(self):
        self.competition.update_leaderboard(
            [
                (self.runners[0], 10.0),
                (self.runners[1], 12.0),
                (self.runners[2], 14.0),
            ]
        )
        self.assertEqual(
            self.competition.leaderboard,
            {
                "1st": ("Elijah", 2),
                "2nd": ("Rupert", 1),
                "3rd": ("Phoebe", 0),
                "4th": None,
                "5th": None,
            },
        )

        # Update leaderboard with some DNF values
        self.competition.update_leaderboard(
            [
                (self.runners[0], "DNF"),
                (self.runners[1], 10.2),
                (self.runners[2], "DNF"),
            ]
        )
        self.assertEqual(
            self.competition.leaderboard,
            {
                "1st": ("Rupert", 3),
                "2nd": ("Elijah", 2),
                "3rd": ("Phoebe", 0),
                "4th": None,
                "5th": None,
            },
        )

    def test_update_leaderboard_invalid_input(self):
        with self.assertRaises(CustomTypeError):
            self.competition.update_leaderboard("Not a list")
        with self.assertRaises(CustomValueError):
            self.competition.update_leaderboard([(self.runners[0], "10.0")])
        with self.assertRaises(CustomValueError):
            self.competition.update_leaderboard([(self.runners[0], -1.0)])
        with self.assertRaises(CustomValueError):
            self.competition.update_leaderboard([(self.runners[0], "D_N_F")])


if __name__ == "__main__":
    unittest.main()

