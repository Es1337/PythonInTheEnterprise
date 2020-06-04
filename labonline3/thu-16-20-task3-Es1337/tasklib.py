import math


class DriverLeft(Exception):
    pass


class InvalidAction(Exception):
    pass


class Car:
    def __init__(self, initial_speed=0, initial_steering_wheel_angle=0):
        self.speed = initial_speed
        self.steering_wheel_angle = initial_steering_wheel_angle
        self.events = []

    def stop(self):
        self.speed = 0
    
    def speed_up(self):
        self.speed = self.speed + 1

    def speed_down(self):
        self.speed = self.speed - 1

    def turn_right(self):
        self.steering_wheel_angle = self.steering_wheel_angle + math.pi / 4
        if self.steering_wheel_angle > math.pi / 2:
            self.steering_wheel_angle = math.pi / 2

    def turn_left(self):
        self.steering_wheel_angle = self.steering_wheel_angle - math.pi / 4
        if self.steering_wheel_angle < -math.pi / 2:
            self.steering_wheel_angle = -math.pi / 2

    def act(self, event):
        self.events.append(event)

        if event == "stop":
            self.stop()
        elif event == "speed up":
            self.speed_up()
        elif event == "speed down":
            self.speed_down()
        elif event == "turn right":
            self.turn_right()
        elif event == "turn left":
            self.turn_left()
        elif event == "exit":
            if self.speed != 0:
                raise InvalidAction("Can not leave moving car! Please stop first.")
            else:
                raise DriverLeft()
        else:
            raise InvalidAction("No such action!")
    
    @staticmethod
    def valid_actions():
        return ["stop", "speed up", "speed down", "turn right", "turn left", "exit"]

    def __repr__(self):
        return ("Driving {} units per second, "
                "steering wheel angle is {}").format(
                    self.speed,
                    self.steering_wheel_angle
                )
