// _gen/mycpp/examples/asdl_generated.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace asdl_generated {  // forward declare
  class arith_expr_t;
  class arith_expr__Const;
}


namespace asdl_generated {  // declare

class arith_expr_t {
 public:
  arith_expr_t();
  
  static constexpr uint32_t field_mask() {
    return kZeroMask;
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(arith_expr_t));
  }

  DISALLOW_COPY_AND_ASSIGN(arith_expr_t)
};

class arith_expr__Const : public ::asdl_generated::arith_expr_t {
 public:
  arith_expr__Const(int i);

  int i{};
  
  static constexpr uint32_t field_mask() {
    return ::asdl_generated::arith_expr_t::field_mask();
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(arith_expr__Const));
  }

  DISALLOW_COPY_AND_ASSIGN(arith_expr__Const)
};

void run_tests();
void run_benchmarks();

}  // declare namespace asdl_generated

namespace asdl_generated {  // define


arith_expr_t::arith_expr_t() {
  ;  // pass
}

arith_expr__Const::arith_expr__Const(int i) : ::asdl_generated::arith_expr_t() {
  this->i = i;
}

void run_tests() {
  asdl_generated::arith_expr__Const* x = nullptr;
  x = Alloc<arith_expr__Const>(5);
  mylib::print_stderr(StrFormat("x = %d", x->i));
}

void run_benchmarks() {
  int i;
  int n;
  asdl_generated::arith_expr__Const* x = nullptr;
  i = 0;
  n = 1000000;
  while (i < n) {
    x = Alloc<arith_expr__Const>(i);
    i = (i + 1);
    mylib::MaybeCollect();
  }
}

}  // define namespace asdl_generated

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    asdl_generated::run_benchmarks();
  } else {
    asdl_generated::run_tests();
  }

  gHeap.CleanProcessExit();
}
