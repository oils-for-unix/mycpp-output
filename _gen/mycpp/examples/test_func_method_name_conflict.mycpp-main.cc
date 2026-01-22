#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mycpp/runtime.h"

namespace test_func_method_name_conflict {
void run_tests();
void run_benchmarks();
}

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_func_method_name_conflict::run_benchmarks();
  } else {
    test_func_method_name_conflict::run_tests();
  }

  gHeap.CleanProcessExit();
}
