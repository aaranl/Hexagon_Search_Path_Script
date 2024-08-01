import os
import json
import pickle


def delete_tool_dat_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("Tool.dat"):
                file_path = os.path.join(root, file)
                try:
                    send2trash(file_path)
                    print(f"Sent to trash: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

def modify_json_files(directory):

    original_paths = {}
    looking_for = {"PostOutPath","PostInPath", "LoadProbeUserSearchDirectory", "RecallAlignUserSearchDirectory", "SubroutineUserSearchDirectory", "DefaultPartProgram"}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("UserSettings.json"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8-sig') as f:
                    data = json.load(f)

                file_original_paths = {}

                for item in data:
                    entry = item.get('Entry')
                    if 'DefaultValues' in item and item.get('Entry') in looking_for:
                        original_path = item['DefaultValues'][0]
                        file_original_paths[entry] = original_path

                original_paths[file_path] = file_original_paths

    with open('original_paths.pkl', 'wb') as f:
        pickle.dump(original_paths, f)

    print("Original paths have been saved. You can restore them later.")

def restore_search_paths():
    if not os.path.exists('original_paths.pkl'):
        print("No saved original paths found.")
        return

    with open('original_paths.pkl', 'rb') as f:
        original_paths = pickle.load(f)

    for file_path, file_original_paths in original_paths.items():
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)

            modified = False

            for item in data:
                entry = item.get('Entry')
                if entry in file_original_paths and 'DefaultValues' in item:
                    item['DefaultValues'][0] = file_original_paths[entry]
                    modified = True
                    print(f"Restored {entry} in {file_path}")
                    print(f"Restored value: {file_original_paths[entry]}")

            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
        else:
            print(f"Warning: File {file_path} no longer exists.")

    print("Restoration complete.")
    
def set_search_paths():
    user = os.getlogin()
    filepath1 = "C:\\ProgramData\\Hexagon\\PC-DMIS"
    filepath2 = os.path.join("C:\\Users", user, "AppData", "Local", "Hexagon", "PC-DMIS")
    delete_tool_dat_files(filepath1)
    modify_json_files(filepath2)

if __name__ == "__main__":
    choice = int(input("Select Operations \n 1. set_search_paths \n 2. restore_search_paths\n"))
    if choice == 1:
        set_search_paths()
    if choice == 2:
        restore_search_paths()