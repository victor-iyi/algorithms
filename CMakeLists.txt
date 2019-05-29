# CMake Requirements.
cmake_minimum_required(VERSION 3.5)

# Set project name, version & description.
set(PROJECT_NAME "algorithms")
set(PROJECT_VERSION_MAJOR 1)
set(PROJECT_VERSION_MINOR 0)
set(PROJECT_VERSION_PATCH 0)
set(PROJECT_DESCRIPTION
    "Implementation of various Data structures and algorithms.")
set(PROJECT_HOMEPAGE_URL "https://github.com/victor-iyiola/algorithms")

# Project name.
project(
  ${PROJECT_NAME}
  VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}"
  DESCRIPTION "${PROJECT_DESCRIPTION}"
  HOMEPAGE_URL "${PROJECT_HOMEPAGE_URL}"
  LANGUAGES CXX)

# --------------------------------------------------------------------
# compiler config
# --------------------------------------------------------------------
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Enables testing. (Enables `add_test()` cmd).
enable_testing()

set(ALGORITHMS_DIR "${CMAKE_SOURCE_DIR}/algorithms")
set(BUILD_DIR "${CMAKE_SOURCE_DIR}/build")


# !----------------- Definitions, Optinos & Macros.-----------------!#
option(ALG_DEBUG "Build algorithms in Debug mode." ON)
option(ALG_BUILD_STATIC "Build as a static library." ON)
option(ALG_BUILD_DLL "Build as Dynamic Linked Library." OFF)
option(ALG_BUILD_DIST "Turn on algorithms distribution build." OFF)

option(ALG_ENABLE_ASSERTS "Enable algorithms assertions." ON)
option(ALG_USE_EXTERNAL_JSON "Use an external JSON library." OFF)
option(ALG_USE_PCH "Use algorithms's pre-compiled header." OFF)
option(ALG_USE_SYSTEM_INCLUDES
       "Use C++ includes in pre-compiled headers (Recommended)." ON)

# Set default Build DataType.
if(NOT CMAKE_BUILD_TYPE)
  if(ALG_DEBUG)
    set(CMAKE_BUILD_TYPE "Debug")
  else()
    set(CMAKE_BUILD_TYPE "Release")
  endif(ALG_DEBUG)
endif(NOT CMAKE_BUILD_TYPE)

# Based on platform.
if(APPLE)
  set(ALG_PLATFORM_UNIX ON) # Unix-like.
  set(ALG_PLATFORM_DARWIN ON) # MacOS.
elseif(UNIX)
  set(ALG_PLATFORM_UNIX ON) # Linux.
elseif(WIN32)
  set(ALG_PLATFORM_WINDOWS ON) # Windows.
endif()

# Based on build-type.
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(ALG_ENABLE_ASSERTS ON)
else()
  set(ALG_ENABLE_ASSERTS OFF)
endif()

# !----------------- Set warning & compiler flags.-----------------!#
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "gcc"
   OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU"
   OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "clang")

  # # Use these warnings for gcc or clang compilers.
  add_compile_options("-Wall")
  add_compile_options("-Wextra")
  add_compile_options("-Wconversion")
  add_compile_options("-pedantic")
  add_compile_options("-Wfatal-errors")

  # # Use these warnings for gcc or clang compilers. set(warnings "-Wall -Wextra
  # -Werror -Wconversion -pedantic -Wfatal-errors")

  # Use these compiler flag for gcc or clang compilers. set(compiler_flags
  # "${CMAKE_CXX_FLAGS} -std=c++17 -stdlib=libc++")
  set(compiler_flags "${CMAKE_CXX_FLAGS} -std=c++17")

  # Microsoft Visual Studio Compiler.
elseif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")

  # Use these warnings for MSVC compiler.
  set(warnings "/W4 /wd4512 /WX /EHsc")
  # Disabled Warnings: 4512 "assignment operator could not be generated" This
  # warning provides no useful information and will occur in well formed
  # programs. <http://msdn.microsoft.com/en-us/library/hsyx7kbz.aspx>

  # Use these compiler flag for gcc or clang compilers.
  set(compiler_flags "${CMAKE_CXX_FLAGS} /std:c++17 /stdlib:libc++")
endif()

# !----------------------- Configuration file. -----------------------!#
if(NOT CONFIGURED_ONCE)
  # Make CMake Configurations to be available in source files.
  configure_file(# Where configurations are defined.
                 "${ALGORITHMS_DIR}/config/cpp/config.hpp.in"
                 # Where CMake writes auto configuration @build time.
                 "${ALGORITHMS_DIR}/include/config.hpp")

  # Setting warnings & compiler flags.
  set(CMAKE_CXX_FLAGS ${compiler_flags}
      CACHE STRING "Flags used by compiler during all build types."
      FORCE)
  set(CMAKE_C_FLAGS ${compiler_flags}
      CACHE STRING "Flags used by compiler during all build types."
      FORCE)
endif()

# Include path for libraries.
include_directories("${ALGORITHMS_DIR}/include")

# Libaries directory.
add_subdirectory("algorithms")

# Application executable.
file(GLOB_RECURSE EXAMPLES "${ALGORITHMS_DIR}/src/examples/**.cc")
add_executable(examples ${EXAMPLES})

# Link libraries.
target_link_libraries(examples algorithms)

# Adds test to current directory which will be run by CTest. Only if
# `enable_testing()` is enabled.
add_test(algorithmstest examples)

# Set configuration check.
set(CONFIGURED_ONCE TRUE
    CACHE INTERNAL "A flag showing CMake has been configured at least once.")
