// _gen/mycpp/examples/test_integers.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace test_integers {  // forward declare
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_Alb, "ok");
GLOBAL_STR(S_sbi, "round trip equal");

namespace test_integers {  // declare

void run_tests();
void run_benchmarks();

}  // declare namespace test_integers

namespace test_integers {  // define


void run_tests() {
  int a;
  mops::BigInt i1;
  mops::BigInt i2;
  mops::BigInt i3;
  mops::BigInt i4;
  mops::BigInt x;
  mops::BigInt y;
  mops::BigInt max_positive;
  mops::BigInt z;
  mops::BigInt max_negative;
  BigStr* s1 = nullptr;
  bool ok;
  mops::BigInt max_negative2;
  mops::BigInt big;
  int small;
  a = (3 + 2);
  print(StrFormat("a = %d", a));
  i1 = mops::LShift(mops::BigInt(1), mops::BigInt(31));
  i2 = mops::Add(i1, i1);
  i3 = mops::Add(i2, i1);
  print(StrFormat("i1 = %s", mops::ToStr(i1)));
  print(StrFormat("i2 = %s", mops::ToStr(i2)));
  print(StrFormat("i3 = %s", mops::ToStr(i3)));
  print(S_Aoo);
  i4 = mops::LShift(mops::BigInt(1), mops::BigInt(63));
  x = mops::LShift(mops::BigInt(1), mops::BigInt(62));
  y = mops::Sub(x, mops::BigInt(1));
  max_positive = mops::Add(x, y);
  print(StrFormat("max_positive = %s", mops::ToStr(max_positive)));
  z = mops::Sub(mops::BigInt(0), x);
  max_negative = mops::Sub(z, x);
  print(StrFormat("max_negative = %s", mops::ToStr(max_negative)));
  s1 = mops::ToStr(max_negative);
  print(StrFormat("max_negative string = %s", s1));
  Tuple2<bool, mops::BigInt> tup0 = mops::FromStr2(s1);
  ok = tup0.at0();
  max_negative2 = tup0.at1();
  print(StrFormat("max_negative2 = %s", mops::ToStr(max_negative2)));
  if (ok) {
    print(S_Alb);
  }
  if (mops::Equal(max_negative, max_negative2)) {
    print(S_sbi);
  }
  big = mops::IntWiden(a);
  print(StrFormat("big = %s", mops::ToStr(big)));
  small = mops::BigTruncate(big);
  print(StrFormat("small = %d", small));
}

void run_benchmarks() {
  ;  // pass
}

}  // define namespace test_integers

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_integers::run_benchmarks();
  } else {
    test_integers::run_tests();
  }

  gHeap.CleanProcessExit();
}
