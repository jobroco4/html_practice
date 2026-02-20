import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_code(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r'(`.*?`)', node.text)
        for part in parts:
            if re.match(r'`.*?`', part):
                new_nodes.append(TextNode(part[1:-1], TextType.CODE))
            elif part:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def split_nodes_bold(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r'(\*\*.*?\*\*)', node.text)
        for part in parts:
            if re.match(r'\*\*.*?\*\*', part):
                new_nodes.append(TextNode(part[2:-2], TextType.BOLD))
            elif part:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes

def split_nodes_italic(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r'(\*.*?\*|_.*?_)', node.text)
        for part in parts:
            if re.match(r'\*.*?\*|_.*?_', part):
                new_nodes.append(TextNode(part[1:-1], TextType.ITALIC))
            elif part:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes