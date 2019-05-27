# CMake Requirements.
cmake_minimum_required(VERSION 3.5)

# Set project name, version & description.
set(PROJECT_NAME "algorithms")
set(PROJECT_VERSION_MAJOR 1)
set(PROJECT_VERSION_MINOR 0)
set(PROJECT_DESCRIPTION "Implementation of various Data structures and algorithms.")

# Project name.
project("${PROJECT_NAME}"
        VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}"
        DESCRIPTION "${PROJECT_DESCRIPTION}")

set(CMAKE_CXX_STANDARD 17)
if(MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /std:c++17")
endif(MSVC)

# Enables testing. (Enables `add_test()` cmd).
enable_testing()
set(ALGORITHMS_DIR "${CMAKE_SOURCE_DIR}/algorithms")

# Make CMake Configurations to be available in source files.
configure_file(
  # Where configurations are defined.
  "${CMAKE_BINARY_DIR}/build/config.h"
  # Where CMake writes auto configuration @build time.
  "${ALGORITHMS_DIR}/include/config.h"
)


# Set warning flags.
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "gcc" OR
   "${CMAKE_CXX_COMPILER_ID}" STREQUAL "clang")

   # Use these warnings for gcc or clang compilers.
  set(warnings "-Wall -Wextra -Werror")

  # Use these compiler flag for gcc or clang compilers.
  set(compiler_flags "${CMAKE_CXX_FLAGS} -std=c++17")

# Microsoft Visual Studio Compiler.
elseif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")

  # Use these warnings for MSVC compiler.
  set(warnings "/W4 /WX /EHsc")

  # Use these compiler flag for gcc or clang compilers.
  set(compiler_flags "${CMAKE_CXX_FLAGS} /std:c++17")
endif()


# Set language flags.
if(NOT CONFIGURED_ONCE)
  set(CMAKE_CXX_FLAGS "${warnings} ${compiler_flags}"
      CACHE STRING "Flags used by compiler during all build types." FORCE)
  set(CMAKE_C_FLAGS "${warnings} ${compiler_flags}"
      CACHE STRING "Flags used by compiler during all build types." FORCE)
endif()


# Include path for libraries.
include_directories("${ALGORITHMS_DIR}/include")

# Libaries directory.
add_subdirectory("algorithms")


# Application executable.
file(GLOB_RECURSE EXAMPLES "${ALGORITHMS_DIR}/src/examples/**.cc")
add_executable(algorithms ${EXAMPLES})


# Link libraries.
target_link_libraries(algorithms algorithmsCore)


# Adds test to current directory which will be run by CTest.
# Only if `enable_testing()` is enabled.
add_test(AlgorithmsExecutable algorithms)


# Set configuration check.
set(CONFIGURED_ONCE TRUE
    CACHE INTERNAL "A flag showing CMake has been configured at least once.")
