import unittest
import generator

class TestGenerator(unittest.TestCase):
    def test__init__(self):
        gen = generator.Generate(1,25,2)
        self.assertLessEqual(gen.start, 1,'set start from 1 or greater than 1')
        self.assertGreaterEqual(gen.stop, gen.start, 'stop must greater than start')

