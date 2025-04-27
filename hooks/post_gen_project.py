import os
import shutil
import time

def flatten():
    project_dir = os.getcwd()  # e.g., .../demo
    parent = os.path.dirname(project_dir)  # one level up

    os.chdir(parent)  # Change dir BEFORE trying to delete anything

    # Move everything up first
    for name in os.listdir(project_dir):
        src = os.path.join(project_dir, name)
        dst = os.path.join(parent, name)
        if os.path.exists(dst):
            continue
        shutil.move(src, dst)

    # Try to delete the project_dir with retries
    max_attempts = 10
    delay_seconds = 0.5

    for attempt in range(1, max_attempts + 1):
        try:
            shutil.rmtree(project_dir)
            print(f"✅ Successfully deleted {project_dir}")
            break
        except PermissionError:
            print(f"⚠️ Attempt {attempt}: Folder is still locked. Waiting {delay_seconds}s...")
            time.sleep(delay_seconds)
    else:
        print(f"❌ Failed to delete {project_dir} after {max_attempts} attempts.")

if __name__ == "__main__":
    flatten()
