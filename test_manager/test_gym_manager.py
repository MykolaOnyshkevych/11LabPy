import unittest


from main.manager_package.gym_manager_utils import GymManagerUtils
from main.manager_package.gym_manager import GymManager
from main.model_package.abstract_exercise_machine import AbstractExerciseMachine


def get_the_list(get_me, given_list):
    return given_list[get_me]


class GymManagerTest(unittest.TestCase):
    def setUp(self):
        self.first_machine = AbstractExerciseMachine(40, 34, "UKRAINE", "SH_URA")
        self.second_machine = AbstractExerciseMachine(30, 45, "Russia", "vodka")
        self.third_machine = AbstractExerciseMachine(50, 67, "USA", "say_ga")
        self.fourth_machine = AbstractExerciseMachine(60, 89, "Uganda", "old_school")
        self.exercise_machine_list = [self.first_machine, self.second_machine,
                                      self.third_machine, self.fourth_machine]
        self.gym_manager = GymManager(self.exercise_machine_list)


class TestFinding(GymManagerTest):
    def test_finding_by_price(self):
        self.assertEqual(first=self.gym_manager.find_exercise_machine_by_price(40), second=[self.second_machine])
        self.assertEqual(first=self.gym_manager.find_exercise_machine_by_price(50), second=[self.first_machine, self.third_machine])

    def test_finding_by_model(self):
        self.assertEqual(first=self.gym_manager.find_exercise_machine_by_model("vodka"), second=[self.second_machine])


class TestSorting(GymManagerTest):
    def test_sorting_by_price(self):
        GymManagerUtils.sort_by_price(self.exercise_machine_list)
        self.assertEqual(first=get_the_list(0, self.exercise_machine_list), second=self.second_machine)
        self.assertEqual(first=get_the_list(1, self.exercise_machine_list), second=self.first_machine)
        self.assertEqual(first=get_the_list(2, self.exercise_machine_list), second=self.third_machine)
        self.assertEqual(first=get_the_list(3, self.exercise_machine_list), second=self.fourth_machine)

    def test_sorting_by_duration(self):
        GymManagerUtils.sort_by_duration(self.exercise_machine_list)
        self.assertEqual(first=get_the_list(0, self.exercise_machine_list), second=self.first_machine)
        self.assertEqual(first=get_the_list(1, self.exercise_machine_list), second=self.second_machine)
        self.assertEqual(first=get_the_list(2, self.exercise_machine_list), second=self.third_machine)
        self.assertEqual(first=get_the_list(3, self.exercise_machine_list), second=self.fourth_machine)


if __name__ == '__main__':
    unittest.main()
