import os
import shutil

def recurse_static(src, dst):
    dirlist = os.listdir(src)
    for content in dirlist:
        src_path = os.path.join(src, content)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst)
        else:
            dst_path = os.path.join(dst, content)
            os.mkdir(dst_path)
            recurse_static(src_path, dst_path)

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    recurse_static(src, dst)

def main():
    copy_static("./static", "./public")

main()


