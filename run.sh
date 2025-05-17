#!/usr/bin/env bash
#
# Usage:
#   ./run.sh <function name>

: ${LIB_OSH=../oils/stdlib/osh}
source $LIB_OSH/task-five.sh

update-golden() {
  local path=_gen/bin/oils_for_unix.mycpp.cc
  cp -v ../oils/$path $path
}

task-five "$@"
