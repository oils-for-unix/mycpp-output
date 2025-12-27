from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class tok_t(pybase.SimpleObj):
  pass

class tok_e(object):
  Const = tok_t(1)
  Var = tok_t(2)
  Op1 = tok_t(3)
  Op2 = tok_t(4)
  Paren = tok_t(5)
  Eof = tok_t(6)
  Invalid = tok_t(7)

_tok_str = {
  1: 'Const',
  2: 'Var',
  3: 'Op1',
  4: 'Op2',
  5: 'Paren',
  6: 'Eof',
  7: 'Invalid',
}

def tok_str(val, dot=True):
  # type: (tok_t, bool) -> str
  v = _tok_str[val]
  if dot:
    return "tok.%s" % v
  else:
    return v

class expr_e(object):
  Const = 1
  Var = 2
  Binary = 3

_expr_str = {
  1: 'Const',
  2: 'Var',
  3: 'Binary',
}

def expr_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _expr_str[tag]
  if dot:
    return "expr.%s" % v
  else:
    return v

class expr_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class expr(object):
  class Const(expr_t):
    _type_tag = 1
    __slots__ = ('i',)
  
    def __init__(self, i):
      # type: (int) -> None
      self.i = i
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Const
      return expr.Const(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Const')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
      L.append(Field('i', x0))
  
      return out_node
  
  class Var(expr_t):
    _type_tag = 2
    __slots__ = ('name',)
  
    def __init__(self, name):
      # type: (str) -> None
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Var
      return expr.Var('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Var')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      return out_node
  
  class Binary(expr_t):
    _type_tag = 3
    __slots__ = ('op', 'left', 'right')
  
    def __init__(self, op, left, right):
      # type: (str, expr_t, expr_t) -> None
      self.op = op
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Binary
      return expr.Binary('', cast('expr_t', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Binary')
      L = out_node.fields
  
      x0 = NewLeaf(self.op, color_e.StringConst)
      L.append(Field('op', x0))
  
      assert self.left is not None
      x1 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  pass

class Measure_v(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('a', 'b')

  def __init__(self, a, b):
    # type: (int, int) -> None
    self.a = a
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Measure_v
    return Measure_v(-1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Measure_v')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.a), color_e.OtherConst)
    L.append(Field('a', x0))

    x1 = hnode.Leaf(str(self.b), color_e.OtherConst)
    L.append(Field('b', x1))

    return out_node

class MeasuredDoc(pybase.CompoundObj):
  _type_tag = 66
  __slots__ = ('s', 'measure')

  def __init__(self, s, measure):
    # type: (str, Measure_v) -> None
    self.s = s
    self.measure = measure

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> MeasuredDoc
    return MeasuredDoc('', cast('Measure_v', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('MeasuredDoc')
    L = out_node.fields

    x0 = NewLeaf(self.s, color_e.StringConst)
    L.append(Field('s', x0))

    assert self.measure is not None
    x1 = self.measure.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('measure', x1))

    return out_node

class CompoundWord(pybase.CompoundObj, List[str]):
  _type_tag = 64
  @staticmethod
  def New():
    # type: () -> CompoundWord
    return CompoundWord()

  @staticmethod
  def Take(plain_list):
    # type: (List[str]) -> CompoundWord
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

