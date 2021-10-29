import unittest

from game import Game


class NewTestCase(unittest.TestCase):
    def test_get_item(self):
        game = Game()
        game.player.position.row = 0
        game.player.position.col = 1

        current_room = game.map.get_current_room(game.player.position)
        key_item = [item for item in current_room.items if item.name == "key"][0]
        game.player.get_item('key', current_room)
        items_in_room = game.map.map[0][1].items

        self.assertTrue(key_item not in items_in_room)  # add assertion here

    def test_get_and_drop_item(self):
        game = Game()
        game.player.position.row = 0
        game.player.position.col = 1

        current_room = game.map.get_current_room(game.player.position)
        key_item = [item for item in current_room.items if item.name == "key"][0]
        game.player.get_item('key', current_room)

        game.player.position.row = 1
        game.player.position.col = 0
        current_room = game.map.get_current_room(game.player.position)
        game.player.drop_item('key', current_room)
        items_in_room = game.map.map[1][0].items

        self.assertTrue(key_item in items_in_room)  # add assertion here


if __name__ == '__main__':
    unittest.main()
