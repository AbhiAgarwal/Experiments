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
include CMakeFiles/serialization_test.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/serialization_test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/serialization_test.dir/flags.make

CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o: CMakeFiles/serialization_test.dir/flags.make
CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o: ../tests/serialization_test.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/CMakeFiles" $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o -c "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/tests/serialization_test.cpp"

CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/tests/serialization_test.cpp" > CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.i

CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/tests/serialization_test.cpp" -o CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.s

CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.requires:
.PHONY : CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.requires

CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.provides: CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.requires
	$(MAKE) -f CMakeFiles/serialization_test.dir/build.make CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.provides.build
.PHONY : CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.provides

CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.provides.build: CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o

# Object files for target serialization_test
serialization_test_OBJECTS = \
"CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o"

# External object files for target serialization_test
serialization_test_EXTERNAL_OBJECTS =

serialization_test: CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o
serialization_test: CMakeFiles/serialization_test.dir/build.make
serialization_test: libcppcms.1.0.4.dylib
serialization_test: booster/libbooster.0.0.2.dylib
serialization_test: /usr/lib/libpthread.dylib
serialization_test: /usr/local/lib/libpcre.dylib
serialization_test: /opt/local/lib/libicuuc.dylib
serialization_test: /opt/local/lib/libicui18n.dylib
serialization_test: /opt/local/lib/libicudata.dylib
serialization_test: /usr/lib/libiconv.dylib
serialization_test: /usr/lib/libcrypto.dylib
serialization_test: /usr/lib/libz.dylib
serialization_test: CMakeFiles/serialization_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable serialization_test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/serialization_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/serialization_test.dir/build: serialization_test
.PHONY : CMakeFiles/serialization_test.dir/build

CMakeFiles/serialization_test.dir/requires: CMakeFiles/serialization_test.dir/tests/serialization_test.cpp.o.requires
.PHONY : CMakeFiles/serialization_test.dir/requires

CMakeFiles/serialization_test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/serialization_test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/serialization_test.dir/clean

CMakeFiles/serialization_test.dir/depend:
	cd "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build" "/Users/Abhi/Desktop/Github/Experimentation/Web Development/C++/cppcms_source/build/CMakeFiles/serialization_test.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/serialization_test.dir/depend

