from main.model_package.abstract_exercise_machine import AbstractExerciseMachine


class GymManager:

    def __init__(self):
        self.exercise_machine_list = []

    def add_exercise_machines(self, *all_exercise_machines: AbstractExerciseMachine):
        for exercise_machine in all_exercise_machines:
            self.exercise_machine_list.append(exercise_machine)

    def find_exercise_machine_by_price(self, needed_price: int):
        """
        >>> exercise_machine_first = AbstractExerciseMachine(20, 30, "Ukraine", "TL-100")
        >>> exercise_machine_second = AbstractExerciseMachine(30, 65, "USA", "Anti-Guk")
        >>> exercise_machine_third = AbstractExerciseMachine(40, 30, "Holland", "GorillaGlue")
        >>> gym_manager = GymManager()
        >>> gym_manager.add_exercise_machines(exercise_machine_first, exercise_machine_second, exercise_machine_third)
        >>> result = gym_manager.find_exercise_machine_by_price(20)
        >>> [exercise_machine.price_per_hour for exercise_machine in result]
        [20]
        """
        result: list = []
        for exercise_machine in self.exercise_machine_list:
            if exercise_machine.price_per_hour == needed_price:
                result.append(exercise_machine)
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, extraglobs={'gym_manager': GymManager()})

#from main.manager_package.gym_manager_utils import GymManagerUtils

#
# class GymManager:
#
#     def __init__(self, exercise_machine_list):
#         self.exercise_machine_list = exercise_machine_list
#
#     def add_exercise_machines(self, *all_exercise_machines: AbstractExerciseMachine):
#         for exercise_machine in all_exercise_machines:
#             self.exercise_machine_list.append(exercise_machine)
#
#     def find_exercise_machine_by_price(self, needed_price=None):
#         founded_machines = []
#         for exercise_machine in self.exercise_machine_list:
#             if exercise_machine.price_per_hour == needed_price:
#                 founded_machines.append(exercise_machine)
#             return founded_machines
#
#     def find_exercise_machine_by_model(self, model):
#         founded_machines = []
#         for exercise_machine in self.exercise_machine_list:
#             if exercise_machine.model == model:
#                 founded_machines.append(exercise_machine)
#         return founded_machines
