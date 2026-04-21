import re

def extract_markdown_images(text):
    matches_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_images
def extract_markdown_links(text):
    matches_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_links