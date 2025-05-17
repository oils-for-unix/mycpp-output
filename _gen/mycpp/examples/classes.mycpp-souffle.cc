// _gen/mycpp/examples/classes.mycpp-souffle.cc - generated from Python source code

#include "mycpp/runtime.h"

// BEGIN mycpp output
namespace classes {  // forward declare
  class ColorOutput;
  class TextOutput;
  class Abstract;
  class Base;
  class DerivedI;
  class DerivedSS;
  class Node;
}

GLOBAL_STR(S_Aoo, "");
GLOBAL_STR(S_foD, "BenchmarkSimpleNode");
GLOBAL_STR(S_jqE, "BenchmarkVirtualNodes");
GLOBAL_STR(S_ACu, "BenchmarkWriter");
GLOBAL_STR(S_FAj, "TextOutput constructor");
GLOBAL_STR(S_cxq, "bar\n");
GLOBAL_STR(S_rxu, "foo\n");
GLOBAL_STR(S_saq, "left");
GLOBAL_STR(S_nxB, "next");
GLOBAL_STR(S_lbA, "null");
GLOBAL_STR(S_swE, "right");

namespace classes {  // declare

class ColorOutput {
 public:
  ColorOutput(mylib::Writer* f);
  void write(BigStr* s);
  mylib::Writer* f{};
  int num_chars{};
  
  static constexpr uint32_t field_mask() {
    return maskbit(offsetof(ColorOutput, f));
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(ColorOutput));
  }

  DISALLOW_COPY_AND_ASSIGN(ColorOutput)
};

class TextOutput : public ::classes::ColorOutput {
 public:
  TextOutput(mylib::Writer* f);
  void MutateFields();
  void PrintFields();

  int i{};
  
  static constexpr uint32_t field_mask() {
    return ::classes::ColorOutput::field_mask();
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(TextOutput));
  }

  DISALLOW_COPY_AND_ASSIGN(TextOutput)
};

class Abstract {
 public:
  Abstract();
  virtual BigStr* TypeString();
  
  static constexpr uint32_t field_mask() {
    return kZeroMask;
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(Abstract));
  }

  DISALLOW_COPY_AND_ASSIGN(Abstract)
};

class Base : public ::classes::Abstract {
 public:
  Base(classes::Base* n);
  virtual BigStr* TypeString();

  classes::Base* next{};
  
  static constexpr uint32_t field_mask() {
    return ::classes::Abstract::field_mask()
         | maskbit(offsetof(Base, next));
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(Base));
  }

  DISALLOW_COPY_AND_ASSIGN(Base)
};

class DerivedI : public ::classes::Base {
 public:
  DerivedI(classes::Base* n, int i);
  int Integer();
  virtual BigStr* TypeString();

  int i{};
  
  static constexpr uint32_t field_mask() {
    return ::classes::Base::field_mask();
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(DerivedI));
  }

  DISALLOW_COPY_AND_ASSIGN(DerivedI)
};

class DerivedSS : public ::classes::Base {
 public:
  DerivedSS(classes::Base* n, BigStr* t, BigStr* u);
  virtual BigStr* TypeString();

  BigStr* t{};
  BigStr* u{};
  
  static constexpr uint32_t field_mask() {
    return ::classes::Base::field_mask()
         | maskbit(offsetof(DerivedSS, t))
         | maskbit(offsetof(DerivedSS, u));
  }

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassFixed(field_mask(), sizeof(DerivedSS));
  }

  DISALLOW_COPY_AND_ASSIGN(DerivedSS)
};

class Node {
 public:
  Node(classes::Node* n, int i);
  classes::Node* next{};
  int i{};

  static constexpr ObjHeader obj_header() {
    return ObjHeader::ClassScanned(1, sizeof(Node));
  }

  DISALLOW_COPY_AND_ASSIGN(Node)
};

void TestMethods();
BigStr* f(classes::Base* obj);
void TestInheritance();
void run_tests();
void BenchmarkWriter(int n);
void PrintLength(classes::Node* node);
void BenchmarkSimpleNode(int n);
void PrintLengthBase(classes::Base* current);
void BenchmarkVirtualNodes(int n);
void run_benchmarks();

}  // declare namespace classes

