# Sverchok Library
A demo library of parametric Sverchok objects to be exported as ifcProjectLibrary. Currently not linked wit the library generator.

#Sverchok parametric library
##Description
A demo of our ifc library generator based on a BOLTS database. It has four parts:
1. Sverchok interface - provides a basic input interface. You can load the BOLTS database as csv and filter the object you want to have in your ifc Library
2. default_library.py - currently a python file with parametric object definitions
3. library_generator.py - a scripted node using Python to generate Sverchok geometry based on the object library
4. Sverchok ifc nodes - we use the ifc sverchok nodes to convert the sverchok geometry to ifc and export it
##Use
The default_library can currently only generate a box for the 3D and a plane for the 2D representation
Following steps are necessary to test the generator:
1. Install Blender 3.3.0,  Sverchok 1.1.0 and Sverchok ifc https://github.com/mdjska/IfcOpenShell/tree/v0.7.0/src/ifcsverchok
2. Download the bolts library
3. Save the defult_library.py and the geometry.py somewhere your Blender Python can find them 
4. Load the BOLTS csv to sverchok and use it to filter out the elements you don't need
5. Update all nodes and use the export ifc button to save the library.
