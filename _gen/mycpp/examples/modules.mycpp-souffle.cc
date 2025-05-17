// _gen/mycpp/examples/modules.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace module1 {  // forward declare
  class Cat;
}

namespace module2 {  // forward declare
}

namespace modules {  // forward declare
  class Dog;
  class Sphinx;
}

GLOBAL_STR(S_edf, "CONST module1");
GLOBAL_STR(S_yCx, "CONST module2");
GLOBAL_STR(S_mxp, "abstract");
GLOBAL_STR(S_ruz, "brown");
GLOBAL_STR(S_Deg, "cat");
GLOBAL_STR(S_odg, "func1");
GLOBAL_STR(S_nAe, "func2");
GLOBAL_STR(S_scd, "white");

namespace module1 {  // declare

extern BigStr* CONST1;
void func1();
int fortytwo();
class Cat {
 public:
  Cat();
  virtual void Speak();
  virtual void AbstractMethod();
  
  static constexpr uint32_t field_mask() {
    return kZeroMask;
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(Cat));
  }

  DISALLOW_COPY_AND_ASSIGN(Cat)
};


}  // declare namespace module1

namespace module2 {  // declare

extern BigStr* CONST2;
void func2();

}  // declare namespace module2

namespace modules {  // declare

void run_tests();
void run_benchmarks();
class Dog {
 public:
  Dog(BigStr* color);
  void Speak();
  BigStr* color{};

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassScanned(1, sizeof(Dog));
  }

  DISALLOW_COPY_AND_ASSIGN(Dog)
};

class Sphinx : public ::module1::Cat {
 public:
  Sphinx(BigStr* color);
  virtual void Speak();
  virtual void AbstractMethod();

  BigStr* color{};
  
  static constexpr uint32_t field_mask() {
    return ::module1::Cat::field_mask()
         | maskbit(offsetof(Sphinx, color));
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(Sphinx));
  }

  DISALLOW_COPY_AND_ASSIGN(Sphinx)
};


}  // declare namespace modules

namespace module1 {  // define

BigStr* CONST1 = S_edf;

void func1() {
  mylib::print_stderr(S_odg);
  mylib::print_stderr(module2::CONST2);
}

int fortytwo() {
  return 42;
}

Cat::Cat() {
  ;  // pass
}

void Cat::Speak() {
  mylib::print_stderr(S_Deg);
}

void Cat::AbstractMethod() {
  FAIL(kNotImplemented);  // Python NotImplementedError
}

}  // define namespace module1

namespace module2 {  // define

BigStr* CONST2 = S_yCx;

void func2() {
  mylib::print_stderr(S_nAe);
  mylib::print_stderr(module1::CONST1);
}

}  // define namespace module2

namespace modules {  // define

using module2::func2;

void run_tests() {
  modules::Dog* dog = nullptr;
  module1::Cat* cat = nullptr;
  modules::Sphinx* cat2 = nullptr;
  module1::func1();
  func2();
  dog = Alloc<Dog>(S_scd);
  dog->Speak();
  cat = Alloc<module1::Cat>();
  cat->Speak();
  cat2 = Alloc<Sphinx>(S_ruz);
  cat2->Speak();
  cat = cat2;
  cat->Speak();
  cat->AbstractMethod();
}

void run_benchmarks() {
  int i;
  int n;
  int result;
  i = 0;
  n = 2000000;
  result = 0;
  while (i < n) {
    result += module1::fortytwo();
    i = (i + 1);
  }
  mylib::print_stderr(StrFormat("result = %d", result));
}

Dog::Dog(BigStr* color) {
  this->color = color;
}

void Dog::Speak() {
  mylib::print_stderr(StrFormat("%s dog: meow", this->color));
}

Sphinx::Sphinx(BigStr* color) : ::module1::Cat() {
  this->color = color;
}

void Sphinx::Speak() {
  mylib::print_stderr(StrFormat("%s sphinx", this->color));
}

void Sphinx::AbstractMethod() {
  mylib::print_stderr(S_mxp);
}

}  // define namespace modules

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    modules::run_benchmarks();
  } else {
    modules::run_tests();
  }

  gHeap.CleanProcessExit();
}
