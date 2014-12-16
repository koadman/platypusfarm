---
layout: mauvepage
---

### Compiling mauveAligner from source on Linux

Although Mauve is provided as a pre-compiled binary for Windows, Linux, and Mac OS X, we also make the source code available so that users can modify Mauve and compile it on other platforms. This chapter describes the procedure for compiling the command-line mauveAligner and progressiveMauve tools from source code on a unix system. Project files for Microsoft Visual studio are included to compile Mauve in a Windows environment.

#### Brief instructions for the lazy 

1.  Ensure that all prerequisites are installed (step 0 below)
2.  `svn co https://svn.code.sf.net/p/mauve/code/build_scripts`
3.  `cd build_scripts`
4.  `./build_linux_x64.sh`

The resulting GUI build will be located in
`build/mauve/dist/`


#### 0. Prerequisites

The following command will install all prerequisites on debian and ubuntu:

`sudo apt-get update ; sudo apt-get install g++ make pkg-config subversion libtool autoconf libbz2-dev libz-dev subversion bzip2 ant openjdk-7-jdk`


#### 1. Obtain Mauve source code

The command-line aligner tools are contained in a source package called "mauveAligner". mauveAligner depends on several additional software packages. 
Each of these packages must be downloaded and installed in order to compile mauveAligner successfully.  The easiest way to obtain the code is to check it out directly from the sourceforge subversion repository, especially if the code will be modified and changes will be committed back to the repository.  To do so, execute the following series of commands inside a development directory:

	svn co svn://svn.code.sf.net/p/mauve/code/libGenome/trunk libGenome
	svn co svn://svn.code.sf.net/p/mauve/code/libMems/trunk libMems
	svn co svn://svn.code.sf.net/p/mauve/code/muscle/trunk muscle
	svn co svn://svn.code.sf.net/p/mauve/code/sgEvolver/trunk sgEvolver
	svn co svn://svn.code.sf.net/p/mauve/code/mauveAligner/trunk mauveAligner
	svn co svn://svn.code.sf.net/p/mauve/code/mauve/trunk mauve

The developers make no guarantee that the latest source code will compile or otherwise work.


#### 1. Installing Boost

Boost may be installed as a package on Linux systems using apt-get or yum, or from source on Windows and Mac OS X. We recommend building boost from source on all platforms.  To do so it is necessary to ensure zlib-devel and bzip2-devel packages are already installed. A default build of the boost source may be done using the commands:

	./bootstrap.sh --prefix=$HOME --with-libraries=filesystem,iostreams,program_options,system
	./b2 -a -j4 link=static install

#### 2. Installing libGenome

Once downloaded and untarred, libGenome can be compiled and installed using the following commands from within the libGenome directory:

	./configure --prefix=$HOME
	make
	make install

libGenome is installed by default in the /usr/local directory. The --prefix argument to ./configure is optional and specifies the location where libGenome gets installed.

#### 3. Installing muscle

The installation procedure for the muscle library is similar to that for libGenome. From the software package's directory, execute the following commands:

	./configure --prefix=$HOME
	make
	make install

An error usually occurs after running the 'make' command.  It is safe to ignore and simply continue with 'make install'.  Again, the --prefix is an optional argument to ./configure which specifies the location where the library gets installed.

#### 4. Installing libMems

Since libMems depends on the functionality provided by libGenome, muscle, and boost these packages must be installed before libMems. Also, libMems requires the pkg-config software to determine the location of libGenome and muscle during the installation process. From the libMems directory, execute the following commands:

	./configure --prefix=$HOME --with-boost=/path/to/boost
	make
	make install

Here `/path/to/boost` must be replaced with the location of your boost installation. If you've got a systemwide installation this might be `/usr/`. If boost was installed to your home directory it might be `$HOME`. Also, if muscle or libGenome were installed to a non-standard directory, the directory may need to be added to the PKG_CONFIG_PATH environment variable. For example, if libGenome were installed in the prefix $HOME, the PKG_CONFIG_PATH variable could be set with this command: `export PKG_CONFIG_PATH="$PKG_CONFIG_PATH:$HOME/lib/pkgconfig"` It's a good idea to add PKG_CONFIG_PATH to the .profile or .bashrc or another login script so it doesn't need to be set manually every time the user logs in. As with the other packages, the installation prefix can be specified using the --prefix argument.

