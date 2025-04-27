# import os
# import shutil

# def flatten():
#     project_dir = os.getcwd()  # .../demo
#     parent = os.path.dirname(project_dir)  # one level up
#     for name in os.listdir(project_dir):
#         src = os.path.join(project_dir, name)
#         dst = os.path.join(parent, name)
#         # skip if somehow already exists
#         if os.path.exists(dst):
#             continue
#         shutil.move(src, dst)
#     # go up and remove the empty demo/ folder
#     os.chdir(parent)
#     shutil.rmtree(project_dir)

# if __name__ == "__main__":
#     flatten()
