# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Applications/CMake 2.8-12.app/Contents/bin/cmake"

# The command to remove a file.
RM = "/Applications/CMake 2.8-12.app/Contents/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = "/Applications/CMake 2.8-12.app/Contents/bin/ccmake"

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build"

# Include any dependencies generated for this target.
include CMakeFiles/tc_skin.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/tc_skin.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/tc_skin.dir/flags.make

tc_skin.cpp: ../bin/cppcms_tmpl_cc
tc_skin.cpp: ../tests/tc_skin.tmpl
	$(CMAKE_COMMAND) -E cmake_progress_report "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/CMakeFiles" $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating tc_skin.cpp"
	/Library/Frameworks/Python.framework/Versions/2.7/bin/python2 /Users/Abhi/Desktop/Github/Experimentation/Web\ Development/C++/cppcms_source/bin/cppcms_tmpl_cc -o /Users/Abhi/Desktop/Github/Experimentation/Web\ Development/C++/cppcms_source/build/tc_skin.cpp /Users/Abhi/Desktop/Github/Experimentation/Web\ Development/C++/cppcms_source/tests/tc_skin.tmpl

CMakeFiles/tc_skin.dir/tc_skin.cpp.o: CMakeFiles/tc_skin.dir/flags.make
CMakeFiles/tc_skin.dir/tc_skin.cpp.o: tc_skin.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/CMakeFiles" $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/tc_skin.dir/tc_skin.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/tc_skin.dir/tc_skin.cpp.o -c "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/tc_skin.cpp"

CMakeFiles/tc_skin.dir/tc_skin.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tc_skin.dir/tc_skin.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/tc_skin.cpp" > CMakeFiles/tc_skin.dir/tc_skin.cpp.i

CMakeFiles/tc_skin.dir/tc_skin.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tc_skin.dir/tc_skin.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/tc_skin.cpp" -o CMakeFiles/tc_skin.dir/tc_skin.cpp.s

CMakeFiles/tc_skin.dir/tc_skin.cpp.o.requires:
.PHONY : CMakeFiles/tc_skin.dir/tc_skin.cpp.o.requires

CMakeFiles/tc_skin.dir/tc_skin.cpp.o.provides: CMakeFiles/tc_skin.dir/tc_skin.cpp.o.requires
	$(MAKE) -f CMakeFiles/tc_skin.dir/build.make CMakeFiles/tc_skin.dir/tc_skin.cpp.o.provides.build
.PHONY : CMakeFiles/tc_skin.dir/tc_skin.cpp.o.provides

CMakeFiles/tc_skin.dir/tc_skin.cpp.o.provides.build: CMakeFiles/tc_skin.dir/tc_skin.cpp.o

# Object files for target tc_skin
tc_skin_OBJECTS = \
"CMakeFiles/tc_skin.dir/tc_skin.cpp.o"

# External object files for target tc_skin
tc_skin_EXTERNAL_OBJECTS =

libtc_skin.dylib: CMakeFiles/tc_skin.dir/tc_skin.cpp.o
libtc_skin.dylib: CMakeFiles/tc_skin.dir/build.make
libtc_skin.dylib: libcppcms.1.0.4.dylib
libtc_skin.dylib: booster/libbooster.0.0.2.dylib
libtc_skin.dylib: /usr/lib/libpthread.dylib
libtc_skin.dylib: /usr/local/lib/libpcre.dylib
libtc_skin.dylib: /opt/local/lib/libicuuc.dylib
libtc_skin.dylib: /opt/local/lib/libicui18n.dylib
libtc_skin.dylib: /opt/local/lib/libicudata.dylib
libtc_skin.dylib: /usr/lib/libiconv.dylib
libtc_skin.dylib: /usr/lib/libcrypto.dylib
libtc_skin.dylib: /usr/lib/libz.dylib
libtc_skin.dylib: CMakeFiles/tc_skin.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared library libtc_skin.dylib"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tc_skin.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/tc_skin.dir/build: libtc_skin.dylib
.PHONY : CMakeFiles/tc_skin.dir/build

CMakeFiles/tc_skin.dir/requires: CMakeFiles/tc_skin.dir/tc_skin.cpp.o.requires
.PHONY : CMakeFiles/tc_skin.dir/requires

CMakeFiles/tc_skin.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tc_skin.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tc_skin.dir/clean

CMakeFiles/tc_skin.dir/depend: tc_skin.cpp
	cd "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/CMakeFiles/tc_skin.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/tc_skin.dir/depend

