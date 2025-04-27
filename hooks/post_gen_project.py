import os
import shutil

def flatten():
    project_dir = os.getcwd()  # .../demo
    parent = os.path.dirname(project_dir)  # one level up

    os.chdir(parent)  # <-- Move up immediately to avoid lock!

    for name in os.listdir(project_dir):
        src = os.path.join(project_dir, name)
        dst = os.path.join(parent, name)
        # skip if somehow already exists
        if os.path.exists(dst):
            continue
        shutil.move(src, dst)

    shutil.rmtree(project_dir)  # Now safe to delete

if __name__ == "__main__":
    flatten()
