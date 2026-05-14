from blocktype import block_to_block_type
from blocktype import BlockType
from blocktype import ParentNode
from split import markdown_to_blocks
from split import text_to_textnodes
from textnode import text_node_to_html_node
from textnode import TextNode
from textnode import TextType

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    block_nodes = []

    for block in block_list:
        block_type = block_to_block_type(block)

        if block_type == BlockType.block_heading:
            counter = 0
            for char in block:
                if char == "#":
                    counter += 1
                else:
                    break
            tag = "h" + str(counter)
            remaining_text = block[counter+1:]
            parent = ParentNode(tag, text_to_children(remaining_text))
            block_nodes.append(parent)
        
        if block_type == BlockType.block_paragraph:
            result = block.replace("\n", " ")
            parent = ParentNode("p", text_to_children(result))
            block_nodes.append(parent)

        if block_type == BlockType.block_quote:
            result = block.split("\n")
            cleaned_list = [line.lstrip(">").strip() for line in result]
            final_result = " ".join(cleaned_list)
            parent = ParentNode("blockquote", text_to_children(final_result))
            block_nodes.append(parent)
        
        if block_type == BlockType.block_code:
            result = block[4:-3]
            text_node = TextNode(result, TextType.text_plain)
            leaf = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [leaf])
            pre_node = ParentNode("pre", [code_node])
            block_nodes.append(pre_node)

        

            

    return ParentNode("div", block_nodes)


def text_to_children(text):
    htmlnodes_list = []
    current_textnodes = text_to_textnodes(text)
    for i in current_textnodes:
        current_htmlnode = text_node_to_html_node(i)
        htmlnodes_list.append(current_htmlnode)
    return htmlnodes_list



