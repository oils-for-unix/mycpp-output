// _gen/mycpp/examples/length.mycpp.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace length {  // forward declare
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_gCD, "a");
GLOBAL_STR(S_buF, "abcd");
GLOBAL_STR(S_jFv, "b");
GLOBAL_STR(S_clt, "bar");
GLOBAL_STR(S_emj, "c");
GLOBAL_STR(S_lqB, "foo");
GLOBAL_STR(S_pfC, "w");
GLOBAL_STR(S_rqD, "x");
GLOBAL_STR(S_vCs, "y");
GLOBAL_STR(S_zjx, "z");

namespace length {  // declare

void TestMaybeStrEquals();
void run_tests();
void run_benchmarks();

}  // declare namespace length

namespace length {  // define


void TestMaybeStrEquals() {
  BigStr* a = nullptr;
  BigStr* b = nullptr;
  BigStr* y = nullptr;
  BigStr* n = nullptr;
  StackRoot _root0(&a);
  StackRoot _root1(&b);
  StackRoot _root2(&y);
  StackRoot _root3(&n);

  a = S_lqB;
  b = S_clt;
  y = S_lqB;
  n = nullptr;
  mylib::print_stderr(StrFormat("a == b  ->  %d", str_equals(a, b)));
  mylib::print_stderr(StrFormat("a != b  ->  %d", !(str_equals(a, b))));
  mylib::print_stderr(StrFormat("a == y  ->  %d", maybe_str_equals(a, y)));
  mylib::print_stderr(StrFormat("a != y  ->  %d", !(maybe_str_equals(a, y))));
  mylib::print_stderr(StrFormat("a == n  ->  %d", maybe_str_equals(a, n)));
  mylib::print_stderr(StrFormat("a != n  ->  %d", !(maybe_str_equals(a, n))));
}

void run_tests() {
  BigStr* mystr = nullptr;
  List<BigStr*>* mylist = nullptr;
  BigStr* c2 = nullptr;
  StackRoot _root0(&mystr);
  StackRoot _root1(&mylist);
  StackRoot _root2(&c2);

  mystr = S_buF;
  mylib::print_stderr(StrFormat("len(mystr) = %d", len(mystr)));
  mylib::print_stderr(StrFormat("mystr[1] = %s", mystr->at(1)));
  mylib::print_stderr(StrFormat("mystr[1:] = %s", mystr->slice(1)));
  mylib::print_stderr(StrFormat("mystr[1:3] = %s", mystr->slice(1, 3)));
  mylib::print_stderr(StrFormat("mystr[:-2] = %s", mystr->slice(0, -2)));
  for (StrIter it(mystr); !it.Done(); it.Next()) {
    BigStr* c = it.Value();
    StackRoot _for(&c  );
    if (str_equals(c, S_jFv)) {
      continue;
    }
    mylib::print_stderr(StrFormat("c = %s", c));
    if (str_equals(c, S_emj)) {
      break;
    }
  }
  mylib::print_stderr(S_Aoo);
  mylist = NewList<BigStr*>(std::initializer_list<BigStr*>{S_pfC, S_rqD, S_vCs, S_zjx});
  mylib::print_stderr(StrFormat("len(mylist) = %d", len(mylist)));
  mylib::print_stderr(StrFormat("mylist[1] = %s", mylist->at(1)));
  mylib::print_stderr(StrFormat("len(mylist[1:]) = %d", len(mylist->slice(1))));
  for (ListIter<BigStr*> it(mylist); !it.Done(); it.Next()) {
    BigStr* c = it.Value();
    StackRoot _for(&c  );
    if (str_equals(c, S_rqD)) {
      continue;
    }
    mylib::print_stderr(StrFormat("c = %s", c));
    if (str_equals(c, S_vCs)) {
      break;
    }
  }
  c2 = nullptr;
  for (StrIter it(mystr); !it.Done(); it.Next()) {
    BigStr* c2 = it.Value();
    StackRoot _for(&c2  );
    if (!(str_equals(c2, S_gCD))) {
      mylib::print_stderr(StrFormat("%s != a", c2));
    }
  }
  mylib::print_stderr(S_Aoo);
  TestMaybeStrEquals();
}

void run_benchmarks() {
  int n;
  BigStr* mystr = nullptr;
  List<BigStr*>* mylist = nullptr;
  int result;
  int i;
  StackRoot _root0(&mystr);
  StackRoot _root1(&mylist);

  n = 1000000;
  mystr = S_buF;
  mylist = NewList<BigStr*>(std::initializer_list<BigStr*>{S_pfC, S_rqD, S_vCs, S_zjx});
  result = 0;
  i = 0;
  while (i < n) {
    result += len(mystr->slice(1));
    result += len(mylist->slice(1));
    i += 1;
    mylib::MaybeCollect();
  }
  mylib::print_stderr(StrFormat("result = %d", result));
  mylib::print_stderr(StrFormat("iterations = %d", n));
}

}  // define namespace length

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    length::run_benchmarks();
  } else {
    length::run_tests();
  }

  gHeap.CleanProcessExit();
}
