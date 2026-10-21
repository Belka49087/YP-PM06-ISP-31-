# User Manual for Information System Operation

## 1. Brief Program Description
The developed software system is a specialized console-graphical application written in Python, designed for high-precision modeling and forecasting of storage capacity and transaction workload on server equipment. The application allows computing the values of arithmetic and geometric progression members in either automatic or interactive modes based on the initial sequence parameters provided by the user. The program features an autonomous maintenance subsystem that ensures reliable serialization of configuration profiles and implements algorithms for their regular backup and emergency recovery during information system failures.

## Technologies
* Python 3.8+ — Core programming language
* Tkinter — Graphical User Interface (GUI)
* JSON — Text format for data exchange and storing parameter profiles
* Shutil and OS — Maintenance, backup, and file system operations modules
* Unittest — Framework for automated module testing

## 2. Installation Guide

### System Requirements:
* Operating System: Windows 10/11, macOS, or Linux distributions.
* Interpreter: Python runtime environment version 3.8 or higher.
* Access Rights: Permission to write files to the target project directory.

### Step-by-Step Installation Process:
1. Download three source code files (ispolnitelnie.py, graficheskie.py, functionalnie.py) from the repository.
2. Place all three files into a single working folder on your computer's drive (it is recommended to use a path without spaces or Cyrillic characters, for example: C:\praktika\).
3. Open the terminal or Windows Command Prompt in the created directory containing the files.
4. Verify that the Python interpreter is available in the system by running the following command:
   ```bash
   python --version
   ```
   *No additional installation of third-party libraries or packages is required.*

## Project Structure
```text
praktika/
├── functionalnie.py  # Core module for calculations, serialization, and backup
├── graficheskie.py   # Tkinter graphical shell and localization dictionaries (RU/EN)
├── ispolnitelnie.py  # Main executable module (system launch file)
├── test_prog.py      # Automated unit tests for code verification
├── TZ.md             # Technical Specifications (Customer C-requirements)
└── README_EN.md      # User Documentation (User Manual in English)
```

## 3. Usage Guide

### Information System Launch:
To initialize the information system, run the launch command of the main executable module in your terminal:
```bash
python ispolnitelnie.py
```
The graphical application window will open on the screen. If necessary, you can switch the interface language using the drop-down list in the upper right corner (RU/EN).

### Interactive Calculation in the GUI Window:
1. Select the progression type radio button (Arithmetic or Geometric).
2. Enter numeric parameter values into the corresponding fields of the form:
   * **First member (a1/b1)** — initial volume or workload level.
   * **Step or denominator (d/q)** — data change intensity.
   * **Element number (n)** — forecasting depth (an integer greater than 0).
3. Click the **"Compute"** button to immediately display the resulting value in the output field.
4. Click the **"Save Profile"** button to record the current parameters into the persistent local database for future reuse.

### Batch Processing Mode for JSON Files:
1. Click the **"Batch File Process"** button.
2. In the opened system explorer window, select the input parameter configuration file (for example, `input.json`).
3. In the next dialog window, specify the path and filename to save the results (for example, `output.json`). The computations will run in an automated background mode.

### Administrative Maintenance Regulations (Backup):
* **Recovery Point Creation:** Click the **"Create Backup Point"** button. The subsystem will automatically copy the profile database into an isolated `backups/` directory with a unique system date and time stamp.
* **Emergency Restore:** In case of accidental deletion or corruption of the active configuration, click the **"Restore from Backup"** button. The system will independently find the latest stable archive and restore the information system to a working state.

**Developer:** Alexandrov S. S.
