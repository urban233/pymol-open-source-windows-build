cmake_minimum_required(VERSION 3.13)
set(VCPKG_TARGET_TRIPLET x64-windows-static)

project(_cmd)

set(CMAKE_VERBOSE_MAKEFILE on)

set(ALL_SRC
        vendor/pymol-open-source/build/generated/ShaderText.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/PlugIOManagerInit.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/abinitplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/avsplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/basissetplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/bgfplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/binposplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/biomoccaplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/brixplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/carplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/ccp4plugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/corplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/crdplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/cubeplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dcdplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dlpolyplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dsn6plugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dtrplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dxplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/edmplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/fs4plugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/gamessplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/graspplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/grdplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/gridplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/gromacsplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/hash.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/inthash.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/jsplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/maeffplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/mapplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/mdfplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/mol2plugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/moldenplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/molemeshplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/msmsplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/namdbinplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/netcdfplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/offplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/parm7plugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/parmplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pbeqplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pdbplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pdbxplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/phiplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pltplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/plyplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pqrplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/psfplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/raster3dplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/rst7plugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/situsplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/spiderplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/stlplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/tinkerplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/uhbdplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vasp5xdatcarplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspchgcarplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspoutcarplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspparchgplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspposcarplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspxdatcarplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspxmlplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vtfplugin.c
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vtkplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/xbgfplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/xsfplugin.cpp
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/xyzplugin.c
        vendor/pymol-open-source/layer0/Bezier.cpp
        vendor/pymol-open-source/layer0/Block.cpp
        vendor/pymol-open-source/layer0/CarveHelper.cpp
        vendor/pymol-open-source/layer0/ContourSurf.cpp
        vendor/pymol-open-source/layer0/Crystal.cpp
        vendor/pymol-open-source/layer0/Err.cpp
        vendor/pymol-open-source/layer0/Feedback.cpp
        vendor/pymol-open-source/layer0/Field.cpp
        vendor/pymol-open-source/layer0/File.cpp
        vendor/pymol-open-source/layer0/GFXManager.cpp
        vendor/pymol-open-source/layer0/GenericBuffer.cpp
        vendor/pymol-open-source/layer0/GraphicsUtil.cpp
        vendor/pymol-open-source/layer0/Isosurf.cpp
        vendor/pymol-open-source/layer0/Map.cpp
        vendor/pymol-open-source/layer0/Match.cpp
        vendor/pymol-open-source/layer0/Matrix.cpp
        vendor/pymol-open-source/layer0/MemoryDebug.cpp
        vendor/pymol-open-source/layer0/MemoryUsage.cpp
        vendor/pymol-open-source/layer0/MyPNG.cpp
        vendor/pymol-open-source/layer0/Parse.cpp
        vendor/pymol-open-source/layer0/Pixmap.cpp
        vendor/pymol-open-source/layer0/PostProcess.cpp
        vendor/pymol-open-source/layer0/PrintUtils.cpp
        vendor/pymol-open-source/layer0/ShaderMgr.cpp
        vendor/pymol-open-source/layer0/ShaderPreprocessor.cpp
        vendor/pymol-open-source/layer0/ShaderPrg.cpp
        vendor/pymol-open-source/layer0/Sphere.cpp
        vendor/pymol-open-source/layer0/TTT.cpp
        vendor/pymol-open-source/layer0/Tetsurf.cpp
        vendor/pymol-open-source/layer0/Texture.cpp
        vendor/pymol-open-source/layer0/Tracker.cpp
        vendor/pymol-open-source/layer0/Triangle.cpp
        vendor/pymol-open-source/layer0/Util.cpp
        vendor/pymol-open-source/layer0/Util2.cpp
        vendor/pymol-open-source/layer0/Vector.cpp
        vendor/pymol-open-source/layer0/Word.cpp
        vendor/pymol-open-source/layer0/ccealignmodule.cpp
        vendor/pymol-open-source/layer0/marching_cubes.cpp
        vendor/pymol-open-source/layer0/os_gl.cpp
        vendor/pymol-open-source/layer1/Basis.cpp
        vendor/pymol-open-source/layer1/ButMode.cpp
        vendor/pymol-open-source/layer1/CGO.cpp
        vendor/pymol-open-source/layer1/CGOGL.cpp
        vendor/pymol-open-source/layer1/CGORenderer.cpp
        vendor/pymol-open-source/layer1/COLLADA.cpp
        vendor/pymol-open-source/layer1/Camera.cpp
        vendor/pymol-open-source/layer1/Character.cpp
        vendor/pymol-open-source/layer1/Color.cpp
        vendor/pymol-open-source/layer1/Control.cpp
        vendor/pymol-open-source/layer1/Extrude.cpp
        vendor/pymol-open-source/layer1/Font.cpp
        vendor/pymol-open-source/layer1/FontGLUT.cpp
        vendor/pymol-open-source/layer1/FontGLUT8x13.cpp
        vendor/pymol-open-source/layer1/FontGLUT9x15.cpp
        vendor/pymol-open-source/layer1/FontGLUTHel10.cpp
        vendor/pymol-open-source/layer1/FontGLUTHel12.cpp
        vendor/pymol-open-source/layer1/FontGLUTHel18.cpp
        vendor/pymol-open-source/layer1/FontType.cpp
        vendor/pymol-open-source/layer1/Movie.cpp
        vendor/pymol-open-source/layer1/Ortho.cpp
        vendor/pymol-open-source/layer1/P.cpp
        vendor/pymol-open-source/layer1/PConv.cpp
        vendor/pymol-open-source/layer1/Picking.cpp
        vendor/pymol-open-source/layer1/Pop.cpp
        vendor/pymol-open-source/layer1/PyMOLObject.cpp
        vendor/pymol-open-source/layer1/Ray.cpp
        vendor/pymol-open-source/layer1/Rep.cpp
        vendor/pymol-open-source/layer1/Scene.cpp
        vendor/pymol-open-source/layer1/SceneMouse.cpp
        vendor/pymol-open-source/layer1/ScenePicking.cpp
        vendor/pymol-open-source/layer1/SceneRay.cpp
        vendor/pymol-open-source/layer1/SceneRender.cpp
        vendor/pymol-open-source/layer1/SceneView.cpp
        vendor/pymol-open-source/layer1/ScrollBar.cpp
        vendor/pymol-open-source/layer1/Seq.cpp
        vendor/pymol-open-source/layer1/Setting.cpp
        vendor/pymol-open-source/layer1/Shaker.cpp
        vendor/pymol-open-source/layer1/SymOp.cpp
        vendor/pymol-open-source/layer1/SymOpPConv.cpp
        vendor/pymol-open-source/layer1/SymOpTools.cpp
        vendor/pymol-open-source/layer1/Symmetry.cpp
        vendor/pymol-open-source/layer1/Text.cpp
        vendor/pymol-open-source/layer1/TypeFace.cpp
        vendor/pymol-open-source/layer1/View.cpp
        vendor/pymol-open-source/layer1/Wizard.cpp
        vendor/pymol-open-source/layer2/AssemblyHelpers.cpp
        vendor/pymol-open-source/layer2/AtomInfo.cpp
        vendor/pymol-open-source/layer2/AtomInfoHistory.cpp
        vendor/pymol-open-source/layer2/BondTypeHistory.cpp
        vendor/pymol-open-source/layer2/CifFile.cpp
        vendor/pymol-open-source/layer2/CifMoleculeReader.cpp
        vendor/pymol-open-source/layer2/CoordSet.cpp
        vendor/pymol-open-source/layer2/DistSet.cpp
        vendor/pymol-open-source/layer2/GadgetSet.cpp
        vendor/pymol-open-source/layer2/HydrogenAdder.cpp
        vendor/pymol-open-source/layer2/MmodTyping.cpp
        vendor/pymol-open-source/layer2/MmtfMoleculeReader.cpp
        vendor/pymol-open-source/layer2/Mol2Typing.cpp
        vendor/pymol-open-source/layer2/MolV3000.cpp
        vendor/pymol-open-source/layer2/ObjectAlignment.cpp
        vendor/pymol-open-source/layer2/ObjectCGO.cpp
        vendor/pymol-open-source/layer2/ObjectCallback.cpp
        vendor/pymol-open-source/layer2/ObjectCurve.cpp
        vendor/pymol-open-source/layer2/ObjectDist.cpp
        vendor/pymol-open-source/layer2/ObjectGadget.cpp
        vendor/pymol-open-source/layer2/ObjectGadgetRamp.cpp
        vendor/pymol-open-source/layer2/ObjectGroup.cpp
        vendor/pymol-open-source/layer2/ObjectMap.cpp
        vendor/pymol-open-source/layer2/ObjectMesh.cpp
        vendor/pymol-open-source/layer2/ObjectMolecule.cpp
        vendor/pymol-open-source/layer2/ObjectMolecule2.cpp
        vendor/pymol-open-source/layer2/ObjectMolecule3.cpp
        vendor/pymol-open-source/layer2/ObjectSlice.cpp
        vendor/pymol-open-source/layer2/ObjectSurface.cpp
        vendor/pymol-open-source/layer2/ObjectVolume.cpp
        vendor/pymol-open-source/layer2/RepAngle.cpp
        vendor/pymol-open-source/layer2/RepCartoon.cpp
        vendor/pymol-open-source/layer2/RepCylBond.cpp
        vendor/pymol-open-source/layer2/RepDihedral.cpp
        vendor/pymol-open-source/layer2/RepDistDash.cpp
        vendor/pymol-open-source/layer2/RepDistLabel.cpp
        vendor/pymol-open-source/layer2/RepDot.cpp
        vendor/pymol-open-source/layer2/RepEllipsoid.cpp
        vendor/pymol-open-source/layer2/RepLabel.cpp
        vendor/pymol-open-source/layer2/RepMesh.cpp
        vendor/pymol-open-source/layer2/RepNonbonded.cpp
        vendor/pymol-open-source/layer2/RepNonbondedSphere.cpp
        vendor/pymol-open-source/layer2/RepRibbon.cpp
        vendor/pymol-open-source/layer2/RepSphere.cpp
        vendor/pymol-open-source/layer2/RepSphereGenerate.cpp
        vendor/pymol-open-source/layer2/RepSphereImmediate.cpp
        vendor/pymol-open-source/layer2/RepSurface.cpp
        vendor/pymol-open-source/layer2/RepWireBond.cpp
        vendor/pymol-open-source/layer2/Sculpt.cpp
        vendor/pymol-open-source/layer2/SculptCache.cpp
        vendor/pymol-open-source/layer2/SideChainHelper.cpp
        vendor/pymol-open-source/layer2/VFont.cpp
        vendor/pymol-open-source/layer3/AtomIterators.cpp
        vendor/pymol-open-source/layer3/CifDataValueFormatter.cpp
        vendor/pymol-open-source/layer3/Editor.cpp
        vendor/pymol-open-source/layer3/Executive.cpp
        vendor/pymol-open-source/layer3/ExecutivePython.cpp
        vendor/pymol-open-source/layer3/Interactions.cpp
        vendor/pymol-open-source/layer3/MaeExportHelpers.cpp
        vendor/pymol-open-source/layer3/MoleculeExporter.cpp
        vendor/pymol-open-source/layer3/MovieScene.cpp
        vendor/pymol-open-source/layer3/PlugIOManager.cpp
        vendor/pymol-open-source/layer3/RingFinder.cpp
        vendor/pymol-open-source/layer3/Seeker.cpp
        vendor/pymol-open-source/layer3/Selector.cpp
        vendor/pymol-open-source/layer3/SelectorTmp.cpp
        vendor/pymol-open-source/layer3/SpecRec.cpp
        vendor/pymol-open-source/layer3/SpecRecSpecial.cpp
        vendor/pymol-open-source/layer4/Cmd.cpp
        vendor/pymol-open-source/layer4/Menu.cpp
        vendor/pymol-open-source/layer4/PopUp.cpp
        vendor/pymol-open-source/layer5/PyMOL.cpp
        vendor/pymol-open-source/layer5/TestPyMOL.cpp
        vendor/pymol-open-source/layer5/main.cpp
        vendor/pymol-open-source/ov/src/OVContext.cpp
        vendor/pymol-open-source/ov/src/OVHeap.cpp
        vendor/pymol-open-source/ov/src/OVHeapArray.cpp
        vendor/pymol-open-source/ov/src/OVLexicon.cpp
        vendor/pymol-open-source/ov/src/OVOneToAny.cpp
        vendor/pymol-open-source/ov/src/OVOneToOne.cpp
        vendor/pymol-open-source/ov/src/OVRandom.cpp
        vendor/pymol-open-source/ov/src/ov_utility.cpp
)
add_library(_cmd SHARED ${ALL_SRC})

