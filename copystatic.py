import os, shutil

if os.path.exists("public") == False:
    print("Public folder does not exist")
elif os.path.exists("static") == False:
    print("Static folder does not exist")
else:
    content_static = os.listdir("static")
    shutil.rmtree("public")   
    os.mkdir("public")
    
    for item in content_static:     
        source_path = os.path.join("static", item)
        dest_path = os.path.join("public", item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, "public")
        else:
            os.mkdir(dest_path)

