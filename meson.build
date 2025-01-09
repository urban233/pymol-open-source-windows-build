# Meson build configuration for PyMOL
project('pymol', ['cpp', 'c'], version: '3.0.1', meson_version: '>= 0.53.0')

# Include Python dependency
python = import('python').find_installation(pure: false)
fs = import('fs')

# Include directories from ALL_INC_DIR
inc_dirs = include_directories(
    'vendor/pymol-open-source/include',
    'vendor/pymol-open-source/contrib/uiuc/plugins/include',
    'vendor/pymol-open-source/ov/src',
    'vendor/pymol-open-source/layer0',
    'vendor/pymol-open-source/layer1',
    'vendor/pymol-open-source/layer2',
    'vendor/pymol-open-source/layer3',
    'vendor/pymol-open-source/layer4',
    'vendor/pymol-open-source/layer5',
    'vendor/pymol-open-source/build/generated',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src',
    '.venv/Lib/site-packages/numpy/core/include',
    'C:/Users/student/AppData/Local/Programs/Python/Python311/Include'  # TODO: Make this variable!
)

# Define compiler arguments from ALL_COMP_ARGS
if meson.get_compiler('cpp').get_id() == 'gcc' or meson.get_compiler('cpp').get_id() == 'clang'
    # GCC/Clang-specific flags
    add_project_arguments(
        '-std=c++17',  # Use C++17 standard
        '-fopenmp',    # Enable OpenMP
        '-DWIN32',     # Preprocessor definitions
        '-D_PYMOL_OPENMP',
        '-D_PYMOL_LIBPNG',
        '-D_PYMOL_FREETYPE',
        '-D_PYMOL_VMD_PLUGINS',
        #'-D_HAVE_LIBXML',
        '-D_PYMOL_NO_MSGPACKC',
        '-D_PYMOL_NO_MAIN',
        '-D_PYMOL_NUMPY',
        language: 'cpp'
    )
    add_project_arguments(
        '-DWIN32',
        language: 'c'
    )
else
    # MSVC-specific flags
    add_project_arguments(
        '/std:c++17',
        '/openmp',
        '/DWIN32',
        '/D_PYMOL_OPENMP',
        '/D_PYMOL_LIBPNG',
        '/D_PYMOL_FREETYPE',
        '/D_PYMOL_VMD_PLUGINS',
        #'/D_HAVE_LIBXML',
        '/D_PYMOL_NO_MSGPACKC',
        '/D_PYMOL_NO_MAIN',
        '/D_PYMOL_NUMPY',
        '/MP',
        language: 'cpp'
    )
    add_project_arguments(
        '/DWIN32',
        language: 'c'
    )
endif

