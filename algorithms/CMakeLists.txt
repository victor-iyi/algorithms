# Path to google test.
set(GOOGLE_TEST_DIR "vendor/googletest"
    CACHE PATH "Path to Google Test Distribution.")


# Visual Studio defaults to linking to Multi-Threaded, DLL-specific
# version of the standard library. Google overrides this behavior by default.
if("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")

  # Force option to `ON`  so that Google test will use /MD instead of /MT
  # /MD is now the default for Visual Studio - which has already been configured
  # in top level CMakeLists.txt file.
  option(gtest_force_shared_crt
         "Use shared (DLL) run-time lib even when Google Test is built as static lib"
         ON)

elseif(APPLE)

  # Tell GoogleTest to use it's own version of std::tr1 namespace - which is not
  # present in C++ 11.
  add_definitions(-DGTEST_USE_OWN_TR1_TUPLE=1)

endif()


# Specifying sub directory containing CMakeLists.txt for Google Tests.
add_subdirectory("${GOOGLE_TEST_DIR}" "${CMAKE_BINARY_DIR}/googletest")


# Disable all warnings for both gcc & clang.
set_property(TARGET gtest APPEND_STRING PROPERTY COMPILE_FLAGS " -w")


# Specify compiler's search path for GoogleTest.
include_directories(SYSTEM
                    "${GOOGLE_TEST_DIR}/googletest/include"
                    "${GOOGLE_TEST_DIR}/googlemock/include")

# Algorithms (core) source library files.
file(GLOB ALGORITHMS_CORE "src/algorithms/*.cc")
add_library(algorithms ${ALGORITHMS_CORE})


# Todo (test) source files.
file(GLOB ALGORITHMS_TESTS "tests/*cc")

# Build executable - where algorithms &
# gmock are it's dependencies.
add_executable(algorithmstests ${ALGORITHMS_TESTS})

# Link dependencies of algorithmstests lib.
target_link_libraries(algorithmstests algorithms gmock_main)

# Add Test for CTest.
add_test(tests algorithmstests)
