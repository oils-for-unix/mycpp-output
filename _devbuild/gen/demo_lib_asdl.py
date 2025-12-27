from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class value_e(object):
  Str = 1
  Array = 2

_value_str = {
  1: 'Str',
  2: 'Array',
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

class value__Str(value_t):
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

    out_node = NewRecord('value.Str')
    L = out_node.fields

    return out_node

class value(object):
  Str = value__Str()
  
  class Array(value_t):
    _type_tag = 2
    __slots__ = ('a',)
  
    def __init__(self, a):
      # type: (int) -> None
      self.a = a
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> value.Array
      return value.Array(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('value.Array')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.a), color_e.OtherConst)
      L.append(Field('a', x0))
  
      return out_node
  
  pass

class t2(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('a', 'b')

  def __init__(self, a, b):
    # type: (int, int) -> None
    self.a = a
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> t2
    return t2(-1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('t2')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.a), color_e.OtherConst)
    L.append(Field('a', x0))

    x1 = hnode.Leaf(str(self.b), color_e.OtherConst)
    L.append(Field('b', x1))

    return out_node

class t3(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('a', 'b')

  def __init__(self, a, b):
    # type: (int, int) -> None
    self.a = a
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> t3
    return t3(-1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('t3')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.a), color_e.OtherConst)
    L.append(Field('a', x0))

    x1 = hnode.Leaf(str(self.b), color_e.OtherConst)
    L.append(Field('b', x1))

    return out_node

class t4(pybase.CompoundObj):
  _type_tag = 66
  __slots__ = ('a', 'b')

  def __init__(self, a, b):
    # type: (int, int) -> None
    self.a = a
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> t4
    return t4(-1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('t4')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.a), color_e.OtherConst)
    L.append(Field('a', x0))

    x1 = hnode.Leaf(str(self.b), color_e.OtherConst)
    L.append(Field('b', x1))

    return out_node

class LibToken(pybase.CompoundObj):
  _type_tag = 67
  __slots__ = ('s', 'i')

  def __init__(self, s, i):
    # type: (str, int) -> None
    self.s = s
    self.i = i

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> LibToken
    return LibToken('', -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('LibToken')
    L = out_node.fields

    x0 = NewLeaf(self.s, color_e.StringConst)
    L.append(Field('s', x0))

    x1 = hnode.Leaf(str(self.i), color_e.OtherConst)
    L.append(Field('i', x1))

    return out_node

