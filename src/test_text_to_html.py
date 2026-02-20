import unittest

from textnode import TextNode, TextType
from text_to_html import split_nodes_delimiter  


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.TEXT)], "`", TextType.CODE)
        node2 = split_nodes_delimiter([TextNode("This is text with a `code block` word", TextType.TEXT)], "`", TextType.CODE)
        self.assertEqual(node, node2)