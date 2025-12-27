from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING
class color_t(pybase.SimpleObj):
  pass

class color_e(object):
  TypeName = color_t(1)
  StringConst = color_t(2)
  OtherConst = color_t(3)
  UserType = color_t(4)
  External = color_t(5)

_color_str = {
  1: 'TypeName',
  2: 'StringConst',
  3: 'OtherConst',
  4: 'UserType',
  5: 'External',
}

def color_str(val, dot=True):
  # type: (color_t, bool) -> str
  v = _color_str[val]
  if dot:
    return "color.%s" % v
  else:
    return v

class hnode_e(object):
  AlreadySeen = 1
  Leaf = 2
  Array = 3
  Record = 4

_hnode_str = {
  1: 'AlreadySeen',
  2: 'Leaf',
  3: 'Array',
  4: 'Record',
}

def hnode_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _hnode_str[tag]
  if dot:
    return "hnode.%s" % v
  else:
    return v

class hnode_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class hnode(object):
  class AlreadySeen(hnode_t):
    _type_tag = 1
    __slots__ = ('heap_id',)
  
    def __init__(self, heap_id):
      # type: (int) -> None
      self.heap_id = heap_id
  
  class Leaf(hnode_t):
    _type_tag = 2
    __slots__ = ('s', 'color')
  
    def __init__(self, s, color):
      # type: (str, color_t) -> None
      self.s = s
      self.color = color
  
  class Array(hnode_t):
    _type_tag = 3
    __slots__ = ('children',)
  
    def __init__(self, children):
      # type: (List[hnode_t]) -> None
      self.children = children
  
  class Record(hnode_t):
    _type_tag = 4
    __slots__ = ('node_type', 'left', 'right', 'fields', 'unnamed_fields')
  
    def __init__(self, node_type, left, right, fields, unnamed_fields):
      # type: (str, str, str, List[Field], Optional[List[hnode_t]]) -> None
      self.node_type = node_type
      self.left = left
      self.right = right
      self.fields = fields
      self.unnamed_fields = unnamed_fields
  
  pass

class alloc_members_t(pybase.SimpleObj):
  pass

class alloc_members_e(object):
  List = alloc_members_t(1)
  Dict = alloc_members_t(2)
  Struct = alloc_members_t(3)

_alloc_members_str = {
  1: 'List',
  2: 'Dict',
  3: 'Struct',
}

def alloc_members_str(val, dot=True):
  # type: (alloc_members_t, bool) -> str
  v = _alloc_members_str[val]
  if dot:
    return "alloc_members.%s" % v
  else:
    return v

class Field(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('name', 'val')

  def __init__(self, name, val):
    # type: (str, hnode_t) -> None
    self.name = name
    self.val = val

