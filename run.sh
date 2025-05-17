#!/usr/bin/env bash
#
# Usage:
#   ./run.sh <function name>

: ${LIB_OSH=../oils/stdlib/osh}
source $LIB_OSH/task-five.sh

update-big() {
  local path=_gen/bin/oils_for_unix.mycpp.cc
  cp -v ../oils/$path $path
}

update-all() {
  mkdir -p _tmp
  local tmp_tar=$PWD/_tmp/oils.tar  # absolute path

  pushd ../oils

  # This builds mycpp/examples
  mycpp/TEST.sh ex-gcalways

  # This builds the files we'll release
  devtools/release-native.sh make-tar

  find _gen -name '*.mycpp.cc' -o -name '*.mycpp-souffle.cc' |
    xargs tar --create --file $tmp_tar

  popd

  tar --extract < $tmp_tar
}

diff-souffle() {
  local diff=${1:-diff -u}

  $diff _gen/bin/oils_for_unix.{mycpp,mycpp-souffle}.cc
}

task-five "$@"
