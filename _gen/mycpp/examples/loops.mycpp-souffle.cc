// _gen/mycpp/examples/loops.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace loops {  // forward declare
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_Bjq, "-");
GLOBAL_STR(S_Axw, "-- list comp dict");
GLOBAL_STR(S_jFE, "-- list comp enumerate");
GLOBAL_STR(S_lvd, "-- list comp iteritems");
GLOBAL_STR(S_sBa, "-- list comp tuple unpacking");
GLOBAL_STR(S_xnh, "-- list comp xrange");
GLOBAL_STR(S_xqi, "-- list comprehension filtering");
GLOBAL_STR(S_jvb, "--- Dict");
GLOBAL_STR(S_oyf, "--- enumerate()");
GLOBAL_STR(S_Bxm, "--- iterate over bytes in string");
GLOBAL_STR(S_EAn, "--- iterate over items in list");
GLOBAL_STR(S_skz, "--- list comprehension");
GLOBAL_STR(S_oey, "--- list comprehension over strings");
GLOBAL_STR(S_Eie, "--- one arg xrange()");
GLOBAL_STR(S_yns, "--- reversed() list");
GLOBAL_STR(S_bdx, "--- reversed() list with tuple unpacking");
GLOBAL_STR(S_tsC, "--- three arg reverse xrange()");
GLOBAL_STR(S_Exl, "--- three arg xrange()");
GLOBAL_STR(S_nFa, "--- tuple unpacking");
GLOBAL_STR(S_tDv, "--- two arg xrange()");
GLOBAL_STR(S_gCD, "a");
GLOBAL_STR(S_jng, "abc");
GLOBAL_STR(S_jFv, "b");
GLOBAL_STR(S_ver, "big");
GLOBAL_STR(S_emj, "c");
GLOBAL_STR(S_Dne, "eggs");
GLOBAL_STR(S_nsm, "five");
GLOBAL_STR(S_yfr, "hairless");
GLOBAL_STR(S_tyE, "k");
GLOBAL_STR(S_FDA, "k2");
GLOBAL_STR(S_Epb, "one");
GLOBAL_STR(S_Ens, "six");
GLOBAL_STR(S_juD, "small");
GLOBAL_STR(S_Eow, "spam");
GLOBAL_STR(S_nfE, "two");
GLOBAL_STR(S_Ado, "v");
GLOBAL_STR(S_bfb, "v2");
GLOBAL_STR(S_DEE, "xx");
GLOBAL_STR(S_sfk, "yy");

namespace loops {  // declare

void TestListComp();
void TestListCompParity();
void TestDict();
extern List<BigStr*>* CATS;
void TestForLoop();
void run_tests();
void run_benchmarks();

}  // declare namespace loops

