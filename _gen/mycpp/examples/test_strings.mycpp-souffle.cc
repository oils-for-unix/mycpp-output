// _gen/mycpp/examples/test_strings.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace test_strings {  // forward declare
  class Foo;
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_ayy, "\u0000bar");
GLOBAL_STR(S_Clk, "\"double\"");
GLOBAL_STR(S_kua, "%dfoo");
GLOBAL_STR(S_ubF, "%s");
GLOBAL_STR(S_dcg, "'single'");
GLOBAL_STR(S_ysn, "---");
GLOBAL_STR(S_hyA, "0xff");
GLOBAL_STR(S_wdo, "BACKSLASH");
GLOBAL_STR(S_xBu, "EQUAL ==");
GLOBAL_STR(S_wuh, "LEFT");
GLOBAL_STR(S_vmj, "RIGHT");
GLOBAL_STR(S_jwf, "TestByteOperations");
GLOBAL_STR(S_myw, "TestBytes2");
GLOBAL_STR(S_ldx, "TestFormat");
GLOBAL_STR(S_Eax, "[");
GLOBAL_STR(S_iyu, "\\");
GLOBAL_STR(S_pcD, "]");
GLOBAL_STR(S_bzi, "a\tb\nc\td\n");
GLOBAL_STR(S_sFg, "a1");
GLOBAL_STR(S_cia, "a1 yes");
GLOBAL_STR(S_sff, "a1b2c3d4e5");
GLOBAL_STR(S_dab, "a1bc");
GLOBAL_STR(S_aps, "aa");
GLOBAL_STR(S_Dfv, "aaa-bb-cc");
GLOBAL_STR(S_qds, "aaaa");
GLOBAL_STR(S_jng, "abc");
GLOBAL_STR(S_smu, "abcXYZ");
GLOBAL_STR(S_qpB, "anchor");
GLOBAL_STR(S_jFv, "b");
GLOBAL_STR(S_clt, "bar");
GLOBAL_STR(S_Bkj, "bc");
GLOBAL_STR(S_ohc, "bc yes");
GLOBAL_STR(S_emj, "c");
GLOBAL_STR(S_Dne, "eggs");
GLOBAL_STR(S_kdC, "empty yes");
GLOBAL_STR(S_ksc, "f");
GLOBAL_STR(S_lqB, "foo");
GLOBAL_STR(S_vzt, "foo ");
GLOBAL_STR(S_Dgz, "foo%d");
GLOBAL_STR(S_qmd, "mystr");
GLOBAL_STR(S_anC, "s");
GLOBAL_STR(S_Cgm, "should be equal");
GLOBAL_STR(S_apm, "tab\tline\nline\r\n");
GLOBAL_STR(S_rqD, "x");
GLOBAL_STR(S_zjx, "z");
GLOBAL_STR(S_xww, "zz");
GLOBAL_STR(S_ecE, "zz no");
GLOBAL_STR(S_yfv, "zzyyxx");
GLOBAL_STR(S_yCt, "zzzzzz");
GLOBAL_STR(S_xEt, "zzzzzz no");

namespace test_strings {  // declare

extern List<BigStr*>* MYLIST;
void banner(BigStr* s);
class Foo {
 public:
  Foo();
  BigStr* s{};

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassScanned(1, sizeof(Foo));
  }

  DISALLOW_COPY_AND_ASSIGN(Foo)
};

void TestMethods();
void TestFormat();
void TestByteOperations();
void TestBytes2();
void run_tests();
void run_benchmarks();

}  // declare namespace test_strings

