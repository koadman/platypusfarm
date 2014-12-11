---
layout: mauvepage
---

### Installing and Running Mauve

Whether Mauve will be running under Windows, Linux, Mac OS X, or another operating system, it requires Java version 1.4 or later. Many systems already have Java 1.4 installed, so this will not be a concern. The Windows version of Mauve includes the Java installer for 32-bit windows systems that don't already have it. On other systems Java may need to be installed separately.

### Downloading

Download the latest version of Mauve for your operating system from the [Mauve download site](http://darlinglab.org/mauve/download).

#### Installation on Windows

##### Installing

Run the Mauve installer that has been downloaded. Click the "Next" button several times. If you do not already have Java 1.4 or later and your computer runs 32-bit Windows, the Mauve installer will offer to start the Java installer for you.  If your computer uses 64-bit Windows, you will need to download and install the 64-bit Java Runtime Environment from [Oracle's Java web site](http://www.oracle.com/technetwork/java/javase/downloads/index.html). 

##### Running

After installation, Mauve will appear in your system's Start Menu. To run Mauve simply select it from the Start Menu. Alternatively, the command-line mauveAligner and progressiveMauve programs may be run from the directory where Mauve was installed. See the chapter on command-line execution for more details.

#### Installation on Mac OS X

##### Installing

Download the Mauve disk image and copy the Mauve application to your "Applications" folder or another folder of your choice.

##### Running

Easy.  Double-click the Mauve application.

#### Installation on Linux

##### Prerequisites

The Linux version is compiled for 32-bit and 64-bit x86 architecture and will only run on such hardware.  Mauve can be built from source code to run on other architectures.  Mauve requires the Oracle Java runtime environment to work properly.  The GNU gcj java runtime environment, which is the default environment on linux distributions such as Fedora, Red Hat and others, may work but is not supported.  Please download and install a [Oracle java runtime environment](http://www.oracle.com/technetwork/java/javase/downloads/index.html) for your system.

##### Configuring

If java is not in the executable path, the Mauve script may need to be edited to point to the Java installation. Once downloaded and uncompressed, edit the file Mauve by changing the variable JAVA_CMD to contain the full path to the java executable.

##### Running

Simply run ./Mauve from within the Mauve directory to start the Mauve Java GUI. Alternatively, the command-line alignment programs mauveAligner and progressiveMauve can be used and provide more flexibility than the Mauve GUI. You may want to add the directory containing Mauve to your executable path.

#### Other Unix-like operating systems

Although we only provide pre-compiled binary distributions of Mauve for Windows,  Linux, and Mac OS X, we do make the source code for the Mauve GUI and mauveAligner available. If the mauveAligner source code can be compiled on a system, then the compiled binary can be used as a drop-in replacement for the mauveAligner binary distributed with the Linux version of Mauve. Mauve should then behave just as it does under Linux.
