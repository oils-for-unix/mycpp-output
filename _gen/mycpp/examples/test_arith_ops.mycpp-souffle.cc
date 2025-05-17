// _gen/mycpp/examples/test_arith_ops.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
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

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_arith_ops::run_benchmarks();
  } else {
    test_arith_ops::run_tests();
  }

  gHeap.CleanProcessExit();
}
