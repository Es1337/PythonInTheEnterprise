import math
from tasklib import Car, DriverLeft, InvalidAction


if __name__ == "__main__":
    instance = Car(initial_steering_wheel_angle=math.pi / 3)
    is_running = True
    while is_running:
        print(instance)
        user_input = input().lower()
        try:
            instance.act(user_input)
        except DriverLeft:
            is_running = False
            print("See you soon!")
        except InvalidAction as exc:
            print("This action is not valid: {}".format(exc))
            print("Valid actions are: {}".format(Car.valid_actions()))

    print("\nRecorded events:")
    for x in instance.events:
        print(x)