namespace loops {  // define


void TestListComp() {
  List<int>* x = nullptr;
  List<int>* y = nullptr;
  List<BigStr*>* z = nullptr;
  List<BigStr*>* parts = nullptr;
  List<BigStr*>* tmp = nullptr;
  List<BigStr*>* tmp2 = nullptr;
  mylib::print_stderr(S_skz);
  x = NewList<int>(std::initializer_list<int>{1, 2, 3, 4});
  y = Alloc<List<int>>();
  for (ListIter<int> it(x->slice(1)); !it.Done(); it.Next()) {
    int i = it.Value();
    y->append((i * 5));
  }
  mylib::print_stderr(StrFormat("len = %d", len(y)));
  mylib::print_stderr(StrFormat("y[0] = %d", y->at(0)));
  mylib::print_stderr(StrFormat("y[-1] = %d", y->at(-1)));
  mylib::print_stderr(S_oey);
  z = Alloc<List<BigStr*>>();
  for (ListIter<int> it(x->slice(1, -1)); !it.Done(); it.Next()) {
    int i = it.Value();
    z->append(StrFormat("[%d]", i));
  }
  mylib::print_stderr(StrFormat("len = %d", len(z)));
  mylib::print_stderr(StrFormat("z[0] = %s", z->at(0)));
  mylib::print_stderr(StrFormat("z[-1] = %s", z->at(-1)));
  mylib::print_stderr(S_xqi);
  parts = NewList<BigStr*>(std::initializer_list<BigStr*>{S_gCD, nullptr, S_jFv});
  tmp = Alloc<List<BigStr*>>();
  for (ListIter<BigStr*> it(parts); !it.Done(); it.Next()) {
    BigStr* s = it.Value();
    if (s != nullptr) {
      tmp->append(s);
    }
  }
  print(S_Aoo->join(tmp));
  tmp2 = Alloc<List<BigStr*>>();
  for (ListIter<BigStr*> it(tmp); !it.Done(); it.Next()) {
    BigStr* s = it.Value();
    if (s->startswith(S_Bjq)) {
      tmp2->append(s);
    }
  }
  print(S_Aoo->join(tmp2));
}

void TestListCompParity() {
  List<int>* mylist = nullptr;
  List<Tuple2<BigStr*, int>*>* pairs = nullptr;
  List<BigStr*>* first = nullptr;
  Dict<BigStr*, BigStr*>* d = nullptr;
  mylib::print_stderr(S_xnh);
  mylib::print_stderr(S_jFE);
  mylist = NewList<int>(std::initializer_list<int>{3, 4, 5});
  mylib::print_stderr(S_sBa);
  pairs = NewList<Tuple2<BigStr*, int>*>(std::initializer_list<Tuple2<BigStr*, int>*>{(Alloc<Tuple2<BigStr*, int>>(S_Epb, 1)), (Alloc<Tuple2<BigStr*, int>>(S_nfE, 2))});
  first = Alloc<List<BigStr*>>();
  for (ListIter<Tuple2<BigStr*, int>*> it(pairs); !it.Done(); it.Next()) {
    Tuple2<BigStr*, int>* tup0 = it.Value();
    BigStr* listcomp_iter_var = tup0->at0();
    first->append(listcomp_iter_var);
  }
  for (ListIter<BigStr*> it(first); !it.Done(); it.Next()) {
    BigStr* s2 = it.Value();
    mylib::print_stderr(StrFormat("first = %s", s2));
  }
  mylib::print_stderr(S_Axw);
  d = Alloc<Dict<BigStr*, BigStr*>>();
  d->set(S_tyE, S_Ado);
  d->set(S_FDA, S_bfb);
  mylib::print_stderr(S_lvd);
}

void TestDict() {
  Dict<BigStr*, int>* d = nullptr;
  mylib::print_stderr(S_jvb);
  d = Alloc<Dict<BigStr*, int>>();
  d->set(S_gCD, 99);
  d->set(S_emj, 42);
  d->set(S_jFv, 0);
  mylib::print_stderr(StrFormat("a = %d", d->at(S_gCD)));
  mylib::print_stderr(StrFormat("b = %d", d->at(S_jFv)));
  mylib::print_stderr(StrFormat("c = %d", d->at(S_emj)));
  for (DictIter<BigStr*, int> it(d); !it.Done(); it.Next()) {
    BigStr* k = it.Key();
    mylib::print_stderr(StrFormat("k = %s", k));
  }
  for (DictIter<BigStr*, int> it(d); !it.Done(); it.Next()) {
    BigStr* k = it.Key();
    int v = it.Value();
    mylib::print_stderr(StrFormat("k = %s, v = %d", k, v));
  }
}
GLOBAL_LIST(CATS, BigStr*, 3, {S_ver COMMA S_juD COMMA S_yfr});

void TestForLoop() {
  List<Tuple2<int, BigStr*>*>* list_of_tuples = nullptr;
  int m;
  int n;
  int i;
  int index;
  BigStr* s = nullptr;
  List<BigStr*>* list_of_strings = nullptr;
  mylib::print_stderr(S_Bxm);
  for (StrIter it(S_jng); !it.Done(); it.Next()) {
    BigStr* ch = it.Value();
    mylib::print_stderr(StrFormat("ch = %s", ch));
  }
  mylib::print_stderr(S_EAn);
  for (ListIter<BigStr*> it(NewList<BigStr*>(std::initializer_list<BigStr*>{S_DEE, S_sfk})); !it.Done(); it.Next()) {
    BigStr* item = it.Value();
    mylib::print_stderr(StrFormat("item = %s", item));
  }
  mylib::print_stderr(S_nFa);
  list_of_tuples = NewList<Tuple2<int, BigStr*>*>(std::initializer_list<Tuple2<int, BigStr*>*>{(Alloc<Tuple2<int, BigStr*>>(5, S_nsm)), (Alloc<Tuple2<int, BigStr*>>(6, S_Ens))});
  for (ListIter<Tuple2<int, BigStr*>*> it(list_of_tuples); !it.Done(); it.Next()) {
    Tuple2<int, BigStr*>* tup1 = it.Value();
    int tuple_iter_1 = tup1->at0();
    BigStr* tuple_iter_2 = tup1->at1();
    mylib::print_stderr(StrFormat("- [%d] %s", tuple_iter_1, tuple_iter_2));
  }
  mylib::print_stderr(S_Eie);
  m = 2;
  n = 3;
  for (int j = 0; j < (m * 2); ++j) {
    mylib::print_stderr(StrFormat("%d", j));
  }
  mylib::print_stderr(S_tDv);
  for (int k = (m + 2); k < (n + 5); ++k) {
    mylib::print_stderr(StrFormat("%d", k));
  }
  mylib::print_stderr(S_Exl);
  for (int m = 0; m < 5; m += 2) {
    mylib::print_stderr(StrFormat("%d", m));
  }
  mylib::print_stderr(S_tsC);
  for (int m = 0; m > -1; m += -1) {
    mylib::print_stderr(StrFormat("reverse %d", m));
  }
  mylib::print_stderr(S_oyf);
  i = 0;
  for (ListIter<BigStr*> it(CATS); !it.Done(); it.Next(), ++i) {
    BigStr* c = it.Value();
    mylib::print_stderr(StrFormat("%d %s", i, c));
  }
  i = 0;
  for (ListIter<Tuple2<int, BigStr*>*> it(list_of_tuples); !it.Done(); it.Next(), ++i) {
    Tuple2<int, BigStr*>* pair = it.Value();
    Tuple2<int, BigStr*>* tup2 = pair;
    index = tup2->at0();
    s = tup2->at1();
    mylib::print_stderr(StrFormat("%d %d %s", i, index, s));
  }
  mylib::print_stderr(S_yns);
  list_of_strings = NewList<BigStr*>(std::initializer_list<BigStr*>{S_Eow, S_Dne});
  for (ReverseListIter<BigStr*> it(list_of_strings); !it.Done(); it.Next()) {
    BigStr* item = it.Value();
    mylib::print_stderr(StrFormat("- %s", item));
  }
  mylib::print_stderr(S_bdx);
  for (ReverseListIter<Tuple2<int, BigStr*>*> it(list_of_tuples); !it.Done(); it.Next()) {
    Tuple2<int, BigStr*>* tup3 = it.Value();
    int i = tup3->at0();
    BigStr* item = tup3->at1();
    mylib::print_stderr(StrFormat("- [%d] %s", i, item));
  }
}

void run_tests() {
  TestForLoop();
  TestListComp();
  TestListCompParity();
  TestDict();
}

void run_benchmarks() {
  int n;
  int result;
  int i;
  int j;
  n = 500000;
  result = 0;
  i = 0;
  while (i < n) {
    for (int j = 3; j < 10; ++j) {
      result += j;
    }
    j = 0;
    for (ListIter<BigStr*> it(CATS); !it.Done(); it.Next(), ++j) {
      BigStr* c = it.Value();
      result += j;
      result += len(c);
    }
    i += 1;
  }
  mylib::print_stderr(StrFormat("result = %d", result));
  mylib::print_stderr(StrFormat("Ran %d iterations of xrange/enumerate", n));
}

}  // define namespace loops

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    loops::run_benchmarks();
  } else {
    loops::run_tests();
  }

  gHeap.CleanProcessExit();
}