srcs = files(
    'vendor/pymol-open-source/build/generated/ShaderText.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/PlugIOManagerInit.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/abinitplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/avsplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/basissetplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/bgfplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/binposplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/biomoccaplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/brixplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/carplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/ccp4plugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/corplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/crdplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/cubeplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dcdplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dlpolyplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dsn6plugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dtrplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/dxplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/edmplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/fs4plugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/gamessplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/graspplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/grdplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/gridplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/gromacsplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/hash.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/inthash.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/jsplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/maeffplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/mapplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/mdfplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/mol2plugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/moldenplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/molemeshplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/msmsplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/namdbinplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/netcdfplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/offplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/parm7plugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/parmplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pbeqplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pdbplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pdbxplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/phiplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pltplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/plyplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/pqrplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/psfplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/raster3dplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/rst7plugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/situsplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/spiderplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/stlplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/tinkerplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/uhbdplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vasp5xdatcarplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspchgcarplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspoutcarplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspparchgplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspposcarplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspxdatcarplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vaspxmlplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vtfplugin.c',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/vtkplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/xbgfplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/xsfplugin.cpp',
    'vendor/pymol-open-source/contrib/uiuc/plugins/molfile_plugin/src/xyzplugin.c',
    'vendor/pymol-open-source/layer0/Bezier.cpp',
    'vendor/pymol-open-source/layer0/Block.cpp',
    'vendor/pymol-open-source/layer0/CarveHelper.cpp',
    'vendor/pymol-open-source/layer0/ContourSurf.cpp',
    'vendor/pymol-open-source/layer0/Crystal.cpp',
    'vendor/pymol-open-source/layer0/Err.cpp',
    'vendor/pymol-open-source/layer0/Feedback.cpp',
    'vendor/pymol-open-source/layer0/Field.cpp',
    'vendor/pymol-open-source/layer0/File.cpp',
    'vendor/pymol-open-source/layer0/GFXManager.cpp',
    'vendor/pymol-open-source/layer0/GenericBuffer.cpp',
    'vendor/pymol-open-source/layer0/GraphicsUtil.cpp',
    'vendor/pymol-open-source/layer0/Isosurf.cpp',
    'vendor/pymol-open-source/layer0/Map.cpp',
    'vendor/pymol-open-source/layer0/Match.cpp',
    'vendor/pymol-open-source/layer0/Matrix.cpp',
    'vendor/pymol-open-source/layer0/MemoryDebug.cpp',
    'vendor/pymol-open-source/layer0/MemoryUsage.cpp',
    'vendor/pymol-open-source/layer0/MyPNG.cpp',
    'vendor/pymol-open-source/layer0/Parse.cpp',
    'vendor/pymol-open-source/layer0/Pixmap.cpp',
    'vendor/pymol-open-source/layer0/PostProcess.cpp',
    'vendor/pymol-open-source/layer0/PrintUtils.cpp',
    'vendor/pymol-open-source/layer0/ShaderMgr.cpp',
    'vendor/pymol-open-source/layer0/ShaderPreprocessor.cpp',
    'vendor/pymol-open-source/layer0/ShaderPrg.cpp',
    'vendor/pymol-open-source/layer0/Sphere.cpp',
    'vendor/pymol-open-source/layer0/TTT.cpp',
    'vendor/pymol-open-source/layer0/Tetsurf.cpp',
    'vendor/pymol-open-source/layer0/Texture.cpp',
    'vendor/pymol-open-source/layer0/Tracker.cpp',
    'vendor/pymol-open-source/layer0/Triangle.cpp',
    'vendor/pymol-open-source/layer0/Util.cpp',
    'vendor/pymol-open-source/layer0/Util2.cpp',
    'vendor/pymol-open-source/layer0/Vector.cpp',
    'vendor/pymol-open-source/layer0/Word.cpp',
    'vendor/pymol-open-source/layer0/ccealignmodule.cpp',
    'vendor/pymol-open-source/layer0/marching_cubes.cpp',
    'vendor/pymol-open-source/layer0/os_gl.cpp',
    'vendor/pymol-open-source/layer1/Basis.cpp',
    'vendor/pymol-open-source/layer1/ButMode.cpp',
    'vendor/pymol-open-source/layer1/CGO.cpp',
    'vendor/pymol-open-source/layer1/CGOGL.cpp',
    'vendor/pymol-open-source/layer1/CGORenderer.cpp',
    'vendor/pymol-open-source/layer1/COLLADA.cpp',
    'vendor/pymol-open-source/layer1/Camera.cpp',
    'vendor/pymol-open-source/layer1/Character.cpp',
    'vendor/pymol-open-source/layer1/Color.cpp',
    'vendor/pymol-open-source/layer1/Control.cpp',
    'vendor/pymol-open-source/layer1/Extrude.cpp',
    'vendor/pymol-open-source/layer1/Font.cpp',
    'vendor/pymol-open-source/layer1/FontGLUT.cpp',
    'vendor/pymol-open-source/layer1/FontGLUT8x13.cpp',
    'vendor/pymol-open-source/layer1/FontGLUT9x15.cpp',
    'vendor/pymol-open-source/layer1/FontGLUTHel10.cpp',
    'vendor/pymol-open-source/layer1/FontGLUTHel12.cpp',
    'vendor/pymol-open-source/layer1/FontGLUTHel18.cpp',
    'vendor/pymol-open-source/layer1/FontType.cpp',
    'vendor/pymol-open-source/layer1/Movie.cpp',
    'vendor/pymol-open-source/layer1/Ortho.cpp',
    'vendor/pymol-open-source/layer1/P.cpp',
    'vendor/pymol-open-source/layer1/PConv.cpp',
    'vendor/pymol-open-source/layer1/Picking.cpp',
    'vendor/pymol-open-source/layer1/Pop.cpp',
    'vendor/pymol-open-source/layer1/PyMOLObject.cpp',
    'vendor/pymol-open-source/layer1/Ray.cpp',
    'vendor/pymol-open-source/layer1/Rep.cpp',
    'vendor/pymol-open-source/layer1/Scene.cpp',
    'vendor/pymol-open-source/layer1/SceneMouse.cpp',
    'vendor/pymol-open-source/layer1/ScenePicking.cpp',
    'vendor/pymol-open-source/layer1/SceneRay.cpp',
    'vendor/pymol-open-source/layer1/SceneRender.cpp',
    'vendor/pymol-open-source/layer1/SceneView.cpp',
    'vendor/pymol-open-source/layer1/ScrollBar.cpp',
    'vendor/pymol-open-source/layer1/Seq.cpp',
    'vendor/pymol-open-source/layer1/Setting.cpp',
    'vendor/pymol-open-source/layer1/Shaker.cpp',
    'vendor/pymol-open-source/layer1/SymOp.cpp',
    'vendor/pymol-open-source/layer1/SymOpPConv.cpp',
    'vendor/pymol-open-source/layer1/SymOpTools.cpp',
    'vendor/pymol-open-source/layer1/Symmetry.cpp',
    'vendor/pymol-open-source/layer1/Text.cpp',
    'vendor/pymol-open-source/layer1/TypeFace.cpp',
    'vendor/pymol-open-source/layer1/View.cpp',
    'vendor/pymol-open-source/layer1/Wizard.cpp',
    'vendor/pymol-open-source/layer2/AssemblyHelpers.cpp',
    'vendor/pymol-open-source/layer2/AtomInfo.cpp',
    'vendor/pymol-open-source/layer2/AtomInfoHistory.cpp',
    'vendor/pymol-open-source/layer2/BondTypeHistory.cpp',
    'vendor/pymol-open-source/layer2/CifFile.cpp',
    'vendor/pymol-open-source/layer2/CifMoleculeReader.cpp',
    'vendor/pymol-open-source/layer2/CoordSet.cpp',
    'vendor/pymol-open-source/layer2/DistSet.cpp',
    'vendor/pymol-open-source/layer2/GadgetSet.cpp',
    'vendor/pymol-open-source/layer2/HydrogenAdder.cpp',
    'vendor/pymol-open-source/layer2/MmodTyping.cpp',
    'vendor/pymol-open-source/layer2/MmtfMoleculeReader.cpp',
    'vendor/pymol-open-source/layer2/Mol2Typing.cpp',
    'vendor/pymol-open-source/layer2/MolV3000.cpp',
    'vendor/pymol-open-source/layer2/ObjectAlignment.cpp',
    'vendor/pymol-open-source/layer2/ObjectCGO.cpp',
    'vendor/pymol-open-source/layer2/ObjectCallback.cpp',
    'vendor/pymol-open-source/layer2/ObjectCurve.cpp',
    'vendor/pymol-open-source/layer2/ObjectDist.cpp',
    'vendor/pymol-open-source/layer2/ObjectGadget.cpp',
    'vendor/pymol-open-source/layer2/ObjectGadgetRamp.cpp',
    'vendor/pymol-open-source/layer2/ObjectGroup.cpp',
    'vendor/pymol-open-source/layer2/ObjectMap.cpp',
    'vendor/pymol-open-source/layer2/ObjectMesh.cpp',
    'vendor/pymol-open-source/layer2/ObjectMolecule.cpp',
    'vendor/pymol-open-source/layer2/ObjectMolecule2.cpp',
    'vendor/pymol-open-source/layer2/ObjectMolecule3.cpp',
    'vendor/pymol-open-source/layer2/ObjectSlice.cpp',
    'vendor/pymol-open-source/layer2/ObjectSurface.cpp',
    'vendor/pymol-open-source/layer2/ObjectVolume.cpp',
    'vendor/pymol-open-source/layer2/RepAngle.cpp',
    'vendor/pymol-open-source/layer2/RepCartoon.cpp',
    'vendor/pymol-open-source/layer2/RepCylBond.cpp',
    'vendor/pymol-open-source/layer2/RepDihedral.cpp',
    'vendor/pymol-open-source/layer2/RepDistDash.cpp',
    'vendor/pymol-open-source/layer2/RepDistLabel.cpp',
    'vendor/pymol-open-source/layer2/RepDot.cpp',
    'vendor/pymol-open-source/layer2/RepEllipsoid.cpp',
    'vendor/pymol-open-source/layer2/RepLabel.cpp',
    'vendor/pymol-open-source/layer2/RepMesh.cpp',
    'vendor/pymol-open-source/layer2/RepNonbonded.cpp',
    'vendor/pymol-open-source/layer2/RepNonbondedSphere.cpp',
    'vendor/pymol-open-source/layer2/RepRibbon.cpp',
    'vendor/pymol-open-source/layer2/RepSphere.cpp',
    'vendor/pymol-open-source/layer2/RepSphereGenerate.cpp',
    'vendor/pymol-open-source/layer2/RepSphereImmediate.cpp',
    'vendor/pymol-open-source/layer2/RepSurface.cpp',
    'vendor/pymol-open-source/layer2/RepWireBond.cpp',
    'vendor/pymol-open-source/layer2/Sculpt.cpp',
    'vendor/pymol-open-source/layer2/SculptCache.cpp',
    'vendor/pymol-open-source/layer2/SideChainHelper.cpp',
    'vendor/pymol-open-source/layer2/VFont.cpp',
    'vendor/pymol-open-source/layer3/AtomIterators.cpp',
    'vendor/pymol-open-source/layer3/CifDataValueFormatter.cpp',
    'vendor/pymol-open-source/layer3/Editor.cpp',
    'vendor/pymol-open-source/layer3/Executive.cpp',
    'vendor/pymol-open-source/layer3/ExecutivePython.cpp',
    'vendor/pymol-open-source/layer3/Interactions.cpp',
    'vendor/pymol-open-source/layer3/MaeExportHelpers.cpp',
    'vendor/pymol-open-source/layer3/MoleculeExporter.cpp',
    'vendor/pymol-open-source/layer3/MovieScene.cpp',
    'vendor/pymol-open-source/layer3/PlugIOManager.cpp',
    'vendor/pymol-open-source/layer3/RingFinder.cpp',
    'vendor/pymol-open-source/layer3/Seeker.cpp',
    'vendor/pymol-open-source/layer3/Selector.cpp',
    'vendor/pymol-open-source/layer3/SelectorTmp.cpp',
    'vendor/pymol-open-source/layer3/SpecRec.cpp',
    'vendor/pymol-open-source/layer3/SpecRecSpecial.cpp',
    'vendor/pymol-open-source/layer4/Cmd.cpp',
    'vendor/pymol-open-source/layer4/Menu.cpp',
    'vendor/pymol-open-source/layer4/PopUp.cpp',
    'vendor/pymol-open-source/layer5/PyMOL.cpp',
    'vendor/pymol-open-source/layer5/TestPyMOL.cpp',
    'vendor/pymol-open-source/layer5/main.cpp',
    'vendor/pymol-open-source/ov/src/OVContext.cpp',
    'vendor/pymol-open-source/ov/src/OVHeap.cpp',
    'vendor/pymol-open-source/ov/src/OVHeapArray.cpp',
    'vendor/pymol-open-source/ov/src/OVLexicon.cpp',
    'vendor/pymol-open-source/ov/src/OVOneToAny.cpp',
    'vendor/pymol-open-source/ov/src/OVOneToOne.cpp',
    'vendor/pymol-open-source/ov/src/OVRandom.cpp',
    'vendor/pymol-open-source/ov/src/ov_utility.cpp'
)

