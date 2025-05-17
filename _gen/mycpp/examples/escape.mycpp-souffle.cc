// _gen/mycpp/examples/escape.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace escape {  // forward declare
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_Fgw, "*");
GLOBAL_STR(S_Aru, ".");
GLOBAL_STR(S_wto, "NOT IN *");
GLOBAL_STR(S_bma, "NOT IN .");
GLOBAL_STR(S_iyu, "\\");
GLOBAL_STR(S_Dvk, "\\*?[]-:!");
GLOBAL_STR(S_smA, "echo *.[ch] *.?");

namespace escape {  // declare

BigStr* BackslashEscape(BigStr* s, BigStr* meta_chars);
extern BigStr* GLOB_META_CHARS;
void TestNotIn();
void run_tests();
void run_benchmarks();

}  // declare namespace escape

namespace escape {  // define


BigStr* BackslashEscape(BigStr* s, BigStr* meta_chars) {
  List<BigStr*>* escaped = nullptr;
  escaped = Alloc<List<BigStr*>>();
  for (StrIter it(s); !it.Done(); it.Next()) {
    BigStr* c = it.Value();
    if (str_contains(meta_chars, c)) {
      escaped->append(S_iyu);
    }
    escaped->append(c);
  }
  return S_Aoo->join(escaped);
}
BigStr* GLOB_META_CHARS = S_Dvk;

void TestNotIn() {
  if (!str_contains(GLOB_META_CHARS, S_Aru)) {
    print(S_bma);
  }
  if (!str_contains(GLOB_META_CHARS, S_Fgw)) {
    print(S_wto);
  }
}

void run_tests() {
  mylib::print_stderr(StrFormat("result: %s", BackslashEscape(S_smA, GLOB_META_CHARS)));
  TestNotIn();
}

void run_benchmarks() {
  int i;
  int n;
  BigStr* s = nullptr;
  i = 0;
  n = 200000;
  while (i < n) {
    s = S_smA;
    BackslashEscape(s, GLOB_META_CHARS);
    i = (i + 1);
    mylib::MaybeCollect();
  }
}

}  // define namespace escape

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    escape::run_benchmarks();
  } else {
    escape::run_tests();
  }

  gHeap.CleanProcessExit();
}
