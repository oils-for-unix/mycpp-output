// _gen/mycpp/examples/varargs.mycpp.cc - generated from Python source code

#include "mycpp/examples/varargs_preamble.h"

// BEGIN mycpp output
namespace varargs {  // forward declare
}

GLOBAL_STR(S_mch, " \"repr\"");
GLOBAL_STR(S_oBf, "'repr'");
GLOBAL_STR(S_uay, "LL");
GLOBAL_STR(S_jCe, "constant string");
GLOBAL_STR(S_okc, "stderr_line");
GLOBAL_STR(S_mxm, "string");

namespace varargs {  // declare

void run_tests();
void run_benchmarks();

}  // declare namespace varargs

namespace varargs {  // define

using mylib::print_stderr;

void run_tests() {
  mylib::print_stderr(S_jCe);
  print_stderr(S_okc);
  mylib::print_stderr(StrFormat("log %d %s", 42, S_uay));
  mylib::print_stderr(StrFormat("[%%] %d %s", 42, S_uay));
}

void run_benchmarks() {
  BigStr* r = nullptr;
  StackRoot _root0(&r);

  r = str_concat(S_oBf, S_mch);
  for (int i = 0; i < 10000; ++i) {
    mylib::print_stderr(StrFormat("[%%] %d %s %r", 123456789, S_mxm, r));
  }
}

}  // define namespace varargs

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
