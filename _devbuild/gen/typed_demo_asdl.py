from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

if TYPE_CHECKING:
  from _devbuild.gen.demo_lib_asdl import value_t, LibToken

if TYPE_CHECKING:
  from asdl.examples import typed_demo

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class op_id_t(pybase.SimpleObj):
  pass

class op_id_e(object):
  Plus = op_id_t(1)
  Minus = op_id_t(2)
  Star = op_id_t(3)

_op_id_str = {
  1: 'Plus',
  2: 'Minus',
  3: 'Star',
}

def op_id_str(val, dot=True):
  # type: (op_id_t, bool) -> str
  v = _op_id_str[val]
  if dot:
    return "op_id.%s" % v
  else:
    return v

class cflow_e(object):
  Break = 1
  Continue = 2
  Return = 3
  PrimitiveList = 4

_cflow_str = {
  1: 'Break',
  2: 'Continue',
  3: 'Return',
  4: 'PrimitiveList',
}

def cflow_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _cflow_str[tag]
  if dot:
    return "cflow.%s" % v
  else:
    return v

class cflow_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class cflow__Break(cflow_t):
  _type_tag = 1
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('cflow.Break')
    L = out_node.fields

    return out_node

class cflow__Continue(cflow_t):
  _type_tag = 2
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('cflow.Continue')
    L = out_node.fields

    return out_node

