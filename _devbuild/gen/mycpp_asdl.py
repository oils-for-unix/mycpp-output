from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class mtype_t(pybase.SimpleObj):
  pass

class mtype_e(object):
  Foo = mtype_t(1)

_mtype_str = {
  1: 'Foo',
}

def mtype_str(val, dot=True):
  # type: (mtype_t, bool) -> str
  v = _mtype_str[val]
  if dot:
    return "mtype.%s" % v
  else:
    return v

class yaks_type_e(object):
  NoneType = 1
  NoReturn = 2
  IOError_OSError = 3
  Bool = 4
  Int = 5
  Float = 6
  Str = 7
  Class = 8
  Callable = 9
  Dict_ = 10
  List_ = 11
  Iterator = 12
  Tuple = 13
  Optional = 14
  Alias = 15

_yaks_type_str = {
  1: 'NoneType',
  2: 'NoReturn',
  3: 'IOError_OSError',
  4: 'Bool',
  5: 'Int',
  6: 'Float',
  7: 'Str',
  8: 'Class',
  9: 'Callable',
  10: 'Dict_',
  11: 'List_',
  12: 'Iterator',
  13: 'Tuple',
  14: 'Optional',
  15: 'Alias',
}

def yaks_type_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _yaks_type_str[tag]
  if dot:
    return "yaks_type.%s" % v
  else:
    return v

class yaks_type_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class yaks_type__NoneType(yaks_type_t):
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

    out_node = NewRecord('yaks_type.NoneType')
    L = out_node.fields

    return out_node

class yaks_type__NoReturn(yaks_type_t):
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

    out_node = NewRecord('yaks_type.NoReturn')
    L = out_node.fields

    return out_node

class yaks_type__IOError_OSError(yaks_type_t):
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

    out_node = NewRecord('yaks_type.IOError_OSError')
    L = out_node.fields

    return out_node

class yaks_type__Bool(yaks_type_t):
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

    out_node = NewRecord('yaks_type.Bool')
    L = out_node.fields

    return out_node

class yaks_type__Int(yaks_type_t):
  _type_tag = 5
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

    out_node = NewRecord('yaks_type.Int')
    L = out_node.fields

    return out_node

class yaks_type__Float(yaks_type_t):
  _type_tag = 6
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

    out_node = NewRecord('yaks_type.Float')
    L = out_node.fields

    return out_node

class yaks_type__Str(yaks_type_t):
  _type_tag = 7
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

    out_node = NewRecord('yaks_type.Str')
    L = out_node.fields

    return out_node

