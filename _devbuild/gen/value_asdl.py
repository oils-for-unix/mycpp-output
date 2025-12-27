from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

if TYPE_CHECKING:
  from _devbuild.gen.syntax_asdl import loc_t, Token, expr_t, command_t, DoubleQuoted, re_t, proc_sig_t, Func, NameType, EggexFlag, BraceGroup, SourceLine, debug_frame_t, ShFunction, cmd_frag_t
  from _devbuild.gen.runtime_asdl import Cell

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class y_lvalue_e(object):
  Local = 67
  Container = 2

_y_lvalue_str = {
  2: 'Container',
  67: 'Local',
}

def y_lvalue_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _y_lvalue_str[tag]
  if dot:
    return "y_lvalue.%s" % v
  else:
    return v

class y_lvalue_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class y_lvalue(object):
  class Container(y_lvalue_t):
    _type_tag = 2
    __slots__ = ('obj', 'index')
  
    def __init__(self, obj, index):
      # type: (value_t, value_t) -> None
      self.obj = obj
      self.index = index
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> y_lvalue.Container
      return y_lvalue.Container(cast('value_t', None), cast('value_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('y_lvalue.Container')
      L = out_node.fields
  
      assert self.obj is not None
      x0 = self.obj.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('obj', x0))
  
      assert self.index is not None
      x1 = self.index.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('index', x1))
  
      return out_node
  
  pass

class sh_lvalue_e(object):
  Var = 67
  Indexed = 2
  Keyed = 3

_sh_lvalue_str = {
  2: 'Indexed',
  3: 'Keyed',
  67: 'Var',
}

def sh_lvalue_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _sh_lvalue_str[tag]
  if dot:
    return "sh_lvalue.%s" % v
  else:
    return v

