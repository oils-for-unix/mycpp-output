// _gen/mycpp/examples/cgi.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace cgi {  // forward declare
}

GLOBAL_STR(S_krt, "\"");
GLOBAL_STR(S_Clt, "&");
GLOBAL_STR(S_usD, "&amp;");
GLOBAL_STR(S_dyr, "&gt;");
GLOBAL_STR(S_Dcl, "&lt;");
GLOBAL_STR(S_cFo, "&quot;");
GLOBAL_STR(S_eox, "<");
GLOBAL_STR(S_pay, "<html>");
GLOBAL_STR(S_jye, ">");
GLOBAL_STR(S_awm, "X");
GLOBAL_STR(S_iyu, "\\");
GLOBAL_STR(S_jrm, "\\d+");
GLOBAL_STR(S_rqD, "x");
GLOBAL_STR(S_lmB, "xo--xo");

namespace cgi {  // declare

extern BigStr* BACKSLASH;
extern BigStr* RAW_BACKSLASH;
BigStr* escape(BigStr* s, bool quote = false);
void run_tests();
void run_benchmarks();

}  // declare namespace cgi

namespace cgi {  // define

BigStr* BACKSLASH = S_iyu;
BigStr* RAW_BACKSLASH = S_jrm;

BigStr* escape(BigStr* s, bool quote) {
  s = s->replace(S_Clt, S_usD);
  s = s->replace(S_eox, S_Dcl);
  s = s->replace(S_jye, S_dyr);
  if (quote) {
    s = s->replace(S_krt, S_cFo);
  }
  return s;
}

void run_tests() {
  BigStr* mystr = nullptr;
  mystr = S_lmB;
  mylib::print_stderr(StrFormat("s: %s", mystr));
  mylib::print_stderr(StrFormat("escaped: %s", escape(S_pay, true)));
  mylib::print_stderr(StrFormat("%s\n", mystr->replace(S_rqD, S_awm)));
}

void run_benchmarks() {
  int i;
  int n;
  i = 0;
  n = 1000000;
  while (i < n) {
    escape(S_pay, true);
    i = (i + 1);
    mylib::MaybeCollect();
  }
}

}  // define namespace cgi

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    cgi::run_benchmarks();
  } else {
    cgi::run_tests();
  }

  gHeap.CleanProcessExit();
}
