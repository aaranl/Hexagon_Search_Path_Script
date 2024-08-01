# PC-DMIS Search Paths Management Script

This script is designed to manage search paths and tool data files for PC-DMIS installations. It provides functionalities to:

1. Delete specific `.dat` files (`Tool.dat`) from designated directories.
2. Save the current search paths from `UserSettings.json` files.
3. Restore previously saved search paths.

## Usage

### Prerequisites

- Ensure Python is installed on your system.
- Install the `send2trash` library if it's not already installed. You can install it via pip:
  ```sh
  pip install send2trash
  ```

### How to Run

1. **Clone or download the script to your local machine.**

2. **Navigate to the directory containing the script in your terminal or command prompt.**

3. **Run the script:**
   ```sh
   python script_name.py
   ```

### Options

Upon running the script, you will be prompted to select an operation:

1. **Set Search Paths:** This option will delete specific `.dat` files and save the current search paths from `UserSettings.json` files.
2. **Restore Search Paths:** This option will restore the search paths to their previously saved state.


