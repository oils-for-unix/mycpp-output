from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class op_t(pybase.SimpleObj):
  pass

class op_e(object):
  Plus = op_t(1)
  Minus = op_t(2)

_op_str = {
  1: 'Plus',
  2: 'Minus',
}

def op_str(val, dot=True):
  # type: (op_t, bool) -> str
  v = _op_str[val]
  if dot:
    return "op.%s" % v
  else:
    return v

class kexpr_e(object):
  Bool = 65
  Int = 66
  Str = 67
  MultiStr = 68
  Unary = 5
  Binary = 6
  Ternary = 7
  Call = 8

_kexpr_str = {
  5: 'Unary',
  6: 'Binary',
  7: 'Ternary',
  8: 'Call',
  65: 'Bool',
  66: 'Int',
  67: 'Str',
  68: 'MultiStr',
}

def kexpr_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _kexpr_str[tag]
  if dot:
    return "kexpr.%s" % v
  else:
    return v

class kexpr_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class kexpr(object):
  class Unary(kexpr_t):
    _type_tag = 5
    __slots__ = ('op', 'child')
  
    def __init__(self, op, child):
      # type: (Token, kexpr_t) -> None
      self.op = op
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> kexpr.Unary
      return kexpr.Unary(cast('Token', None), cast('kexpr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('kexpr.Unary')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      return out_node
  
  class Binary(kexpr_t):
    _type_tag = 6
    __slots__ = ('op', 'left', 'right')
  
    def __init__(self, op, left, right):
      # type: (Token, kexpr_t, kexpr_t) -> None
      self.op = op
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> kexpr.Binary
      return kexpr.Binary(cast('Token', None), cast('kexpr_t', None), cast('kexpr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('kexpr.Binary')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.left is not None
      x1 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class Ternary(kexpr_t):
    _type_tag = 7
    __slots__ = ('op', 'left', 'cond', 'right')
  
    def __init__(self, op, left, cond, right):
      # type: (Token, kexpr_t, kexpr_t, kexpr_t) -> None
      self.op = op
      self.left = left
      self.cond = cond
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> kexpr.Ternary
      return kexpr.Ternary(cast('Token', None), cast('kexpr_t', None), cast('kexpr_t', None), cast('kexpr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('kexpr.Ternary')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.left is not None
      x1 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x1))
  
      assert self.cond is not None
      x2 = self.cond.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('cond', x2))
  
      assert self.right is not None
      x3 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x3))
  
      return out_node
  
  class Call(kexpr_t):
    _type_tag = 8
    __slots__ = ('f', 'args')
  
    def __init__(self, f, args):
      # type: (kexpr_t, List[kexpr_t]) -> None
      self.f = f
      self.args = args
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> kexpr.Call
      return kexpr.Call(cast('kexpr_t', None), [] if alloc_lists else cast('List[kexpr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('kexpr.Call')
      L = out_node.fields
  
      assert self.f is not None
      x0 = self.f.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('f', x0))
  
      if self.args is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.args:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('args', x1))
  
      return out_node
  
  pass

class ktype_e(object):
  Bool = 1
  Int = 2
  Str = 3
  List = 4
  Dict = 5
  Class = 6
  Data = 7
  Enum = 8

_ktype_str = {
  1: 'Bool',
  2: 'Int',
  3: 'Str',
  4: 'List',
  5: 'Dict',
  6: 'Class',
  7: 'Data',
  8: 'Enum',
}

def ktype_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _ktype_str[tag]
  if dot:
    return "ktype.%s" % v
  else:
    return v

class ktype_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class ktype__Bool(ktype_t):
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

    out_node = NewRecord('ktype.Bool')
    L = out_node.fields

    return out_node

class ktype__Int(ktype_t):
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

    out_node = NewRecord('ktype.Int')
    L = out_node.fields

    return out_node

class ktype__Str(ktype_t):
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

    out_node = NewRecord('ktype.Str')
    L = out_node.fields

    return out_node

class ktype(object):
  Bool = ktype__Bool()
  
  Int = ktype__Int()
  
  Str = ktype__Str()
  
  class List(ktype_t):
    _type_tag = 4
    __slots__ = ('T',)
  
    def __init__(self, T):
      # type: (ktype_t) -> None
      self.T = T
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> ktype.List
      return ktype.List(cast('ktype_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('ktype.List')
      L = out_node.fields
  
      assert self.T is not None
      x0 = self.T.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('T', x0))
  
      return out_node
  
  class Dict(ktype_t):
    _type_tag = 5
    __slots__ = ('K', 'V')
  
    def __init__(self, K, V):
      # type: (ktype_t, ktype_t) -> None
      self.K = K
      self.V = V
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> ktype.Dict
      return ktype.Dict(cast('ktype_t', None), cast('ktype_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('ktype.Dict')
      L = out_node.fields
  
      assert self.K is not None
      x0 = self.K.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('K', x0))
  
      assert self.V is not None
      x1 = self.V.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('V', x1))
  
      return out_node
  
  class Class(ktype_t):
    _type_tag = 6
    __slots__ = ('name',)
  
    def __init__(self, name):
      # type: (str) -> None
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> ktype.Class
      return ktype.Class('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('ktype.Class')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      return out_node
  
  class Data(ktype_t):
    _type_tag = 7
    __slots__ = ('fields',)
  
    def __init__(self, fields):
      # type: (List[Field_]) -> None
      self.fields = fields
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> ktype.Data
      return ktype.Data([] if alloc_lists else cast('List[Field_]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('ktype.Data')
      L = out_node.fields
  
      if self.fields is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.fields:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('fields', x0))
  
      return out_node
  
  class Enum(ktype_t):
    _type_tag = 8
    __slots__ = ('variants',)
  
    def __init__(self, variants):
      # type: (List[variant]) -> None
      self.variants = variants
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> ktype.Enum
      return ktype.Enum([] if alloc_lists else cast('List[variant]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('ktype.Enum')
      L = out_node.fields
  
      if self.variants is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.variants:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('variants', x0))
  
      return out_node
  
  pass

class stmt_e(object):
  VarDecl = 1
  PlaceMutation = 2
  If = 3
  Switch = 4
  For = 5
  While = 6
  Break = 7
  Continue = 8
  Return = 9
  Try = 10
  With = 11

_stmt_str = {
  1: 'VarDecl',
  2: 'PlaceMutation',
  3: 'If',
  4: 'Switch',
  5: 'For',
  6: 'While',
  7: 'Break',
  8: 'Continue',
  9: 'Return',
  10: 'Try',
  11: 'With',
}

def stmt_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _stmt_str[tag]
  if dot:
    return "stmt.%s" % v
  else:
    return v

class stmt_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class stmt__If(stmt_t):
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

    out_node = NewRecord('stmt.If')
    L = out_node.fields

    return out_node

class stmt__Switch(stmt_t):
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

    out_node = NewRecord('stmt.Switch')
    L = out_node.fields

    return out_node

class stmt__For(stmt_t):
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

    out_node = NewRecord('stmt.For')
    L = out_node.fields

    return out_node

class stmt__While(stmt_t):
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

    out_node = NewRecord('stmt.While')
    L = out_node.fields

    return out_node

class stmt__Break(stmt_t):
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

    out_node = NewRecord('stmt.Break')
    L = out_node.fields

    return out_node

class stmt__Continue(stmt_t):
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

    out_node = NewRecord('stmt.Continue')
    L = out_node.fields

    return out_node

class stmt__Try(stmt_t):
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

    out_node = NewRecord('stmt.Try')
    L = out_node.fields

    return out_node

class stmt__With(stmt_t):
  _type_tag = 11
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

    out_node = NewRecord('stmt.With')
    L = out_node.fields

    return out_node

class stmt(object):
  class VarDecl(stmt_t):
    _type_tag = 1
    __slots__ = ('keyword',)
  
    def __init__(self, keyword):
      # type: (Token) -> None
      self.keyword = keyword
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> stmt.VarDecl
      return stmt.VarDecl(cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('stmt.VarDecl')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      return out_node
  
  class PlaceMutation(stmt_t):
    _type_tag = 2
    __slots__ = ('keyword',)
  
    def __init__(self, keyword):
      # type: (Token) -> None
      self.keyword = keyword
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> stmt.PlaceMutation
      return stmt.PlaceMutation(cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('stmt.PlaceMutation')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      return out_node
  
  If = stmt__If()
  
  Switch = stmt__Switch()
  
  For = stmt__For()
  
  While = stmt__While()
  
  Break = stmt__Break()
  
  Continue = stmt__Continue()
  
  class Return(stmt_t):
    _type_tag = 9
    __slots__ = ('e',)
  
    def __init__(self, e):
      # type: (kexpr_t) -> None
      self.e = e
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> stmt.Return
      return stmt.Return(cast('kexpr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('stmt.Return')
      L = out_node.fields
  
      assert self.e is not None
      x0 = self.e.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('e', x0))
  
      return out_node
  
  Try = stmt__Try()
  
  With = stmt__With()
  
  pass

class class_def_t(pybase.SimpleObj):
  pass

class class_def_e(object):
  Constructor = class_def_t(1)
  Destructor = class_def_t(2)
  Method = class_def_t(3)
  Field = class_def_t(4)

_class_def_str = {
  1: 'Constructor',
  2: 'Destructor',
  3: 'Method',
  4: 'Field',
}

def class_def_str(val, dot=True):
  # type: (class_def_t, bool) -> str
  v = _class_def_str[val]
  if dot:
    return "class_def.%s" % v
  else:
    return v

class mod_def_e(object):
  Global = 1
  Func = 2
  Class = 3
  Import = 4
  Include = 5
  Data = 6
  Enum = 7

_mod_def_str = {
  1: 'Global',
  2: 'Func',
  3: 'Class',
  4: 'Import',
  5: 'Include',
  6: 'Data',
  7: 'Enum',
}

def mod_def_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _mod_def_str[tag]
  if dot:
    return "mod_def.%s" % v
  else:
    return v

class mod_def_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class mod_def__Import(mod_def_t):
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

    out_node = NewRecord('mod_def.Import')
    L = out_node.fields

    return out_node

class mod_def__Data(mod_def_t):
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

    out_node = NewRecord('mod_def.Data')
    L = out_node.fields

    return out_node

class mod_def__Enum(mod_def_t):
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

    out_node = NewRecord('mod_def.Enum')
    L = out_node.fields

    return out_node

class mod_def(object):
  class Global(mod_def_t):
    _type_tag = 1
    __slots__ = ('name_type',)
  
    def __init__(self, name_type):
      # type: (NameType) -> None
      self.name_type = name_type
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> mod_def.Global
      return mod_def.Global(cast('NameType', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('mod_def.Global')
      L = out_node.fields
  
      assert self.name_type is not None
      x0 = self.name_type.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('name_type', x0))
  
      return out_node
  
  class Func(mod_def_t):
    _type_tag = 2
    __slots__ = ('name', 'sig', 'statements')
  
    def __init__(self, name, sig, statements):
      # type: (str, Signature, List[stmt_t]) -> None
      self.name = name
      self.sig = sig
      self.statements = statements
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> mod_def.Func
      return mod_def.Func('', cast('Signature', None), [] if alloc_lists else cast('List[stmt_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('mod_def.Func')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      assert self.sig is not None
      x1 = self.sig.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('sig', x1))
  
      if self.statements is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.statements:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('statements', x2))
  
      return out_node
  
  class Class(mod_def_t):
    _type_tag = 3
    __slots__ = ('name', 'defs')
  
    def __init__(self, name, defs):
      # type: (str, List[class_def_t]) -> None
      self.name = name
      self.defs = defs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> mod_def.Class
      return mod_def.Class('', [] if alloc_lists else cast('List[class_def_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('mod_def.Class')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      if self.defs is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.defs:
          x1.children.append(hnode.Leaf(class_def_str(i1), color_e.TypeName))
        L.append(Field('defs', x1))
  
      return out_node
  
  Import = mod_def__Import()
  
  class Include(mod_def_t):
    _type_tag = 5
    __slots__ = ('path',)
  
    def __init__(self, path):
      # type: (str) -> None
      self.path = path
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> mod_def.Include
      return mod_def.Include('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('mod_def.Include')
      L = out_node.fields
  
      x0 = NewLeaf(self.path, color_e.StringConst)
      L.append(Field('path', x0))
  
      return out_node
  
  Data = mod_def__Data()
  
  Enum = mod_def__Enum()
  
  pass

class Token(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('path', 'chunk', 'start', 'length')

  def __init__(self, path, chunk, start, length):
    # type: (str, str, int, int) -> None
    self.path = path
    self.chunk = chunk
    self.start = start
    self.length = length

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Token
    return Token('', '', -1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Token')
    L = out_node.fields

    x0 = NewLeaf(self.path, color_e.StringConst)
    L.append(Field('path', x0))

    x1 = NewLeaf(self.chunk, color_e.StringConst)
    L.append(Field('chunk', x1))

    x2 = hnode.Leaf(str(self.start), color_e.OtherConst)
    L.append(Field('start', x2))

    x3 = hnode.Leaf(str(self.length), color_e.OtherConst)
    L.append(Field('length', x3))

    return out_node

class Bool(kexpr_t):
  _type_tag = 65
  __slots__ = ('b', 'loc')

  def __init__(self, b, loc):
    # type: (bool, Token) -> None
    self.b = b
    self.loc = loc

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Bool
    return Bool(False, cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Bool')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.b else 'F', color_e.OtherConst)
    L.append(Field('b', x0))

    assert self.loc is not None
    x1 = self.loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('loc', x1))

    return out_node

class Int(kexpr_t):
  _type_tag = 66
  __slots__ = ('i', 'loc')

  def __init__(self, i, loc):
    # type: (int, Token) -> None
    self.i = i
    self.loc = loc

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Int
    return Int(-1, cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Int')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
    L.append(Field('i', x0))

    assert self.loc is not None
    x1 = self.loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('loc', x1))

    return out_node

class Str(kexpr_t):
  _type_tag = 67
  __slots__ = ('s', 'loc')

  def __init__(self, s, loc):
    # type: (str, Token) -> None
    self.s = s
    self.loc = loc

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Str
    return Str('', cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Str')
    L = out_node.fields

    x0 = NewLeaf(self.s, color_e.StringConst)
    L.append(Field('s', x0))

    assert self.loc is not None
    x1 = self.loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('loc', x1))

    return out_node

class MultiStr(kexpr_t):
  _type_tag = 68
  __slots__ = ('lines',)

  def __init__(self, lines):
    # type: (List[Token]) -> None
    self.lines = lines

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> MultiStr
    return MultiStr([] if alloc_lists else cast('List[Token]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('MultiStr')
    L = out_node.fields

    if self.lines is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.lines:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('lines', x0))

    return out_node

class Field_(pybase.CompoundObj):
  _type_tag = 69
  __slots__ = ('name', 'typ')

  def __init__(self, name, typ):
    # type: (str, ktype_t) -> None
    self.name = name
    self.typ = typ

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Field_
    return Field_('', cast('ktype_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Field_')
    L = out_node.fields

    x0 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x0))

    assert self.typ is not None
    x1 = self.typ.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('typ', x1))

    return out_node

class variant(pybase.CompoundObj):
  _type_tag = 70
  __slots__ = ('fields',)

  def __init__(self, fields):
    # type: (List[Field_]) -> None
    self.fields = fields

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> variant
    return variant([] if alloc_lists else cast('List[Field_]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('variant')
    L = out_node.fields

    if self.fields is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.fields:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('fields', x0))

    return out_node

class NameType(pybase.CompoundObj):
  _type_tag = 71
  __slots__ = ('name', 'typ')

  def __init__(self, name, typ):
    # type: (str, ktype_t) -> None
    self.name = name
    self.typ = typ

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> NameType
    return NameType('', cast('ktype_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('NameType')
    L = out_node.fields

    x0 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x0))

    assert self.typ is not None
    x1 = self.typ.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('typ', x1))

    return out_node

class Signature(pybase.CompoundObj):
  _type_tag = 72
  __slots__ = ('params', 'return_type')

  def __init__(self, params, return_type):
    # type: (List[NameType], ktype_t) -> None
    self.params = params
    self.return_type = return_type

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Signature
    return Signature([] if alloc_lists else cast('List[NameType]', None), cast('ktype_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Signature')
    L = out_node.fields

    if self.params is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.params:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('params', x0))

    assert self.return_type is not None
    x1 = self.return_type.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('return_type', x1))

    return out_node

class Module(pybase.CompoundObj):
  _type_tag = 73
  __slots__ = ('name', 'defs')

  def __init__(self, name, defs):
    # type: (str, List[mod_def_t]) -> None
    self.name = name
    self.defs = defs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Module
    return Module('', [] if alloc_lists else cast('List[mod_def_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Module')
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

class Program(pybase.CompoundObj):
  _type_tag = 74
  __slots__ = ('main_module', 'modules')

  def __init__(self, main_module, modules):
    # type: (str, List[Module]) -> None
    self.main_module = main_module
    self.modules = modules

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Program
    return Program('', [] if alloc_lists else cast('List[Module]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Program')
    L = out_node.fields

    x0 = NewLeaf(self.main_module, color_e.StringConst)
    L.append(Field('main_module', x0))

    if self.modules is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.modules:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('modules', x1))

    return out_node

