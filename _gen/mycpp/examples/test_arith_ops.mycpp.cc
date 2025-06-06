// This file is GENERATED by mycpp, from Python source code

#include "mycpp/runtime.h"

namespace test_arith_ops {  // forward declare
}

GLOBAL_STR(S_Aoo, "");

namespace test_arith_ops {  // declare

void run_tests();
void run_benchmarks();

}  // declare namespace test_arith_ops

namespace test_arith_ops {  // define


void run_tests() {
  for (int i = 0; i < 8; ++i) {
    mylib::print_stderr(StrFormat("%d // 3 = %d", i, (i / 3)));
  }
  mylib::print_stderr(S_Aoo);
}

void run_benchmarks() {
  ;  // pass
}

}  // define namespace test_arith_ops

