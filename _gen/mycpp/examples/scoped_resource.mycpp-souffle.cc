// _gen/mycpp/examples/scoped_resource.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace scoped_resource {  // forward declare
  class MyError;
  class ctx_BadName;
  class ctx_NoArgs;
  class ctx_DirStack;
  class DirStack;
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_kEC, "< NoArgs");
GLOBAL_STR(S_zrp, "> NoArgs");
GLOBAL_STR(S_mrf, "CWD");
GLOBAL_STR(S_Dsq, "exception");
GLOBAL_STR(S_zCe, "exited with exception");
GLOBAL_STR(S_lqB, "foo");
GLOBAL_STR(S_cEk, "hi");

namespace scoped_resource {  // declare

class MyError {
 public:
  MyError();

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassScanned(0, sizeof(MyError));
  }

  DISALLOW_COPY_AND_ASSIGN(MyError)
};

void Error(bool error);
class ctx_BadName {
 public:
  ctx_BadName();
  ~ctx_BadName();
  int i{};

  DISALLOW_COPY_AND_ASSIGN(ctx_BadName)
};

class ctx_NoArgs {
 public:
  ctx_NoArgs();
  ~ctx_NoArgs();

  DISALLOW_COPY_AND_ASSIGN(ctx_NoArgs)
};

class ctx_DirStack {
 public:
  ctx_DirStack(scoped_resource::DirStack* state, BigStr* entry);
  ~ctx_DirStack();
  scoped_resource::DirStack* state{};
  List<BigStr*>* restored{};
  int non_pointer_member{};

  DISALLOW_COPY_AND_ASSIGN(ctx_DirStack)
};

class DirStack {
 public:
  DirStack();
  void Reset();
  void Push(BigStr* entry);
  BigStr* Pop();
  List<BigStr*>* Iter();
  List<BigStr*>* stack{};

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassScanned(1, sizeof(DirStack));
  }

  DISALLOW_COPY_AND_ASSIGN(DirStack)
};

void DoWork(scoped_resource::DirStack* d, bool do_raise);
void run_tests();
void run_benchmarks();

}  // declare namespace scoped_resource

namespace scoped_resource {  // define


MyError::MyError() {
  ;  // pass
}

void Error(bool error) {
  if (error) {
    throw Alloc<MyError>();
  }
}

ctx_BadName::ctx_BadName() {
  this->i = 42;
}

ctx_BadName::~ctx_BadName() {
  this->i = 43;
}

ctx_NoArgs::ctx_NoArgs() {
  print(S_zrp);
}

ctx_NoArgs::~ctx_NoArgs() {
  print(S_kEC);
}

ctx_DirStack::ctx_DirStack(scoped_resource::DirStack* state, BigStr* entry) {
  gHeap.PushRoot(reinterpret_cast<RawObject**>(&(this->restored)));
  gHeap.PushRoot(reinterpret_cast<RawObject**>(&(this->state)));
  this->state = state;
  state->Push(entry);
  this->restored = Alloc<List<BigStr*>>();
  this->restored->append(S_lqB);
  this->non_pointer_member = 42;
}

ctx_DirStack::~ctx_DirStack() {
  this->restored->pop();
  this->state->Pop();
  gHeap.PopRoot();
  gHeap.PopRoot();
}

DirStack::DirStack() {
  this->stack = Alloc<List<BigStr*>>();
  this->Reset();
}

void DirStack::Reset() {
  this->stack->clear();
  this->stack->append(S_mrf);
}

void DirStack::Push(BigStr* entry) {
  this->stack->append(entry);
}

BigStr* DirStack::Pop() {
  if (len(this->stack) <= 1) {
    return nullptr;
  }
  this->stack->pop();
  return this->stack->at(-1);
}

List<BigStr*>* DirStack::Iter() {
  List<BigStr*>* ret = nullptr;
  ret = Alloc<List<BigStr*>>();
  ret->extend(this->stack);
  ret->reverse();
  return ret;
}

void DoWork(scoped_resource::DirStack* d, bool do_raise) {
  {  // with
    ctx_DirStack ctx{d, S_lqB};

    mylib::print_stderr(StrFormat("  in context stack %d", len(d->stack)));
    if (do_raise) {
      Error(do_raise);
    }
  }
}

void run_tests() {
  scoped_resource::DirStack* d = nullptr;
  d = Alloc<DirStack>();
  for (ListIter<bool> it(NewList<bool>(std::initializer_list<bool>{false, true})); !it.Done(); it.Next()) {
    bool do_raise = it.Value();
    mylib::print_stderr(S_Aoo);
    mylib::print_stderr(StrFormat("-> dir stack %d", len(d->stack)));
    try {
      DoWork(d, do_raise);
    }
    catch (MyError*) {
      mylib::print_stderr(S_zCe);
    }
    mylib::print_stderr(StrFormat("<- dir stack %d", len(d->stack)));
  }
  {  // with
    ctx_NoArgs ctx{};

    print(S_cEk);
  }
}

void run_benchmarks() {
  scoped_resource::DirStack* d = nullptr;
  StackRoot _root0(&d);

  d = Alloc<DirStack>();
  for (int i = 0; i < 1000000; ++i) {
    try {
      {  // with
        ctx_DirStack ctx{d, S_lqB};

        mylib::MaybeCollect();
        if ((i % 10000) == 0) {
          throw Alloc<MyError>();
        }
      }
    }
    catch (MyError*) {
      mylib::print_stderr(S_Dsq);
    }
  }
}

}  // define namespace scoped_resource

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    scoped_resource::run_benchmarks();
  } else {
    scoped_resource::run_tests();
  }

  gHeap.CleanProcessExit();
}
