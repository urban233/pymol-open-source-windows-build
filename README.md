# Unofficial PyMOL Windows Build (Binary Wheel)

This repository offers **unofficial** binary wheels for the open-source version of PyMOL, (including an updated menu stylesheet and an alternative splash screen) tailored for Python on **Windows**.

A convenient one-click installer for Open-Source PyMOL can be downloaded from this repository: [pymol-open-source-windows-setup]()

## About PyMOL

PyMOL™ is a powerful visualization software for rendering and animating 3D molecular structures. PyMOL is a trademark of Schrödinger, LLC.

Please note that the files provided here are **unofficial**. They are informal, unrecognized, and unsupported, offered for testing and evaluation purposes only. No warranty or liability is provided, and the software is made available "as-is."

## Building the Wheel File
### Prerequisites:
- MSBuild
  - Part of [VS 2022](https://visualstudio.microsoft.com/vs/) (incl. Community edition)
- CMake
  - To download the MSI installer click [here](https://github.com/Kitware/CMake/releases/download/v3.31.4/cmake-3.31.4-windows-x86_64.msi)
  - To download the portable version click [here](https://github.com/Kitware/CMake/releases/download/v3.31.4/cmake-3.31.4-windows-x86_64.zip)
  - **Be aware**: Add the cmake.exe to your PATH variable ([short guide](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14))). Check by running `cmake --version`

### Steps to build the wheel file
To build the wheel file, follow these steps (the working directory is the repository root directory):

1. Set up the build environment by running:
   ```powershell
   .\vendor\taskfile\bin\task.exe setup-build-env
   ```

2. Once the environment is set up and **activated**, build the wheel file with:
   ```powershell
   python .\run_automation.py build-wheel 
   ```
    or if the environment is not activated run:
    ```powershell
    .\.venv\Scripts\python.exe .\run_automation.py build-wheel
    ```

3. After the build process completes, you can find the generated wheel file in the `dist` folder located in the project root.

Feel free to contribute or test the files as needed.
