---
layout: mauvepage
---

### Building Mauve for Mac

#### Brief instructions for the lazy 

1.  Ensure that pkg-config is installed
2.  `svn co https://mauve.svn.sourceforge.net/svnroot/mauve/build_scripts`
3.  `cd build_scripts`
4.  `./build_osx.sh`

The resulting universal binaries will be located in
`osx_build/mauveAligner/src`

#### Detailed build instructions 

##### Phase 0.  Install Xcode developer tools 

This can be obtained from the App store

##### Phase 1. Install autotools & pkg-config

These are required to build Mauve, and many other open source tools:

	curl -OL http://ftpmirror.gnu.org/autoconf/autoconf-2.69.tar.gz
	tar -xzf autoconf-2.69.tar.gz 
	cd autoconf-2.69
	./configure && make && sudo make install
	cd ..
	 
	curl -OL http://ftpmirror.gnu.org/automake/automake-1.14.1.tar.gz
	tar -xzf automake-1.14.1.tar.gz
	cd automake-1.14.1
	./configure && make && sudo make install
	cd ..
	 
	curl -OL http://ftpmirror.gnu.org/libtool/libtool-2.4.4.tar.gz
	tar -xzf libtool-2.4.4.tar.gz
	cd libtool-2.4.4
	./configure && make && sudo make install
	cd ..
	
	curl -OL http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz
	tar -xzf pkg-config-0.28.tar.gz
	cd pkg-config-0.28
	./configure --with-internal-glib && make && sudo make install
	cd ..
	
##### Phase 2.  Build the aligners

Once Xcode, autotools, and pkg-config have been installed, it's necessary to set CFLAGS and CXXFLAGS appropriately:

	export CFLAGS="-O3 -g -mmacosx-version-min=10.7 -arch i386 -arch x86_64"
	export CXXFLAGS="-O3 -g -mmacosx-version-min=10.7 -arch i386 -arch x86_64" 

**the above do not permit linking with boost libs!**

It may be desirable to set these variables inside $HOME/.profile so they get configured automatically on login.  Other important environment variables and their settings may be:

	export PKG_CONFIG_PATH="$HOME/lib/pkgconfig" 
	export LD_LIBRARY_PATH="$HOME/lib"
	export SVN_EDITOR=vi
	export PATH="/usr/local/bin:$HOME/bin:$PATH"

At this point, the mauveAligner source and libraries can be built with the usual procedure.  When running ./configure, it is necessary to add both --disable-shared for an OS X build:


	curl -OL http://downloads.sourceforge.net/project/boost/boost/1.57.0/boost_1_57_0.tar.bz2
	tar -xjf boost_1_57_0.tar.bz2
	cd boost_1_57_0
	./bootstrap.sh --prefix=$HOME --with-libraries=filesystem,iostreams,program_options,system
	./b2 -a -j4 toolset=darwin link=static install
	cd ..

	cd libGenome ; ./autogen.sh
	./configure --prefix=$HOME --disable-shared
	make install ; cd ..

	cd muscle ; ./autogen.sh
	./configure --prefix=$HOME --disable-shared
	make ; make install ; cd ..
	
	cd libMems ; ./autogen.sh
	./configure --prefix=$HOME --disable-shared
	make install ; cd ..

	cd mauveAligner ; ./autogen.sh
	./configure --prefix=$HOME --disable-shared
	make install ; cd ..

	cd sgEvolver ; ./autogen.sh
	./configure --prefix=$HOME --disable-shared
	make install ; cd ..


##### Phase 3.  Build the Java GUI and make a disk image

This part of the build requires a [Java Development Kit](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) and [Apache Ant](http://ant.apache.org) to be installed.  With that done, copy the freshly build `mauveAligner` and `progressiveMauve` binaries into the mauve/osx subdirectory and strip them of debugging symbols:

	strip osx/mauveAligner
	strip osx/progressiveMauve

That reduces the distributable binary size from >100Mb to less than 10Mb.  Then run:

	ant macdist


#### Historical information on building for Mac OS X 10.3

Since Apple's migration to Intel CPUs, Mac software should be compiled for both Intel and PowerPC CPUs, at least for the time being. Apple refers to programs with both PPC and x86 code as "universal". Building a universal library with GNU autotools is nearly impossible, so it's necessary to build x86 and PPC libraries and binaries separately and then join the result with the lipo tool. To build for a PowerPC CPU on an Intel machine, set the following environment variables:

	export CFLAGS="-O3 -g -isysroot /Developer/SDKs/MacOSX10.3.9.sdk -arch ppc"
	export CXXFLAGS="-O3 -g -isysroot /Developer/SDKs/MacOSX10.3.9.sdk -arch ppc"

And compile boost with `bjam "-sTOOLS=darwin" "-sGXX=g++ -O3 -g -isysroot /Developer/SDKs/MacOSX10.3.9.sdk -arch ppc" "-sGCC=gcc -O3 -g -isysroot /Developer/SDKs/MacOSX10.3.9.sdk -arch ppc" "-sBUILD=release <linkflags>-Wl,-syslibroot,/Developer/SDKs/MacOSX10.3.9.sdk <runtime-link>static <threading>single/multi" --prefix=$HOME install` The rest of the build procedure remains the same. The resulting libraries and applications will run on any PowerPC mac with an OS as old as 10.3.9. To create a single universal binary for mauveAligner, run something akin to the following command `lipo -create mauveAligner-intel mauveAligner-ppc -output mauveAligner` where mauveAligner-intel and mauveAligner-ppc are the paths to the intel and ppc mauveAligner binaries, respectively.


