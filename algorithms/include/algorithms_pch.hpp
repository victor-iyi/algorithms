#ifndef ALGORITHMS_PCH_HPP
#define ALGORITHMS_PCH_HPP

// algorithms "static" includes.
#include "algorithms/config.hpp"

// #ifdef ALG_USE_SYSTEM_INCLUDES

// C-standard library.

// C++ standard library.
#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <memory>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

// #endif  // ALG_USE_SYSTEM_INCLUDES

// Win32 API.
#ifdef ALG_PLATFORM_WINDOWS
  #include <Windows.h>
#endif  // ALG_PLATFORM_WINDOWS

// External libs.

#endif  // !ALGORITHMS_PCH_HPP
