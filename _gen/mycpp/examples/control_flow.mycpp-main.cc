#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mycpp/runtime.h"

namespace control_flow {
void run_tests();
void run_benchmarks();
}

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    control_flow::run_benchmarks();
  } else {
    control_flow::run_tests();
  }

  gHeap.CleanProcessExit();
}
