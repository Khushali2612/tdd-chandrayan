
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
    def main():
    spacecraft = Spacecraft((0, 0, 0), 'N')
    commands = ['f', 'r', 'u', 'b', 'l']
    spacecraft.execute_commands(commands)
    final_position = spacecraft.position
    final_direction = spacecraft.direction
    print(f"Final Position: {final_position}")
    print(f"Final Direction: {final_direction}")


if __name__ == '__main__':
    unittest.main()
