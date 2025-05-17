// _gen/mycpp/examples/fib_recursive.mycpp.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace fib_recursive {  // forward declare
}


namespace fib_recursive {  // declare

int fib_recursive(int n);
void run_tests();
void run_benchmarks();

}  // declare namespace fib_recursive

namespace fib_recursive {  // define


int fib_recursive(int n) {
  if (n == 0) {
    return 1;
  }
  if (n == 1) {
    return 1;
  }
  return (fib_recursive((n - 1)) + fib_recursive((n - 2)));
}

void run_tests() {
  int x;
  int result;
  x = 33;
  result = fib_recursive(x);
  mylib::print_stderr(StrFormat("fib_recursive(%d) = %d", x, result));
}

void run_benchmarks() {
  int n;
  int x;
  int result;
  int i;
  n = 1;
  x = 33;
  result = -1;
  i = 0;
  while (i < n) {
    result = fib_recursive(x);
    i += 1;
  }
  mylib::print_stderr(StrFormat("fib_recursive(%d) = %d", x, result));
}

}  // define namespace fib_recursive

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    fib_recursive::run_benchmarks();
  } else {
    fib_recursive::run_tests();
  }

  gHeap.CleanProcessExit();
}
