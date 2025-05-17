// _gen/mycpp/examples/test_ctx_pattern.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace test_ctx_pattern {  // forward declare
  class ctx_Eval;
}

GLOBAL_STR(S_rqD, "x");
GLOBAL_STR(S_vCs, "y");

namespace test_ctx_pattern {  // declare

class ctx_Eval {
 public:
  ctx_Eval(Dict<BigStr*, BigStr*>* vars);
  ~ctx_Eval();
  Dict<BigStr*, BigStr*>* vars{};
  List<BigStr*>* restore{};

  DISALLOW_COPY_AND_ASSIGN(ctx_Eval)
};

void run_tests();
void run_benchmarks();

}  // declare namespace test_ctx_pattern

namespace test_ctx_pattern {  // define


ctx_Eval::ctx_Eval(Dict<BigStr*, BigStr*>* vars) {
  gHeap.PushRoot(reinterpret_cast<RawObject**>(&(this->restore)));
  gHeap.PushRoot(reinterpret_cast<RawObject**>(&(this->vars)));
  this->vars = vars;
  if (vars != nullptr) {
    this->restore = Alloc<List<BigStr*>>();
    this->restore->append(S_rqD);
  }
  mylib::MaybeCollect();
}

ctx_Eval::~ctx_Eval() {
  if (this->vars != nullptr) {
    this->restore->pop();
  }
  gHeap.PopRoot();
  gHeap.PopRoot();
}

void run_tests() {
  Dict<BigStr*, BigStr*>* d = nullptr;
  d = Alloc<Dict<BigStr*, BigStr*>>(std::initializer_list<BigStr*>{S_rqD}, std::initializer_list<BigStr*>{S_vCs});
  for (int i = 0; i < 1000; ++i) {
    {  // with
      ctx_Eval ctx{nullptr};

      print(StrFormat("none %d", i));
    }
  }
}

void run_benchmarks() {
  ;  // pass
}

}  // define namespace test_ctx_pattern

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_ctx_pattern::run_benchmarks();
  } else {
    test_ctx_pattern::run_tests();
  }

  gHeap.CleanProcessExit();
}
