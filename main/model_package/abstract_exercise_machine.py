
class MainExerciseMachine:

    def __init__(self, price_per_hour=0, duration_in_minutes=0, producing_country="choose",
                 model="nt-200"):
        self.price_per_hour = price_per_hour
        self.duration_in_minutes = duration_in_minutes
        self.producing_country = producing_country
        self.model = model

    def __str__(self):
        return "price per hour is  {} \t duration in minutes is {} \t producing country is {}" \
               "\t model is {}" \
            .format(self. price_per_hour, self.duration_in_minutes, self.producing_country,
                    self.model)
