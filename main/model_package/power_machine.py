from main.model_package.abstract_exercise_machine import AbstractExerciseMachine


class PowerMachine(AbstractExerciseMachine):
    def __init__(self, gain_of_weight_in_kilo=0):
        super(AbstractExerciseMachine, self).__init__()
        self.gain_of_weight_in_kilo = gain_of_weight_in_kilo

    def __str__(self):
        return super().__str__() + ", gain_of_weight_in_kilo %s" % self.gain_of_weight_in_kilo
