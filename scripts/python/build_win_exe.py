import os
import pathlib
import shutil
import zipfile

from cx_Freeze import Freezer, Executable

FILE_ROOT_PATH = pathlib.Path(__file__).parent

# Define the entry point of your application
executable = Executable(
  script="pymol/__init__.py",  # Replace with your script name
  target_name="Open-Source-PyMOL.exe",  # Optional: Set the name of the .exe file
  #base="Win32GUI",  # Uncomment to suppress command window
  icon=pathlib.Path(FILE_ROOT_PATH.parent / "alternative_design" / "logo.ico")
)

# Create a freezer instance
freezer = Freezer(
  executables=[executable],
  includes=[
    "PyQt5.uic", "pymol.povray", "pymol.parser"
  ],
  excludes=[],  # Exclude unnecessary modules
  include_files=[],  # Include additional files
  zip_exclude_packages=[]
)


def remove_dist_info_folders(directory: pathlib.Path):
  """
  Remove all folders ending with .dist-info from the specified directory.

  Args:
      directory (str): The path to the directory to search.
  """
  for root, dirs, files in os.walk(str(directory)):
    for dir_name in dirs:
      if dir_name.endswith(".dist-info"):
        dist_info_path = os.path.join(root, dir_name)
        shutil.rmtree(dist_info_path)


if __name__ == '__main__':
  freezer.freeze()
  with zipfile.ZipFile(pathlib.Path(f"{FILE_ROOT_PATH}/build/exe.win-amd64-3.11/lib/library.zip"), 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path(f"{FILE_ROOT_PATH}/build/exe.win-amd64-3.11/lib"))
  _CMD_FROM_BUILD_DIR = pathlib.Path(FILE_ROOT_PATH.parent / "buildDir" / "_cmd.cp311-win_amd64.pyd")
  _CMD_FROM_PRE_BUILT_DIR = pathlib.Path(FILE_ROOT_PATH.parent / "pre-built" / "_cmd.cp311-win_amd64.pyd")
  if _CMD_FROM_BUILD_DIR.exists():
    shutil.copy(
      _CMD_FROM_BUILD_DIR,
      pathlib.Path(FILE_ROOT_PATH / "build/exe.win-amd64-3.11/lib/pymol" / "_cmd.cp311-win_amd64.pyd")
    )
  else:
    shutil.copy(
      _CMD_FROM_PRE_BUILT_DIR,
      pathlib.Path(FILE_ROOT_PATH / "build/exe.win-amd64-3.11/lib/pymol" / "_cmd.cp311-win_amd64.pyd")
    )
  remove_dist_info_folders(pathlib.Path(FILE_ROOT_PATH / "build/exe.win-amd64-3.11/lib"))
  shutil.copytree(
    str(pathlib.Path(FILE_ROOT_PATH / "pymol/wizard")),
    str(pathlib.Path(FILE_ROOT_PATH / "build/exe.win-amd64-3.11/lib/pymol/wizard")),
    dirs_exist_ok=True
  )
  shutil.copytree(
    str(pathlib.Path(FILE_ROOT_PATH / "pymol/data/startup")),
    str(pathlib.Path(FILE_ROOT_PATH / "build/exe.win-amd64-3.11/lib/pymol/data/startup")),
    dirs_exist_ok=True
  )
