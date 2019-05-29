#!/usr/bin/env bash

# Set Message Colors.
reset='\033[0m'      # Text Reset

# Regular Colors.
red='\033[0;31m'     # Red
purple='\033[0;35m'  # Purple
green='\033[0;32m'   # Green
#yellow='\033[0;33m'  # Yellow

# Bold.
bred='\033[1;31m'    # Red
bwhite='\033[1;37m'  # White
bpurple='\033[1;35m' # Purple
byellow='\033[1;33m' # Yellow
# bgreen='\033[1;32m' # Green

# Run directory: "/scripts/build/*"
PROJECT_DIR="$(cd -P "$(dirname ${BASH_SOURCE[0]})/.." && pwd)"
BUILD_DIR="${PROJECT_DIR}/build"
ALGORITHMS_DIR="${PROJECT_DIR}/algorithms"

# Build scripts options.
GENERATOR="Unix Makefiles" # -G --generator "Xcode" | "Unix Makefiles" | "Ninja"
BUILD_TYPE="Debug"         # -B --build-type
BUILD_PRECOMPILED="YES"    # -pch --pre-compiled
JOBS=4                     # -j --jobs
CLEAN_BUILD="NO"           # -c --clean-build
BUILD_MAKE="NO"            # -m --build-make

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | SHOW USAGE MESSAGE.
# +--------------------------------------------------------------------------------------------+
################################################################################################
function usage() {
  echo -e "${bpurple}Description:${purple} Build script for hazel.${reset}"
  echo
  echo -e "${bwhite}Usage: ${green}${BASH_SOURCE[0]}${reset}
    -h   | --help            = Show this help message.
    -G   | --generator-name  = Specify a build system generator: <${GENERATOR}> \"Xcode\" | \"Unix Makefiles\"
    -b   | --build-type      = Build type: <${BUILD_TYPE}> \"Debug\" | \"Release\".
    -c   | --clean-build     = Clean build files before starting build: <${CLEAN_BUILD}>. \"YES\" | \"NO\".
    -p   | --build-pch       = Build pre-compiled headers: <${BUILD_PRECOMPILED}> \"YES\" | \"NO\".
    -m   | --build-make      = Build make scripts: <${BUILD_MAKE}> \"YES\" | \"NO\".
    -j   | --jobs            = No of parallel jobs to run: <${JOBS}>.
  "
  # cmake -h
}

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | PARSE PASSED ARGUMENTS.
# +--------------------------------------------------------------------------------------------+
################################################################################################
# Parser loop.
for i in "$@"; do
  case ${i} in
  -h | -H | --help)
    usage
    exit
    ;;
  -G=* | --generator-name=*)
    GENERATOR="${i#*=}"
    shift # past argument=value
    ;;
  -b=* | --build-type=*)
    BUILD_TYPE="${i#*=}"
    shift # past argument=value
    ;;
  -c=* | --clean-build=*)
    CLEAN_BUILD="${i#*=}"
    shift # past argument=value
    ;;
  -p=* | --build-pch=*)
    BUILD_PRECOMPILED="${i#*=}"
    shift # past argument=value
    ;;
  -j=* | --jobs=*)
    JOBS="${i#*=}"
    shift # past argument=value
    ;;
  #	--default)
  #		DEFAULT=YES
  #		shift # past argument with no value
  #		;;
  *)
    # unknown option
    echo -e "${bred}ERROR: ${red}Unknown parameter \"$i\"${reset}"
    usage
    exit 1
    ;;
  esac
done

# Clean built folder before building project.
if [[ ${CLEAN_BUILD} == "YES" ]]; then
  sh "${PROJECT_DIR}/scripts/clean.sh"
  echo
fi

# Pre-compiled header.
if [[ ${BUILD_PRECOMPILED} == "YES" ]]; then
  # Pre-compiled header path.
  PCH_PATH="${ALGORITHMS_DIR}/include/algorithms_pch.hpp"
  if [[ -f "${PCH_PATH}.gch" ]]; then
    echo -e "${byellow}Pre-compiled header exists...${reset}"
  else
    echo -e "${bpurple}Running pre-compiled header...${reset}"
    g++ -std=c++17 ${PCH_PATH} -I"${ALGORITHMS_DIR}/include"
  fi
fi

################################################################################################
# +--------------------------------------------------------------------------------------------+
# | Configure & build CMake...
# +--------------------------------------------------------------------------------------------+
################################################################################################
# Create build directory if it doesn't exist.
mkdir -p ${BUILD_DIR}

# Change directory to "run/" directory.
cd "${BUILD_DIR}" || exit

# Run CMake configuration & build.
echo -e "${bpurple}Running CMake...${reset}"
cmake .. -G"${GENERATOR}" -DCMAKE_BUILD_TYPE=${BUILD_TYPE}
cmake --build . --config ${BUILD_TYPE}

# Run Make files for "Unix Makefiles".
if [[ ${GENERATOR} == "Unix Makefiles" ]]; then
  if [[ ${BUILD_MAKE} == "YES" ]]; then
    if command -v make >/dev/null 2>&1; then
      if [[ -f './example' ]]; then
        make && ./example
      else
        echo -e "${red}Unable to build executable target: \"example\"${reset}"
        exit 1
      fi
    else
      echo -e "${bred}You do not have make installed. ${reset}"
      exit 1
    fi
  fi
fi
