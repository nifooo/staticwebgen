from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	text_plain = "plain"
	text_bold = "bold"
	text_italic = "italic"
	text_code = "code"
	format_link = "link"
	format_image = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	def __repr__ (self):
		return  f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
	if text_node is None:
		raise Exception("Text Node can not be None")
	if text_node.text_type == TextType.text_plain:
		return LeafNode(None, text_node.text)
	if text_node.text_type == TextType.text_bold:
		return LeafNode("b", text_node.text)
	if text_node.text_type == TextType.text_italic:
		return LeafNode("i", text_node.text) 
	if text_node.text_type == TextType.text_code:
		return LeafNode("code", text_node.text)
	if text_node.text_type == TextType.format_link:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	if text_node.text_type == TextType.format_image:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
		
		
		