namespace test_strings {  // define

GLOBAL_LIST(MYLIST, BigStr*, 1, {S_yfv});

void banner(BigStr* s) {
  print(S_Aoo);
  print(StrFormat("=== %s ===", s));
  print(S_Aoo);
}

Foo::Foo() {
  this->s = S_qmd;
}

void TestMethods() {
  BigStr* s = nullptr;
  List<BigStr*>* substrs = nullptr;
  int pos;
  s = S_dab;
  if (s->startswith(S_Aoo)) {
    print(S_kdC);
  }
  if (s->startswith(S_sFg)) {
    print(S_cia);
  }
  if (!s->startswith(S_xww)) {
    print(S_ecE);
  }
  if (s->endswith(S_Aoo)) {
    print(S_kdC);
  }
  if (s->endswith(S_Bkj)) {
    print(S_ohc);
  }
  if (s->endswith(S_emj)) {
    print(S_ohc);
  }
  if (!s->endswith(S_yCt)) {
    print(S_xEt);
  }
  s = S_Dfv;
  substrs = NewList<BigStr*>(std::initializer_list<BigStr*>{S_aps, S_jFv, S_zjx, S_qds, S_Aoo});
  for (ListIter<BigStr*> it(substrs); !it.Done(); it.Next()) {
    BigStr* substr = it.Value();
    for (int start = 0; start < len(s); ++start) {
      pos = s->find(substr, start);
      print(StrFormat("%s find %s start:%d => %d", s, substr, start, pos));
    }
  }
  print(S_ysn);
  for (ListIter<BigStr*> it(substrs); !it.Done(); it.Next()) {
    BigStr* substr = it.Value();
    for (int end = 0; end < len(s); ++end) {
      pos = s->find(substr, 0, end);
      print(StrFormat("%s find %s end:%d => %d", s, substr, end, pos));
    }
  }
  print(S_ysn);
  for (int start = 0; start < 3; ++start) {
    for (int end = 0; end < 3; ++end) {
      pos = s->find(S_Aoo, start, end);
      print(StrFormat("%s find empty [%d, %d) => %d", s, start, end, pos));
    }
  }
}

void TestFormat() {
  test_strings::Foo* obj = nullptr;
  BigStr* s = nullptr;
  BigStr* x = nullptr;
  BigStr* fmt = nullptr;
  List<BigStr*>* fmts = nullptr;
  banner(S_ldx);
  print(str_concat(S_lqB, S_clt));
  print(str_repeat(S_lqB, 3));
  obj = Alloc<Foo>();
  print(str_concat(S_lqB, obj->s));
  s = S_qmd;
  print(StrFormat("[%s]", s));
  s = S_qmd;
  print(StrFormat("[%s, %s]", s, S_jng));
  print(StrFormat("%s: 5%%-100%%", S_jng));
  print(StrFormat("<a href=\"foo.html\">%s</a>", S_qpB));
  print(StrFormat("foo? %d", str_contains(s, S_ksc)));
  print(StrFormat("str? %d", str_contains(s, S_anC)));
  print(StrFormat("int 5d %5d", 35));
  print(S_dcg);
  print(S_Clk);
  print(S_bzi);
  x = S_rqD;
  print(StrFormat("%s\tb\n%s\td\n", x, x));
  fmt = S_kua;
  print(StrFormat(fmt, 10));
  fmts = NewList<BigStr*>(std::initializer_list<BigStr*>{S_Dgz});
  print(StrFormat(fmts->at(0), 10));
  print(StrFormat(str_concat(S_vzt, S_ubF), S_clt));
  s = StrFormat("spam\u0000%s", S_Dne);
  s = StrFormat("foo%s", S_ayy);
  print(StrFormat("len(s) = %d", len(s)));
  print(StrFormat("%o", 12345));
  print(StrFormat("%17o", 12345));
  print(StrFormat("%017o", 12345));
  print(StrFormat("%%%d%%%%", 12345));
  print(StrFormat("%r", S_apm));
  s = S_sff;
  print(s->upper());
}

void TestByteOperations() {
  BigStr* s = nullptr;
  int i;
  int n;
  int total;
  int total2;
  int byte;
  int byte2;
  banner(S_jwf);
  s = str_repeat(S_lqB, 10);
  i = 0;
  n = len(s);
  total = 0;
  total2 = 0;
  while (i < n) {
    byte = ord(s->at(i));
    byte2 = mylib::ByteAt(s, i);
    total += byte;
    total2 += byte2;
    i += 1;
  }
  if (total != total2) {
    assert(0);  // AssertionError
  }
  print(StrFormat("total = %d", total));
  print(StrFormat("total2 = %d", total2));
}

void TestBytes2() {
  List<int>* b = nullptr;
  List<BigStr*>* ch = nullptr;
  int j;
  BigStr* all_bytes = nullptr;
  BigStr* b2 = nullptr;
  int n;
  int i;
  int byte;
  banner(S_myw);
  b = Alloc<List<int>>();
  ch = Alloc<List<BigStr*>>();
  for (int i = 0; i < 256; ++i) {
    j = (255 - i);
    if (j == 2) {
      j = 0;
    }
    b->append(j);
    ch->append(chr(j));
  }
  print(StrFormat("len(b) = %d", len(b)));
  print(StrFormat("len(ch) = %d", len(ch)));
  all_bytes = S_Aoo->join(ch);
  b2 = mylib::JoinBytes(b);
  if (str_equals(all_bytes, b2)) {
    print(S_xBu);
  }
  else {
    assert(0);  // AssertionError
  }
  n = len(all_bytes);
  print(StrFormat("len(all_bytes) = %d", n));
  print(S_Aoo);
  i = 0;
  while (i < n) {
    byte = mylib::ByteAt(all_bytes, i);
    if (mylib::ByteEquals(byte, S_Eax)) {
      print(S_wuh);
    }
    if (mylib::ByteEquals(byte, S_pcD)) {
      print(S_vmj);
    }
    if (mylib::ByteEquals(byte, S_iyu)) {
      print(S_wdo);
    }
    if (mylib::ByteEquals(byte, chr(255))) {
      print(S_hyA);
    }
    if (mylib::ByteInSet(byte, S_smu)) {
      print(S_smu);
    }
    i += 1;
  }
  print(S_Aoo);
}

void run_tests() {
  TestFormat();
  TestMethods();
  TestByteOperations();
  TestBytes2();
  print(StrFormat("len(MYLIST) = %d", len(MYLIST)));
}

void run_benchmarks() {
  ;  // pass
}

}  // define namespace test_strings

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    test_strings::run_benchmarks();
  } else {
    test_strings::run_tests();
  }

  gHeap.CleanProcessExit();
}
