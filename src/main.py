from textnode import TextNode 
from textnode import TextType
import os, shutil


def main():
    node = TextNode("This is some anchor text", TextType.format_link, "https://www.boot.dev")
    print(node)

    if os.path.exists("static") == False:
        print("Static folder does not exist")
        return
    
    if os.path.exists("public") == True: 
        shutil.rmtree("public")   
    
    os.mkdir("public")
    copydir("static", "public")


def copydir(source, destination):
    content_static = os.listdir(source)
    for item in content_static:     
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            os.mkdir(dest_path)
            copydir(source_path, dest_path)

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# ") :
            title = line.lstrip("#").strip()
            return title
    
    raise ValueError("No Title to extract!")

if __name__ == "__main__":
    main()
    
