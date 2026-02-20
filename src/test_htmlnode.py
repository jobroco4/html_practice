import unittest
from htmlnode import *
class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'Hello World', [], {'class': 'text'})
        node2 = HTMLNode('p', 'Hello World', [], {'class': 'text'})
        self.assertNotEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode('p', 'Hello World', [], {'class': 'text'})
        node2 = HTMLNode('p', 'Hello World', [], {'class': 'other'})
        self.assertNotEqual(node, node2)
        
    def test_link(self):
        node = HTMLNode('a', 'Hello World', [], {'href': 'http://example.com'})
        node2 = HTMLNode('a', 'Hello World', [], {'href': 'http://example.com'})
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = HTMLNode('h1', 'Hello World', [], {'class': 'text'})
        node2 = HTMLNode('h2', 'Hello World', [], {'class': 'text'})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = HTMLNode.LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = HTMLNode.LeafNode("span", "child")
        parent_node = HTMLNode.ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = HTMLNode.LeafNode("b", "grandchild")
        child_node = HTMLNode.ParentNode("span", [grandchild_node])
        parent_node = HTMLNode.ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()