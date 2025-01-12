# Unofficial PyMOL Windows Build (Binary Wheel)

This repository offers **unofficial** binary wheels for the open-source version of PyMOL, (including an updated menu stylesheet and an alternative splash screen) tailored for Python on **Windows**.

A convenient one-click installer for Open-Source PyMOL can be downloaded from this repository: [pymol-open-source-windows-setup]()

## About PyMOL

PyMOL™ is a powerful visualization software for rendering and animating 3D molecular structures. PyMOL is a trademark of Schrödinger, LLC.

Please note that the files provided here are **unofficial**. They are informal, unrecognized, and unsupported, offered for testing and evaluation purposes only. No warranty or liability is provided, and the software is made available "as-is."

## Building the Wheel File

To build the wheel file, follow these steps:

1. Set up the build environment by running:
   ```powershell
   .\vendor\taskfile\bin\task.exe setup-build-env
   ```

2. Once the environment is set up, build the wheel file with:
   ```powershell
   .\vendor\taskfile\bin\task.exe poetry-build
   ```

3. After the build process completes, you can find the generated wheel file in the `dist` folder located in the project root.

Feel free to contribute or test the files as needed.
