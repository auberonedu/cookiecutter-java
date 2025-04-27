import os
import shutil
import gc

def flatten():
    project_dir = os.getcwd()  # .../demo
    parent = os.path.dirname(project_dir)  # one level up

    for name in os.listdir(project_dir):
        src = os.path.join(project_dir, name)
        dst = os.path.join(parent, name)
        if os.path.exists(dst):
            continue
        shutil.move(src, dst)

    os.chdir(parent)

    # Commenting out for now because it ain't working with the file locks
    # Will handle in the utility script instead
    #shutil.rmtree(project_dir)


if __name__ == "__main__":
    flatten()
