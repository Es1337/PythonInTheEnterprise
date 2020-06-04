import random
from collections import namedtuple
import keyboard
import time

##################### Car class #########################
class Car:
    def __init__(self, color):
        self.current_speed = 0
        self.top_speed = 180
        self.color = color
        self.accel_coefficient = 10
        self.driving = False
        self.wheel_angle = 0

    def drive(self, limit):
        if self.current_speed > limit:
            self.current_speed = limit

        driving_message = f'Driving. Mode: {limit_switcher(limit)}  Current speed: {str(self.current_speed)}. Current wheel angle: {str(self.wheel_angle)} .'

        if self.wheel_angle < 0 and self.wheel_angle <= -10:
            self.wheel_angle += 10
        elif self.wheel_angle > 0 and self.wheel_angle >= 10:
            self.wheel_angle -= 10
        else:
            self.wheel_angle = 0

        self.driving = True
        return driving_message

    def accelerate(self, time):
        if self.current_speed < self.top_speed:
            self.current_speed += self.accel_coefficient * time

    def brake(self):
        self.current_speed = 0
        self.driving = False
        return 'Braking.'

    def slow_down(self):
        if(self.current_speed > 50):
            self.current_speed = 50
            return 'Slowing down.'
        else:
            return ''

    def turn(self, direction):
        is_slowing_down = self.slow_down()
        if abs(self.wheel_angle) <= 15:
            if direction == 'right':
                self.wheel_angle += 15
            else:
                self.wheel_angle -= 15
        return f'{is_slowing_down} Turning {direction}'

################### Obstacle detection ####################
Obstacles = namedtuple('Obstacles',
                       ['pedestrian_crossing', 'red_light', 'subordinated_road', 'no_obstacle'])

def obstacle_switcher(key):
    obstacles_dict = {
            2: 'pedestrian crossing', 
            5: 'red light', 
            3: 'subordinated road'
        }
    return obstacles_dict.get(key, 'no obstacle')

def detect_obstacle(car):
    obstacles_list = Obstacles(2, 5, 3, 0)
    detected = random.choices(obstacles_list, k=1, weights=[1, 1, 1, 20])
    
    if detected[0] is not obstacles_list.no_obstacle:
        is_braking = car.brake()
        time.sleep(detected[0])
        return f'{is_braking} Waiting for {detected[0]} seconds because car stopped for {obstacle_switcher(detected[0])}'
    else:
        return '' 
    

################### Curve detection ####################
Directions = namedtuple('Directions',
                        ['right', 'left', 'straight'])

def direction_switcher(key):
    direction_dict = {
            1: 'right', 
            2: 'left'
        }
    return direction_dict.get(key, 'straight')

def detect_curve(car):
    directions_list = Directions(1, 2, 0)
    detected = random.choices(directions_list, k=1, weights=[1, 1, 3])
    direction_message = ''

    if detected[0] is not directions_list.straight:
        direction_message = car.turn(direction_switcher(detected[0]))
        time.sleep(1)
    
    return direction_message

################# Speed limit detection ##################
Limits = namedtuple('Limits',
                    ['neighbourhood', 'city', 'main', 'speedy_boi'])

def limit_switcher(key):
    limits_dict = {
            30: 'neighbourhood road',
            50: 'city', 
            70: 'main road'
        }
    return limits_dict.get(key, 'speedy boi')

def detect_limit(car):

    limits_list = Limits(30, 50, 70, 200)
    detected = random.choices(limits_list, k=1, weights=[1, 2, 3, 1])

    return detected[0]

####################### Game itself ########################
player_car = Car('blue')
checked_limit_time = time.time()
current_limit = 50

if __name__ == "__main__":
    print('If you want to stop the car press S')

    while True:
        if keyboard.is_pressed('s'):
            print('Stop.')
            break

        if (time.time() - checked_limit_time) > 10:
            current_limit = detect_limit(player_car)
            checked_limit_time = time.time()

        driving_text = player_car.drive(current_limit)
        obstacle_text = detect_obstacle(player_car)

        direction_text = ''

        if player_car.driving:
            direction_text = detect_curve(player_car)
            player_car.accelerate(1)
            time.sleep(1)

        print(f'{driving_text} {obstacle_text} {direction_text}')

    print(f'The car was {player_car.color} by the way.')