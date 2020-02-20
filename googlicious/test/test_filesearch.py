import unittest
import googlicious.filesearch

class testsearch(unittest.TestCase):
    def testsearchobj(self):
        self.assertTrue(g = googlicious.filesearch.googler())

if __name__ == '__main__':
    unittest.main()