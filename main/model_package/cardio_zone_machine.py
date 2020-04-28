from main.model_package.abstract_exercise_machine import AbstractExerciseMachine


class CardioZoneMachine(AbstractExerciseMachine):
    def __init__(self, dropped_weight_in_kilo=0):
        super(AbstractExerciseMachine, self).__init__()
        self.dropped_weight_in_kilo = dropped_weight_in_kilo

    def __str__(self):
        return super().__str__() + ", dropped_weight_in_kilo %s" % self.dropped_weight_in_kilo
