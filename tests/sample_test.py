from it.isaura.python.sample.node import Node
import unittest


class TestNodeMethods(unittest.TestCase):
    def test_print(self):
        node = Node(1, 'first node', [1, 2]);
        _w = node.getWeights();
        self.assertEqual(_w,[1,2]);
        print _w;
