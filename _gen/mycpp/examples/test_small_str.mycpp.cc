// _gen/mycpp/examples/test_small_str.mycpp.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace test_small_str {  // forward declare
}

GLOBAL_STR(S_zbt, "food");

namespace test_small_str {  // declare

BigStr* f(BigStr* s);
void run_tests();
void run_benchmarks();

}  // declare namespace test_small_str

namespace test_small_str {  // define


BigStr* f(BigStr* s) {
  StackRoot _root0(&s);

  return s->at(1)->upper();
}

void run_tests() {
  BigStr* a = nullptr;
  StackRoot _root0(&a);

  a = S_zbt;
  print(a->upper());
  print(f(a));
}

void run_benchmarks() {
  ;  // pass
}

}  // define namespace test_small_str

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_small_str::run_benchmarks();
  } else {
    test_small_str::run_tests();
  }

  gHeap.CleanProcessExit();
}