#### 5. Compiling mauveAligner

Once libGenome, muscle, and libMems are installed, the aligner software can be compiled. From the mauveAligner directory, issue the following commands:

	./configure
	make
	make install

In addition to mauveAligner and progressiveMauve, several supporting applications will be compileld. We do not have explicit documentation for them. Many of them are self-explanatory and give their usage instructions when run without arguments.

The statically linked version of mauveAligner is called mauveStatic. It includes the necessary part of the support libraries directly in the program and can be used on other systems without first installing the support libraries. Note that Mac OS X doesn't support static linking and any applications built on OS X will be dynamically linked.

#### Compiling from a source snapshot

The development code in the source code repositories do not have a complete build system. In order to build these, the build system must be regenerated using a recent version of the autotools software. To prepare the source for a build, execute the following command:

	./autogen.sh

You will need GNU autotools installed, including autoconf, automake, and libtool. The source directory will now be ready for a build with the usual configure, make, make install procedure.

#### A complete example

The following series of commands will build all libraries and source code from the latest source snapshots on an x86 Linux system, installing software to the user's home directory:

	# create essential directories if they don't exist
	mkdir -p ~/bin
	mkdir -p ~/lib
	export PATH="$HOME/bin:$PATH"
	export LD_LIBRARY_PATH="$HOME/lib:$LD_LIBRARY_PATH"

	# make a build directory
	mkdir build
	cd build

	# download the source
	svn co svn://svn.code.sf.net/p/mauve/code/libGenome/trunk libGenome
	svn co svn://svn.code.sf.net/p/mauve/code/libMems/trunk libMems
	svn co svn://svn.code.sf.net/p/mauve/code/muscle/trunk muscle
	svn co svn://svn.code.sf.net/p/mauve/code/sgEvolver/trunk sgEvolver
	svn co svn://svn.code.sf.net/p/mauve/code/mauveAligner/trunk mauveAligner
	svn co svn://svn.code.sf.net/p/mauve/code/mauve/trunk mauve

	# build pkg-config
	curl -OL http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz
	tar -xzf pkg-config-0.28.tar.gz
	cd pkg-config-0.28
	./configure --with-internal-glib  --prefix=$HOME && make && make install
	export PKG_CONFIG_PATH="$HOME/lib/pkgconfig"
	cd ..

	# build boost
	curl -OL http://downloads.sourceforge.net/project/boost/boost/1.57.0/boost_1_57_0.tar.bz2
	tar -xjf boost_1_57_0.tar.bz2
	cd boost_1_57_0
	./bootstrap.sh --prefix=$HOME --with-libraries=filesystem,iostreams,program_options,system
	./b2 -a -j4 link=static install
	cd ..

	# build libraries
	cd libGenome
	./autogen.sh
	./configure --prefix=$HOME && make install
	cd ..

	cd muscle
	./autogen.sh
	./configure --prefix=$HOME && make ; make ; make install
	cd ..

	cd libMems
	./autogen.sh
	./configure --prefix=$HOME --with-boost=$HOME && make install
	cd ..

	cd mauveAligner
	./autogen.sh
	./configure --prefix=$HOME && make install
	cd ..

	cd sgEvolver
	./autogen.sh
	./configure --prefix=$HOME && make install
	cd ..

If you will be building the source more than once, or especially if you will be editing and recompiling the source, it will be desirable to have `PATH`, `LD_LIBRARY_PATH`, and `PKG_CONFIG_PATH` set automatically on login. Edit one of `$HOME/.profile` or `$HOME/.bashrc` or `$HOME/.profile.local` to set the environment variables.

To build the GUI, execute the following additional commands:

	cp mauveAligner/src/mauveStatic mauve/linux-x86/mauveAligner
	cp mauveAligner/src/progressiveMauveStatic mauve/linux-x86/progressiveMauve
	cd mauve
	ant dist

The Mauve GUI build will reside in `mauve/dist/`
