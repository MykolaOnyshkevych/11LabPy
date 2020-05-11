from main.model_package.abstract_exercise_machine import MainExerciseMachine


class GymManager:

    def __init__(self):
        self.exercise_machine_list = []

    def add_exercise_machines(self, *all_exercise_machines: MainExerciseMachine):
        for exercise_machine in all_exercise_machines:
            self.exercise_machine_list.append(exercise_machine)

    def find_exercise_machine_by_price(self, needed_price: int):
        """
        >>> exercise_machine_first = MainExerciseMachine(20, 30, "Ukraine", "TL-100")
        >>> exercise_machine_second = MainExerciseMachine(30, 65, "USA", "Anti-Guk")
        >>> exercise_machine_third = MainExerciseMachine(40, 30, "Holland", "GorillaGlue")
        >>> gym_manager = GymManager()
        >>> gym_manager.add_exercise_machines(exercise_machine_first, exercise_machine_second, exercise_machine_third)
        >>> founded_exercise_machine_list = gym_manager.find_exercise_machine_by_price(20)
        >>> [exercise_machine.price_per_hour for exercise_machine in founded_exercise_machine_list]
        [20]
        """
        founded_exercise_machine_list: list = []
        for exercise_machine in self.exercise_machine_list:
            if exercise_machine.price_per_hour == needed_price:
                founded_exercise_machine_list.append(exercise_machine)
        return founded_exercise_machine_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, extraglobs={'gym_manager': GymManager()})

# from main.manager_package.gym_manager_utils import GymManagerUtils
#
#
# class GymManager:
#
#     def __init__(self, exercise_machine_list):
#         self.exercise_machine_list = exercise_machine_list
#
#     def add_exercise_machine(self, exercise_machine):
#         self.exercise_machine_list.append(exercise_machine)
#
#     def add_exercise_machines(self, *all_exercise_machines: MainExerciseMachine):
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