class yaks_type(object):
  NoneType = yaks_type__NoneType()
  
  NoReturn = yaks_type__NoReturn()
  
  IOError_OSError = yaks_type__IOError_OSError()
  
  Bool = yaks_type__Bool()
  
  Int = yaks_type__Int()
  
  Float = yaks_type__Float()
  
  Str = yaks_type__Str()
  
  class Class(yaks_type_t):
    _type_tag = 8
    __slots__ = ('mod_parts', 'name')
  
    def __init__(self, mod_parts, name):
      # type: (List[str], str) -> None
      self.mod_parts = mod_parts
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Class
      return yaks_type.Class([] if alloc_lists else cast('List[str]', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Class')
      L = out_node.fields
  
      if self.mod_parts is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.mod_parts:
          x0.children.append(NewLeaf(i0, color_e.StringConst))
        L.append(Field('mod_parts', x0))
  
      x1 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x1))
  
      return out_node
  
  class Callable(yaks_type_t):
    _type_tag = 9
    __slots__ = ('args', 'return_')
  
    def __init__(self, args, return_):
      # type: (List[yaks_type_t], yaks_type_t) -> None
      self.args = args
      self.return_ = return_
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Callable
      return yaks_type.Callable([] if alloc_lists else cast('List[yaks_type_t]', None), cast('yaks_type_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Callable')
      L = out_node.fields
  
      if self.args is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.args:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('args', x0))
  
      assert self.return_ is not None
      x1 = self.return_.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('return_', x1))
  
      return out_node
  
  class Dict_(yaks_type_t):
    _type_tag = 10
    __slots__ = ('k', 'v')
  
    def __init__(self, k, v):
      # type: (yaks_type_t, yaks_type_t) -> None
      self.k = k
      self.v = v
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Dict_
      return yaks_type.Dict_(cast('yaks_type_t', None), cast('yaks_type_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Dict_')
      L = out_node.fields
  
      assert self.k is not None
      x0 = self.k.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('k', x0))
  
      assert self.v is not None
      x1 = self.v.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('v', x1))
  
      return out_node
  
  class List_(yaks_type_t):
    _type_tag = 11
    __slots__ = ('t',)
  
    def __init__(self, t):
      # type: (yaks_type_t) -> None
      self.t = t
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.List_
      return yaks_type.List_(cast('yaks_type_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.List_')
      L = out_node.fields
  
      assert self.t is not None
      x0 = self.t.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('t', x0))
  
      return out_node
  
  class Iterator(yaks_type_t):
    _type_tag = 12
    __slots__ = ('t',)
  
    def __init__(self, t):
      # type: (yaks_type_t) -> None
      self.t = t
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Iterator
      return yaks_type.Iterator(cast('yaks_type_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Iterator')
      L = out_node.fields
  
      assert self.t is not None
      x0 = self.t.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('t', x0))
  
      return out_node
  
  class Tuple(yaks_type_t):
    _type_tag = 13
    __slots__ = ('children',)
  
    def __init__(self, children):
      # type: (List[yaks_type_t]) -> None
      self.children = children
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Tuple
      return yaks_type.Tuple([] if alloc_lists else cast('List[yaks_type_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Tuple')
      L = out_node.fields
  
      if self.children is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('children', x0))
  
      return out_node
  
  class Optional(yaks_type_t):
    _type_tag = 14
    __slots__ = ('child',)
  
    def __init__(self, child):
      # type: (yaks_type_t) -> None
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Optional
      return yaks_type.Optional(cast('yaks_type_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Optional')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      return out_node
  
  class Alias(yaks_type_t):
    _type_tag = 15
    __slots__ = ('child',)
  
    def __init__(self, child):
      # type: (yaks_type_t) -> None
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_type.Alias
      return yaks_type.Alias(cast('yaks_type_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_type.Alias')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      return out_node
  
  pass

class yaks_expr_e(object):
  BoolExpr = 1
  IntExpr = 2
  FloatExpr = 3
  StrExpr = 4
  MemberExpr = 5
  CallExpr = 6
  Cast = 7

_yaks_expr_str = {
  1: 'BoolExpr',
  2: 'IntExpr',
  3: 'FloatExpr',
  4: 'StrExpr',
  5: 'MemberExpr',
  6: 'CallExpr',
  7: 'Cast',
}

def yaks_expr_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _yaks_expr_str[tag]
  if dot:
    return "yaks_expr.%s" % v
  else:
    return v

class yaks_expr_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class yaks_expr__MemberExpr(yaks_expr_t):
  _type_tag = 5
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

    out_node = NewRecord('yaks_expr.MemberExpr')
    L = out_node.fields

    return out_node

class yaks_expr__CallExpr(yaks_expr_t):
  _type_tag = 6
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

    out_node = NewRecord('yaks_expr.CallExpr')
    L = out_node.fields

    return out_node

class yaks_expr__Cast(yaks_expr_t):
  _type_tag = 7
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

    out_node = NewRecord('yaks_expr.Cast')
    L = out_node.fields

    return out_node

class yaks_expr(object):
  class BoolExpr(yaks_expr_t):
    _type_tag = 1
    __slots__ = ('value',)
  
    def __init__(self, value):
      # type: (bool) -> None
      self.value = value
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_expr.BoolExpr
      return yaks_expr.BoolExpr(False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_expr.BoolExpr')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.value else 'F', color_e.OtherConst)
      L.append(Field('value', x0))
  
      return out_node
  
  class IntExpr(yaks_expr_t):
    _type_tag = 2
    __slots__ = ('value',)
  
    def __init__(self, value):
      # type: (int) -> None
      self.value = value
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_expr.IntExpr
      return yaks_expr.IntExpr(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_expr.IntExpr')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.value), color_e.OtherConst)
      L.append(Field('value', x0))
  
      return out_node
  
  class FloatExpr(yaks_expr_t):
    _type_tag = 3
    __slots__ = ('value',)
  
    def __init__(self, value):
      # type: (float) -> None
      self.value = value
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_expr.FloatExpr
      return yaks_expr.FloatExpr(0.0)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_expr.FloatExpr')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.value), color_e.OtherConst)
      L.append(Field('value', x0))
  
      return out_node
  
  class StrExpr(yaks_expr_t):
    _type_tag = 4
    __slots__ = ('value',)
  
    def __init__(self, value):
      # type: (str) -> None
      self.value = value
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_expr.StrExpr
      return yaks_expr.StrExpr('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_expr.StrExpr')
      L = out_node.fields
  
      x0 = NewLeaf(self.value, color_e.StringConst)
      L.append(Field('value', x0))
  
      return out_node
  
  MemberExpr = yaks_expr__MemberExpr()
  
  CallExpr = yaks_expr__CallExpr()
  
  Cast = yaks_expr__Cast()
  
  pass

class yaks_stmt_e(object):
  PassStmt = 1
  ExpressionStmt = 2
  DelStmt = 3
  RaiseStmt = 4
  AssignmentStmt = 5
  IfStmt = 6
  ForStmt = 7
  WhileStmt = 8
  Break = 9
  Continue = 10
  Return = 11
  WithStmt = 12
  TryStmt = 13
  FuncDef = 14
  ClassDef = 15
  ImportFrom = 16

_yaks_stmt_str = {
  1: 'PassStmt',
  2: 'ExpressionStmt',
  3: 'DelStmt',
  4: 'RaiseStmt',
  5: 'AssignmentStmt',
  6: 'IfStmt',
  7: 'ForStmt',
  8: 'WhileStmt',
  9: 'Break',
  10: 'Continue',
  11: 'Return',
  12: 'WithStmt',
  13: 'TryStmt',
  14: 'FuncDef',
  15: 'ClassDef',
  16: 'ImportFrom',
}

def yaks_stmt_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _yaks_stmt_str[tag]
  if dot:
    return "yaks_stmt.%s" % v
  else:
    return v

class yaks_stmt_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class yaks_stmt__PassStmt(yaks_stmt_t):
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

    out_node = NewRecord('yaks_stmt.PassStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__ExpressionStmt(yaks_stmt_t):
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

    out_node = NewRecord('yaks_stmt.ExpressionStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__DelStmt(yaks_stmt_t):
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

    out_node = NewRecord('yaks_stmt.DelStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__RaiseStmt(yaks_stmt_t):
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

    out_node = NewRecord('yaks_stmt.RaiseStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__AssignmentStmt(yaks_stmt_t):
  _type_tag = 5
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

    out_node = NewRecord('yaks_stmt.AssignmentStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__IfStmt(yaks_stmt_t):
  _type_tag = 6
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

    out_node = NewRecord('yaks_stmt.IfStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__ForStmt(yaks_stmt_t):
  _type_tag = 7
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

    out_node = NewRecord('yaks_stmt.ForStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__WhileStmt(yaks_stmt_t):
  _type_tag = 8
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

    out_node = NewRecord('yaks_stmt.WhileStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__Break(yaks_stmt_t):
  _type_tag = 9
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

    out_node = NewRecord('yaks_stmt.Break')
    L = out_node.fields

    return out_node

class yaks_stmt__Continue(yaks_stmt_t):
  _type_tag = 10
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

    out_node = NewRecord('yaks_stmt.Continue')
    L = out_node.fields

    return out_node

class yaks_stmt__WithStmt(yaks_stmt_t):
  _type_tag = 12
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

    out_node = NewRecord('yaks_stmt.WithStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__TryStmt(yaks_stmt_t):
  _type_tag = 13
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

    out_node = NewRecord('yaks_stmt.TryStmt')
    L = out_node.fields

    return out_node

class yaks_stmt__ImportFrom(yaks_stmt_t):
  _type_tag = 16
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

    out_node = NewRecord('yaks_stmt.ImportFrom')
    L = out_node.fields

    return out_node

class yaks_stmt(object):
  PassStmt = yaks_stmt__PassStmt()
  
  ExpressionStmt = yaks_stmt__ExpressionStmt()
  
  DelStmt = yaks_stmt__DelStmt()
  
  RaiseStmt = yaks_stmt__RaiseStmt()
  
  AssignmentStmt = yaks_stmt__AssignmentStmt()
  
  IfStmt = yaks_stmt__IfStmt()
  
  ForStmt = yaks_stmt__ForStmt()
  
  WhileStmt = yaks_stmt__WhileStmt()
  
  Break = yaks_stmt__Break()
  
  Continue = yaks_stmt__Continue()
  
  class Return(yaks_stmt_t):
    _type_tag = 11
    __slots__ = ('val',)
  
    def __init__(self, val):
      # type: (yaks_expr_t) -> None
      self.val = val
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_stmt.Return
      return yaks_stmt.Return(cast('yaks_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_stmt.Return')
      L = out_node.fields
  
      assert self.val is not None
      x0 = self.val.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('val', x0))
  
      return out_node
  
  WithStmt = yaks_stmt__WithStmt()
  
  TryStmt = yaks_stmt__TryStmt()
  
  class FuncDef(yaks_stmt_t):
    _type_tag = 14
    __slots__ = ('name',)
  
    def __init__(self, name):
      # type: (str) -> None
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_stmt.FuncDef
      return yaks_stmt.FuncDef('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_stmt.FuncDef')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      return out_node
  
  class ClassDef(yaks_stmt_t):
    _type_tag = 15
    __slots__ = ('name',)
  
    def __init__(self, name):
      # type: (str) -> None
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> yaks_stmt.ClassDef
      return yaks_stmt.ClassDef('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('yaks_stmt.ClassDef')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      return out_node
  
  ImportFrom = yaks_stmt__ImportFrom()
  
  pass

class yaks_file(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('name', 'defs')

  def __init__(self, name, defs):
    # type: (str, List[yaks_stmt_t]) -> None
    self.name = name
    self.defs = defs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> yaks_file
    return yaks_file('', [] if alloc_lists else cast('List[yaks_stmt_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('yaks_file')
    L = out_node.fields

    x0 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x0))

    if self.defs is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.defs:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('defs', x1))

    return out_node