set(ALL_COMP_ARGS
        /MP
        /openmp
        /std:c++17
)
target_compile_options(_cmd PRIVATE ${ALL_COMP_ARGS})

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

set(SHARED_SUFFIX
        .cp311-win_amd64.pyd
)
set_target_properties(_cmd PROPERTIES SUFFIX ${SHARED_SUFFIX})

target_compile_features(_cmd PRIVATE cxx_std_17)

set_target_properties(_cmd PROPERTIES PREFIX "")

execute_process(
        COMMAND ${Python_EXECUTABLE} -c "import numpy; print(numpy.get_include())"
        OUTPUT_VARIABLE NUMPY_INCLUDE_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
)

set (ALL_INC_DIR
        vendor/pymol-open-source/include
        vendor/pymol-open-source/contrib/uiuc/plugins/include
        vendor/pymol-open-source/ov/src
        vendor/pymol-open-source/layer0
        vendor/pymol-open-source/layer1
        vendor/pymol-open-source/layer2
        vendor/pymol-open-source/layer3
        vendor/pymol-open-source/layer4
        vendor/pymol-open-source/layer5
        vendor/pymol-open-source/build/generated
        vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src
        .venv/Lib/site-packages/numpy/core/include
        vcpkg_installed/x64-windows-static/include
        #includes/python  # TODO: Fix this include!
        ${Python3_INCLUDE_DIRS}
)
target_include_directories(_cmd PUBLIC ${ALL_INC_DIR})

