from main.model_package.cardio_zone_machine import CardioZoneMachine


class RaceTrack(CardioZoneMachine):
    def __init__(self, track_speed_in_meters_per_second=0):
        super(CardioZoneMachine, self).__init__()
        self.track_speed_in_meters_per_second = track_speed_in_meters_per_second

    def __str__(self):
        return super().__str__() + ", track_speed_in_meters_per_second %s" % self.track_speed_in_meters_per_second
