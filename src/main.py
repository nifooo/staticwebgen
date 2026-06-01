from textnode import TextNode 
from textnode import TextType
from markdownhtml import markdown_to_html_node 
from htmlnode import HTMLNode
import os, shutil


def main():
   

    if os.path.exists("static") == False:
        print("Static folder does not exist")
        return
    
    if os.path.exists("public") == True: 
        shutil.rmtree("public")   
    
    os.mkdir("public")
    copydir("static", "public")
    # generate_page("content/index.md", "template.html", "public/index.html" )
    generate_pages_recursive("content/", "template.html", "public/")

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

def generate_page(from_path, template_path, dest_path):
    print("Generating page from " + from_path + " to " + dest_path + " using " + template_path)

    with open(from_path, "r", encoding="utf-8") as f:
        content_md = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        content_html_template = f.read()
   
    
    html_node = markdown_to_html_node(content_md)
    convert_to_html = html_node.to_html()
    title = extract_title(content_md)
    page = content_html_template.replace("{{ Title }}", title)
    final_page = page.replace("{{ Content }}", convert_to_html)
    directory = os.path.dirname(dest_path)

    if directory:
       os.makedirs(directory,  exist_ok=True) 

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_page)
    

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        full_path_content = os.path.join(dir_path_content, item)
        
        if os.path.isfile(full_path_content):
            file_name, file_type = os.path.splitext(item)
            if file_type == ".md":
                
                file_path = os.path.join(dest_dir_path, file_name + ".html")
                generate_page(full_path_content, template_path, file_path)

        else:
            full_path_dest = os.path.join(dest_dir_path, item)
            
            generate_pages_recursive(full_path_content, template_path, full_path_dest)

if __name__ == "__main__":
    main()
    
