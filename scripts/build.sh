#!/bin/sh

cd build/

cmake -G "Unix Makefiles" ../ && make
./examples
