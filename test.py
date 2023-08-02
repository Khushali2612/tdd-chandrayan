
import unittest
from space import chand

class SpacecraftTest(unittest.TestCase):

    def test1(self):
        spacecraft = chand((0, 0, 0), 'N')
        self.assertEqual(spacecraft.position, (0, 0, 0))
        self.assertEqual(spacecraft.direction, 'N')
    def test_move(self):
        spacecraft = chand((0, 0, 0), 'N')
        spacecraft.move('f')
        self.assertEqual(spacecraft.position, (0, 1, 0))
        spacecraft.move('b')
        self.assertEqual(spacecraft.position, (0, 0, 0))
   

if __name__ == '__main__':
    unittest.main()
    def test_turn(self):
        spacecraft = chand((0, 0, 0), 'N')
        spacecraft.turn('u')
        self.assertEqual(spacecraft.direction, 'Up')
        spacecraft.turn('d')
        self.assertEqual(spacecraft.direction, 'N')

if __name__ == '__main__':
    unittest.main()