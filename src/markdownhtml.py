from blocktype import block_to_block_type
from split import markdown_to_blocks
from split import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    for i in block_list:
        current_block = block_to_block_type(i)

def text_to_children(text):
    htmlnodes_list = []
    current_textnodes = text_to_textnodes(text)
    for i in current_textnodes:
        current_htmlnode = text_node_to_html_node(i)
        htmlnodes_list.append(current_htmlnode)
    return htmlnodes_list