class cflow(object):
  Break = cflow__Break()
  
  Continue = cflow__Continue()
  
  class Return(cflow_t):
    _type_tag = 3
    __slots__ = ('status',)
  
    def __init__(self, status):
      # type: (int) -> None
      self.status = status
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> cflow.Return
      return cflow.Return(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('cflow.Return')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.status), color_e.OtherConst)
      L.append(Field('status', x0))
  
      return out_node
  
  class PrimitiveList(cflow_t):
    _type_tag = 4
    __slots__ = ('ints',)
  
    def __init__(self, ints):
      # type: (List[int]) -> None
      self.ints = ints
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> cflow.PrimitiveList
      return cflow.PrimitiveList([] if alloc_lists else cast('List[int]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('cflow.PrimitiveList')
      L = out_node.fields
  
      if self.ints is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.ints:
          x0.children.append(hnode.Leaf(str(i0), color_e.OtherConst))
        L.append(Field('ints', x0))
  
      return out_node
  
  pass

class cflow2_e(object):
  Break = 1
  Continue = 2
  Return = 3

_cflow2_str = {
  1: 'Break',
  2: 'Continue',
  3: 'Return',
}

def cflow2_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _cflow2_str[tag]
  if dot:
    return "cflow2.%s" % v
  else:
    return v

class cflow2_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class cflow2__Break(cflow2_t):
  _type_tag = 1
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('cflow2.Break')
    L = out_node.fields

    return out_node

class cflow2__Continue(cflow2_t):
  _type_tag = 2
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('cflow2.Continue')
    L = out_node.fields

    return out_node

class cflow2(object):
  Break = cflow2__Break()
  
  Continue = cflow2__Continue()
  
  class Return(cflow2_t):
    _type_tag = 3
    __slots__ = ('status',)
  
    def __init__(self, status):
      # type: (int) -> None
      self.status = status
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> cflow2.Return
      return cflow2.Return(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('cflow2.Return')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.status), color_e.OtherConst)
      L.append(Field('status', x0))
  
      return out_node
  
  pass

class word_part_e(object):
  Literal = 68
  BoolSub = 2

_word_part_str = {
  2: 'BoolSub',
  68: 'Literal',
}

def word_part_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _word_part_str[tag]
  if dot:
    return "word_part.%s" % v
  else:
    return v

class word_part_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class word_part(object):
  class BoolSub(word_part_t):
    _type_tag = 2
    __slots__ = ('b',)
  
    def __init__(self, b):
      # type: (bool_expr_t) -> None
      self.b = b
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.BoolSub
      return word_part.BoolSub(cast('bool_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.BoolSub')
      L = out_node.fields
  
      assert self.b is not None
      x0 = self.b.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('b', x0))
  
      return out_node
  
  pass

class word2_e(object):
  Operator = 68
  Compound = 2

_word2_str = {
  2: 'Compound',
  68: 'Operator',
}

def word2_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _word2_str[tag]
  if dot:
    return "word2.%s" % v
  else:
    return v

class word2_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class word2(object):
  class Compound(word2_t):
    _type_tag = 2
    __slots__ = ('parts',)
  
    def __init__(self, parts):
      # type: (List[word_part_t]) -> None
      self.parts = parts
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word2.Compound
      return word2.Compound([] if alloc_lists else cast('List[word_part_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word2.Compound')
      L = out_node.fields
  
      if self.parts is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.parts:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('parts', x0))
  
      return out_node
  
  pass

class bool_expr_e(object):
  WordTest = 1
  Unary = 2
  Binary = 3
  LogicalNot = 4
  LogicalBinary = 5

_bool_expr_str = {
  1: 'WordTest',
  2: 'Unary',
  3: 'Binary',
  4: 'LogicalNot',
  5: 'LogicalBinary',
}

def bool_expr_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _bool_expr_str[tag]
  if dot:
    return "bool_expr.%s" % v
  else:
    return v

class bool_expr_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class bool_expr(object):
  class WordTest(bool_expr_t):
    _type_tag = 1
    __slots__ = ('child',)
  
    def __init__(self, child):
      # type: (word2_t) -> None
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.WordTest
      return bool_expr.WordTest(cast('word2_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.WordTest')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      return out_node
  
  class Unary(bool_expr_t):
    _type_tag = 2
    __slots__ = ('child',)
  
    def __init__(self, child):
      # type: (word) -> None
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.Unary
      return bool_expr.Unary(cast('word', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.Unary')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      return out_node
  
  class Binary(bool_expr_t):
    _type_tag = 3
    __slots__ = ('left', 'right')
  
    def __init__(self, left, right):
      # type: (word, word) -> None
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.Binary
      return bool_expr.Binary(cast('word', None), cast('word', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.Binary')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.right is not None
      x1 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x1))
  
      return out_node
  
  class LogicalNot(bool_expr_t):
    _type_tag = 4
    __slots__ = ('b',)
  
    def __init__(self, b):
      # type: (bool_expr_t) -> None
      self.b = b
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.LogicalNot
      return bool_expr.LogicalNot(cast('bool_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.LogicalNot')
      L = out_node.fields
  
      assert self.b is not None
      x0 = self.b.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('b', x0))
  
      return out_node
  
  class LogicalBinary(bool_expr_t):
    _type_tag = 5
    __slots__ = ('op', 'left', 'right')
  
    def __init__(self, op, left, right):
      # type: (op_id_t, bool_expr_t, bool_expr_t) -> None
      self.op = op
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.LogicalBinary
      return bool_expr.LogicalBinary(op_id_e.Plus, cast('bool_expr_t', None), cast('bool_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.LogicalBinary')
      L = out_node.fields
  
      x0 = hnode.Leaf(op_id_str(self.op), color_e.TypeName)
      L.append(Field('op', x0))
  
      assert self.left is not None
      x1 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  pass

class flag_type_e(object):
  Bool = 1
  Int = 2
  Float = 3
  Str = 4
  Enum = 5

_flag_type_str = {
  1: 'Bool',
  2: 'Int',
  3: 'Float',
  4: 'Str',
  5: 'Enum',
}

def flag_type_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _flag_type_str[tag]
  if dot:
    return "flag_type.%s" % v
  else:
    return v

class flag_type_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class flag_type__Bool(flag_type_t):
  _type_tag = 1
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('flag_type.Bool')
    L = out_node.fields

    return out_node

class flag_type__Int(flag_type_t):
  _type_tag = 2
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('flag_type.Int')
    L = out_node.fields

    return out_node

class flag_type__Float(flag_type_t):
  _type_tag = 3
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('flag_type.Float')
    L = out_node.fields

    return out_node

class flag_type__Str(flag_type_t):
  _type_tag = 4
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('flag_type.Str')
    L = out_node.fields

    return out_node

class flag_type(object):
  Bool = flag_type__Bool()
  
  Int = flag_type__Int()
  
  Float = flag_type__Float()
  
  Str = flag_type__Str()
  
  class Enum(flag_type_t):
    _type_tag = 5
    __slots__ = ('alts',)
  
    def __init__(self, alts):
      # type: (List[str]) -> None
      self.alts = alts
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> flag_type.Enum
      return flag_type.Enum([] if alloc_lists else cast('List[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('flag_type.Enum')
      L = out_node.fields
  
      if self.alts is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.alts:
          x0.children.append(NewLeaf(i0, color_e.StringConst))
        L.append(Field('alts', x0))
  
      return out_node
  
  pass

class arith_expr_e(object):
  NoOp = 1
  Const = 2

_arith_expr_str = {
  1: 'NoOp',
  2: 'Const',
}

def arith_expr_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _arith_expr_str[tag]
  if dot:
    return "arith_expr.%s" % v
  else:
    return v

class arith_expr_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class arith_expr__NoOp(arith_expr_t):
  _type_tag = 1
  __slots__ = ()

  def __init__(self, ):
    # type: () -> None
    pass

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('arith_expr.NoOp')
    L = out_node.fields

    return out_node

class arith_expr(object):
  NoOp = arith_expr__NoOp()
  
  class Const(arith_expr_t):
    _type_tag = 2
    __slots__ = ('i',)
  
    def __init__(self, i):
      # type: (int) -> None
      self.i = i
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Const
      return arith_expr.Const(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Const')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
      L.append(Field('i', x0))
  
      return out_node
  
  pass

class a_word_e(object):
  String = 1
  CompoundWord = 74

_a_word_str = {
  1: 'String',
  74: 'CompoundWord',
}

def a_word_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _a_word_str[tag]
  if dot:
    return "a_word.%s" % v
  else:
    return v

class a_word_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class a_word(object):
  class String(a_word_t):
    _type_tag = 1
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> a_word.String
      return a_word.String('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('a_word.String')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  pass

class op_array(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('ops',)

  def __init__(self, ops):
    # type: (List[op_id_t]) -> None
    self.ops = ops

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> op_array
    return op_array([] if alloc_lists else cast('List[op_id_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('op_array')
    L = out_node.fields

    if self.ops is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.ops:
        x0.children.append(hnode.Leaf(op_id_str(i0), color_e.TypeName))
      L.append(Field('ops', x0))

    return out_node

class assign(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('name', 'flags')

  def __init__(self, name, flags):
    # type: (str, List[str]) -> None
    self.name = name
    self.flags = flags

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> assign
    return assign('', [] if alloc_lists else cast('List[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('assign')
    L = out_node.fields

    x0 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x0))

    if self.flags is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.flags:
        x1.children.append(NewLeaf(i1, color_e.StringConst))
      L.append(Field('flags', x1))

    return out_node

class source_location(pybase.CompoundObj):
  _type_tag = 66
  __slots__ = ('path', 'line', 'col', 'length')

  def __init__(self, path, line, col, length):
    # type: (str, int, int, int) -> None
    self.path = path
    self.line = line
    self.col = col
    self.length = length

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> source_location
    return source_location('', -1, -1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('source_location')
    L = out_node.fields

    x0 = NewLeaf(self.path, color_e.StringConst)
    L.append(Field('path', x0))

    x1 = hnode.Leaf(str(self.line), color_e.OtherConst)
    L.append(Field('line', x1))

    x2 = hnode.Leaf(str(self.col), color_e.OtherConst)
    L.append(Field('col', x2))

    x3 = hnode.Leaf(str(self.length), color_e.OtherConst)
    L.append(Field('length', x3))

    return out_node

class word(pybase.CompoundObj):
  _type_tag = 67
  __slots__ = ('value',)

  def __init__(self, value):
    # type: (str) -> None
    self.value = value

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> word
    return word('')

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('word')
    L = out_node.fields

    x0 = NewLeaf(self.value, color_e.StringConst)
    L.append(Field('value', x0))

    return out_node

class Token(word_part_t, word2_t):
  _type_tag = 68
  __slots__ = ('s', 'b')

  def __init__(self, s, b):
    # type: (str, bool) -> None
    self.s = s
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Token
    return Token('', False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Token')
    L = out_node.fields

    x0 = NewLeaf(self.s, color_e.StringConst)
    L.append(Field('s', x0))

    x1 = hnode.Leaf('T' if self.b else 'F', color_e.OtherConst)
    L.append(Field('b', x1))

    return out_node

class Dicts(pybase.CompoundObj):
  _type_tag = 69
  __slots__ = ('ss', 'ib', 'tokens')

  def __init__(self, ss, ib, tokens):
    # type: (Dict[str, str], Dict[int, bool], Dict[str, Token]) -> None
    self.ss = ss
    self.ib = ib
    self.tokens = tokens

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Dicts
    return Dicts(cast('Dict[str, str]', None), cast('Dict[int, bool]', None), cast('Dict[str, Token]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Dicts')
    L = out_node.fields

    if self.ss is not None:  # Dict
      unnamed0 = []  # type: List[hnode_t]
      x0 = hnode.Record("", "{", "}", [], unnamed0)
      for k0, v0 in self.ss.iteritems():
        unnamed0.append(NewLeaf(k0, color_e.StringConst))
        unnamed0.append(NewLeaf(v0, color_e.StringConst))
      L.append(Field('ss', x0))

    if self.ib is not None:  # Dict
      unnamed1 = []  # type: List[hnode_t]
      x1 = hnode.Record("", "{", "}", [], unnamed1)
      for k1, v1 in self.ib.iteritems():
        unnamed1.append(hnode.Leaf(str(k1), color_e.OtherConst))
        unnamed1.append(hnode.Leaf('T' if v1 else 'F', color_e.OtherConst))
      L.append(Field('ib', x1))

    if self.tokens is not None:  # Dict
      unnamed2 = []  # type: List[hnode_t]
      x2 = hnode.Record("", "{", "}", [], unnamed2)
      for k2, v2 in self.tokens.iteritems():
        unnamed2.append(NewLeaf(k2, color_e.StringConst))
        unnamed2.append(v2.PrettyTree(do_abbrev, trav=trav))
      L.append(Field('tokens', x2))

    return out_node

class SetToArg_(pybase.CompoundObj):
  _type_tag = 70
  __slots__ = ('name', 'flag_type', 'quit_parsing_flags')

  def __init__(self, name, flag_type, quit_parsing_flags):
    # type: (str, flag_type_t, bool) -> None
    self.name = name
    self.flag_type = flag_type
    self.quit_parsing_flags = quit_parsing_flags

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> SetToArg_
    return SetToArg_('', cast('flag_type_t', None), False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('SetToArg_')
    L = out_node.fields

    x0 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x0))

    assert self.flag_type is not None
    x1 = self.flag_type.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('flag_type', x1))

    x2 = hnode.Leaf('T' if self.quit_parsing_flags else 'F', color_e.OtherConst)
    L.append(Field('quit_parsing_flags', x2))

    return out_node

class Strings(pybase.CompoundObj):
  _type_tag = 71
  __slots__ = ('required', 'optional')

  def __init__(self, required, optional):
    # type: (str, Optional[str]) -> None
    self.required = required
    self.optional = optional

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Strings
    return Strings('', cast('Optional[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Strings')
    L = out_node.fields

    x0 = NewLeaf(self.required, color_e.StringConst)
    L.append(Field('required', x0))

    if self.optional is not None:  # Optional
      x1 = NewLeaf(self.optional, color_e.StringConst)
      L.append(Field('optional', x1))

    return out_node

class Maybes(pybase.CompoundObj):
  _type_tag = 72
  __slots__ = ('op', 'arg')

  def __init__(self, op, arg):
    # type: (Optional[Token], Optional[word]) -> None
    self.op = op
    self.arg = arg

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Maybes
    return Maybes(cast('Optional[Token]', None), cast('Optional[word]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Maybes')
    L = out_node.fields

    if self.op is not None:  # Optional
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))

    if self.arg is not None:  # Optional
      x1 = self.arg.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('arg', x1))

    return out_node

class OptionalList(pybase.CompoundObj):
  _type_tag = 73
  __slots__ = ('words',)

  def __init__(self, words):
    # type: (Optional[List[word]]) -> None
    self.words = words

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> OptionalList
    return OptionalList(cast('Optional[List[word]]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('OptionalList')
    L = out_node.fields

    if self.words is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.words:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('words', x0))

    return out_node

class foo(pybase.CompoundObj):
  _type_tag = 75
  __slots__ = ('x', 'y')

  def __init__(self, x, y):
    # type: (typed_demo._Callable, typed_demo._Callable) -> None
    self.x = x
    self.y = y

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> foo
    return foo(cast('typed_demo._Callable', None), cast('typed_demo._Callable', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('foo')
    L = out_node.fields

    assert self.x is not None
    x0 = self.x.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('x', x0))

    assert self.y is not None
    x1 = self.y.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('y', x1))

    return out_node

class ContainsLib(pybase.CompoundObj):
  _type_tag = 76
  __slots__ = ('t',)

  def __init__(self, t):
    # type: (LibToken) -> None
    self.t = t

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ContainsLib
    return ContainsLib(cast('LibToken', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ContainsLib')
    L = out_node.fields

    assert self.t is not None
    x0 = self.t.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('t', x0))

    return out_node

class CompoundWord(a_word_t, List[arith_expr_t]):
  _type_tag = 74
  @staticmethod
  def New():
    # type: () -> CompoundWord
    return CompoundWord()

  @staticmethod
  def Take(plain_list):
    # type: (List[arith_expr_t]) -> CompoundWord
    result = CompoundWord(plain_list)
    del plain_list[:]
    return result

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True
    h = runtime.NewRecord('CompoundWord')
    h.unnamed_fields = [c.PrettyTree(do_abbrev) for c in self]
    return h