if(APPLE)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -undefined dynamic_lookup")
endif()

add_library(opengl32 STATIC IMPORTED)
set_target_properties(opengl32 PROPERTIES IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/pre-built/windows/libx64/OpenGL32.lib)

find_package(freetype CONFIG REQUIRED)
find_package(glew CONFIG REQUIRED)
find_package(PNG CONFIG REQUIRED)
find_package(libxml2 CONFIG REQUIRED)
find_package(netcdf CONFIG REQUIRED)
# I don't know if the lines below could become useful.
#find_library(Advapi32 NAMES Advapi32 REQUIRED)
#find_library(Ws2_32 NAMES Ws2_32 REQUIRED)
#find_library(Crypt32 NAMES Crypt32 REQUIRED)
#find_library(Shlwapi NAMES Shlwapi REQUIRED)

add_library(python311 STATIC IMPORTED)
set_target_properties(python311 PROPERTIES IMPORTED_LOCATION ${Python3_LIBRARIES})

target_link_directories(_cmd PRIVATE ${CMAKE_SOURCE_DIR}/vcpkg_installed/x64-windows-static/lib)
target_link_libraries(
        _cmd PRIVATE
        freetype opengl32 glew32 PNG::PNG libxml2 netCDF::netcdf python311
)

set(ALL_DEF
        _PYMOL_LIBPNG
        _PYMOL_FREETYPE
        PYMOL_OPENMP
        _PYMOL_VMD_PLUGINS
        #_HAVE_LIBXML  # I had problems compiling with this flag on.
        _PYMOL_NO_MSGPACKC
        _PYMOL_NO_MAIN
        WIN32
        _PYMOL_NUMPY
)
target_compile_definitions(_cmd PUBLIC ${ALL_DEF})

install(TARGETS _cmd DESTINATION pymol)
