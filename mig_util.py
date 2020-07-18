import shutil
import sys
import os

def remove_migs(project_folder, app_folder):
    CACHE_TARGET = "__pycache__"
    MIGRATIONS_TARGET = "migrations"
    DB_TARGET = "db.sqlite3"

    targets = [CACHE_TARGET, MIGRATIONS_TARGET]
    if os.path.exists(project_folder):
        sys.stdout.write(f"[+] Project folder {project_folder} detected \n".format())
        os.chdir(project_folder)
        for tgt in targets:
            if os.path.exists(tgt):
                shutil.rmtree(tgt, ignore_errors=True)

            else:
                print("[!] Path not located")
                continue 

    else:
        sys.stdout.write(f"[!] Project folder {project_folder} not found".format())

    os.chdir("..")
    if os.path.exists(app_folder):
        sys.stdout.write(f"[+] App folder {app_folder} detected \n".format())
        os.chdir(app_folder)
        for tgt in targets:
            if os.path.exists(tgt):
                shutil.rmtree(tgt, ignore_errors=True)

            else:
                print("[!] Path not located")
                continue 

    else:
        sys.stdout.write(f"[!] App folder {app_folder} not found \n".format())

    os.chdir("..")
    if os.path.isfile(DB_TARGET):
        os.remove(DB_TARGET)

    else:
        print(f"[!] {DB_TARGET} not found")


project_folder = input("Django Project Folder > ")
app_folder = input("Django App Folder > ")

remove_migs(project_folder, app_folder)