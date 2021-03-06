---
layout: mauvepage
---

### Mauve Development Overview
The developer's guide contains instructions for compiling the command-line alignment software for both Windows and unix-like systems.

The Mauve graphical interface is written in Java and can be compiled on any system with an installed Java Development Kit.

Windows releases are packaged with the [Nullsoft Scriptable Installer System](http://nsis.sourceforge.net/Main_Page) to produce an installer binary.

#### Source code 

The Mauve source code is licensed freely under the [GNU General Public License (GPL)](http://www.gnu.org/copyleft/gpl.html).
Mauve source code can be downloaded from the [sourceforge.net project page](http://sf.net/p/mauve)
We also maintain a [subversion repository of all source code](http://sf.net/p/mauve/code).

#### API documentation 

API documentation is automatically generated from our subversion repository. Thus, the online API documentation reflects the latest state of the code and may differ slightly from the most recent official source code release. [Browse the online API documentation](http://gel.ahabs.wisc.edu/apidocs/)

Alternatively, the API documentation can be generated by running the command:

`doxygen projects/[doxyfile]`

from the top-level directory of any source package.
