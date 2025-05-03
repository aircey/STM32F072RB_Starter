#!/usr/bin/python3

import os
import re
import shutil

def validate_project_name(name):
    return re.match(r'^[A-Za-z0-9_-]+$', name) is not None

def replace_in_file(filepath, old, new):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    project_name = input("Please enter project name: ").strip()

    if not validate_project_name(project_name):
        print("Invalid project name. Only letters, numbers, hyphens, and underscores are allowed.")
        return

    files_to_edit = ["CMakeLists.txt", "STM32F072RB_Starter.ioc"]

    for file in files_to_edit:
        if os.path.exists(file):
            replace_in_file(file, "STM32F072RB_Starter", project_name)
            print(f"Updated {file}")
        else:
            print(f"{file} not found.")

    # Rename .ioc file
    old_ioc = "STM32F072RB_Starter.ioc"
    new_ioc = f"{project_name}.ioc"
    if os.path.exists(old_ioc):
        os.rename(old_ioc, new_ioc)
        print(f"Renamed {old_ioc} to {new_ioc}")

    # Ask to delete .git directory
    delete_git = input("Do you want to delete the existing git setup? (y/n): ").strip().lower()
    if delete_git == 'y':
        if os.path.isdir(".git"):
            shutil.rmtree(".git")
            print(".git directory deleted.")
        else:
            print(".git directory not found.")

    # Ask to rename current directory
    rename_folder = input("Do you want to rename the current folder to the project name? (y/n): ").strip().lower()
    if rename_folder == 'y':
        current_dir = os.path.basename(os.getcwd())
        parent_dir = os.path.dirname(os.getcwd())
        new_dir_path = os.path.join(parent_dir, project_name)

        if current_dir != project_name:
            os.rename(os.getcwd(), new_dir_path)
            print(f"Renamed folder to {project_name}.")
        else:
            print("Current folder already has the project name.")

if __name__ == "__main__":
    main()
