// _gen/mycpp/examples/test_io_os_error.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace test_io_os_error {  // forward declare
  class ctx_TerminalControl;
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_FcA, "TerminalControl exit");
GLOBAL_STR(S_fko, "TerminalControl init");
GLOBAL_STR(S_vwC, "TestDestructor");
GLOBAL_STR(S_dmc, "Throw and Catch within destructor seems OK");
GLOBAL_STR(S_cEk, "hi");
GLOBAL_STR(S_epA, "osh I/O error (main)");

namespace test_io_os_error {  // declare

void Close(int fd);
void Pop(int fd);
int AppBundleMain(List<BigStr*>* argv);
int TestRethrow();
class ctx_TerminalControl {
 public:
  ctx_TerminalControl();
  ~ctx_TerminalControl();

  DISALLOW_COPY_AND_ASSIGN(ctx_TerminalControl)
};

void TestDestructor();
int run_tests();
void run_benchmarks();

}  // declare namespace test_io_os_error

namespace test_io_os_error {  // define

using mylib::print_stderr;

void Close(int fd) {
  throw Alloc<OSError>(0);
}

void Pop(int fd) {
  try {
    Close(fd);
  }
  catch (IOError_OSError* e) {
    mylib::print_stderr(StrFormat("Error closing descriptor %d", fd));
    throw;
  }
}

int AppBundleMain(List<BigStr*>* argv) {
  Pop(3);
  return 0;
}

int TestRethrow() {
  List<BigStr*>* argv = nullptr;
  argv = Alloc<List<BigStr*>>();
  try {
    return AppBundleMain(argv);
  }
  catch (ValueError* e) {
    return 2;
  }
  catch (KeyboardInterrupt*) {
    print(S_Aoo);
    return 130;
  }
  catch (IOError_OSError* e) {
    print_stderr(S_epA);
    return 2;
  }
}

ctx_TerminalControl::ctx_TerminalControl() {
  mylib::print_stderr(S_fko);
}

ctx_TerminalControl::~ctx_TerminalControl() {
  mylib::print_stderr(S_FcA);
  TestRethrow();
  mylib::print_stderr(S_dmc);
}

void TestDestructor() {
  {  // with
    ctx_TerminalControl ctx{};

    mylib::print_stderr(S_cEk);
  }
}

int run_tests() {
  TestRethrow();
  mylib::print_stderr(S_Aoo);
  mylib::print_stderr(S_vwC);
  mylib::print_stderr(S_Aoo);
  TestDestructor();
  return 0;
}

void run_benchmarks() {
  FAIL(kNotImplemented);  // Python NotImplementedError
}

}  // define namespace test_io_os_error

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_io_os_error::run_benchmarks();
  } else {
    test_io_os_error::run_tests();
  }

  gHeap.CleanProcessExit();
}