# Dependencies from ALL_LIB
# Declare dependencies
### ------ freetype dependency ------ ###
brotlicommon_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/brotlicommon.lib']
)
brotlidec_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/brotlidec.lib']
)
brotlienc_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/brotlienc.lib']
)
bz2_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/bz2.lib']
)
freetype_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [
        meson.source_root() / 'libx64/freetype.lib',
        meson.source_root() / 'libx64/brotlicommon.lib',
        meson.source_root() / 'libx64/brotlidec.lib',
        meson.source_root() / 'libx64/brotlienc.lib',
        meson.source_root() / 'libx64/bz2.lib'
    ]
)

### ------ OpenGL dependency ------ ###
opengl_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/OpenGL32.lib']
)

### ------ glew dependency ------ ###
glu32_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/GlU32.Lib']
)

glew_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [
        meson.source_root() / 'libx64/glew32.lib',
        meson.source_root() / 'libx64/OpenGL32.lib',
        meson.source_root() / 'libx64/GlU32.Lib'
    ]
)

### ------ libpng dependency ------ ###
zlib_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/zlib.lib']
)
libpng_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [
        meson.source_root() / 'libx64/libpng16.lib',
        meson.source_root() / 'libx64/zlib.lib' # Add zlib here
    ]
)

### ------ libxml2 dependency ------ ###
libxml2_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/libxml2.lib']
)