class sh_lvalue_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class sh_lvalue(object):
  class Indexed(sh_lvalue_t):
    _type_tag = 2
    __slots__ = ('name', 'index', 'blame_loc')
  
    def __init__(self, name, index, blame_loc):
      # type: (str, int, loc_t) -> None
      self.name = name
      self.index = index
      self.blame_loc = blame_loc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> sh_lvalue.Indexed
      return sh_lvalue.Indexed('', -1, cast('loc_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('sh_lvalue.Indexed')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      x1 = hnode.Leaf(str(self.index), color_e.OtherConst)
      L.append(Field('index', x1))
  
      assert self.blame_loc is not None
      x2 = self.blame_loc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_loc', x2))
  
      return out_node
  
  class Keyed(sh_lvalue_t):
    _type_tag = 3
    __slots__ = ('name', 'key', 'blame_loc')
  
    def __init__(self, name, key, blame_loc):
      # type: (str, str, loc_t) -> None
      self.name = name
      self.key = key
      self.blame_loc = blame_loc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> sh_lvalue.Keyed
      return sh_lvalue.Keyed('', '', cast('loc_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('sh_lvalue.Keyed')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      x1 = NewLeaf(self.key, color_e.StringConst)
      L.append(Field('key', x1))
  
      assert self.blame_loc is not None
      x2 = self.blame_loc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_loc', x2))
  
      return out_node
  
  pass

class eggex_ops_e(object):
  No = 1
  Yes = 2

_eggex_ops_str = {
  1: 'No',
  2: 'Yes',
}

def eggex_ops_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _eggex_ops_str[tag]
  if dot:
    return "eggex_ops.%s" % v
  else:
    return v

class eggex_ops_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class eggex_ops__No(eggex_ops_t):
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

    out_node = NewRecord('eggex_ops.No')
    L = out_node.fields

    return out_node

class eggex_ops(object):
  No = eggex_ops__No()
  
  class Yes(eggex_ops_t):
    _type_tag = 2
    __slots__ = ('convert_funcs', 'convert_toks', 'capture_names')
  
    def __init__(self, convert_funcs, convert_toks, capture_names):
      # type: (List[Optional[value_t]], List[Optional[Token]], List[Optional[str]]) -> None
      self.convert_funcs = convert_funcs
      self.convert_toks = convert_toks
      self.capture_names = capture_names
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> eggex_ops.Yes
      return eggex_ops.Yes([] if alloc_lists else cast('List[Optional[value_t]]', None), [] if alloc_lists else cast('List[Optional[Token]]', None), [] if alloc_lists else cast('List[Optional[str]]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('eggex_ops.Yes')
      L = out_node.fields
  
      if self.convert_funcs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.convert_funcs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('convert_funcs', x0))
  
      if self.convert_toks is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.convert_toks:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('convert_toks', x1))
  
      if self.capture_names is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.capture_names:
          x2.children.append(NewLeaf(i2, color_e.StringConst))
        L.append(Field('capture_names', x2))
  
      return out_node
  
  pass

class regex_match_e(object):
  No = 1
  Yes = 68

_regex_match_str = {
  1: 'No',
  68: 'Yes',
}

def regex_match_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _regex_match_str[tag]
  if dot:
    return "regex_match.%s" % v
  else:
    return v

class regex_match_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class regex_match__No(regex_match_t):
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

    out_node = NewRecord('regex_match.No')
    L = out_node.fields

    return out_node

class regex_match(object):
  No = regex_match__No()
  
  pass

class value_e(object):
  Interrupted = 1
  Stdin = 2
  Slice = 3
  Undef = 4
  Str = 5
  InitializerList = 6
  InternalStringArray = 7
  BashArray = 8
  BashAssoc = 9
  Null = 10
  Bool = 11
  Int = 12
  Float = 13
  List = 14
  Dict = 15
  Obj = 69
  Range = 17
  Eggex = 18
  Match = 68
  Place = 20
  Frame = 21
  DebugFrame = 22
  BoundFunc = 23
  BuiltinFunc = 24
  Func = 25
  BuiltinProc = 26
  Proc = 27
  Expr = 28
  CommandFrag = 29
  Command = 30

_value_str = {
  1: 'Interrupted',
  2: 'Stdin',
  3: 'Slice',
  4: 'Undef',
  5: 'Str',
  6: 'InitializerList',
  7: 'InternalStringArray',
  8: 'BashArray',
  9: 'BashAssoc',
  10: 'Null',
  11: 'Bool',
  12: 'Int',
  13: 'Float',
  14: 'List',
  15: 'Dict',
  17: 'Range',
  18: 'Eggex',
  20: 'Place',
  21: 'Frame',
  22: 'DebugFrame',
  23: 'BoundFunc',
  24: 'BuiltinFunc',
  25: 'Func',
  26: 'BuiltinProc',
  27: 'Proc',
  28: 'Expr',
  29: 'CommandFrag',
  30: 'Command',
  68: 'Match',
  69: 'Obj',
}

def value_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _value_str[tag]
  if dot:
    return "value.%s" % v
  else:
    return v

class value_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class value__Interrupted(value_t):
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

    out_node = NewRecord('value.Interrupted')
    L = out_node.fields

    return out_node

class value__Stdin(value_t):
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

    out_node = NewRecord('value.Stdin')
    L = out_node.fields

    return out_node

class value__Undef(value_t):
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

    out_node = NewRecord('value.Undef')
    L = out_node.fields

    return out_node

class value__Null(value_t):
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

    out_node = NewRecord('value.Null')
    L = out_node.fields

    return out_node

class value(object):
  Interrupted = value__Interrupted()
  
  Stdin = value__Stdin()
  
  class Slice(value_t):
    _type_tag = 3
    __slots__ = ('lower', 'upper')
  
    def __init__(self, lower, upper):
      # type: (Optional[IntBox], Optional[IntBox]) -> None
      self.lower = lower
      self.upper = upper
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Slice
      return value.Slice(cast('Optional[IntBox]', None), cast('Optional[IntBox]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Slice')
      L = out_node.fields
  
      if self.lower is not None:  # Optional
        x0 = self.lower.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('lower', x0))
  
      if self.upper is not None:  # Optional
        x1 = self.upper.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('upper', x1))
  
      return out_node
  
  Undef = value__Undef()
  
  class Str(value_t):
    _type_tag = 5
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Str
      return value.Str('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Str')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  class InitializerList(value_t):
    _type_tag = 6
    __slots__ = ('assigns',)
  
    def __init__(self, assigns):
      # type: (List[InitializerValue]) -> None
      self.assigns = assigns
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.InitializerList
      return value.InitializerList([] if alloc_lists else cast('List[InitializerValue]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.InitializerList')
      L = out_node.fields
  
      if self.assigns is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.assigns:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('assigns', x0))
  
      return out_node
  
  class InternalStringArray(value_t):
    _type_tag = 7
    __slots__ = ('strs',)
  
    def __init__(self, strs):
      # type: (List[str]) -> None
      self.strs = strs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.InternalStringArray
      return value.InternalStringArray([] if alloc_lists else cast('List[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.InternalStringArray')
      L = out_node.fields
  
      if self.strs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.strs:
          x0.children.append(NewLeaf(i0, color_e.StringConst))
        L.append(Field('strs', x0))
  
      return out_node
  
  class BashArray(value_t):
    _type_tag = 8
    __slots__ = ('d', 'max_index')
  
    def __init__(self, d, max_index):
      # type: (Dict[mops.BigInt, str], mops.BigInt) -> None
      self.d = d
      self.max_index = max_index
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.BashArray
      return value.BashArray(cast('Dict[mops.BigInt, str]', None), mops.BigInt(-1))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.BashArray')
      L = out_node.fields
  
      if self.d is not None:  # Dict
        unnamed0 = []  # type: List[hnode_t]
        x0 = hnode.Record("", "{", "}", [], unnamed0)
        for k0, v0 in self.d.iteritems():
          unnamed0.append(hnode.Leaf(mops.ToStr(k0), color_e.OtherConst))
          unnamed0.append(NewLeaf(v0, color_e.StringConst))
        L.append(Field('d', x0))
  
      x1 = hnode.Leaf(mops.ToStr(self.max_index), color_e.OtherConst)
      L.append(Field('max_index', x1))
  
      return out_node
  
  class BashAssoc(value_t):
    _type_tag = 9
    __slots__ = ('d',)
  
    def __init__(self, d):
      # type: (Dict[str, str]) -> None
      self.d = d
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.BashAssoc
      return value.BashAssoc(cast('Dict[str, str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.BashAssoc')
      L = out_node.fields
  
      if self.d is not None:  # Dict
        unnamed0 = []  # type: List[hnode_t]
        x0 = hnode.Record("", "{", "}", [], unnamed0)
        for k0, v0 in self.d.iteritems():
          unnamed0.append(NewLeaf(k0, color_e.StringConst))
          unnamed0.append(NewLeaf(v0, color_e.StringConst))
        L.append(Field('d', x0))
  
      return out_node
  
  Null = value__Null()
  
  class Bool(value_t):
    _type_tag = 11
    __slots__ = ('b',)
  
    def __init__(self, b):
      # type: (bool) -> None
      self.b = b
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Bool
      return value.Bool(False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Bool')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.b else 'F', color_e.OtherConst)
      L.append(Field('b', x0))
  
      return out_node
  
  class Int(value_t):
    _type_tag = 12
    __slots__ = ('i',)
  
    def __init__(self, i):
      # type: (mops.BigInt) -> None
      self.i = i
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Int
      return value.Int(mops.BigInt(-1))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Int')
      L = out_node.fields
  
      x0 = hnode.Leaf(mops.ToStr(self.i), color_e.OtherConst)
      L.append(Field('i', x0))
  
      return out_node
  
  class Float(value_t):
    _type_tag = 13
    __slots__ = ('f',)
  
    def __init__(self, f):
      # type: (float) -> None
      self.f = f
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Float
      return value.Float(0.0)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Float')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.f), color_e.OtherConst)
      L.append(Field('f', x0))
  
      return out_node
  
  class List(value_t):
    _type_tag = 14
    __slots__ = ('items',)
  
    def __init__(self, items):
      # type: (List[value_t]) -> None
      self.items = items
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.List
      return value.List([] if alloc_lists else cast('List[value_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.List')
      L = out_node.fields
  
      if self.items is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.items:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('items', x0))
  
      return out_node
  
  class Dict(value_t):
    _type_tag = 15
    __slots__ = ('d',)
  
    def __init__(self, d):
      # type: (Dict[str, value_t]) -> None
      self.d = d
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Dict
      return value.Dict(cast('Dict[str, value_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Dict')
      L = out_node.fields
  
      if self.d is not None:  # Dict
        unnamed0 = []  # type: List[hnode_t]
        x0 = hnode.Record("", "{", "}", [], unnamed0)
        for k0, v0 in self.d.iteritems():
          unnamed0.append(NewLeaf(k0, color_e.StringConst))
          unnamed0.append(v0.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('d', x0))
  
      return out_node
  
  class Range(value_t):
    _type_tag = 17
    __slots__ = ('lower', 'upper')
  
    def __init__(self, lower, upper):
      # type: (int, int) -> None
      self.lower = lower
      self.upper = upper
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Range
      return value.Range(-1, -1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Range')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.lower), color_e.OtherConst)
      L.append(Field('lower', x0))
  
      x1 = hnode.Leaf(str(self.upper), color_e.OtherConst)
      L.append(Field('upper', x1))
  
      return out_node
  
  class Eggex(value_t):
    _type_tag = 18
    __slots__ = ('spliced', 'canonical_flags', 'convert_funcs', 'convert_toks',
                 'as_ere', 'capture_names')
  
    def __init__(self, spliced, canonical_flags, convert_funcs, convert_toks,
                 as_ere, capture_names):
      # type: (re_t, str, List[Optional[value_t]], List[Optional[Token]], Optional[str], List[Optional[str]]) -> None
      self.spliced = spliced
      self.canonical_flags = canonical_flags
      self.convert_funcs = convert_funcs
      self.convert_toks = convert_toks
      self.as_ere = as_ere
      self.capture_names = capture_names
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Eggex
      return value.Eggex(cast('re_t', None), '', [] if alloc_lists else cast('List[Optional[value_t]]', None), [] if alloc_lists else cast('List[Optional[Token]]', None), cast('Optional[str]', None), [] if alloc_lists else cast('List[Optional[str]]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Eggex')
      L = out_node.fields
  
      assert self.spliced is not None
      x0 = self.spliced.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('spliced', x0))
  
      x1 = NewLeaf(self.canonical_flags, color_e.StringConst)
      L.append(Field('canonical_flags', x1))
  
      if self.convert_funcs is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.convert_funcs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('convert_funcs', x2))
  
      if self.convert_toks is not None:  # List
        x3 = hnode.Array([])
        for i3 in self.convert_toks:
          h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
               i3.PrettyTree(do_abbrev, trav=trav))
          x3.children.append(h)
        L.append(Field('convert_toks', x3))
  
      if self.as_ere is not None:  # Optional
        x4 = NewLeaf(self.as_ere, color_e.StringConst)
        L.append(Field('as_ere', x4))
  
      if self.capture_names is not None:  # List
        x5 = hnode.Array([])
        for i5 in self.capture_names:
          x5.children.append(NewLeaf(i5, color_e.StringConst))
        L.append(Field('capture_names', x5))
  
      return out_node
  
  class Place(value_t):
    _type_tag = 20
    __slots__ = ('lval', 'frame')
  
    def __init__(self, lval, frame):
      # type: (y_lvalue_t, Dict[str, Cell]) -> None
      self.lval = lval
      self.frame = frame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Place
      return value.Place(cast('y_lvalue_t', None), cast('Dict[str, Cell]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Place')
      L = out_node.fields
  
      assert self.lval is not None
      x0 = self.lval.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('lval', x0))
  
      if self.frame is not None:  # Dict
        unnamed1 = []  # type: List[hnode_t]
        x1 = hnode.Record("", "{", "}", [], unnamed1)
        for k1, v1 in self.frame.iteritems():
          unnamed1.append(NewLeaf(k1, color_e.StringConst))
          unnamed1.append(v1.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('frame', x1))
  
      return out_node
  
  class Frame(value_t):
    _type_tag = 21
    __slots__ = ('frame',)
  
    def __init__(self, frame):
      # type: (Dict[str, Cell]) -> None
      self.frame = frame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Frame
      return value.Frame(cast('Dict[str, Cell]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Frame')
      L = out_node.fields
  
      if self.frame is not None:  # Dict
        unnamed0 = []  # type: List[hnode_t]
        x0 = hnode.Record("", "{", "}", [], unnamed0)
        for k0, v0 in self.frame.iteritems():
          unnamed0.append(NewLeaf(k0, color_e.StringConst))
          unnamed0.append(v0.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('frame', x0))
  
      return out_node
  
  class DebugFrame(value_t):
    _type_tag = 22
    __slots__ = ('frame',)
  
    def __init__(self, frame):
      # type: (debug_frame_t) -> None
      self.frame = frame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.DebugFrame
      return value.DebugFrame(cast('debug_frame_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.DebugFrame')
      L = out_node.fields
  
      assert self.frame is not None
      x0 = self.frame.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('frame', x0))
  
      return out_node
  
  class BoundFunc(value_t):
    _type_tag = 23
    __slots__ = ('me', 'func')
  
    def __init__(self, me, func):
      # type: (value_t, value_t) -> None
      self.me = me
      self.func = func
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.BoundFunc
      return value.BoundFunc(cast('value_t', None), cast('value_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.BoundFunc')
      L = out_node.fields
  
      assert self.me is not None
      x0 = self.me.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('me', x0))
  
      assert self.func is not None
      x1 = self.func.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('func', x1))
  
      return out_node
  
  class BuiltinFunc(value_t):
    _type_tag = 24
    __slots__ = ('callable',)
  
    def __init__(self, callable):
      # type: (Any) -> None
      self.callable = callable
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.BuiltinFunc
      return value.BuiltinFunc(cast('Any', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.BuiltinFunc')
      L = out_node.fields
  
      x0 = NewLeaf(str(self.callable), color_e.External)
      L.append(Field('callable', x0))
  
      return out_node
  
  class Func(value_t):
    _type_tag = 25
    __slots__ = ('name', 'parsed', 'pos_defaults', 'named_defaults',
                 'captured_frame', 'module_frame')
  
    def __init__(self, name, parsed, pos_defaults, named_defaults,
                 captured_frame, module_frame):
      # type: (str, Func, List[value_t], Dict[str, value_t], Dict[str, Cell], Dict[str, Cell]) -> None
      self.name = name
      self.parsed = parsed
      self.pos_defaults = pos_defaults
      self.named_defaults = named_defaults
      self.captured_frame = captured_frame
      self.module_frame = module_frame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Func
      return value.Func('', cast('Func', None), [] if alloc_lists else cast('List[value_t]', None), cast('Dict[str, value_t]', None), cast('Dict[str, Cell]', None), cast('Dict[str, Cell]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Func')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      assert self.parsed is not None
      x1 = self.parsed.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('parsed', x1))
  
      if self.pos_defaults is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.pos_defaults:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('pos_defaults', x2))
  
      if self.named_defaults is not None:  # Dict
        unnamed3 = []  # type: List[hnode_t]
        x3 = hnode.Record("", "{", "}", [], unnamed3)
        for k3, v3 in self.named_defaults.iteritems():
          unnamed3.append(NewLeaf(k3, color_e.StringConst))
          unnamed3.append(v3.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('named_defaults', x3))
  
      if self.captured_frame is not None:  # Dict
        unnamed4 = []  # type: List[hnode_t]
        x4 = hnode.Record("", "{", "}", [], unnamed4)
        for k4, v4 in self.captured_frame.iteritems():
          unnamed4.append(NewLeaf(k4, color_e.StringConst))
          unnamed4.append(v4.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('captured_frame', x4))
  
      if self.module_frame is not None:  # Dict
        unnamed5 = []  # type: List[hnode_t]
        x5 = hnode.Record("", "{", "}", [], unnamed5)
        for k5, v5 in self.module_frame.iteritems():
          unnamed5.append(NewLeaf(k5, color_e.StringConst))
          unnamed5.append(v5.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('module_frame', x5))
  
      return out_node
  
  class BuiltinProc(value_t):
    _type_tag = 26
    __slots__ = ('builtin',)
  
    def __init__(self, builtin):
      # type: (Any) -> None
      self.builtin = builtin
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.BuiltinProc
      return value.BuiltinProc(cast('Any', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.BuiltinProc')
      L = out_node.fields
  
      x0 = NewLeaf(str(self.builtin), color_e.External)
      L.append(Field('builtin', x0))
  
      return out_node
  
  class Proc(value_t):
    _type_tag = 27
    __slots__ = ('name', 'name_tok', 'sig', 'body', 'defaults', 'sh_compat',
                 'captured_frame', 'module_frame', 'code_str')
  
    def __init__(self, name, name_tok, sig, body, defaults, sh_compat,
                 captured_frame, module_frame, code_str):
      # type: (str, Token, proc_sig_t, command_t, Optional[ProcDefaults], bool, Dict[str, Cell], Dict[str, Cell], Optional[str]) -> None
      self.name = name
      self.name_tok = name_tok
      self.sig = sig
      self.body = body
      self.defaults = defaults
      self.sh_compat = sh_compat
      self.captured_frame = captured_frame
      self.module_frame = module_frame
      self.code_str = code_str
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Proc
      return value.Proc('', cast('Token', None), cast('proc_sig_t', None), cast('command_t', None), cast('Optional[ProcDefaults]', None), False, cast('Dict[str, Cell]', None), cast('Dict[str, Cell]', None), cast('Optional[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Proc')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      assert self.name_tok is not None
      x1 = self.name_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('name_tok', x1))
  
      assert self.sig is not None
      x2 = self.sig.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('sig', x2))
  
      assert self.body is not None
      x3 = self.body.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('body', x3))
  
      if self.defaults is not None:  # Optional
        x4 = self.defaults.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('defaults', x4))
  
      x5 = hnode.Leaf('T' if self.sh_compat else 'F', color_e.OtherConst)
      L.append(Field('sh_compat', x5))
  
      if self.captured_frame is not None:  # Dict
        unnamed6 = []  # type: List[hnode_t]
        x6 = hnode.Record("", "{", "}", [], unnamed6)
        for k6, v6 in self.captured_frame.iteritems():
          unnamed6.append(NewLeaf(k6, color_e.StringConst))
          unnamed6.append(v6.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('captured_frame', x6))
  
      if self.module_frame is not None:  # Dict
        unnamed7 = []  # type: List[hnode_t]
        x7 = hnode.Record("", "{", "}", [], unnamed7)
        for k7, v7 in self.module_frame.iteritems():
          unnamed7.append(NewLeaf(k7, color_e.StringConst))
          unnamed7.append(v7.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('module_frame', x7))
  
      if self.code_str is not None:  # Optional
        x8 = NewLeaf(self.code_str, color_e.StringConst)
        L.append(Field('code_str', x8))
  
      return out_node
  
  class Expr(value_t):
    _type_tag = 28
    __slots__ = ('e', 'captured_frame', 'module_frame')
  
    def __init__(self, e, captured_frame, module_frame):
      # type: (expr_t, Dict[str, Cell], Dict[str, Cell]) -> None
      self.e = e
      self.captured_frame = captured_frame
      self.module_frame = module_frame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Expr
      return value.Expr(cast('expr_t', None), cast('Dict[str, Cell]', None), cast('Dict[str, Cell]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Expr')
      L = out_node.fields
  
      assert self.e is not None
      x0 = self.e.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('e', x0))
  
      if self.captured_frame is not None:  # Dict
        unnamed1 = []  # type: List[hnode_t]
        x1 = hnode.Record("", "{", "}", [], unnamed1)
        for k1, v1 in self.captured_frame.iteritems():
          unnamed1.append(NewLeaf(k1, color_e.StringConst))
          unnamed1.append(v1.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('captured_frame', x1))
  
      if self.module_frame is not None:  # Dict
        unnamed2 = []  # type: List[hnode_t]
        x2 = hnode.Record("", "{", "}", [], unnamed2)
        for k2, v2 in self.module_frame.iteritems():
          unnamed2.append(NewLeaf(k2, color_e.StringConst))
          unnamed2.append(v2.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('module_frame', x2))
  
      return out_node
  
  class CommandFrag(value_t):
    _type_tag = 29
    __slots__ = ('c',)
  
    def __init__(self, c):
      # type: (command_t) -> None
      self.c = c
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.CommandFrag
      return value.CommandFrag(cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.CommandFrag')
      L = out_node.fields
  
      assert self.c is not None
      x0 = self.c.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('c', x0))
  
      return out_node
  
  class Command(value_t):
    _type_tag = 30
    __slots__ = ('frag', 'captured_frame', 'module_frame')
  
    def __init__(self, frag, captured_frame, module_frame):
      # type: (cmd_frag_t, Dict[str, Cell], Dict[str, Cell]) -> None
      self.frag = frag
      self.captured_frame = captured_frame
      self.module_frame = module_frame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Command
      return value.Command(cast('cmd_frag_t', None), cast('Dict[str, Cell]', None), cast('Dict[str, Cell]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Command')
      L = out_node.fields
  
      assert self.frag is not None
      x0 = self.frag.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('frag', x0))
  
      if self.captured_frame is not None:  # Dict
        unnamed1 = []  # type: List[hnode_t]
        x1 = hnode.Record("", "{", "}", [], unnamed1)
        for k1, v1 in self.captured_frame.iteritems():
          unnamed1.append(NewLeaf(k1, color_e.StringConst))
          unnamed1.append(v1.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('captured_frame', x1))
  
      if self.module_frame is not None:  # Dict
        unnamed2 = []  # type: List[hnode_t]
        x2 = hnode.Record("", "{", "}", [], unnamed2)
        for k2, v2 in self.module_frame.iteritems():
          unnamed2.append(NewLeaf(k2, color_e.StringConst))
          unnamed2.append(v2.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('module_frame', x2))
  
      return out_node
  
  pass

class IntBox(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('i',)

  def __init__(self, i):
    # type: (int) -> None
    self.i = i

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> IntBox
    return IntBox(-1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('IntBox')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
    L.append(Field('i', x0))

    return out_node

class InitializerValue(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('key', 'rval', 'plus_eq')

  def __init__(self, key, rval, plus_eq):
    # type: (Optional[str], str, bool) -> None
    self.key = key
    self.rval = rval
    self.plus_eq = plus_eq

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> InitializerValue
    return InitializerValue(cast('Optional[str]', None), '', False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('InitializerValue')
    L = out_node.fields

    if self.key is not None:  # Optional
      x0 = NewLeaf(self.key, color_e.StringConst)
      L.append(Field('key', x0))

    x1 = NewLeaf(self.rval, color_e.StringConst)
    L.append(Field('rval', x1))

    x2 = hnode.Leaf('T' if self.plus_eq else 'F', color_e.OtherConst)
    L.append(Field('plus_eq', x2))

    return out_node

class ProcDefaults(pybase.CompoundObj):
  _type_tag = 66
  __slots__ = ('for_word', 'for_typed', 'for_named', 'for_block')

  def __init__(self, for_word, for_typed, for_named, for_block):
    # type: (Optional[List[value_t]], Optional[List[value_t]], Optional[Dict[str, value_t]], Optional[value_t]) -> None
    self.for_word = for_word
    self.for_typed = for_typed
    self.for_named = for_named
    self.for_block = for_block

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ProcDefaults
    return ProcDefaults(cast('Optional[List[value_t]]', None), cast('Optional[List[value_t]]', None), cast('Optional[Dict[str, value_t]]', None), cast('Optional[value_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ProcDefaults')
    L = out_node.fields

    if self.for_word is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.for_word:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('for_word', x0))

    if self.for_typed is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.for_typed:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('for_typed', x1))

    if self.for_named is not None:  # Dict
      unnamed2 = []  # type: List[hnode_t]
      x2 = hnode.Record("", "{", "}", [], unnamed2)
      for k2, v2 in self.for_named.iteritems():
        unnamed2.append(NewLeaf(k2, color_e.StringConst))
        unnamed2.append(v2.PrettyTree(do_abbrev, trav=trav))
      L.append(Field('for_named', x2))

    if self.for_block is not None:  # Optional
      x3 = self.for_block.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('for_block', x3))

    return out_node

class LeftName(y_lvalue_t, sh_lvalue_t):
  _type_tag = 67
  __slots__ = ('name', 'blame_loc')

  def __init__(self, name, blame_loc):
    # type: (str, loc_t) -> None
    self.name = name
    self.blame_loc = blame_loc

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> LeftName
    return LeftName('', cast('loc_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('LeftName')
    L = out_node.fields

    x0 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x0))

    assert self.blame_loc is not None
    x1 = self.blame_loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('blame_loc', x1))

    return out_node

class RegexMatch(regex_match_t, value_t):
  _type_tag = 68
  __slots__ = ('s', 'indices', 'ops')

  def __init__(self, s, indices, ops):
    # type: (str, List[int], eggex_ops_t) -> None
    self.s = s
    self.indices = indices
    self.ops = ops

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> RegexMatch
    return RegexMatch('', [] if alloc_lists else cast('List[int]', None), cast('eggex_ops_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('RegexMatch')
    L = out_node.fields

    x0 = NewLeaf(self.s, color_e.StringConst)
    L.append(Field('s', x0))

    if self.indices is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.indices:
        x1.children.append(hnode.Leaf(str(i1), color_e.OtherConst))
      L.append(Field('indices', x1))

    assert self.ops is not None
    x2 = self.ops.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('ops', x2))

    return out_node

class Obj(value_t):
  _type_tag = 69
  __slots__ = ('prototype', 'd')

  def __init__(self, prototype, d):
    # type: (Optional[Obj], Dict[str, value_t]) -> None
    self.prototype = prototype
    self.d = d

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Obj
    return Obj(cast('Optional[Obj]', None), cast('Dict[str, value_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Obj')
    L = out_node.fields

    if self.prototype is not None:  # Optional
      x0 = self.prototype.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('prototype', x0))

    if self.d is not None:  # Dict
      unnamed1 = []  # type: List[hnode_t]
      x1 = hnode.Record("", "{", "}", [], unnamed1)
      for k1, v1 in self.d.iteritems():
        unnamed1.append(NewLeaf(k1, color_e.StringConst))
        unnamed1.append(v1.PrettyTree(do_abbrev, trav=trav))
      L.append(Field('d', x1))

    return out_node

