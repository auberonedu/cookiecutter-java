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

    gc.collect()  # Force Python to clean up handles

    try:
        shutil.rmtree(project_dir)
    except PermissionError:
        pass  # Ignore if still locked

if __name__ == "__main__":
    flatten()
