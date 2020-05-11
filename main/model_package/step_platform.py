from main.model_package.cardio_zone_machine import CardioZoneMachine


class StepPlatform(CardioZoneMachine):
    def __init__(self, high_of_the_platform=0):
        super(CardioZoneMachine, self).__init__()
        self.high_of_the_platform = high_of_the_platform
        
    def __str__(self):
        return super().__str__() + ", high_of_the_platform %s" % self.high_of_the_platform
