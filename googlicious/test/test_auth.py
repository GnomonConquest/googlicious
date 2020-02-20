import unittest

import googlicious.auth

class authtest(unittest.TestCase):
    def test(self):
        self.assertTrue(googlicious.auth.gauth(verbose=True))

if __name__ == '__main__':
    unittest.main()