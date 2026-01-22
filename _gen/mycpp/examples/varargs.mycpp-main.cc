#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mycpp/runtime.h"

namespace varargs {
void run_tests();
void run_benchmarks();
}

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    varargs::run_benchmarks();
  } else {
    varargs::run_tests();
  }

  gHeap.CleanProcessExit();
}
