cmake_minimum_required(VERSION 3.8)
project(algorithms)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
    apis/c_cpp/functions.c
    apis/cython/algorithms.c)

add_executable(algorithms ${SOURCE_FILES})