import unittest

from text_to_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
from text_to_links import split_nodes_image, split_nodes_link, text_to_textnodes

class TestTextToLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is a [link](http://example.com) and another [link2](https://example.org)."
        expected_links = [("link","http://example.com"), ("link2","https://example.org")]
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](http://example.com/image.png) and another ![alt2](https://example.org/photo.jpg)."
        expected_images = [("alt text","http://example.com/image.png"), ("alt2","https://example.org/photo.jpg")]
        self.assertEqual(extract_markdown_images(text), expected_images)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is a [link](http://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)."
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "http://example.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertListEqual(text_to_textnodes(text), expected_nodes)