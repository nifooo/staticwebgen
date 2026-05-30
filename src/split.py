from regx import extract_markdown_images
from regx import extract_markdown_links
from textnode import TextNode
from textnode import TextType
from delimiter import split_nodes_delimiter



def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.text_plain:
            new_nodes.append(node)
        else:
            image_extracted = extract_markdown_images(node.text)
            if image_extracted == []:
                new_nodes.append(node)
                continue
            remaining = node.text
            for image_alt, image_link in image_extracted:
                sections = remaining.split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.text_plain))
                new_nodes.append(TextNode(image_alt, TextType.format_image, image_link))
                remaining = sections[1]
            if remaining != "":
                new_nodes.append(TextNode(remaining, TextType.text_plain))
    return new_nodes                  

           

def split_nodes_link(old_nodes):
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.text_plain:
            new_nodes.append(node)
        else:
            link_extracted = extract_markdown_links(node.text)
            if link_extracted == []:
                new_nodes.append(node)
                continue
            remaining = node.text
            for text, url in link_extracted:
                sections = remaining.split(f"[{text}]({url})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.text_plain))
                new_nodes.append(TextNode(text, TextType.format_link, url))
                remaining = sections[1]
            if remaining != "":
                new_nodes.append(TextNode(remaining, TextType.text_plain))
    return new_nodes


def text_to_textnodes(text):
    node = [TextNode(text, TextType.text_plain)]
    split_first = split_nodes_delimiter(node, "**", TextType.text_bold)
    split_second = split_nodes_delimiter(split_first, "_", TextType.text_italic)
    split_third = split_nodes_delimiter(split_second, "`", TextType.text_code)
    
    images = split_nodes_image(split_third)
    links = split_nodes_link(images)
    return links

def markdown_to_blocks(markdown):
    new_list = []
    splitter = markdown.split("\n\n")
    for b in splitter:
        clean = b.strip()
        if clean != "":
            new_list.append(clean)
    return new_list
                              