### ------ netcdf dependency ------ ###
aec_static_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/aec-static.lib']
)
libcurl_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/libcurl.lib']
)
libhdf5_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/libhdf5.lib']
)
libhdf5_hl_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/libhdf5_hl.lib']
)
szip_static_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [meson.source_root() / 'libx64/szip-static.lib']
)
netcdf_dep = declare_dependency(
    include_directories: include_directories('includes'),
    link_args: [
        meson.source_root() / 'libx64/netcdf.lib',
        meson.source_root() / 'libx64/aec-static.lib',
        meson.source_root() / 'libx64/libcurl.lib',
        meson.source_root() / 'libx64/libhdf5.lib',
        meson.source_root() / 'libx64/libhdf5_hl.lib',
        meson.source_root() / 'libx64/szip-static.lib'
    ]
)

# System libraries (Advapi32, Ws2_32)
cc = meson.get_compiler('c')
system_libx64 = [
    cc.find_library('Advapi32', required: true),
    cc.find_library('Ws2_32', required: true),
    cc.find_library('Crypt32', required: true),
    cc.find_library('Shlwapi', required: true),
]

# Create the Python extension module (_cmd)
_cmd = python.extension_module(
    '_cmd',
    srcs,
    include_directories: inc_dirs,
    dependencies: [
        glew_dep,
        freetype_dep,
        libpng_dep,
        libxml2_dep,
        opengl_dep,
        netcdf_dep,
    # glew dependencies
        glu32_dep,
    # libpng dependency
        zlib_dep,
    # freetype dependencies
        brotlicommon_dep,
        brotlidec_dep,
        brotlienc_dep,
        bz2_dep,
    # netcdf dependencies
        aec_static_dep,
        libcurl_dep,
        libhdf5_dep,
        libhdf5_hl_dep,
        szip_static_dep
    ] + system_libx64,
    install: true,
    install_dir: python.get_install_dir(), # Install in Python's site-packages
    c_args: ['/MD'], # Compiler optimization flags
)
