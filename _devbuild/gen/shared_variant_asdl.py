from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class expr_e(object):
  Binary = 1
  DoubleQuoted = 65

_expr_str = {
  1: 'Binary',
  65: 'DoubleQuoted',
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
  class Binary(expr_t):
    _type_tag = 1
    __slots__ = ('left', 'right')
  
    def __init__(self, left, right):
      # type: (expr_t, expr_t) -> None
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Binary
      return expr.Binary(cast('expr_t', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Binary')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.right is not None
      x1 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x1))
  
      return out_node
  
  pass

class tok_e(object):
  Eof = 1
  Token = 66

_tok_str = {
  1: 'Eof',
  66: 'Token',
}

def tok_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _tok_str[tag]
  if dot:
    return "tok.%s" % v
  else:
    return v

class tok_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class tok__Eof(tok_t):
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

    out_node = NewRecord('tok.Eof')
    L = out_node.fields

    return out_node

class tok(object):
  Eof = tok__Eof()
  
  pass

class word_part_e(object):
  Literal = 1
  DoubleQuoted = 65

_word_part_str = {
  1: 'Literal',
  65: 'DoubleQuoted',
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
  class Literal(word_part_t):
    _type_tag = 1
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.Literal
      return word_part.Literal('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.Literal')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  pass

class cflow_e(object):
  Break = 1
  Continue = 2
  Return = 3

_cflow_str = {
  1: 'Break',
  2: 'Continue',
  3: 'Return',
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
    __slots__ = ('val',)
  
    def __init__(self, val):
      # type: (int) -> None
      self.val = val
  
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
  
      x0 = hnode.Leaf(str(self.val), color_e.OtherConst)
      L.append(Field('val', x0))
  
      return out_node
  
  pass

class prod(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('a', 'b')

  def __init__(self, a, b):
    # type: (str, str) -> None
    self.a = a
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> prod
    return prod('', '')

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('prod')
    L = out_node.fields

    x0 = NewLeaf(self.a, color_e.StringConst)
    L.append(Field('a', x0))

    x1 = NewLeaf(self.b, color_e.StringConst)
    L.append(Field('b', x1))

    return out_node

class DoubleQuoted(expr_t, word_part_t):
  _type_tag = 65
  __slots__ = ('left', 'tokens')

  def __init__(self, left, tokens):
    # type: (int, List[str]) -> None
    self.left = left
    self.tokens = tokens

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> DoubleQuoted
    return DoubleQuoted(-1, [] if alloc_lists else cast('List[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('DoubleQuoted')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.left), color_e.OtherConst)
    L.append(Field('left', x0))

    if self.tokens is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.tokens:
        x1.children.append(NewLeaf(i1, color_e.StringConst))
      L.append(Field('tokens', x1))

    return out_node

class Token(tok_t):
  _type_tag = 66
  __slots__ = ('id', 'val')

  def __init__(self, id, val):
    # type: (int, str) -> None
    self.id = id
    self.val = val

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Token
    return Token(-1, '')

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Token')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.id), color_e.OtherConst)
    L.append(Field('id', x0))

    x1 = NewLeaf(self.val, color_e.StringConst)
    L.append(Field('val', x1))

    return out_node

class tok_struct(pybase.CompoundObj):
  _type_tag = 67
  __slots__ = ('token', 'x')

  def __init__(self, token, x):
    # type: (tok_t, int) -> None
    self.token = token
    self.x = x

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> tok_struct
    return tok_struct(cast('tok_t', None), -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('tok_struct')
    L = out_node.fields

    assert self.token is not None
    x0 = self.token.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('token', x0))

    x1 = hnode.Leaf(str(self.x), color_e.OtherConst)
    L.append(Field('x', x1))

    return out_node

class tok_array(pybase.CompoundObj):
  _type_tag = 68
  __slots__ = ('tokens',)

  def __init__(self, tokens):
    # type: (List[tok_t]) -> None
    self.tokens = tokens

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> tok_array
    return tok_array([] if alloc_lists else cast('List[tok_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('tok_array')
    L = out_node.fields

    if self.tokens is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.tokens:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('tokens', x0))

    return out_node

