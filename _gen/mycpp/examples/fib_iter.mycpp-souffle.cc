// _gen/mycpp/examples/fib_iter.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace fib_iter {  // forward declare
}


namespace fib_iter {  // declare

int fib_iter(int n);
void run_tests();
void run_benchmarks();

}  // declare namespace fib_iter

namespace fib_iter {  // define


int fib_iter(int n) {
  int a;
  int b;
  int i;
  int tmp;
  a = 0;
  b = 1;
  i = 0;
  while (i < n) {
    tmp = (a + b);
    a = b;
    b = tmp;
    i += 1;
  }
  return b;
}

void run_tests() {
  int x;
  int result;
  x = 33;
  result = fib_iter(x);
  mylib::print_stderr(StrFormat("fib_iter(%d) = %d", x, result));
}

void run_benchmarks() {
  int n;
  int x;
  int result;
  int i;
  n = 500000;
  x = 33;
  result = -1;
  i = 0;
  while (i < n) {
    result = fib_iter(x);
    i += 1;
  }
  mylib::print_stderr(StrFormat("fib_iter(%d) = %d", x, result));
  mylib::print_stderr(StrFormat("Ran %d iterations of fib_iter", n));
}

}  // define namespace fib_iter

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    fib_iter::run_benchmarks();
  } else {
    fib_iter::run_tests();
  }

  gHeap.CleanProcessExit();
}
