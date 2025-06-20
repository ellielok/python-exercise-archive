import unittest
from runner import Runner
from custom_errors import CustomValueError, CustomTypeError


class TestRunner(unittest.TestCase):
    def test_runner_initialization(self):
        runner = Runner("Elijah", 18, "Australia", 5.8, 4.4)

        # Check the initialization of attributes
        self.assertEqual(runner.name, "Elijah")
        self.assertEqual(runner.age, 18)
        self.assertEqual(runner.country, "Australia")
        self.assertEqual(runner.sprint_speed, 5.8)
        self.assertEqual(runner.endurance_speed, 4.4)
        self.assertEqual(runner.energy, 1000)

        # Wrong name attribute for testing
        # Name
        with self.assertRaises(CustomTypeError):
            Runner(888, 18, "Australia", 5.8, 4.4)
        # Age
        with self.assertRaises(CustomTypeError):
            Runner("Elijah", "WrongAge", "Australia", 5.8, 4.4)
        # Country
        with self.assertRaises(CustomTypeError):
            Runner("Elijah", 18, 888, 5.8, 4.4)
        # Sprint speed
        with self.assertRaises(CustomTypeError):
            Runner("Elijah", 18, "Australia", "WrongSpeed", 4.4)
        # Endurance speed
        with self.assertRaises(CustomTypeError):
            Runner("Elijah", 18, "Australia", 5.8, "WrongSpeed")

        # Wrong name attribute for testing
        with self.assertRaises(CustomValueError):
            Runner("Elijah!!!", 20, "Australia", 5.8, 4.4)

        # Wrong age attribute for testing
        with self.assertRaises(CustomValueError):
            Runner("Elijah", 200, "Australia", 5.8, 4.4)

    def test_drain_energy(self):
        runner = Runner("Elijah", 18, "Australia", 5.8, 4.4)

        runner.drain_energy(800)
        self.assertEqual(runner.energy, 200)

        runner.drain_energy(150)
        self.assertEqual(runner.energy, 50)

        with self.assertRaises(CustomValueError):
            runner.recover_energy(-200)

    def recover_drain_energy(self):
        runner = Runner("Elijah", 18, "Australia", 5.8, 4.4)

        runner.drain_energy(800)
        self.assertEqual(runner.energy, 200)

        runner.recover_energy(300)
        self.assertEqual(runner.energy, 500)

        runner.recover_energy(900)
        self.assertEqual(runner.energy, 1000)

        with self.assertRaises(ValueError):
            runner.recover_energy(-200)


if __name__ == "__main__":
    unittest.main()

