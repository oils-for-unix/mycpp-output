// This file is GENERATED by mycpp, from Python source code

#include "mycpp/runtime.h"

namespace test_hoist {  // forward declare
}

GLOBAL_STR(S_Aru, ".");
GLOBAL_STR(S_lqB, "foo");
GLOBAL_STR(S_xrC, "global string");
GLOBAL_STR(S_pee, "greater");
GLOBAL_STR(S_lyq, "less");

namespace test_hoist {  // declare

BigStr* f(BigStr* s);
extern BigStr* S;
void g();
BigStr* strfunc(BigStr* s);
void run_tests();
void run_benchmarks();

}  // declare namespace test_hoist

namespace test_hoist {  // define


BigStr* f(BigStr* s) {
  int x;
  x = 1;
  if (x > 0) {
    s = S_pee;
  }
  else {
    s = S_lyq;
  }
  print(s);
  return s;
}
BigStr* S = S_xrC;

void g() {
  print(S);
}

BigStr* strfunc(BigStr* s) {
  return str_concat(s, S_Aru);
}

void run_tests() {
  f(S_lqB);
  g();
}

void run_benchmarks() {
  FAIL(kNotImplemented);  // Python NotImplementedError
}

}  // define namespace test_hoist

