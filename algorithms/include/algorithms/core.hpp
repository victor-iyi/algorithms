#ifndef ALGORITHMS_CORE_HPP
#define ALGORITHMS_CORE_HPP

#include "algorithms/config.hpp"

// ALG_API
#ifdef ALG_PLATFORM_WINDOWS
  #ifdef ALG_BUILD_DLL
    #define ALG_API __declspec(dllexport)
  #elif ALG_BUILD_STATIC
    #define ALG_API __declspec(dllexport)
  #else
    #define ALG_API __declspec(dllimport)
  #endif
#else
  #define ALG_API
#endif

// ASSERTIONS.
#ifdef ALG_ENABLE_ASSERTS
  #define ALG_ASSERT(x, ...)                             \
    {                                                    \
      if (!(x)) {                                        \
        ALG_ERROR("Assertion Failed: {0}", __VA_ARGS__); \
        __debugbreak();                                  \
      }                                                  \
    }

  #define ALG_CORE_ASSERT(x, ...)                             \
    {                                                         \
      if (!(x)) {                                             \
        ALG_CORE_ERROR("Assertion Failed: {0}", __VA_ARGS__); \
        __debugbreak();                                       \
      }                                                       \
    }
#else
  #define ALG_ASSERT(x, ...)
  #define ALG_CORE_ASSERT(x, ...)
#endif

#define BIT(x) 1 << x;

#endif  // !ALGORITHMS_CORE_HPP
