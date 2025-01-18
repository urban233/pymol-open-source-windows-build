"""
#A* -------------------------------------------------------------------
#B* This file contains source code for building the python package of
#-* the PyMOL computer program
#C* Copyright 2025 by Martin Urban.
#D* -------------------------------------------------------------------
#E* It is unlawful to modify or remove this copyright notice.
#F* -------------------------------------------------------------------
#G* Please see the accompanying LICENSE file for further information.
#H* -------------------------------------------------------------------
#I* Additional authors of this source file include:
#-*
#-*
#-*
#Z* -------------------------------------------------------------------
"""
import os
import pathlib
import shutil
import subprocess

from setuptools import find_packages
from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install
import toml

pyproject_toml = toml.load("pyproject.toml")
PROJECT_NAME = pyproject_toml["project"]["name"]
PROJECT_VERSION = pyproject_toml["project"]["version"]

PROJECT_ROOT_DIR = pathlib.Path(__file__).parent
DEBUG = False  # Debug flag for not cleaning up certain build files.


class CustomInstall(install):
  """Custom command for running pip install ."""

  def copy_pymol_python_sources(self) -> None:
    """Copies the pymol python sources to the src/python directory."""
    tmp_src_path = pathlib.Path(PROJECT_ROOT_DIR / "src/python")
    tmp_pymol_python_src_path = pathlib.Path(PROJECT_ROOT_DIR / "vendor/pymol-open-source/modules")
    if not tmp_src_path.exists():
      tmp_src_path.mkdir(parents=True)
    shutil.copytree(
      tmp_pymol_python_src_path,
      tmp_src_path
    )

  def run(self) -> None:
    """Run method that gets executed if pip install is run."""
    self.run_command("build_ext")
    super().run()
    if not DEBUG:
      shutil.rmtree(pathlib.Path(PROJECT_ROOT_DIR / "src"))


class CMakeBuildExt(build_ext):
  """Custom command to build C++ extension using CMake."""

  def run(self):
    # Run the default build_ext command first
    build_ext.run(self)
    # Then trigger the CMake build
    self.build_cmake_extension()

  def build_cmake_extension(self):
    """Run CMake to build the C++ extension."""
    build_dir = os.path.join(".", "cmake-build-setup_py")
    os.makedirs(build_dir, exist_ok=True)

    # CMake arguments
    cmake_args = [
      "-DCMAKE_TOOLCHAIN_FILE=./vendor/vcpkg/scripts/buildsystems/vcpkg.cmake",
    ]

    # Run CMake to configure and build the extension
    subprocess.check_call(["cmake", PROJECT_ROOT_DIR] + cmake_args, cwd=build_dir)
    subprocess.check_call(["cmake", "--build", build_dir, "--config", "Release"])
    shutil.copytree(
      pathlib.Path(PROJECT_ROOT_DIR / "cmake-build-setup_py/Release"),
      pathlib.Path(PROJECT_ROOT_DIR / 'src/python/pymol'),
      dirs_exist_ok=True
    )


setup(
  name=PROJECT_NAME,  # Name of your package
  version=PROJECT_VERSION,
  packages=find_packages(where='src/python'),  # Looks for packages in src/python
  package_dir={'': 'src/python'},  # src/python as the root for packages
  package_data={"": ["*.*"], "pymol": ["*.*"]},
  ext_modules=[],  # Handled by CMake
  cmdclass={
    "build_ext": CMakeBuildExt,
    "install": CustomInstall
  },
  install_requires=[
    "numpy==1.26.4",
    "toml"
  ]
)
