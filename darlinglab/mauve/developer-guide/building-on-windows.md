---
layout: mauvepage
---

### Compiling mauveAligner and progressiveMauve on Windows

This document describes how to configure a Windows computer to build the command-line mauveAligner and related binary programs.  Several software development tools must be installed, all of which are available free of charge as of 11/11/2006. There are two primary ways to build the software, either through the Visual Studio GUI or from a command-line script. 

#### Step 1.  Install Visual Studio C++

Download and install the free Visual Studio express for Desktop:
[http://www.visualstudio.com/en-US/products/visual-studio-express-vs](http://www.visualstudio.com/en-US/products/visual-studio-express-vs)

Installation must be done as a user with admin rights.  Viz studio must be run at least once by an admin after installation to configure paths and registry values.

#### Step 2.  Install a subversion client

In this example we will use TortoiseSVN:
[http://tortoisesvn.tigris.org/](http://tortoisesvn.tigris.org/)
TortoiseSVN requires admin privs to install

Using the command-line build script requires command-line subversion (the apache flavor), available from:
[https://subversion.apache.org/packages.html#windows](https://subversion.apache.org/packages.html#windows)


### Step 3.  Install the Boost C++ development libraries

The latest version of boost can be installed with the binary installers.  At present, the latest version is 1.57.0, available here:

[https://sourceforge.net/projects/boost/files/boost-binaries/](https://sourceforge.net/projects/boost/files/boost-binaries/)

Alternatively, boost can be built from source.

### Step 4 (GUI only).  Check out Mauve-related source code repositories 

If you are only interested in the automated build script, skip to Step 4 below.  Otherwise, create a development folder e.g. "C:\Development" and right-click inside the development folder.  Select the "SVN checkout" menu item.  A dialog box will pop up asking the location of the repository to check out, and the destination directory.  Perform a checkout for each of the following repositories:

**Repository** | **Checkout Directory**
https://svn.code.sf.net/p/mauve/code/libGenome/trunk | C:\Development\libGenome
https://svn.code.sf.net/p/mauve/code/libMems/trunk | C:\Development\libMems
https://svn.code.sf.net/p/mauve/code/mauveAligner/trunk | C:\Development\mauveAligner
https://svn.code.sf.net/p/mauve/code/muscle/trunk | C:\Development\muscle
https://svn.code.sf.net/p/mauve/code/sgEvolver/trunk | C:\Development\sgEvolver


### Step 5 (GUI only).  Configure Visual Studio paths

In order to build mauve-related software, it is necessary to set the include header and library search paths.  To do so, launch visual studio and from the menu bar, select "Tools->Options..."  In the dialog that appears, select the "Projects and Solutions"->"VC++ Directories" panel.  Then select "Show directories for:"->"Include files" in the preference panel.  Now click the new folder icon and add the following directories:

	C:\Development\libGenome
	C:\Development\libClustalW
	C:\Development\muscle
	C:\Development\muscle\libMUSCLE
	C:\Development\libMems
	C:\Development\boost\boost_1_35_0

If source code was installed in a directory other than C:\Development, change the paths accordingly.  Then select directories for library files ("Show directories for:"->"Library files") and add the following paths:

	C:\Development\libGenome\lib
	C:\Development\libClustalW\lib
	C:\Development\muscle\lib
	C:\Development\libMems\lib
	C:\Development\boost\boost_1_35_0\lib

On 64-bit windows, replace the boost library path with the path to 64-bit libraries, e.g. "C:\Development\boost\boost_1_35_0\lib64"

 

### Step 6 (GUI only).  Build mauveAligner, progressiveMauve, procrastAligner, muscle etc.

Open the file mauveAligner/projects/everything.sln with visual studio.  The workspace contains an assortment of projects related to mauve.  To build all projects, right-click on the text "Solution 'everything'" in the project listing at left and select "Build Solution" from the popup menu.  A batch build can be used to build for several targets at once (menu "Build"->"Batch Build").  When the build succeeds, binaries will generally be in the mauveAligner/projects or mauveAligner/bin directories.

 

### Step 4 (Script only).  Configure and run the build script

Download the latest windows build batch script from:
[http://mauve.svn.sourceforge.net/svnroot/mauve/build_scripts/build_win.bat](http://mauve.svn.sourceforge.net/svnroot/mauve/build_scripts/build_win.bat)

Save the batch script to a temporary build directory, for example `C:\build_temp\`.  Then right click on the build script to edit it.  You must now configure the program paths near the top of the build script.  Once you have finished doing so, simply run the script from a windows command-prompt:  `build_win.bat`

 
