
# Take your partners improved solution to task_1
# And make 10 tests with unittest
# Your code should be runnable as:
# "python -m unittest test_task1"
# If there is not enough code to make 10 tests,
# or the code can't be tested you need to alter the solution,
# so that it would be possible to test it.
# How to get your partners solution:
#  1. go to your own solution on github
#  2. go the adress bar in the browser
#  4. change your username, to your partners username
#  5. enjoy the easy and cheerful task of working with someone's else code
#  6. There is no point 3
#
# On your own, you need to copy his code into this repository!!!
# Remember to include it while commiting.
#
# Fill the data here in the comments
#
# I am using solution by TheYiome
# from the commit https://github.com/pite2020sum/thu-16-20-task1-theYiome.git
#

import unittest
import task
import tasklib
import math

class TestInit(unittest.TestCase):
    def setUp(self):
        self.car = task.Car()

    def test_no_initial_speed(self):
        self.assertEqual(self.car.speed, 0, 'initial speed not zero')

    def test_some_initial_speed(self):
        self.car2 = task.Car(1)
        self.assertEqual(self.car2.speed, 1,'wrong initial speed')

    def test_no_steering_angle(self):
        self.car2 = task.Car()
        self.assertEqual(self.car2.steering_wheel_angle, 0, 'wrong initial steering wheel angle')

    def test_some_steering_angle(self):
        self.car3 = task.Car(initial_steering_wheel_angle = math.pi / 4)
        self.assertEqual(self.car3.steering_wheel_angle, math.pi / 4, 'wrong steering angle')

    def test_stop(self):
        self.car3 = task.Car(1)
        self.car3.act("stop")
        self.assertEqual(self.car3.speed, 0, 'not stopped')

    def test_speed_up(self):
        self.car3 = task.Car()
        self.car3.act("speed up")
        self.assertEqual(self.car3.speed, 1, 'wrong speed')

    def test_speed_down(self):
        self.car3 = task.Car(1)
        self.car3.act("speed down")
        self.assertEqual(self.car3.speed, 0, 'too much speed')

    def test_turn_right(self):
        self.car3 = task.Car()
        self.car3.act("turn right")
        self.assertEqual(self.car3.steering_wheel_angle, math.pi / 4, 'wrong turn right angle')

    def test_turn_left(self):
        self.car3 = task.Car()
        self.car3.act("turn left")
        self.assertEqual(self.car3.steering_wheel_angle, -math.pi / 4, 'wrong turn left angle')

    def test_invalid_action(self):
        self.car3 = task.Car()
        try:
            self.car3.act("asdjmg")
        except tasklib.InvalidAction as exc:
            self.assertEqual("{}".format(exc), "No such action!", 'not detecting invalid action')
            




if __name__ == '__main__':
    unittest.main()
