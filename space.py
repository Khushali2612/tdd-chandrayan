class chand:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
    def move(self, command):
        if command == 'f':
            x, y, z = self.position
            if self.direction == 'N':
                self.position = (x, y + 1, z)
            elif self.direction == 'S':
                self.position = (x, y - 1, z)
            elif self.direction == 'E':
                self.position = (x + 1, y, z)
            elif self.direction == 'W':
                self.position = (x - 1, y, z)
            elif self.direction == 'Up':
                self.position = (x, y, z + 1)
            elif self.direction == 'Down':
                self.position = (x, y, z - 1)
        elif command == 'b':
            # Similar logic as 'f', but reversing the direction.
            x, y, z = self.position
            if self.direction == 'N':
                self.position = (x, y - 1, z)
            elif self.direction == 'S':
                self.position = (x, y + 1, z)
            elif self.direction == 'E':
                self.position = (x - 1, y, z)
            elif self.direction == 'W':
                self.position = (x + 1, y, z)
            elif self.direction == 'Up':
                self.position = (x, y, z - 1)
            elif self.direction == 'Down':
                self.position = (x, y, z + 1)
            # spacecraft.py

    def turn(self, command):
        directions = ['N', 'E', 'S', 'W', 'Up', 'Down']
        current_index = directions.index(self.direction)
        if command == 'r':
            self.direction = directions[(current_index + 1) % len(directions)]
        elif command == 'l':
            self.direction = directions[(current_index - 1) % len(directions)]
        
    




