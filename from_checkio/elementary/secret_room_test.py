from unittest import TestCase, main
from secret_room import secret_room

class SecretRoomTestCase(TestCase):
    def test_secret_room_1(self):
        self.assertEqual(1, secret_room(5))

    def test_secret_room_2(self):
        self.assertEqual(2, secret_room(3))

    def test_secret_room_3(self):
        self.assertEqual(551, secret_room(1000))

    def test_secret_room_4(self):
        self.assertEqual(51, secret_room(100))


if __name__ == '__main__':
    main()