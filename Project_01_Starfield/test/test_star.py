import unittest 
from modelFolder.star import Star

class TestStar(unittest.TestCase):
    
    def test_01_move_right_should_increase_x(self):
        star = Star(x=0, y=0, velocity_x=1, velocity_y=0)
        star.update_position()
        self.assertEqual((star.x, star.y), (1,0))

    def test_02_move_up_should_increase_y(self):
        star = Star(x=0, y=0, velocity_x=0, velocity_y=1)
        star.update_position()
        self.assertEqual((star.x, star.y), (0,1))

    def test_03_move_with_velocity_should_update_position_correctly(self):
        star = Star(x=0, y=0, velocity_x=5, velocity_y=-8)
        star.update_position()
        self.assertEqual((star.x, star.y), (5,-8))

    def test_04_update_position_should_record_previous_position_in_trail(self):
        star = Star(x=0, y=0, velocity_x=5, velocity_y=-8)
        self.assertEqual(star.trail_array, [])
        star.update_position()
        self.assertEqual(star.trail_array, [(0,0)])
        star.update_position()
        self.assertEqual(star.trail_array, [(0, 0), (5, -8)])

    def test_05_get_10th_last_trail_point_should_return_10th_last_when_trail_long_enough(self):
        star = Star(x=0, y=0, velocity_x=1, velocity_y=1)
        star.update_position()
        self.assertEqual(star.get_10th_last_trail_point_or_first(), (0,0))
        star.update_position()
        self.assertEqual(star.get_10th_last_trail_point_or_first(), (0,0))
        for _ in range(8):
            star.update_position()
        self.assertEqual(star.get_10th_last_trail_point_or_first(), (1,1))
        star.update_position()
        self.assertEqual(star.get_10th_last_trail_point_or_first(), (2,2))

    def test_06_get_last_trail_point(self):
        star = Star(x=0, y=0, velocity_x=1, velocity_y=1)
        star.update_position()
        self.assertEqual(star.get_last_trail_point(), (0,0))
        star.update_position()
        self.assertEqual(star.get_last_trail_point(), (1,1))


    

if __name__ == '__main__':
    unittest.main()