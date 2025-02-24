![calculator] (preview.png)
# Getting Started

## Running the Application
To start the application, use the following command:
```bash
py .\main.py
```

## Editing the UI
If you need to edit the user interface, open the `calc3.ui` file using Qt Designer. After making changes, you can convert the updated UI file into Python code with the following command:
```bash
pyuic5 calc3.ui -o calc3.py
```
This command generates a Python file from the `.ui` file, allowing it to be used in the project.

## Converting PNG to QRC
If your project includes PNG images that need to be converted into a Qt resource file (`.qrc`), you can use the following command:
```bash
pyrcc5 filename.qrc -o filename_rc.py
```
This converts the `.qrc` file into a Python file that can be imported and used within the application.

## Required Dependencies
Before running the commands above, ensure that the following dependencies are installed:

- **Python** (Make sure Python is installed and added to your system's PATH.)
- **PyQt5** (Required for working with Qt Designer and converting UI files.) You can install it using:
  ```bash
  pip install PyQt5
  ```
- **PyQt5-tools** (Includes Qt Designer and other utilities.) Install it with:
  ```bash
  pip install PyQt5-tools
  ```
- **pyrcc5** (For converting `.qrc` files to Python.) If it's not available, install it with:
  ```bash
  pip install pyqt5-tools
  ```

With these dependencies installed, you will be able to run, edit, and modify the UI components of the application smoothly.

