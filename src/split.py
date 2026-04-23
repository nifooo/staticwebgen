from regx import extract_markdown_images
from regx import extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            image_extracted = extract_markdown_images(node.text)
            if image_extracted == []:
                return
            else:
                for i in image_extracted:
                    sections = i.split(f"![{image_alt}]({image_link})", 1)
                    
                    new_nodes.append(image_parts)

           

def split_nodes_link(old_nodes):