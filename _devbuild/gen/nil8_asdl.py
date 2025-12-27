from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class nvalue_e(object):
  Null = 1
  Bool = 2
  Int = 3
  Float = 4
  Str = 5
  Symbol = 6
  List = 7
  Record = 8

_nvalue_str = {
  1: 'Null',
  2: 'Bool',
  3: 'Int',
  4: 'Float',
  5: 'Str',
  6: 'Symbol',
  7: 'List',
  8: 'Record',
}

def nvalue_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _nvalue_str[tag]
  if dot:
    return "nvalue.%s" % v
  else:
    return v

class nvalue_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class nvalue__Null(nvalue_t):
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

    out_node = NewRecord('nvalue.Null')
    L = out_node.fields

    return out_node

class nvalue(object):
  Null = nvalue__Null()
  
  class Bool(nvalue_t):
    _type_tag = 2
    __slots__ = ('b',)
  
    def __init__(self, b):
      # type: (bool) -> None
      self.b = b
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.Bool
      return nvalue.Bool(False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.Bool')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.b else 'F', color_e.OtherConst)
      L.append(Field('b', x0))
  
      return out_node
  
  class Int(nvalue_t):
    _type_tag = 3
    __slots__ = ('i',)
  
    def __init__(self, i):
      # type: (int) -> None
      self.i = i
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.Int
      return nvalue.Int(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.Int')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
      L.append(Field('i', x0))
  
      return out_node
  
  class Float(nvalue_t):
    _type_tag = 4
    __slots__ = ('f',)
  
    def __init__(self, f):
      # type: (float) -> None
      self.f = f
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.Float
      return nvalue.Float(0.0)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.Float')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.f), color_e.OtherConst)
      L.append(Field('f', x0))
  
      return out_node
  
  class Str(nvalue_t):
    _type_tag = 5
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.Str
      return nvalue.Str('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.Str')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  class Symbol(nvalue_t):
    _type_tag = 6
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.Symbol
      return nvalue.Symbol('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.Symbol')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  class List(nvalue_t):
    _type_tag = 7
    __slots__ = ('items',)
  
    def __init__(self, items):
      # type: (List[nvalue_t]) -> None
      self.items = items
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.List
      return nvalue.List([] if alloc_lists else cast('List[nvalue_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.List')
      L = out_node.fields
  
      if self.items is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.items:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('items', x0))
  
      return out_node
  
  class Record(nvalue_t):
    _type_tag = 8
    __slots__ = ('name', 'args', 'named')
  
    def __init__(self, name, args, named):
      # type: (str, List[nvalue_t], Dict[str, nvalue_t]) -> None
      self.name = name
      self.args = args
      self.named = named
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> nvalue.Record
      return nvalue.Record('', [] if alloc_lists else cast('List[nvalue_t]', None), cast('Dict[str, nvalue_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('nvalue.Record')
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
  
      if self.named is not None:  # Dict
        unnamed2 = []  # type: List[hnode_t]
        x2 = hnode.Record("", "{", "}", [], unnamed2)
        for k2, v2 in self.named.iteritems():
          unnamed2.append(NewLeaf(k2, color_e.StringConst))
          unnamed2.append(v2.PrettyTree(do_abbrev, trav=trav))
        L.append(Field('named', x2))
  
      return out_node
  
  pass

