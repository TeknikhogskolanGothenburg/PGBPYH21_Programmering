import random
import unittest
from unittest.mock import patch

from game import Game
from capture_output import capture_output


class GoTestCase(unittest.TestCase):
    # def __init__(self):
    #     super().__init__()
    #     self.game = None

    def setUp(self):
        self.game = Game()

    def test_valid_direction(self):
        current_room = self.game.map.get_current_room(self.game.player.position)
        direction = random.choice(current_room.exits)
        position = self.game.player.position
        match direction:
            case 'north':
                position.row -= 1
            case 'south':
                position.row += 1
            case 'west':
                position.col -= 1
            case 'east':
                position.col += 1

        next_room = self.game.map.get_current_room(position)
        new_description = next_room.description

        with patch('builtins.input', return_value='go ' + direction):
            self.game.process_user_input()

        current_room = self.game.map.get_current_room(self.game.player.position)
        self.assertEqual(new_description, current_room.description)

    def test_invalid_direction(self):
        current_room = self.game.map.get_current_room(self.game.player.position)
        exits = current_room.exits
        direction = None
        for _dir in ['south', 'north', 'east', 'west']:
            if _dir not in exits:
                direction = _dir
                break
        with patch('builtins.input', return_value='go ' + direction):
            with capture_output() as (out, _):
                self.game.process_user_input()
        screen_data = out.getvalue()[5:-5]
        expected_data = f"It is impossible to go in the direction {direction}"
        self.assertEqual(expected_data, screen_data)

    def test_strange_direction(self):
        pass


if __name__ == '__main__':
    unittest.main()