namespace classes {  // define


ColorOutput::ColorOutput(mylib::Writer* f) {
  this->f = f;
  this->num_chars = 0;
}

void ColorOutput::write(BigStr* s) {
  this->f->write(s);
  this->num_chars += len(s);
}

TextOutput::TextOutput(mylib::Writer* f) : ::classes::ColorOutput(f) {
  print(S_FAj);
  this->i = 0;
}

void TextOutput::MutateFields() {
  this->num_chars = 42;
  this->i = 43;
}

void TextOutput::PrintFields() {
  print(StrFormat("num_chars = %d", this->num_chars));
  print(StrFormat("i = %d", this->i));
}

Abstract::Abstract() {
  ;  // pass
}

BigStr* Abstract::TypeString() {
  FAIL(kNotImplemented);  // Python NotImplementedError
}

Base::Base(classes::Base* n) : ::classes::Abstract() {
  this->next = n;
}

BigStr* Base::TypeString() {
  return StrFormat("Base(%s)", this->next ? S_nxB : S_lbA);
}

DerivedI::DerivedI(classes::Base* n, int i) : ::classes::Base(n) {
  this->i = i;
}

int DerivedI::Integer() {
  return this->i;
}

BigStr* DerivedI::TypeString() {
  return StrFormat("DerivedI(%s, %d)", this->next ? S_nxB : S_lbA, this->i);
}

DerivedSS::DerivedSS(classes::Base* n, BigStr* t, BigStr* u) : ::classes::Base(n) {
  this->t = t;
  this->u = u;
}

BigStr* DerivedSS::TypeString() {
  return StrFormat("DerivedSS(%s, %s, %s)", this->next ? S_nxB : S_lbA, this->t, this->u);
}

Node::Node(classes::Node* n, int i) {
  this->next = n;
  this->i = i;
}

void TestMethods() {
  mylib::Writer* stdout_ = nullptr;
  classes::TextOutput* out = nullptr;
  stdout_ = mylib::Stdout();
  out = Alloc<TextOutput>(stdout_);
  out->write(S_rxu);
  out->write(S_cxq);
  mylib::print_stderr(StrFormat("Wrote %d bytes", out->num_chars));
  out->MutateFields();
  out->PrintFields();
}

BigStr* f(classes::Base* obj) {
  return obj->TypeString();
}

void TestInheritance() {
  classes::Base* b = nullptr;
  classes::DerivedI* di = nullptr;
  classes::DerivedSS* dss = nullptr;
  b = Alloc<Base>(nullptr);
  di = Alloc<DerivedI>(nullptr, 1);
  dss = Alloc<DerivedSS>(nullptr, S_saq, S_swE);
  mylib::print_stderr(StrFormat("Integer() = %d", di->Integer()));
  mylib::print_stderr(StrFormat("b.TypeString()   %s", b->TypeString()));
  mylib::print_stderr(StrFormat("di.TypeString()  %s", di->TypeString()));
  mylib::print_stderr(StrFormat("dss.TypeString() %s", dss->TypeString()));
  mylib::print_stderr(StrFormat("f(b)           %s", f(b)));
  mylib::print_stderr(StrFormat("f(di)          %s", f(di)));
  mylib::print_stderr(StrFormat("f(dss)         %s", f(dss)));
}

void run_tests() {
  TestMethods();
  TestInheritance();
}

void BenchmarkWriter(int n) {
  mylib::BufWriter* f = nullptr;
  classes::TextOutput* out = nullptr;
  int i;
  mylib::print_stderr(S_ACu);
  mylib::print_stderr(S_Aoo);
  f = Alloc<mylib::BufWriter>();
  out = Alloc<TextOutput>(f);
  i = 0;
  while (i < n) {
    out->write(S_rxu);
    i += 1;
  }
  mylib::print_stderr(StrFormat("  Ran %d iterations", n));
  mylib::print_stderr(StrFormat("  Wrote %d bytes", out->num_chars));
  mylib::print_stderr(S_Aoo);
}

void PrintLength(classes::Node* node) {
  classes::Node* current = nullptr;
  int linked_list_len;
  current = node;
  linked_list_len = 0;
  while (true) {
    if (linked_list_len < 10) {
      mylib::print_stderr(StrFormat("  -> %d", current->i));
    }
    current = current->next;
    if (current == nullptr) {
      break;
    }
    linked_list_len += 1;
  }
  mylib::print_stderr(S_Aoo);
  mylib::print_stderr(StrFormat("  linked list len = %d", linked_list_len));
  mylib::print_stderr(S_Aoo);
}

void BenchmarkSimpleNode(int n) {
  classes::Node* next_ = nullptr;
  classes::Node* node = nullptr;
  mylib::print_stderr(S_foD);
  mylib::print_stderr(S_Aoo);
  next_ = Alloc<Node>(nullptr, -1);
  for (int i = 0; i < n; ++i) {
    node = Alloc<Node>(next_, i);
    next_ = node;
  }
  PrintLength(node);
}

void PrintLengthBase(classes::Base* current) {
  int linked_list_len;
  linked_list_len = 0;
  while (true) {
    if (linked_list_len < 10) {
      mylib::print_stderr(StrFormat("  -> %s", current->TypeString()));
    }
    current = current->next;
    if (current == nullptr) {
      break;
    }
    linked_list_len += 1;
  }
  mylib::print_stderr(S_Aoo);
  mylib::print_stderr(StrFormat("  linked list len = %d", linked_list_len));
  mylib::print_stderr(S_Aoo);
}

void BenchmarkVirtualNodes(int n) {
  classes::Base* next_ = nullptr;
  classes::DerivedI* node1 = nullptr;
  BigStr* s1 = nullptr;
  BigStr* s2 = nullptr;
  classes::DerivedSS* node2 = nullptr;
  classes::Base* node3 = nullptr;
  classes::Base* current = nullptr;
  mylib::print_stderr(S_jqE);
  mylib::print_stderr(S_Aoo);
  next_ = Alloc<Base>(nullptr);
  for (int i = 0; i < n; ++i) {
    node1 = Alloc<DerivedI>(next_, i);
    s1 = str(i);
    s2 = StrFormat("+%d", i);
    node2 = Alloc<DerivedSS>(node1, s1, s2);
    node3 = Alloc<Base>(node2);
    next_ = node3;
  }
  current = nullptr;
  current = node3;
  PrintLengthBase(current);
}

void run_benchmarks() {
  if (1) {
    BenchmarkWriter(30000);
  }
  if (1) {
    BenchmarkSimpleNode(10000);
  }
  if (1) {
    BenchmarkVirtualNodes(1000);
  }
}

}  // define namespace classes

int main(int argc, char **argv) {
  gHeap.Init();

  char* b = getenv("BENCHMARK");
  if (b && strlen(b)) {  // match Python's logic
    fprintf(stderr, "Benchmarking...\n");
    classes::run_benchmarks();
  } else {
    classes::run_tests();
  }

  gHeap.CleanProcessExit();
}
