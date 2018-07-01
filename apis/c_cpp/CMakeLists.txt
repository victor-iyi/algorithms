# Minimum requirement for cmake.
cmake_minimum_required(VERSION 3.8)

# Project name, version & description.
project(algorithms
        VERSION 1.0.0
        DESCRIPTION "Data structures & Algorithm implementation in Python (written in C, C++ & Cython).")

# Set shared libary build type to "Release build".
set(CMAKE_BUILD_TYPE Debug)

# For header files #include directives.
include_directories(${CMAKE_SOURCE_DIR}/include)

# file(GLOB ...) allows for wildcard additions.
file(GLOB_RECURSE SOURCES "src/*.cc")

# Generate static libaries from sources.
# Other options: SHARED | STATIC | MODULE
add_library(algorithms STATIC ${SOURCES})

# install(TARGETS algorithms DESTINATION /usr/lib)
