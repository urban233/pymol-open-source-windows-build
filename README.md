# Unofficial PyMOL Windows Build (Binary Wheel)

This repository offers **unofficial** binary wheels for the open-source version of PyMOL, (including an updated menu stylesheet and an alternative splash screen) tailored for Python on **Windows**.

A convenient one-click installer for Open-Source PyMOL can be downloaded from this repository: [pymol-open-source-windows-setup](https://github.com/kullik01/pymol-open-source-windows-setup.git)

## About PyMOL

[PyMOL™](https://pymol.org/) is a powerful visualization software for rendering and animating 3D molecular structures. PyMOL is a trademark of Schrödinger, LLC.

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
   .\setup_dev_env.bat
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
(Until now the wheel file has a wrong filename containing _none_ and _any_ but is only for **Windows x64**.)

Feel free to contribute or test the files as needed.

## Acknowledgements
**Schrödinger** for being the driving force behind the continued development of PyMOL after Warren's passing, ensuring that the open-source version remained alive and well. 

**NOTE**: the following list has been **created by 
Warren himself** and has not been updated since Fall 2003.  

Since then, the PyMOL effort has grown to such an extent that it is no longer
practical to recognize everyone individually. Fortunately, a public
record of participation exists and can be appreciated on the internet,
and especially via the PyMOL mailing list archives.  Suffice it to say
that the PyMOL user community now numbers well into the thousands and
includes scientists, students, and educators worldwide, spread
throughout academia and the biotechnology and pharmaceutical
industries.  Though DeLano Scientific LLC specifically supports and
maintains the PyMOL code base, the project can only continue to
succeed through the sponsorship and participation of the broader
community.

**Founder and Principal Author**:

      Warren L. DeLano 

Major Authors (5000+ lines of code):

      Ralf W. Grosse-Kunstleve (SGLite Module)

Minor Authors (500+ lines of code):

      Scott Dixon (Metaphorics CEX support)
      Filipe Maia (Slice Objects)

Other Contributors: These are the people who have gone out of
their way to help the project with their ideas, actions,
advice, hardware donations, testing, information, sponsorship,
peer support, or code snippets.

      Daan van Aalten
      Paul Adams 
      Stephen Adler
      Jun Aishima 
      Dennis Allison
      Ricardo Aparicio
      Daniel Appelman   
      Diosdado "Rey" Banatao
      Michael Banck
      Ulrich Baumann
      Joseph Becker
      Balaji Bhyravbhatla
      Jeff Bizzaro
      Jeff Blaney 
      Juergen Bosch 
      Michael Bower
      Sarina Bromberg
      Axel Brunger
      Robert Campbell
      Bronwyn Carlisle 
      Duilio Cascio
      Julien Chiron 
      Shawn Christensen
      Scott Classen
      David Cooper
      Larry Coopet
      Jacob Corn
      Ben Cornett
      Andrew Dalke 
      Koen van der Drift 
      Harry Dailey
      Byron DeLaBarre
      Bill DeGrado
      Thomas Earnest
      Nathaniel Echols
      John Eksterowicz
      Erik Evensen
      David Fahrney
      Tim Fenn
      Thierry Fischmann
      Michael Ford
      Esben Peter Friis
      Kevin Gardner
      R. Michael Garavito
      John Gerig
      Jonathan Greene
      Michael Goodman  
      Joel Harp
      Reece Hart
      Richard Hart
      Peter Haebel
      Matt Henderson
      Douglas Henry 
      Possu Huang 
      Uwe Hoffmann
      Jenny Hinshaw
      Carly Huitema
      Bjorn Kauppi
      Greg Landrum
      Robert Lawrence Kehrer 
      Tom Lee
      Eugen Leitl
      Ken Lind
      Jules Jacobsen
      Luca Jovine
      Andrey Khavryuchenko
      David Konerding
      Greg Landrum
      Michael Love 
      Tadashi Matsushita
      Genevieve Matthews 
      Gerry McDermott 
      Robert McDowell
      Gustavo Mercier      
      Naveen Michaud-Agrawal
      Aaron Miller
      Holly Miller
      Tim Moore
      Kelley Moremen
      Hideaki Moriyama
      Nigel Moriarty 
      Geoffrey Mueller
      Cameron Mura
      Florian Nachon 
      Hanspeter Niederstrasser 
      Michael Nilges
      Hoa Nguyen
      Shoichiro Ono
      Chris Oubridge
      Andre Padilla
      Jay Pandit
      Ezequiel "Zac" Panepucci
      Robert Phillips
      Hans Purkey
      Rama Ranganathan
      Michael Randal
      Daniel Ricklin 
      Ian Robinson
      Eric Ross
      Kristian Rother
      Marc Saric
      Bill Scott
      Keana Scott
      Denis Shcherbakov
      Goede Schueler
      Paul Sherwood
      Ward Smith
      John Somoza
      David van der Spoel
      Paul Sprengeler
      Matt Stephenson 
      Peter Stogios
      John Stone
      Charlie Strauss
      Michael Summers
      Brian Sutton
      Hanna and Abraham Szoke
      Rod Tweten
      Andras Varadi
      Scott Walsh
      Pat Walters
      Mark White
      Michael Wilson
      Dave Weininger
      Chris Wiesmann
      Charles Wolfus
      Richard Xie

Miscellaneous Code Snippets Lifted From:

      Thomas Malik (fast matrix-multiply code)
      John E. Grayson (Author of "Python and Tkinter")
      Doug Hellmann (Wrote code that JEG later modified.)

Open-Source "Enablers" (essential, but not directly involved):

      Brian Paul (Mesa)
      Mark Kilgard (GLUT)
      Guido van Rossum (Python)
      Linus Torvalds (Linux Kernel)

      Precision Insight (DRI)
      The XFree86 Project (Free Windowing System)
      VA Linux (CVS Hosting)
      Richard Stallman/Free Software Foundation (GNU Suite)
      The unknown authors of EISPACK (Linear Algebra)

Graphics Technology "Enablers" (essential!)

      3dfx (RIP)
      nVidia 
      ATI

### Specific Acknowledgments:

* Thanks to Joni W. Lam for making the business work.

* Thanks to John Stone and John Furr for being such excellent
  colleagues.

* Thanks to Ragu Bharadwaj and Marcin Joachimiak for Java expertise
  and encouragement.

* Thanks to Apple Computer for continued encouragement, assistance,
  and HLAs in support of Mac development.  Thanks especially to
  Robert Kehrer for creating so many fun opportunities over the years.

* Thanks to Aaron Miller (GlaxoSmithKline) for a continuous stream of
  thoughtful opinions and suggestions.

* Thanks to Dave Weininger for suggesting the "roving" feature and for
  being such an inspirational friend and mentor.

* Thanks to Matt Hahn and Dave Rogers for proving that it can also be
  done, again.

* Thanks to Mick Savage for providing experienced practical advice on
  the marketing of scientific software.

* Thanks to Ian Matthew for 3D experience and perspective.

* Thanks for Jeff Blaney for numerous insightful discussions.

* Thanks to Elizabeth Pehrson for making this a team effort.

* Thanks to Erin Bradley for schooling in focus and vision.

* Thanks to Vera Povolona for catalytic clarity and introspection.

* Thanks to Anthony Nichols for proving that it can be done, yet again.

* Thanks to Thompson Doman for timely Open-Source validation.

* Thanks to Manfred Sippl for making it all seem so simple.

* Thanks to Kristian Rother for all his excellent work building on the
  PyMOL foundation, and in helping others learn to use the software.

* Thanks to Dave Weininger, Scott Dixon, Roger Sayle, Andrew Dalke,
  Anthony Nichols, Dick Cramer, and David Miller, as well as rest of
  the Daylight and OpenEye teams for thoughtful discussions on PyMOL
  and open-source software during my 2002 pilgrimage to Sante Fe, NM.

* Thanks to Ralf Grosse-Kunstleve for his contribution of the "sglite"
  space group and symmetry handling module.

* Thanks to the scientists and management of Sunesis Pharmaceuticals
  for supporting PyMOL development since program inception.

* Thanks to the Computational Crystallography Initiative (LBNL)
  developers for their encouragement, ideas, and support.

* Thanks to Scott Walsh for being the first individual to provide
  financial support for PyMOL.

* Thanks to the hundreds of individuals, companies, and institutions
  that have provided financial support for the project.

* Thanks to Brian Paul and the Precision Insight team for development
  of Mesa/DRI which greatly assisted in the early development of PyMOL.

* Thanks to Michael Love for the first major outside port of PyMOL
  (to GNU-Darwin/OSX) and for believing in the cause.

* Thanks for Paul Sherwood for making a concerted effort to develop
  using PyMOL long before the software and vision had matured.

* Thanks to Jay Ponder for thoughtful email discussions on Tinker and
  the role of open-source scientific software.

* Thanks to hundreds of PyMOL users for the many forms of feedback,
  bug sightings, and encouragement they've provided.