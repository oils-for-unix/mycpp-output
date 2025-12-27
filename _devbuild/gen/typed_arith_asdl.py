from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

from asdl.examples.typed_arith_abbrev import *

class arith_expr_e(object):
  NoOp = 1
  Const = 2
  Big = 3
  Var = 4
  Unary = 5
  Binary = 6
  Ternary = 7
  FuncCall = 8
  Index = 9
  Slice = 10

_arith_expr_str = {
  1: 'NoOp',
  2: 'Const',
  3: 'Big',
  4: 'Var',
  5: 'Unary',
  6: 'Binary',
  7: 'Ternary',
  8: 'FuncCall',
  9: 'Index',
  10: 'Slice',
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
  
      if do_abbrev:
        p = _arith_expr__Const(self)
        if p:
          return p
  
      out_node = NewRecord('arith_expr.Const')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
      L.append(Field('i', x0))
  
      return out_node
  
  class Big(arith_expr_t):
    _type_tag = 3
    __slots__ = ('b',)
  
    def __init__(self, b):
      # type: (mops.BigInt) -> None
      self.b = b
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Big
      return arith_expr.Big(mops.BigInt(-1))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Big')
      L = out_node.fields
  
      x0 = hnode.Leaf(mops.ToStr(self.b), color_e.OtherConst)
      L.append(Field('b', x0))
  
      return out_node
  
  class Var(arith_expr_t):
    _type_tag = 4
    __slots__ = ('name',)
  
    def __init__(self, name):
      # type: (str) -> None
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Var
      return arith_expr.Var('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      if do_abbrev:
        p = _arith_expr__Var(self)
        if p:
          return p
  
      out_node = NewRecord('arith_expr.Var')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      return out_node
  
  class Unary(arith_expr_t):
    _type_tag = 5
    __slots__ = ('op', 'a')
  
    def __init__(self, op, a):
      # type: (str, arith_expr_t) -> None
      self.op = op
      self.a = a
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Unary
      return arith_expr.Unary('', cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      if do_abbrev:
        p = _arith_expr__Unary(self)
        if p:
          return p
  
      out_node = NewRecord('arith_expr.Unary')
      L = out_node.fields
  
      x0 = NewLeaf(self.op, color_e.StringConst)
      L.append(Field('op', x0))
  
      assert self.a is not None
      x1 = self.a.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('a', x1))
  
      return out_node
  
  class Binary(arith_expr_t):
    _type_tag = 6
    __slots__ = ('op', 'left', 'right')
  
    def __init__(self, op, left, right):
      # type: (str, arith_expr_t, arith_expr_t) -> None
      self.op = op
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Binary
      return arith_expr.Binary('', cast('arith_expr_t', None), cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      if do_abbrev:
        p = _arith_expr__Binary(self)
        if p:
          return p
  
      out_node = NewRecord('arith_expr.Binary')
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
  
  class Ternary(arith_expr_t):
    _type_tag = 7
    __slots__ = ('cond', 'true_expr', 'false_expr')
  
    def __init__(self, cond, true_expr, false_expr):
      # type: (arith_expr_t, arith_expr_t, arith_expr_t) -> None
      self.cond = cond
      self.true_expr = true_expr
      self.false_expr = false_expr
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Ternary
      return arith_expr.Ternary(cast('arith_expr_t', None), cast('arith_expr_t', None), cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Ternary')
      L = out_node.fields
  
      assert self.cond is not None
      x0 = self.cond.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('cond', x0))
  
      assert self.true_expr is not None
      x1 = self.true_expr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('true_expr', x1))
  
      assert self.false_expr is not None
      x2 = self.false_expr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('false_expr', x2))
  
      return out_node
  
  class FuncCall(arith_expr_t):
    _type_tag = 8
    __slots__ = ('name', 'args')
  
    def __init__(self, name, args):
      # type: (str, List[arith_expr_t]) -> None
      self.name = name
      self.args = args
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.FuncCall
      return arith_expr.FuncCall('', [] if alloc_lists else cast('List[arith_expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.FuncCall')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      if self.args is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.args:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('args', x1))
  
      return out_node
  
  class Index(arith_expr_t):
    _type_tag = 9
    __slots__ = ('a', 'index')
  
    def __init__(self, a, index):
      # type: (arith_expr_t, arith_expr_t) -> None
      self.a = a
      self.index = index
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Index
      return arith_expr.Index(cast('arith_expr_t', None), cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Index')
      L = out_node.fields
  
      assert self.a is not None
      x0 = self.a.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('a', x0))
  
      assert self.index is not None
      x1 = self.index.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('index', x1))
  
      return out_node
  
  class Slice(arith_expr_t):
    _type_tag = 10
    __slots__ = ('a', 'begin', 'end', 'stride')
  
    def __init__(self, a, begin, end, stride):
      # type: (arith_expr_t, Optional[arith_expr_t], Optional[arith_expr_t], Optional[arith_expr_t]) -> None
      self.a = a
      self.begin = begin
      self.end = end
      self.stride = stride
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Slice
      return arith_expr.Slice(cast('arith_expr_t', None), cast('Optional[arith_expr_t]', None), cast('Optional[arith_expr_t]', None), cast('Optional[arith_expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Slice')
      L = out_node.fields
  
      assert self.a is not None
      x0 = self.a.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('a', x0))
  
      if self.begin is not None:  # Optional
        x1 = self.begin.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('begin', x1))
  
      if self.end is not None:  # Optional
        x2 = self.end.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('end', x2))
  
      if self.stride is not None:  # Optional
        x3 = self.stride.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('stride', x3))
  
      return out_node
  
  pass

class pipeline(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('negated',)

  def __init__(self, negated):
    # type: (bool) -> None
    self.negated = negated

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> pipeline
    return pipeline(False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('pipeline')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.negated else 'F', color_e.OtherConst)
    L.append(Field('negated', x0))

    return out_node

