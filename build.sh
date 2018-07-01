#!/bin/sh

cd build/apis && rm -rf *

cmake ../../apis/c_cpp && make
