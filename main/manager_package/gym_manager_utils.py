from main.model_package.abstract_exercise_machine import AbstractExerciseMachine
from main.model_package.sort_type import SortType


class GymManagerUtils:

    @staticmethod
    def sort_by_duration(exercise_machine_list, sort_type):
        """
        Sorting by duration
        >>> new_created_list = [AbstractExerciseMachine(0, 30, "none", "none"), \
        AbstractExerciseMachine(0, 25, "none", "none"), AbstractExerciseMachine(0, 40, "none", "none")]
        >>> GymManagerUtils.sort_by_duration(new_created_list, SortType(1))
        >>> print(new_created_list[0].duration_in_minutes)
        25
        >>> print(new_created_list[1].duration_in_minutes)
        30
        >>> print(new_created_list[2].duration_in_minutes)
        40
        """
        if sort_type == SortType(1):
            exercise_machine_list.sort(key=lambda exercise_machine: exercise_machine.duration_in_minutes)
        elif sort_type == SortType(2):
            exercise_machine_list.sort(key=lambda exercise_machine: exercise_machine.duration_in_minutes,
                                       reverse=True)
        else:
            print("Can't sort")

    @staticmethod
    def sort_by_price(exercise_machine_list, sort_type):
        """
        Sorting by price
        >>> new_created_list = [AbstractExerciseMachine(30, 0, "none", "none"), \
        AbstractExerciseMachine(25, 0, "none", "none"), AbstractExerciseMachine(40, 0, "none", "none")]
        >>> GymManagerUtils.sort_by_price(new_created_list, SortType(1))
        >>> print(new_created_list[0].price_per_hour)
        25
        >>> print(new_created_list[1].price_per_hour)
        30
        >>> print(new_created_list[2].price_per_hour)
        40
        """
        if sort_type == SortType(1):
            exercise_machine_list.sort(key=lambda exercise_machine: exercise_machine.price_per_hour)
        elif sort_type == SortType(2):
            exercise_machine_list.sort(key=lambda exercise_machine: exercise_machine.price_per_hour,
                                       reverse=True)
        else:
            print("Can't sort")


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)


# class GymManagerUtils:
#
#     @staticmethod
#     def sort_by_duration(starter_list, sort_type=False):
#         starter_list.sort(key=lambda exercise_machine: exercise_machine.duration_in_minutes, reverse=sort_type)
#
#     @staticmethod
#     def sort_by_price(starter_list, sort_type=False):
#         starter_list.sort(key=lambda exercise_machine: exercise_machine.price_per_hour, reverse=sort_type)
#
#     @staticmethod
#     def sort_by_model(starter_list, sort_type=False):
#         starter_list.sort(key=lambda exercise_machine: exercise_machine.model, reverse=sort_type)