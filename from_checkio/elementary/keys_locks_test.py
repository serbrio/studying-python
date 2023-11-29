from unittest import TestCase, main
from keys_locks import keys_and_locks

class KeysLocksTestCase(TestCase):
    def test_keys_locks_1(self):
        self.assertTrue(keys_and_locks('''
        0##0
        0##0
        00#0
        00##
        00##''',
        '''
        00000
        000##
        #####
        ##000
        00000'''))

    def test_keys_locks_2(self):
        self.assertFalse(keys_and_locks('''
        ###0
        00#0''',
        '''
        00000
        00000
        #0000
        ###00
        0#000
        0#000'''))

    def test_keys_locks_3(self):
        self.assertTrue(keys_and_locks('''
        0##0
        0#00
        0000''',
        '''
        ##000
        #0000
        00000
        00000
        00000'''))

    def test_keys_locks_4(self):
        self.assertFalse(keys_and_locks('''
        ###0
        0#00
        0000''',
        '''
        ##00
        ##00'''))

    def test_keys_locks_5(self):
        self.assertTrue(keys_and_locks('''
        00000000
        #0#0####
        ###00000
        ###00000
        ###00000''',
        '''
        0000000
        0000000
        00####0
        00###00
        00####0
        0000000
        00000#0
        00000#0
        00000#0
        00000#0
        0000000'''))

if __name__ == '__main__':
    main()