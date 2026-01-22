#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mycpp/runtime.h"

namespace test_small_str {
void run_tests();
void run_benchmarks();
}

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
