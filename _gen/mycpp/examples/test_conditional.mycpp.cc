// _gen/mycpp/examples/test_conditional.mycpp.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace test_conditional {  // forward declare
}

GLOBAL_STR(S_akp, "123");
GLOBAL_STR(S_nDd, "CPP");
GLOBAL_STR(S_lmi, "PYTHON");
GLOBAL_STR(S_xbf, "mylist");
GLOBAL_STR(S_Dxe, "no");
GLOBAL_STR(S_Bxn, "yes");

namespace test_conditional {  // declare

void run_tests();
void run_benchmarks();

}  // declare namespace test_conditional

namespace test_conditional {  // define


void run_tests() {
  List<int>* mylist = nullptr;
  int x;
  bool a;
  StackRoot _root0(&mylist);

  // if MYCPP
  {
    mylib::print_stderr(S_nDd);
  }
  // endif MYCPP
  // if not PYTHON
  {
    mylib::print_stderr(S_lmi);
  }
  // endif MYCPP
  mylib::print_stderr(StrFormat("int = %d", to_int(S_akp)));
  mylib::print_stderr(StrFormat("bool = %d", to_bool(42)));
  mylist = Alloc<List<int>>();
  if (len(mylist)) {
    print(S_xbf);
  }
  x = len(mylist) ? 1 : 2;
  mylib::print_stderr(StrFormat("x = %d", x));
  a = false;
  if ((a and (false or true))) {
    print(S_Bxn);
  }
  else {
    print(S_Dxe);
  }
}

void run_benchmarks() {
  FAIL(kNotImplemented);  // Python NotImplementedError
}

}  // define namespace test_conditional

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_conditional::run_benchmarks();
  } else {
    test_conditional::run_tests();
  }

  gHeap.CleanProcessExit();
}
