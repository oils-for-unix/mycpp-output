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

files-to-copy() {
  find _gen -type f -a -print
  find _devbuild/gen -name '*.pyc' -o -type f -a -print

  # Note: we don't have _gen/_tmp in the tarball
  # Could add that
}

update-from-tar() {
  mkdir -p _tmp
  local tmp_tar=$PWD/_tmp/oils.tar  # absolute path

  pushd ../oils

  # This builds mycpp/examples
  mycpp/TEST.sh ex-gcalways

  # This builds the files we'll release
  devtools/release-native.sh make-tar

  files-to-copy | xargs tar --create --file $tmp_tar

  popd

  tar --extract < $tmp_tar
}

update-souffle() {
  pushd ../oils

  local gen=_gen/bin/oils_for_unix.mycpp-souffle.cc
  ninja $gen
  cp -v $gen ../mycpp-output/$gen  # this repo

  popd
}

diff-souffle() {
  local diff=${1:-diff -u}

  $diff _gen/bin/oils_for_unix.{mycpp,mycpp-nosouffle}.cc
}

task-five "$@"
