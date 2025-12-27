from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING
from _devbuild.gen.id_kind_asdl import Id_str

if TYPE_CHECKING:
  from _devbuild.gen.id_kind_asdl import Id_t
  from _devbuild.gen.value_asdl import value_t

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

from frontend.syntax_abbrev import *

class parse_result_e(object):
  EmptyLine = 1
  Eof = 2
  Node = 3

_parse_result_str = {
  1: 'EmptyLine',
  2: 'Eof',
  3: 'Node',
}

def parse_result_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _parse_result_str[tag]
  if dot:
    return "parse_result.%s" % v
  else:
    return v

class parse_result_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class parse_result__EmptyLine(parse_result_t):
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

    out_node = NewRecord('parse_result.EmptyLine')
    L = out_node.fields

    return out_node

class parse_result__Eof(parse_result_t):
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

    out_node = NewRecord('parse_result.Eof')
    L = out_node.fields

    return out_node

class parse_result(object):
  EmptyLine = parse_result__EmptyLine()
  
  Eof = parse_result__Eof()
  
  class Node(parse_result_t):
    _type_tag = 3
    __slots__ = ('cmd',)
  
    def __init__(self, cmd):
      # type: (command_t) -> None
      self.cmd = cmd
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> parse_result.Node
      return parse_result.Node(cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('parse_result.Node')
      L = out_node.fields
  
      assert self.cmd is not None
      x0 = self.cmd.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('cmd', x0))
  
      return out_node
  
  pass

class source_e(object):
  Interactive = 1
  Headless = 2
  Unused = 3
  CFlag = 4
  Stdin = 5
  MainFile = 6
  OtherFile = 7
  Dynamic = 8
  VarRef = 9
  Variable = 10
  Alias = 11
  Reparsed = 12
  Synthetic = 13

_source_str = {
  1: 'Interactive',
  2: 'Headless',
  3: 'Unused',
  4: 'CFlag',
  5: 'Stdin',
  6: 'MainFile',
  7: 'OtherFile',
  8: 'Dynamic',
  9: 'VarRef',
  10: 'Variable',
  11: 'Alias',
  12: 'Reparsed',
  13: 'Synthetic',
}

def source_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _source_str[tag]
  if dot:
    return "source.%s" % v
  else:
    return v

class source_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class source__Interactive(source_t):
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

    out_node = NewRecord('source.Interactive')
    L = out_node.fields

    return out_node

class source__Headless(source_t):
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

    out_node = NewRecord('source.Headless')
    L = out_node.fields

    return out_node

class source__CFlag(source_t):
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

    out_node = NewRecord('source.CFlag')
    L = out_node.fields

    return out_node

class source(object):
  Interactive = source__Interactive()
  
  Headless = source__Headless()
  
  class Unused(source_t):
    _type_tag = 3
    __slots__ = ('comment',)
  
    def __init__(self, comment):
      # type: (str) -> None
      self.comment = comment
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Unused
      return source.Unused('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Unused')
      L = out_node.fields
  
      x0 = NewLeaf(self.comment, color_e.StringConst)
      L.append(Field('comment', x0))
  
      return out_node
  
  CFlag = source__CFlag()
  
  class Stdin(source_t):
    _type_tag = 5
    __slots__ = ('comment',)
  
    def __init__(self, comment):
      # type: (str) -> None
      self.comment = comment
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Stdin
      return source.Stdin('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Stdin')
      L = out_node.fields
  
      x0 = NewLeaf(self.comment, color_e.StringConst)
      L.append(Field('comment', x0))
  
      return out_node
  
  class MainFile(source_t):
    _type_tag = 6
    __slots__ = ('path',)
  
    def __init__(self, path):
      # type: (str) -> None
      self.path = path
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.MainFile
      return source.MainFile('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.MainFile')
      L = out_node.fields
  
      x0 = NewLeaf(self.path, color_e.StringConst)
      L.append(Field('path', x0))
  
      return out_node
  
  class OtherFile(source_t):
    _type_tag = 7
    __slots__ = ('path', 'location')
  
    def __init__(self, path, location):
      # type: (str, loc_t) -> None
      self.path = path
      self.location = location
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.OtherFile
      return source.OtherFile('', cast('loc_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.OtherFile')
      L = out_node.fields
  
      x0 = NewLeaf(self.path, color_e.StringConst)
      L.append(Field('path', x0))
  
      assert self.location is not None
      x1 = self.location.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('location', x1))
  
      return out_node
  
  class Dynamic(source_t):
    _type_tag = 8
    __slots__ = ('what', 'location')
  
    def __init__(self, what, location):
      # type: (str, loc_t) -> None
      self.what = what
      self.location = location
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Dynamic
      return source.Dynamic('', cast('loc_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Dynamic')
      L = out_node.fields
  
      x0 = NewLeaf(self.what, color_e.StringConst)
      L.append(Field('what', x0))
  
      assert self.location is not None
      x1 = self.location.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('location', x1))
  
      return out_node
  
  class VarRef(source_t):
    _type_tag = 9
    __slots__ = ('orig_tok',)
  
    def __init__(self, orig_tok):
      # type: (Token) -> None
      self.orig_tok = orig_tok
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.VarRef
      return source.VarRef(cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.VarRef')
      L = out_node.fields
  
      assert self.orig_tok is not None
      x0 = self.orig_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('orig_tok', x0))
  
      return out_node
  
  class Variable(source_t):
    _type_tag = 10
    __slots__ = ('var_name', 'location')
  
    def __init__(self, var_name, location):
      # type: (str, loc_t) -> None
      self.var_name = var_name
      self.location = location
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Variable
      return source.Variable('', cast('loc_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Variable')
      L = out_node.fields
  
      x0 = NewLeaf(self.var_name, color_e.StringConst)
      L.append(Field('var_name', x0))
  
      assert self.location is not None
      x1 = self.location.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('location', x1))
  
      return out_node
  
  class Alias(source_t):
    _type_tag = 11
    __slots__ = ('argv0', 'argv0_loc')
  
    def __init__(self, argv0, argv0_loc):
      # type: (str, loc_t) -> None
      self.argv0 = argv0
      self.argv0_loc = argv0_loc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Alias
      return source.Alias('', cast('loc_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Alias')
      L = out_node.fields
  
      x0 = NewLeaf(self.argv0, color_e.StringConst)
      L.append(Field('argv0', x0))
  
      assert self.argv0_loc is not None
      x1 = self.argv0_loc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('argv0_loc', x1))
  
      return out_node
  
  class Reparsed(source_t):
    _type_tag = 12
    __slots__ = ('what', 'left_token', 'right_token')
  
    def __init__(self, what, left_token, right_token):
      # type: (str, Token, Token) -> None
      self.what = what
      self.left_token = left_token
      self.right_token = right_token
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Reparsed
      return source.Reparsed('', cast('Token', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Reparsed')
      L = out_node.fields
  
      x0 = NewLeaf(self.what, color_e.StringConst)
      L.append(Field('what', x0))
  
      assert self.left_token is not None
      x1 = self.left_token.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left_token', x1))
  
      assert self.right_token is not None
      x2 = self.right_token.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right_token', x2))
  
      return out_node
  
  class Synthetic(source_t):
    _type_tag = 13
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> source.Synthetic
      return source.Synthetic('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('source.Synthetic')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  pass

class loc_e(object):
  Missing = 1
  Token = 67
  ArgWord = 68
  WordPart = 4
  Word = 5
  Arith = 6
  Command = 7

_loc_str = {
  1: 'Missing',
  4: 'WordPart',
  5: 'Word',
  6: 'Arith',
  7: 'Command',
  67: 'Token',
  68: 'ArgWord',
}

def loc_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _loc_str[tag]
  if dot:
    return "loc.%s" % v
  else:
    return v

class loc_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class loc__Missing(loc_t):
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

    out_node = NewRecord('loc.Missing')
    L = out_node.fields

    return out_node

class loc(object):
  Missing = loc__Missing()
  
  class WordPart(loc_t):
    _type_tag = 4
    __slots__ = ('p',)
  
    def __init__(self, p):
      # type: (word_part_t) -> None
      self.p = p
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> loc.WordPart
      return loc.WordPart(cast('word_part_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('loc.WordPart')
      L = out_node.fields
  
      assert self.p is not None
      x0 = self.p.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('p', x0))
  
      return out_node
  
  class Word(loc_t):
    _type_tag = 5
    __slots__ = ('w',)
  
    def __init__(self, w):
      # type: (word_t) -> None
      self.w = w
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> loc.Word
      return loc.Word(cast('word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('loc.Word')
      L = out_node.fields
  
      assert self.w is not None
      x0 = self.w.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('w', x0))
  
      return out_node
  
  class Arith(loc_t):
    _type_tag = 6
    __slots__ = ('a',)
  
    def __init__(self, a):
      # type: (arith_expr_t) -> None
      self.a = a
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> loc.Arith
      return loc.Arith(cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('loc.Arith')
      L = out_node.fields
  
      assert self.a is not None
      x0 = self.a.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('a', x0))
  
      return out_node
  
  class Command(loc_t):
    _type_tag = 7
    __slots__ = ('c',)
  
    def __init__(self, c):
      # type: (command_t) -> None
      self.c = c
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> loc.Command
      return loc.Command(cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('loc.Command')
      L = out_node.fields
  
      assert self.c is not None
      x0 = self.c.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('c', x0))
  
      return out_node
  
  pass

class debug_frame_e(object):
  MainFile = 1
  Dummy = 2
  Source = 3
  ProcLike = 4
  Token = 67
  CompoundWord = 68
  BeforeErrTrap = 7

_debug_frame_str = {
  1: 'MainFile',
  2: 'Dummy',
  3: 'Source',
  4: 'ProcLike',
  7: 'BeforeErrTrap',
  67: 'Token',
  68: 'CompoundWord',
}

def debug_frame_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _debug_frame_str[tag]
  if dot:
    return "debug_frame.%s" % v
  else:
    return v

class debug_frame_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class debug_frame__Dummy(debug_frame_t):
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

    out_node = NewRecord('debug_frame.Dummy')
    L = out_node.fields

    return out_node

class debug_frame(object):
  class MainFile(debug_frame_t):
    _type_tag = 1
    __slots__ = ('main_filename',)
  
    def __init__(self, main_filename):
      # type: (str) -> None
      self.main_filename = main_filename
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> debug_frame.MainFile
      return debug_frame.MainFile('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('debug_frame.MainFile')
      L = out_node.fields
  
      x0 = NewLeaf(self.main_filename, color_e.StringConst)
      L.append(Field('main_filename', x0))
  
      return out_node
  
  Dummy = debug_frame__Dummy()
  
  class Source(debug_frame_t):
    _type_tag = 3
    __slots__ = ('source_loc', 'source_name')
  
    def __init__(self, source_loc, source_name):
      # type: (CompoundWord, str) -> None
      self.source_loc = source_loc
      self.source_name = source_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> debug_frame.Source
      return debug_frame.Source(cast('CompoundWord', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('debug_frame.Source')
      L = out_node.fields
  
      assert self.source_loc is not None
      x0 = self.source_loc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('source_loc', x0))
  
      x1 = NewLeaf(self.source_name, color_e.StringConst)
      L.append(Field('source_name', x1))
  
      return out_node
  
  class ProcLike(debug_frame_t):
    _type_tag = 4
    __slots__ = ('invoke_loc', 'def_tok', 'proc_name')
  
    def __init__(self, invoke_loc, def_tok, proc_name):
      # type: (CompoundWord, Token, str) -> None
      self.invoke_loc = invoke_loc
      self.def_tok = def_tok
      self.proc_name = proc_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> debug_frame.ProcLike
      return debug_frame.ProcLike(cast('CompoundWord', None), cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('debug_frame.ProcLike')
      L = out_node.fields
  
      assert self.invoke_loc is not None
      x0 = self.invoke_loc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('invoke_loc', x0))
  
      assert self.def_tok is not None
      x1 = self.def_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('def_tok', x1))
  
      x2 = NewLeaf(self.proc_name, color_e.StringConst)
      L.append(Field('proc_name', x2))
  
      return out_node
  
  class BeforeErrTrap(debug_frame_t):
    _type_tag = 7
    __slots__ = ('tok',)
  
    def __init__(self, tok):
      # type: (Token) -> None
      self.tok = tok
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> debug_frame.BeforeErrTrap
      return debug_frame.BeforeErrTrap(cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('debug_frame.BeforeErrTrap')
      L = out_node.fields
  
      assert self.tok is not None
      x0 = self.tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('tok', x0))
  
      return out_node
  
  pass

class bracket_op_e(object):
  WholeArray = 1
  ArrayIndex = 2

_bracket_op_str = {
  1: 'WholeArray',
  2: 'ArrayIndex',
}

def bracket_op_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _bracket_op_str[tag]
  if dot:
    return "bracket_op.%s" % v
  else:
    return v

class bracket_op_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class bracket_op(object):
  class WholeArray(bracket_op_t):
    _type_tag = 1
    __slots__ = ('op_id',)
  
    def __init__(self, op_id):
      # type: (Id_t) -> None
      self.op_id = op_id
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bracket_op.WholeArray
      return bracket_op.WholeArray(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bracket_op.WholeArray')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      return out_node
  
  class ArrayIndex(bracket_op_t):
    _type_tag = 2
    __slots__ = ('expr',)
  
    def __init__(self, expr):
      # type: (arith_expr_t) -> None
      self.expr = expr
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bracket_op.ArrayIndex
      return bracket_op.ArrayIndex(cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bracket_op.ArrayIndex')
      L = out_node.fields
  
      assert self.expr is not None
      x0 = self.expr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('expr', x0))
  
      return out_node
  
  pass

class suffix_op_e(object):
  Nullary = 67
  Unary = 2
  Static = 3
  PatSub = 4
  Slice = 5

_suffix_op_str = {
  2: 'Unary',
  3: 'Static',
  4: 'PatSub',
  5: 'Slice',
  67: 'Nullary',
}

def suffix_op_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _suffix_op_str[tag]
  if dot:
    return "suffix_op.%s" % v
  else:
    return v

class suffix_op_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class suffix_op(object):
  class Unary(suffix_op_t):
    _type_tag = 2
    __slots__ = ('op', 'arg_word')
  
    def __init__(self, op, arg_word):
      # type: (Token, rhs_word_t) -> None
      self.op = op
      self.arg_word = arg_word
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> suffix_op.Unary
      return suffix_op.Unary(cast('Token', None), cast('rhs_word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('suffix_op.Unary')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.arg_word is not None
      x1 = self.arg_word.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('arg_word', x1))
  
      return out_node
  
  class Static(suffix_op_t):
    _type_tag = 3
    __slots__ = ('tok', 'arg')
  
    def __init__(self, tok, arg):
      # type: (Token, str) -> None
      self.tok = tok
      self.arg = arg
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> suffix_op.Static
      return suffix_op.Static(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('suffix_op.Static')
      L = out_node.fields
  
      assert self.tok is not None
      x0 = self.tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('tok', x0))
  
      x1 = NewLeaf(self.arg, color_e.StringConst)
      L.append(Field('arg', x1))
  
      return out_node
  
  class PatSub(suffix_op_t):
    _type_tag = 4
    __slots__ = ('pat', 'replace', 'replace_mode', 'slash_tok')
  
    def __init__(self, pat, replace, replace_mode, slash_tok):
      # type: (CompoundWord, rhs_word_t, Id_t, Token) -> None
      self.pat = pat
      self.replace = replace
      self.replace_mode = replace_mode
      self.slash_tok = slash_tok
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> suffix_op.PatSub
      return suffix_op.PatSub(cast('CompoundWord', None), cast('rhs_word_t', None), -1, cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('suffix_op.PatSub')
      L = out_node.fields
  
      assert self.pat is not None
      x0 = self.pat.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('pat', x0))
  
      assert self.replace is not None
      x1 = self.replace.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('replace', x1))
  
      x2 = hnode.Leaf(Id_str(self.replace_mode, dot=False), color_e.UserType)
      L.append(Field('replace_mode', x2))
  
      assert self.slash_tok is not None
      x3 = self.slash_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('slash_tok', x3))
  
      return out_node
  
  class Slice(suffix_op_t):
    _type_tag = 5
    __slots__ = ('begin', 'length')
  
    def __init__(self, begin, length):
      # type: (arith_expr_t, Optional[arith_expr_t]) -> None
      self.begin = begin
      self.length = length
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> suffix_op.Slice
      return suffix_op.Slice(cast('arith_expr_t', None), cast('Optional[arith_expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('suffix_op.Slice')
      L = out_node.fields
  
      assert self.begin is not None
      x0 = self.begin.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('begin', x0))
  
      if self.length is not None:  # Optional
        x1 = self.length.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('length', x1))
  
      return out_node
  
  pass

class InitializerWord_e(object):
  ArrayWord = 1
  AssocPair = 77

_InitializerWord_str = {
  1: 'ArrayWord',
  77: 'AssocPair',
}

def InitializerWord_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _InitializerWord_str[tag]
  if dot:
    return "InitializerWord.%s" % v
  else:
    return v

class InitializerWord_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class InitializerWord(object):
  class ArrayWord(InitializerWord_t):
    _type_tag = 1
    __slots__ = ('w',)
  
    def __init__(self, w):
      # type: (word_t) -> None
      self.w = w
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> InitializerWord.ArrayWord
      return InitializerWord.ArrayWord(cast('word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('InitializerWord.ArrayWord')
      L = out_node.fields
  
      assert self.w is not None
      x0 = self.w.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('w', x0))
  
      return out_node
  
  pass

class word_part_e(object):
  YshArrayLiteral = 75
  InitializerLiteral = 2
  Literal = 67
  EscapedLiteral = 4
  SingleQuoted = 71
  DoubleQuoted = 70
  SimpleVarSub = 72
  BracedVarSub = 69
  ZshVarSub = 9
  CommandSub = 73
  TildeSub = 11
  ArithSub = 12
  BracedTuple = 13
  BracedRange = 14
  BracedRangeDigit = 15
  ExtGlob = 16
  BashRegexGroup = 17
  Splice = 18
  ExprSub = 74

_word_part_str = {
  2: 'InitializerLiteral',
  4: 'EscapedLiteral',
  9: 'ZshVarSub',
  11: 'TildeSub',
  12: 'ArithSub',
  13: 'BracedTuple',
  14: 'BracedRange',
  15: 'BracedRangeDigit',
  16: 'ExtGlob',
  17: 'BashRegexGroup',
  18: 'Splice',
  67: 'Literal',
  69: 'BracedVarSub',
  70: 'DoubleQuoted',
  71: 'SingleQuoted',
  72: 'SimpleVarSub',
  73: 'CommandSub',
  74: 'ExprSub',
  75: 'YshArrayLiteral',
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
  class InitializerLiteral(word_part_t):
    _type_tag = 2
    __slots__ = ('left', 'pairs', 'right')
  
    def __init__(self, left, pairs, right):
      # type: (Token, List[InitializerWord_t], Token) -> None
      self.left = left
      self.pairs = pairs
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.InitializerLiteral
      return word_part.InitializerLiteral(cast('Token', None), [] if alloc_lists else cast('List[InitializerWord_t]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.InitializerLiteral')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.pairs is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.pairs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('pairs', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class EscapedLiteral(word_part_t):
    _type_tag = 4
    __slots__ = ('token', 'ch')
  
    def __init__(self, token, ch):
      # type: (Token, str) -> None
      self.token = token
      self.ch = ch
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.EscapedLiteral
      return word_part.EscapedLiteral(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.EscapedLiteral')
      L = out_node.fields
  
      assert self.token is not None
      x0 = self.token.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('token', x0))
  
      x1 = NewLeaf(self.ch, color_e.StringConst)
      L.append(Field('ch', x1))
  
      return out_node
  
  class ZshVarSub(word_part_t):
    _type_tag = 9
    __slots__ = ('left', 'ignored', 'right')
  
    def __init__(self, left, ignored, right):
      # type: (Token, CompoundWord, Token) -> None
      self.left = left
      self.ignored = ignored
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.ZshVarSub
      return word_part.ZshVarSub(cast('Token', None), cast('CompoundWord', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.ZshVarSub')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.ignored is not None
      x1 = self.ignored.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('ignored', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class TildeSub(word_part_t):
    _type_tag = 11
    __slots__ = ('left', 'name', 'user_name')
  
    def __init__(self, left, name, user_name):
      # type: (Token, Optional[Token], Optional[str]) -> None
      self.left = left
      self.name = name
      self.user_name = user_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.TildeSub
      return word_part.TildeSub(cast('Token', None), cast('Optional[Token]', None), cast('Optional[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.TildeSub')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.name is not None:  # Optional
        x1 = self.name.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('name', x1))
  
      if self.user_name is not None:  # Optional
        x2 = NewLeaf(self.user_name, color_e.StringConst)
        L.append(Field('user_name', x2))
  
      return out_node
  
  class ArithSub(word_part_t):
    _type_tag = 12
    __slots__ = ('left', 'anode', 'right')
  
    def __init__(self, left, anode, right):
      # type: (Token, arith_expr_t, Token) -> None
      self.left = left
      self.anode = anode
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.ArithSub
      return word_part.ArithSub(cast('Token', None), cast('arith_expr_t', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.ArithSub')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.anode is not None
      x1 = self.anode.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('anode', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class BracedTuple(word_part_t):
    _type_tag = 13
    __slots__ = ('words',)
  
    def __init__(self, words):
      # type: (List[CompoundWord]) -> None
      self.words = words
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.BracedTuple
      return word_part.BracedTuple([] if alloc_lists else cast('List[CompoundWord]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.BracedTuple')
      L = out_node.fields
  
      if self.words is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.words:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('words', x0))
  
      return out_node
  
  class BracedRange(word_part_t):
    _type_tag = 14
    __slots__ = ('blame_tok', 'kind', 'start', 'end', 'step')
  
    def __init__(self, blame_tok, kind, start, end, step):
      # type: (Token, Id_t, str, str, int) -> None
      self.blame_tok = blame_tok
      self.kind = kind
      self.start = start
      self.end = end
      self.step = step
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.BracedRange
      return word_part.BracedRange(cast('Token', None), -1, '', '', -1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.BracedRange')
      L = out_node.fields
  
      assert self.blame_tok is not None
      x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_tok', x0))
  
      x1 = hnode.Leaf(Id_str(self.kind, dot=False), color_e.UserType)
      L.append(Field('kind', x1))
  
      x2 = NewLeaf(self.start, color_e.StringConst)
      L.append(Field('start', x2))
  
      x3 = NewLeaf(self.end, color_e.StringConst)
      L.append(Field('end', x3))
  
      x4 = hnode.Leaf(str(self.step), color_e.OtherConst)
      L.append(Field('step', x4))
  
      return out_node
  
  class BracedRangeDigit(word_part_t):
    _type_tag = 15
    __slots__ = ('s', 'orig_tok')
  
    def __init__(self, s, orig_tok):
      # type: (str, Token) -> None
      self.s = s
      self.orig_tok = orig_tok
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.BracedRangeDigit
      return word_part.BracedRangeDigit('', cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.BracedRangeDigit')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      assert self.orig_tok is not None
      x1 = self.orig_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('orig_tok', x1))
  
      return out_node
  
  class ExtGlob(word_part_t):
    _type_tag = 16
    __slots__ = ('op', 'arms', 'right')
  
    def __init__(self, op, arms, right):
      # type: (Token, List[CompoundWord], Token) -> None
      self.op = op
      self.arms = arms
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.ExtGlob
      return word_part.ExtGlob(cast('Token', None), [] if alloc_lists else cast('List[CompoundWord]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.ExtGlob')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      if self.arms is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.arms:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('arms', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class BashRegexGroup(word_part_t):
    _type_tag = 17
    __slots__ = ('left', 'child', 'right')
  
    def __init__(self, left, child, right):
      # type: (Token, Optional[CompoundWord], Token) -> None
      self.left = left
      self.child = child
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.BashRegexGroup
      return word_part.BashRegexGroup(cast('Token', None), cast('Optional[CompoundWord]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.BashRegexGroup')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.child is not None:  # Optional
        x1 = self.child.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('child', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class Splice(word_part_t):
    _type_tag = 18
    __slots__ = ('blame_tok', 'var_name')
  
    def __init__(self, blame_tok, var_name):
      # type: (Token, str) -> None
      self.blame_tok = blame_tok
      self.var_name = var_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word_part.Splice
      return word_part.Splice(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word_part.Splice')
      L = out_node.fields
  
      assert self.blame_tok is not None
      x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_tok', x0))
  
      x1 = NewLeaf(self.var_name, color_e.StringConst)
      L.append(Field('var_name', x1))
  
      return out_node
  
  pass

class rhs_word_e(object):
  Empty = 1
  Compound = 68

_rhs_word_str = {
  1: 'Empty',
  68: 'Compound',
}

def rhs_word_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _rhs_word_str[tag]
  if dot:
    return "rhs_word.%s" % v
  else:
    return v

class rhs_word_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class rhs_word__Empty(rhs_word_t):
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

    out_node = NewRecord('rhs_word.Empty')
    L = out_node.fields

    return out_node

class rhs_word(object):
  Empty = rhs_word__Empty()
  
  pass

class word_e(object):
  Operator = 67
  Compound = 68
  BracedTree = 3
  String = 4
  Redir = 5

_word_str = {
  3: 'BracedTree',
  4: 'String',
  5: 'Redir',
  67: 'Operator',
  68: 'Compound',
}

def word_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _word_str[tag]
  if dot:
    return "word.%s" % v
  else:
    return v

class word_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class word(object):
  class BracedTree(word_t):
    _type_tag = 3
    __slots__ = ('parts',)
  
    def __init__(self, parts):
      # type: (List[word_part_t]) -> None
      self.parts = parts
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word.BracedTree
      return word.BracedTree([] if alloc_lists else cast('List[word_part_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word.BracedTree')
      L = out_node.fields
  
      if self.parts is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.parts:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('parts', x0))
  
      return out_node
  
  class String(word_t):
    _type_tag = 4
    __slots__ = ('id', 's', 'blame_loc')
  
    def __init__(self, id, s, blame_loc):
      # type: (Id_t, str, Optional[CompoundWord]) -> None
      self.id = id
      self.s = s
      self.blame_loc = blame_loc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word.String
      return word.String(-1, '', cast('Optional[CompoundWord]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word.String')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.id, dot=False), color_e.UserType)
      L.append(Field('id', x0))
  
      x1 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x1))
  
      if self.blame_loc is not None:  # Optional
        x2 = self.blame_loc.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('blame_loc', x2))
  
      return out_node
  
  class Redir(word_t):
    _type_tag = 5
    __slots__ = ('left_tok', 'op')
  
    def __init__(self, left_tok, op):
      # type: (Optional[Token], Token) -> None
      self.left_tok = left_tok
      self.op = op
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> word.Redir
      return word.Redir(cast('Optional[Token]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('word.Redir')
      L = out_node.fields
  
      if self.left_tok is not None:  # Optional
        x0 = self.left_tok.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('left_tok', x0))
  
      assert self.op is not None
      x1 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x1))
  
      return out_node
  
  pass

class sh_lhs_e(object):
  Name = 1
  IndexedName = 2
  UnparsedIndex = 3

_sh_lhs_str = {
  1: 'Name',
  2: 'IndexedName',
  3: 'UnparsedIndex',
}

def sh_lhs_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _sh_lhs_str[tag]
  if dot:
    return "sh_lhs.%s" % v
  else:
    return v

class sh_lhs_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class sh_lhs(object):
  class Name(sh_lhs_t):
    _type_tag = 1
    __slots__ = ('left', 'name')
  
    def __init__(self, left, name):
      # type: (Token, str) -> None
      self.left = left
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> sh_lhs.Name
      return sh_lhs.Name(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('sh_lhs.Name')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      x1 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x1))
  
      return out_node
  
  class IndexedName(sh_lhs_t):
    _type_tag = 2
    __slots__ = ('left', 'name', 'index')
  
    def __init__(self, left, name, index):
      # type: (Token, str, arith_expr_t) -> None
      self.left = left
      self.name = name
      self.index = index
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> sh_lhs.IndexedName
      return sh_lhs.IndexedName(cast('Token', None), '', cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('sh_lhs.IndexedName')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      x1 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x1))
  
      assert self.index is not None
      x2 = self.index.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('index', x2))
  
      return out_node
  
  class UnparsedIndex(sh_lhs_t):
    _type_tag = 3
    __slots__ = ('left', 'name', 'index')
  
    def __init__(self, left, name, index):
      # type: (Token, str, str) -> None
      self.left = left
      self.name = name
      self.index = index
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> sh_lhs.UnparsedIndex
      return sh_lhs.UnparsedIndex(cast('Token', None), '', '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('sh_lhs.UnparsedIndex')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      x1 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x1))
  
      x2 = NewLeaf(self.index, color_e.StringConst)
      L.append(Field('index', x2))
  
      return out_node
  
  pass

class arith_expr_e(object):
  EmptyZero = 1
  EmptyOne = 2
  VarSub = 67
  Word = 68
  UnaryAssign = 5
  BinaryAssign = 6
  Unary = 7
  Binary = 8
  TernaryOp = 9

_arith_expr_str = {
  1: 'EmptyZero',
  2: 'EmptyOne',
  5: 'UnaryAssign',
  6: 'BinaryAssign',
  7: 'Unary',
  8: 'Binary',
  9: 'TernaryOp',
  67: 'VarSub',
  68: 'Word',
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

class arith_expr__EmptyZero(arith_expr_t):
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

    out_node = NewRecord('arith_expr.EmptyZero')
    L = out_node.fields

    return out_node

class arith_expr__EmptyOne(arith_expr_t):
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

    out_node = NewRecord('arith_expr.EmptyOne')
    L = out_node.fields

    return out_node

class arith_expr(object):
  EmptyZero = arith_expr__EmptyZero()
  
  EmptyOne = arith_expr__EmptyOne()
  
  class UnaryAssign(arith_expr_t):
    _type_tag = 5
    __slots__ = ('op_id', 'child')
  
    def __init__(self, op_id, child):
      # type: (Id_t, arith_expr_t) -> None
      self.op_id = op_id
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.UnaryAssign
      return arith_expr.UnaryAssign(-1, cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.UnaryAssign')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      return out_node
  
  class BinaryAssign(arith_expr_t):
    _type_tag = 6
    __slots__ = ('op_id', 'left', 'right')
  
    def __init__(self, op_id, left, right):
      # type: (Id_t, arith_expr_t, arith_expr_t) -> None
      self.op_id = op_id
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.BinaryAssign
      return arith_expr.BinaryAssign(-1, cast('arith_expr_t', None), cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.BinaryAssign')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      assert self.left is not None
      x1 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class Unary(arith_expr_t):
    _type_tag = 7
    __slots__ = ('op_id', 'child')
  
    def __init__(self, op_id, child):
      # type: (Id_t, arith_expr_t) -> None
      self.op_id = op_id
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Unary
      return arith_expr.Unary(-1, cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Unary')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      return out_node
  
  class Binary(arith_expr_t):
    _type_tag = 8
    __slots__ = ('op', 'left', 'right')
  
    def __init__(self, op, left, right):
      # type: (Token, arith_expr_t, arith_expr_t) -> None
      self.op = op
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.Binary
      return arith_expr.Binary(cast('Token', None), cast('arith_expr_t', None), cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.Binary')
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
  
  class TernaryOp(arith_expr_t):
    _type_tag = 9
    __slots__ = ('cond', 'true_expr', 'false_expr')
  
    def __init__(self, cond, true_expr, false_expr):
      # type: (arith_expr_t, arith_expr_t, arith_expr_t) -> None
      self.cond = cond
      self.true_expr = true_expr
      self.false_expr = false_expr
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> arith_expr.TernaryOp
      return arith_expr.TernaryOp(cast('arith_expr_t', None), cast('arith_expr_t', None), cast('arith_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('arith_expr.TernaryOp')
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
  
  pass

class bool_expr_e(object):
  WordTest = 1
  Binary = 2
  Unary = 3
  LogicalNot = 4
  LogicalAnd = 5
  LogicalOr = 6

_bool_expr_str = {
  1: 'WordTest',
  2: 'Binary',
  3: 'Unary',
  4: 'LogicalNot',
  5: 'LogicalAnd',
  6: 'LogicalOr',
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
    __slots__ = ('w',)
  
    def __init__(self, w):
      # type: (word_t) -> None
      self.w = w
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.WordTest
      return bool_expr.WordTest(cast('word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.WordTest')
      L = out_node.fields
  
      assert self.w is not None
      x0 = self.w.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('w', x0))
  
      return out_node
  
  class Binary(bool_expr_t):
    _type_tag = 2
    __slots__ = ('op_id', 'left', 'right')
  
    def __init__(self, op_id, left, right):
      # type: (Id_t, word_t, word_t) -> None
      self.op_id = op_id
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.Binary
      return bool_expr.Binary(-1, cast('word_t', None), cast('word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.Binary')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      assert self.left is not None
      x1 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class Unary(bool_expr_t):
    _type_tag = 3
    __slots__ = ('op_id', 'child')
  
    def __init__(self, op_id, child):
      # type: (Id_t, word_t) -> None
      self.op_id = op_id
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.Unary
      return bool_expr.Unary(-1, cast('word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.Unary')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      return out_node
  
  class LogicalNot(bool_expr_t):
    _type_tag = 4
    __slots__ = ('child',)
  
    def __init__(self, child):
      # type: (bool_expr_t) -> None
      self.child = child
  
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
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      return out_node
  
  class LogicalAnd(bool_expr_t):
    _type_tag = 5
    __slots__ = ('left', 'right')
  
    def __init__(self, left, right):
      # type: (bool_expr_t, bool_expr_t) -> None
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.LogicalAnd
      return bool_expr.LogicalAnd(cast('bool_expr_t', None), cast('bool_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.LogicalAnd')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.right is not None
      x1 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x1))
  
      return out_node
  
  class LogicalOr(bool_expr_t):
    _type_tag = 6
    __slots__ = ('left', 'right')
  
    def __init__(self, left, right):
      # type: (bool_expr_t, bool_expr_t) -> None
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> bool_expr.LogicalOr
      return bool_expr.LogicalOr(cast('bool_expr_t', None), cast('bool_expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('bool_expr.LogicalOr')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.right is not None
      x1 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x1))
  
      return out_node
  
  pass

class redir_loc_e(object):
  Fd = 1
  VarName = 2

_redir_loc_str = {
  1: 'Fd',
  2: 'VarName',
}

def redir_loc_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _redir_loc_str[tag]
  if dot:
    return "redir_loc.%s" % v
  else:
    return v

class redir_loc_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class redir_loc(object):
  class Fd(redir_loc_t):
    _type_tag = 1
    __slots__ = ('fd',)
  
    def __init__(self, fd):
      # type: (int) -> None
      self.fd = fd
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redir_loc.Fd
      return redir_loc.Fd(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redir_loc.Fd')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.fd), color_e.OtherConst)
      L.append(Field('fd', x0))
  
      return out_node
  
  class VarName(redir_loc_t):
    _type_tag = 2
    __slots__ = ('name',)
  
    def __init__(self, name):
      # type: (str) -> None
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redir_loc.VarName
      return redir_loc.VarName('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redir_loc.VarName')
      L = out_node.fields
  
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))
  
      return out_node
  
  pass

class redir_param_e(object):
  Word = 68
  HereWord = 2
  HereDoc = 3

_redir_param_str = {
  2: 'HereWord',
  3: 'HereDoc',
  68: 'Word',
}

def redir_param_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _redir_param_str[tag]
  if dot:
    return "redir_param.%s" % v
  else:
    return v

class redir_param_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class redir_param(object):
  class HereWord(redir_param_t):
    _type_tag = 2
    __slots__ = ('w', 'is_multiline')
  
    def __init__(self, w, is_multiline):
      # type: (CompoundWord, bool) -> None
      self.w = w
      self.is_multiline = is_multiline
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redir_param.HereWord
      return redir_param.HereWord(cast('CompoundWord', None), False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redir_param.HereWord')
      L = out_node.fields
  
      assert self.w is not None
      x0 = self.w.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('w', x0))
  
      x1 = hnode.Leaf('T' if self.is_multiline else 'F', color_e.OtherConst)
      L.append(Field('is_multiline', x1))
  
      return out_node
  
  class HereDoc(redir_param_t):
    _type_tag = 3
    __slots__ = ('here_begin', 'here_end_tok', 'stdin_parts')
  
    def __init__(self, here_begin, here_end_tok, stdin_parts):
      # type: (word_t, Optional[Token], List[word_part_t]) -> None
      self.here_begin = here_begin
      self.here_end_tok = here_end_tok
      self.stdin_parts = stdin_parts
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redir_param.HereDoc
      return redir_param.HereDoc(cast('word_t', None), cast('Optional[Token]', None), [] if alloc_lists else cast('List[word_part_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redir_param.HereDoc')
      L = out_node.fields
  
      assert self.here_begin is not None
      x0 = self.here_begin.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('here_begin', x0))
  
      if self.here_end_tok is not None:  # Optional
        x1 = self.here_end_tok.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('here_end_tok', x1))
  
      if self.stdin_parts is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.stdin_parts:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('stdin_parts', x2))
  
      return out_node
  
  pass

class assign_op_t(pybase.SimpleObj):
  pass

class assign_op_e(object):
  Equal = assign_op_t(1)
  PlusEqual = assign_op_t(2)

_assign_op_str = {
  1: 'Equal',
  2: 'PlusEqual',
}

def assign_op_str(val, dot=True):
  # type: (assign_op_t, bool) -> str
  v = _assign_op_str[val]
  if dot:
    return "assign_op.%s" % v
  else:
    return v

class condition_e(object):
  Shell = 81
  YshExpr = 2

_condition_str = {
  2: 'YshExpr',
  81: 'Shell',
}

def condition_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _condition_str[tag]
  if dot:
    return "condition.%s" % v
  else:
    return v

class condition_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class condition(object):
  class YshExpr(condition_t):
    _type_tag = 2
    __slots__ = ('e',)
  
    def __init__(self, e):
      # type: (expr_t) -> None
      self.e = e
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> condition.YshExpr
      return condition.YshExpr(cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('condition.YshExpr')
      L = out_node.fields
  
      assert self.e is not None
      x0 = self.e.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('e', x0))
  
      return out_node
  
  pass

class case_arg_e(object):
  Word = 1
  YshExpr = 2

_case_arg_str = {
  1: 'Word',
  2: 'YshExpr',
}

def case_arg_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _case_arg_str[tag]
  if dot:
    return "case_arg.%s" % v
  else:
    return v

class case_arg_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class case_arg(object):
  class Word(case_arg_t):
    _type_tag = 1
    __slots__ = ('w',)
  
    def __init__(self, w):
      # type: (word_t) -> None
      self.w = w
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> case_arg.Word
      return case_arg.Word(cast('word_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('case_arg.Word')
      L = out_node.fields
  
      assert self.w is not None
      x0 = self.w.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('w', x0))
  
      return out_node
  
  class YshExpr(case_arg_t):
    _type_tag = 2
    __slots__ = ('e',)
  
    def __init__(self, e):
      # type: (expr_t) -> None
      self.e = e
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> case_arg.YshExpr
      return case_arg.YshExpr(cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('case_arg.YshExpr')
      L = out_node.fields
  
      assert self.e is not None
      x0 = self.e.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('e', x0))
  
      return out_node
  
  pass

class pat_e(object):
  Else = 1
  Words = 2
  YshExprs = 3
  Eggex = 84

_pat_str = {
  1: 'Else',
  2: 'Words',
  3: 'YshExprs',
  84: 'Eggex',
}

def pat_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _pat_str[tag]
  if dot:
    return "pat.%s" % v
  else:
    return v

class pat_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class pat__Else(pat_t):
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

    out_node = NewRecord('pat.Else')
    L = out_node.fields

    return out_node

class pat(object):
  Else = pat__Else()
  
  class Words(pat_t):
    _type_tag = 2
    __slots__ = ('words',)
  
    def __init__(self, words):
      # type: (List[word_t]) -> None
      self.words = words
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> pat.Words
      return pat.Words([] if alloc_lists else cast('List[word_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('pat.Words')
      L = out_node.fields
  
      if self.words is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.words:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('words', x0))
  
      return out_node
  
  class YshExprs(pat_t):
    _type_tag = 3
    __slots__ = ('exprs',)
  
    def __init__(self, exprs):
      # type: (List[expr_t]) -> None
      self.exprs = exprs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> pat.YshExprs
      return pat.YshExprs([] if alloc_lists else cast('List[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('pat.YshExprs')
      L = out_node.fields
  
      if self.exprs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.exprs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('exprs', x0))
  
      return out_node
  
  pass

class for_iter_e(object):
  Args = 1
  Words = 2
  YshExpr = 3

_for_iter_str = {
  1: 'Args',
  2: 'Words',
  3: 'YshExpr',
}

def for_iter_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _for_iter_str[tag]
  if dot:
    return "for_iter.%s" % v
  else:
    return v

class for_iter_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class for_iter__Args(for_iter_t):
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

    out_node = NewRecord('for_iter.Args')
    L = out_node.fields

    return out_node

class for_iter(object):
  Args = for_iter__Args()
  
  class Words(for_iter_t):
    _type_tag = 2
    __slots__ = ('words',)
  
    def __init__(self, words):
      # type: (List[word_t]) -> None
      self.words = words
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> for_iter.Words
      return for_iter.Words([] if alloc_lists else cast('List[word_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('for_iter.Words')
      L = out_node.fields
  
      if self.words is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.words:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('words', x0))
  
      return out_node
  
  class YshExpr(for_iter_t):
    _type_tag = 3
    __slots__ = ('e', 'blame')
  
    def __init__(self, e, blame):
      # type: (expr_t, Token) -> None
      self.e = e
      self.blame = blame
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> for_iter.YshExpr
      return for_iter.YshExpr(cast('expr_t', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('for_iter.YshExpr')
      L = out_node.fields
  
      assert self.e is not None
      x0 = self.e.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('e', x0))
  
      assert self.blame is not None
      x1 = self.blame.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame', x1))
  
      return out_node
  
  pass

class proc_sig_e(object):
  Open = 1
  Closed = 2

_proc_sig_str = {
  1: 'Open',
  2: 'Closed',
}

def proc_sig_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _proc_sig_str[tag]
  if dot:
    return "proc_sig.%s" % v
  else:
    return v

class proc_sig_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class proc_sig__Open(proc_sig_t):
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

    out_node = NewRecord('proc_sig.Open')
    L = out_node.fields

    return out_node

class proc_sig(object):
  Open = proc_sig__Open()
  
  class Closed(proc_sig_t):
    _type_tag = 2
    __slots__ = ('word', 'positional', 'named', 'block_param')
  
    def __init__(self, word, positional, named, block_param):
      # type: (Optional[ParamGroup], Optional[ParamGroup], Optional[ParamGroup], Optional[Param]) -> None
      self.word = word
      self.positional = positional
      self.named = named
      self.block_param = block_param
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> proc_sig.Closed
      return proc_sig.Closed(cast('Optional[ParamGroup]', None), cast('Optional[ParamGroup]', None), cast('Optional[ParamGroup]', None), cast('Optional[Param]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('proc_sig.Closed')
      L = out_node.fields
  
      if self.word is not None:  # Optional
        x0 = self.word.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('word', x0))
  
      if self.positional is not None:  # Optional
        x1 = self.positional.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('positional', x1))
  
      if self.named is not None:  # Optional
        x2 = self.named.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('named', x2))
  
      if self.block_param is not None:  # Optional
        x3 = self.block_param.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('block_param', x3))
  
      return out_node
  
  pass

class cmd_frag_e(object):
  LiteralBlock = 97
  Expr = 2

_cmd_frag_str = {
  2: 'Expr',
  97: 'LiteralBlock',
}

def cmd_frag_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _cmd_frag_str[tag]
  if dot:
    return "cmd_frag.%s" % v
  else:
    return v

class cmd_frag_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class cmd_frag(object):
  class Expr(cmd_frag_t):
    _type_tag = 2
    __slots__ = ('c',)
  
    def __init__(self, c):
      # type: (command_t) -> None
      self.c = c
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> cmd_frag.Expr
      return cmd_frag.Expr(cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('cmd_frag.Expr')
      L = out_node.fields
  
      assert self.c is not None
      x0 = self.c.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('c', x0))
  
      return out_node
  
  pass

class command_e(object):
  NoOp = 1
  Redirect = 2
  Simple = 3
  ExpandedAlias = 4
  Sentence = 5
  ShAssignment = 6
  ControlFlow = 7
  Pipeline = 8
  AndOr = 9
  DoGroup = 10
  BraceGroup = 86
  Subshell = 12
  DParen = 13
  DBracket = 14
  ForEach = 15
  ForExpr = 16
  WhileUntil = 17
  If = 18
  Case = 19
  ShFunction = 96
  TimeBlock = 21
  CommandList = 22
  VarDecl = 93
  BareDecl = 24
  Mutation = 94
  Expr = 95
  Proc = 90
  Func = 91
  Retval = 29

_command_str = {
  1: 'NoOp',
  2: 'Redirect',
  3: 'Simple',
  4: 'ExpandedAlias',
  5: 'Sentence',
  6: 'ShAssignment',
  7: 'ControlFlow',
  8: 'Pipeline',
  9: 'AndOr',
  10: 'DoGroup',
  12: 'Subshell',
  13: 'DParen',
  14: 'DBracket',
  15: 'ForEach',
  16: 'ForExpr',
  17: 'WhileUntil',
  18: 'If',
  19: 'Case',
  21: 'TimeBlock',
  22: 'CommandList',
  24: 'BareDecl',
  29: 'Retval',
  86: 'BraceGroup',
  90: 'Proc',
  91: 'Func',
  93: 'VarDecl',
  94: 'Mutation',
  95: 'Expr',
  96: 'ShFunction',
}

def command_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _command_str[tag]
  if dot:
    return "command.%s" % v
  else:
    return v

class command_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class command__NoOp(command_t):
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

    out_node = NewRecord('command.NoOp')
    L = out_node.fields

    return out_node

class command(object):
  NoOp = command__NoOp()
  
  class Redirect(command_t):
    _type_tag = 2
    __slots__ = ('child', 'redirects')
  
    def __init__(self, child, redirects):
      # type: (command_t, List[Redir]) -> None
      self.child = child
      self.redirects = redirects
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Redirect
      return command.Redirect(cast('command_t', None), [] if alloc_lists else cast('List[Redir]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.Redirect')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      if self.redirects is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.redirects:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('redirects', x1))
  
      return out_node
  
  class Simple(command_t):
    _type_tag = 3
    __slots__ = ('blame_tok', 'more_env', 'words', 'typed_args', 'block',
                 'is_last_cmd', 'redirects')
  
    def __init__(self, blame_tok, more_env, words, typed_args, block,
                 is_last_cmd, redirects):
      # type: (Optional[Token], List[EnvPair], List[word_t], Optional[ArgList], Optional[LiteralBlock], bool, Optional[List[Redir]]) -> None
      self.blame_tok = blame_tok
      self.more_env = more_env
      self.words = words
      self.typed_args = typed_args
      self.block = block
      self.is_last_cmd = is_last_cmd
      self.redirects = redirects
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Simple
      return command.Simple(cast('Optional[Token]', None), [] if alloc_lists else cast('List[EnvPair]', None), [] if alloc_lists else cast('List[word_t]', None), cast('Optional[ArgList]', None), cast('Optional[LiteralBlock]', None), False, cast('Optional[List[Redir]]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      if do_abbrev:
        p = _command__Simple(self)
        if p:
          return p
  
      out_node = NewRecord('command.Simple')
      L = out_node.fields
  
      if self.blame_tok is not None:  # Optional
        x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('blame_tok', x0))
  
      if self.more_env is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.more_env:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('more_env', x1))
  
      if self.words is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.words:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('words', x2))
  
      if self.typed_args is not None:  # Optional
        x3 = self.typed_args.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('typed_args', x3))
  
      if self.block is not None:  # Optional
        x4 = self.block.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('block', x4))
  
      x5 = hnode.Leaf('T' if self.is_last_cmd else 'F', color_e.OtherConst)
      L.append(Field('is_last_cmd', x5))
  
      if self.redirects is not None:  # List
        x6 = hnode.Array([])
        for i6 in self.redirects:
          h = (hnode.Leaf("_", color_e.OtherConst) if i6 is None else
               i6.PrettyTree(do_abbrev, trav=trav))
          x6.children.append(h)
        L.append(Field('redirects', x6))
  
      return out_node
  
  class ExpandedAlias(command_t):
    _type_tag = 4
    __slots__ = ('child', 'more_env')
  
    def __init__(self, child, more_env):
      # type: (command_t, List[EnvPair]) -> None
      self.child = child
      self.more_env = more_env
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.ExpandedAlias
      return command.ExpandedAlias(cast('command_t', None), [] if alloc_lists else cast('List[EnvPair]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.ExpandedAlias')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      if self.more_env is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.more_env:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('more_env', x1))
  
      return out_node
  
  class Sentence(command_t):
    _type_tag = 5
    __slots__ = ('child', 'terminator')
  
    def __init__(self, child, terminator):
      # type: (command_t, Token) -> None
      self.child = child
      self.terminator = terminator
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Sentence
      return command.Sentence(cast('command_t', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.Sentence')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      assert self.terminator is not None
      x1 = self.terminator.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('terminator', x1))
  
      return out_node
  
  class ShAssignment(command_t):
    _type_tag = 6
    __slots__ = ('left', 'pairs')
  
    def __init__(self, left, pairs):
      # type: (Token, List[AssignPair]) -> None
      self.left = left
      self.pairs = pairs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.ShAssignment
      return command.ShAssignment(cast('Token', None), [] if alloc_lists else cast('List[AssignPair]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.ShAssignment')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.pairs is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.pairs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('pairs', x1))
  
      return out_node
  
  class ControlFlow(command_t):
    _type_tag = 7
    __slots__ = ('keyword', 'arg_word')
  
    def __init__(self, keyword, arg_word):
      # type: (Token, Optional[CompoundWord]) -> None
      self.keyword = keyword
      self.arg_word = arg_word
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.ControlFlow
      return command.ControlFlow(cast('Token', None), cast('Optional[CompoundWord]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.ControlFlow')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      if self.arg_word is not None:  # Optional
        x1 = self.arg_word.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('arg_word', x1))
  
      return out_node
  
  class Pipeline(command_t):
    _type_tag = 8
    __slots__ = ('negated', 'children', 'ops')
  
    def __init__(self, negated, children, ops):
      # type: (Optional[Token], List[command_t], List[Token]) -> None
      self.negated = negated
      self.children = children
      self.ops = ops
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Pipeline
      return command.Pipeline(cast('Optional[Token]', None), [] if alloc_lists else cast('List[command_t]', None), [] if alloc_lists else cast('List[Token]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.Pipeline')
      L = out_node.fields
  
      if self.negated is not None:  # Optional
        x0 = self.negated.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('negated', x0))
  
      if self.children is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('children', x1))
  
      if self.ops is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.ops:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('ops', x2))
  
      return out_node
  
  class AndOr(command_t):
    _type_tag = 9
    __slots__ = ('children', 'ops')
  
    def __init__(self, children, ops):
      # type: (List[command_t], List[Token]) -> None
      self.children = children
      self.ops = ops
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.AndOr
      return command.AndOr([] if alloc_lists else cast('List[command_t]', None), [] if alloc_lists else cast('List[Token]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.AndOr')
      L = out_node.fields
  
      if self.children is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('children', x0))
  
      if self.ops is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.ops:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('ops', x1))
  
      return out_node
  
  class DoGroup(command_t):
    _type_tag = 10
    __slots__ = ('left', 'children', 'right')
  
    def __init__(self, left, children, right):
      # type: (Token, List[command_t], Token) -> None
      self.left = left
      self.children = children
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.DoGroup
      return command.DoGroup(cast('Token', None), [] if alloc_lists else cast('List[command_t]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.DoGroup')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.children is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('children', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class Subshell(command_t):
    _type_tag = 12
    __slots__ = ('left', 'child', 'right', 'is_last_cmd')
  
    def __init__(self, left, child, right, is_last_cmd):
      # type: (Token, command_t, Token, bool) -> None
      self.left = left
      self.child = child
      self.right = right
      self.is_last_cmd = is_last_cmd
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Subshell
      return command.Subshell(cast('Token', None), cast('command_t', None), cast('Token', None), False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.Subshell')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      x3 = hnode.Leaf('T' if self.is_last_cmd else 'F', color_e.OtherConst)
      L.append(Field('is_last_cmd', x3))
  
      return out_node
  
  class DParen(command_t):
    _type_tag = 13
    __slots__ = ('left', 'child', 'right')
  
    def __init__(self, left, child, right):
      # type: (Token, arith_expr_t, Token) -> None
      self.left = left
      self.child = child
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.DParen
      return command.DParen(cast('Token', None), cast('arith_expr_t', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.DParen')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class DBracket(command_t):
    _type_tag = 14
    __slots__ = ('left', 'expr', 'right')
  
    def __init__(self, left, expr, right):
      # type: (Token, bool_expr_t, Token) -> None
      self.left = left
      self.expr = expr
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.DBracket
      return command.DBracket(cast('Token', None), cast('bool_expr_t', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.DBracket')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.expr is not None
      x1 = self.expr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('expr', x1))
  
      assert self.right is not None
      x2 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x2))
  
      return out_node
  
  class ForEach(command_t):
    _type_tag = 15
    __slots__ = ('keyword', 'iter_names', 'iterable', 'semi_tok', 'body')
  
    def __init__(self, keyword, iter_names, iterable, semi_tok, body):
      # type: (Token, List[str], for_iter_t, Optional[Token], command_t) -> None
      self.keyword = keyword
      self.iter_names = iter_names
      self.iterable = iterable
      self.semi_tok = semi_tok
      self.body = body
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.ForEach
      return command.ForEach(cast('Token', None), [] if alloc_lists else cast('List[str]', None), cast('for_iter_t', None), cast('Optional[Token]', None), cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.ForEach')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      if self.iter_names is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.iter_names:
          x1.children.append(NewLeaf(i1, color_e.StringConst))
        L.append(Field('iter_names', x1))
  
      assert self.iterable is not None
      x2 = self.iterable.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('iterable', x2))
  
      if self.semi_tok is not None:  # Optional
        x3 = self.semi_tok.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('semi_tok', x3))
  
      assert self.body is not None
      x4 = self.body.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('body', x4))
  
      return out_node
  
  class ForExpr(command_t):
    _type_tag = 16
    __slots__ = ('keyword', 'init', 'cond', 'update', 'body')
  
    def __init__(self, keyword, init, cond, update, body):
      # type: (Token, Optional[arith_expr_t], Optional[arith_expr_t], Optional[arith_expr_t], Optional[command_t]) -> None
      self.keyword = keyword
      self.init = init
      self.cond = cond
      self.update = update
      self.body = body
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.ForExpr
      return command.ForExpr(cast('Token', None), cast('Optional[arith_expr_t]', None), cast('Optional[arith_expr_t]', None), cast('Optional[arith_expr_t]', None), cast('Optional[command_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.ForExpr')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      if self.init is not None:  # Optional
        x1 = self.init.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('init', x1))
  
      if self.cond is not None:  # Optional
        x2 = self.cond.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('cond', x2))
  
      if self.update is not None:  # Optional
        x3 = self.update.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('update', x3))
  
      if self.body is not None:  # Optional
        x4 = self.body.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('body', x4))
  
      return out_node
  
  class WhileUntil(command_t):
    _type_tag = 17
    __slots__ = ('keyword', 'cond', 'body')
  
    def __init__(self, keyword, cond, body):
      # type: (Token, condition_t, command_t) -> None
      self.keyword = keyword
      self.cond = cond
      self.body = body
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.WhileUntil
      return command.WhileUntil(cast('Token', None), cast('condition_t', None), cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.WhileUntil')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      assert self.cond is not None
      x1 = self.cond.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('cond', x1))
  
      assert self.body is not None
      x2 = self.body.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('body', x2))
  
      return out_node
  
  class If(command_t):
    _type_tag = 18
    __slots__ = ('if_kw', 'arms', 'else_kw', 'else_action', 'fi_kw')
  
    def __init__(self, if_kw, arms, else_kw, else_action, fi_kw):
      # type: (Token, List[IfArm], Optional[Token], List[command_t], Optional[Token]) -> None
      self.if_kw = if_kw
      self.arms = arms
      self.else_kw = else_kw
      self.else_action = else_action
      self.fi_kw = fi_kw
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.If
      return command.If(cast('Token', None), [] if alloc_lists else cast('List[IfArm]', None), cast('Optional[Token]', None), [] if alloc_lists else cast('List[command_t]', None), cast('Optional[Token]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.If')
      L = out_node.fields
  
      assert self.if_kw is not None
      x0 = self.if_kw.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('if_kw', x0))
  
      if self.arms is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.arms:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('arms', x1))
  
      if self.else_kw is not None:  # Optional
        x2 = self.else_kw.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('else_kw', x2))
  
      if self.else_action is not None:  # List
        x3 = hnode.Array([])
        for i3 in self.else_action:
          h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
               i3.PrettyTree(do_abbrev, trav=trav))
          x3.children.append(h)
        L.append(Field('else_action', x3))
  
      if self.fi_kw is not None:  # Optional
        x4 = self.fi_kw.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('fi_kw', x4))
  
      return out_node
  
  class Case(command_t):
    _type_tag = 19
    __slots__ = ('case_kw', 'to_match', 'arms_start', 'arms', 'arms_end')
  
    def __init__(self, case_kw, to_match, arms_start, arms, arms_end):
      # type: (Token, case_arg_t, Token, List[CaseArm], Token) -> None
      self.case_kw = case_kw
      self.to_match = to_match
      self.arms_start = arms_start
      self.arms = arms
      self.arms_end = arms_end
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Case
      return command.Case(cast('Token', None), cast('case_arg_t', None), cast('Token', None), [] if alloc_lists else cast('List[CaseArm]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.Case')
      L = out_node.fields
  
      assert self.case_kw is not None
      x0 = self.case_kw.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('case_kw', x0))
  
      assert self.to_match is not None
      x1 = self.to_match.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('to_match', x1))
  
      assert self.arms_start is not None
      x2 = self.arms_start.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('arms_start', x2))
  
      if self.arms is not None:  # List
        x3 = hnode.Array([])
        for i3 in self.arms:
          h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
               i3.PrettyTree(do_abbrev, trav=trav))
          x3.children.append(h)
        L.append(Field('arms', x3))
  
      assert self.arms_end is not None
      x4 = self.arms_end.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('arms_end', x4))
  
      return out_node
  
  class TimeBlock(command_t):
    _type_tag = 21
    __slots__ = ('keyword', 'pipeline')
  
    def __init__(self, keyword, pipeline):
      # type: (Token, command_t) -> None
      self.keyword = keyword
      self.pipeline = pipeline
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.TimeBlock
      return command.TimeBlock(cast('Token', None), cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.TimeBlock')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      assert self.pipeline is not None
      x1 = self.pipeline.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('pipeline', x1))
  
      return out_node
  
  class CommandList(command_t):
    _type_tag = 22
    __slots__ = ('children',)
  
    def __init__(self, children):
      # type: (List[command_t]) -> None
      self.children = children
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.CommandList
      return command.CommandList([] if alloc_lists else cast('List[command_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.CommandList')
      L = out_node.fields
  
      if self.children is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('children', x0))
  
      return out_node
  
  class BareDecl(command_t):
    _type_tag = 24
    __slots__ = ('lhs', 'rhs')
  
    def __init__(self, lhs, rhs):
      # type: (Token, expr_t) -> None
      self.lhs = lhs
      self.rhs = rhs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.BareDecl
      return command.BareDecl(cast('Token', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.BareDecl')
      L = out_node.fields
  
      assert self.lhs is not None
      x0 = self.lhs.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('lhs', x0))
  
      assert self.rhs is not None
      x1 = self.rhs.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('rhs', x1))
  
      return out_node
  
  class Retval(command_t):
    _type_tag = 29
    __slots__ = ('keyword', 'val')
  
    def __init__(self, keyword, val):
      # type: (Token, expr_t) -> None
      self.keyword = keyword
      self.val = val
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> command.Retval
      return command.Retval(cast('Token', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('command.Retval')
      L = out_node.fields
  
      assert self.keyword is not None
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))
  
      assert self.val is not None
      x1 = self.val.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('val', x1))
  
      return out_node
  
  pass

class b_command_e(object):
  VarDecl = 93
  Mutation = 94

_b_command_str = {
  93: 'VarDecl',
  94: 'Mutation',
}

def b_command_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _b_command_str[tag]
  if dot:
    return "b_command.%s" % v
  else:
    return v

class b_command_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class b_command(object):
  pass

class glob_part_e(object):
  Literal = 1
  Operator = 2
  CharClass = 3

_glob_part_str = {
  1: 'Literal',
  2: 'Operator',
  3: 'CharClass',
}

def glob_part_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _glob_part_str[tag]
  if dot:
    return "glob_part.%s" % v
  else:
    return v

class glob_part_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class glob_part(object):
  class Literal(glob_part_t):
    _type_tag = 1
    __slots__ = ('id', 's')
  
    def __init__(self, id, s):
      # type: (Id_t, str) -> None
      self.id = id
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> glob_part.Literal
      return glob_part.Literal(-1, '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('glob_part.Literal')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.id, dot=False), color_e.UserType)
      L.append(Field('id', x0))
  
      x1 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x1))
  
      return out_node
  
  class Operator(glob_part_t):
    _type_tag = 2
    __slots__ = ('op_id',)
  
    def __init__(self, op_id):
      # type: (Id_t) -> None
      self.op_id = op_id
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> glob_part.Operator
      return glob_part.Operator(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('glob_part.Operator')
      L = out_node.fields
  
      x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
      L.append(Field('op_id', x0))
  
      return out_node
  
  class CharClass(glob_part_t):
    _type_tag = 3
    __slots__ = ('negated', 'strs')
  
    def __init__(self, negated, strs):
      # type: (bool, List[str]) -> None
      self.negated = negated
      self.strs = strs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> glob_part.CharClass
      return glob_part.CharClass(False, [] if alloc_lists else cast('List[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('glob_part.CharClass')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.negated else 'F', color_e.OtherConst)
      L.append(Field('negated', x0))
  
      if self.strs is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.strs:
          x1.children.append(NewLeaf(i1, color_e.StringConst))
        L.append(Field('strs', x1))
  
      return out_node
  
  pass

class printf_part_e(object):
  Literal = 67
  Percent = 2

_printf_part_str = {
  2: 'Percent',
  67: 'Literal',
}

def printf_part_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _printf_part_str[tag]
  if dot:
    return "printf_part.%s" % v
  else:
    return v

class printf_part_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class printf_part(object):
  class Percent(printf_part_t):
    _type_tag = 2
    __slots__ = ('flags', 'width', 'precision', 'type')
  
    def __init__(self, flags, width, precision, type):
      # type: (List[Token], Optional[Token], Optional[Token], Token) -> None
      self.flags = flags
      self.width = width
      self.precision = precision
      self.type = type
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> printf_part.Percent
      return printf_part.Percent([] if alloc_lists else cast('List[Token]', None), cast('Optional[Token]', None), cast('Optional[Token]', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('printf_part.Percent')
      L = out_node.fields
  
      if self.flags is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.flags:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('flags', x0))
  
      if self.width is not None:  # Optional
        x1 = self.width.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('width', x1))
  
      if self.precision is not None:  # Optional
        x2 = self.precision.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('precision', x2))
  
      assert self.type is not None
      x3 = self.type.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('type', x3))
  
      return out_node
  
  pass

class expr_context_t(pybase.SimpleObj):
  pass

class expr_context_e(object):
  Load = expr_context_t(1)
  Store = expr_context_t(2)
  Del = expr_context_t(3)
  AugLoad = expr_context_t(4)
  AugStore = expr_context_t(5)
  Param = expr_context_t(6)

_expr_context_str = {
  1: 'Load',
  2: 'Store',
  3: 'Del',
  4: 'AugLoad',
  5: 'AugStore',
  6: 'Param',
}

def expr_context_str(val, dot=True):
  # type: (expr_context_t, bool) -> str
  v = _expr_context_str[val]
  if dot:
    return "expr_context.%s" % v
  else:
    return v

class y_lhs_e(object):
  Var = 67
  Subscript = 102
  Attribute = 103

_y_lhs_str = {
  67: 'Var',
  102: 'Subscript',
  103: 'Attribute',
}

def y_lhs_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _y_lhs_str[tag]
  if dot:
    return "y_lhs.%s" % v
  else:
    return v

class y_lhs_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class y_lhs(object):
  pass

class place_op_e(object):
  Subscript = 1
  Attribute = 2

_place_op_str = {
  1: 'Subscript',
  2: 'Attribute',
}

def place_op_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _place_op_str[tag]
  if dot:
    return "place_op.%s" % v
  else:
    return v

class place_op_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class place_op(object):
  class Subscript(place_op_t):
    _type_tag = 1
    __slots__ = ('op', 'index')
  
    def __init__(self, op, index):
      # type: (Token, expr_t) -> None
      self.op = op
      self.index = index
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> place_op.Subscript
      return place_op.Subscript(cast('Token', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('place_op.Subscript')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.index is not None
      x1 = self.index.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('index', x1))
  
      return out_node
  
  class Attribute(place_op_t):
    _type_tag = 2
    __slots__ = ('op', 'attr')
  
    def __init__(self, op, attr):
      # type: (Token, Token) -> None
      self.op = op
      self.attr = attr
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> place_op.Attribute
      return place_op.Attribute(cast('Token', None), cast('Token', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('place_op.Attribute')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.attr is not None
      x1 = self.attr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('attr', x1))
  
      return out_node
  
  pass

class expr_e(object):
  Var = 1
  Const = 2
  Place = 3
  YshArrayLiteral = 75
  Eggex = 84
  SimpleVarSub = 72
  BracedVarSub = 69
  CommandSub = 73
  ExprSub = 74
  SingleQuoted = 71
  DoubleQuoted = 70
  Literal = 12
  Lambda = 13
  Unary = 14
  Binary = 15
  Compare = 16
  FuncCall = 17
  IfExp = 18
  Tuple = 19
  List = 20
  Dict = 21
  Implicit = 22
  ListComp = 23
  DictComp = 24
  GeneratorExp = 25
  Range = 26
  Slice = 27
  Subscript = 102
  Attribute = 103
  Spread = 30

_expr_str = {
  1: 'Var',
  2: 'Const',
  3: 'Place',
  12: 'Literal',
  13: 'Lambda',
  14: 'Unary',
  15: 'Binary',
  16: 'Compare',
  17: 'FuncCall',
  18: 'IfExp',
  19: 'Tuple',
  20: 'List',
  21: 'Dict',
  22: 'Implicit',
  23: 'ListComp',
  24: 'DictComp',
  25: 'GeneratorExp',
  26: 'Range',
  27: 'Slice',
  30: 'Spread',
  69: 'BracedVarSub',
  70: 'DoubleQuoted',
  71: 'SingleQuoted',
  72: 'SimpleVarSub',
  73: 'CommandSub',
  74: 'ExprSub',
  75: 'YshArrayLiteral',
  84: 'Eggex',
  102: 'Subscript',
  103: 'Attribute',
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

class expr__Implicit(expr_t):
  _type_tag = 22
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

    out_node = NewRecord('expr.Implicit')
    L = out_node.fields

    return out_node

class expr(object):
  class Var(expr_t):
    _type_tag = 1
    __slots__ = ('left', 'name')
  
    def __init__(self, left, name):
      # type: (Token, str) -> None
      self.left = left
      self.name = name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Var
      return expr.Var(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      if do_abbrev:
        p = _expr__Var(self)
        if p:
          return p
  
      out_node = NewRecord('expr.Var')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      x1 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x1))
  
      return out_node
  
  class Const(expr_t):
    _type_tag = 2
    __slots__ = ('c', 'val')
  
    def __init__(self, c, val):
      # type: (Token, value_t) -> None
      self.c = c
      self.val = val
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Const
      return expr.Const(cast('Token', None), cast('value_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      if do_abbrev:
        p = _expr__Const(self)
        if p:
          return p
  
      out_node = NewRecord('expr.Const')
      L = out_node.fields
  
      assert self.c is not None
      x0 = self.c.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('c', x0))
  
      assert self.val is not None
      x1 = self.val.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('val', x1))
  
      return out_node
  
  class Place(expr_t):
    _type_tag = 3
    __slots__ = ('blame_tok', 'var_name', 'ops')
  
    def __init__(self, blame_tok, var_name, ops):
      # type: (Token, str, List[place_op_t]) -> None
      self.blame_tok = blame_tok
      self.var_name = var_name
      self.ops = ops
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Place
      return expr.Place(cast('Token', None), '', [] if alloc_lists else cast('List[place_op_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Place')
      L = out_node.fields
  
      assert self.blame_tok is not None
      x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_tok', x0))
  
      x1 = NewLeaf(self.var_name, color_e.StringConst)
      L.append(Field('var_name', x1))
  
      if self.ops is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.ops:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('ops', x2))
  
      return out_node
  
  class Literal(expr_t):
    _type_tag = 12
    __slots__ = ('inner',)
  
    def __init__(self, inner):
      # type: (expr_t) -> None
      self.inner = inner
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Literal
      return expr.Literal(cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Literal')
      L = out_node.fields
  
      assert self.inner is not None
      x0 = self.inner.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('inner', x0))
  
      return out_node
  
  class Lambda(expr_t):
    _type_tag = 13
    __slots__ = ('params', 'body')
  
    def __init__(self, params, body):
      # type: (List[NameType], expr_t) -> None
      self.params = params
      self.body = body
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Lambda
      return expr.Lambda([] if alloc_lists else cast('List[NameType]', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Lambda')
      L = out_node.fields
  
      if self.params is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.params:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('params', x0))
  
      assert self.body is not None
      x1 = self.body.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('body', x1))
  
      return out_node
  
  class Unary(expr_t):
    _type_tag = 14
    __slots__ = ('op', 'child')
  
    def __init__(self, op, child):
      # type: (Token, expr_t) -> None
      self.op = op
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Unary
      return expr.Unary(cast('Token', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Unary')
      L = out_node.fields
  
      assert self.op is not None
      x0 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      return out_node
  
  class Binary(expr_t):
    _type_tag = 15
    __slots__ = ('op', 'left', 'right')
  
    def __init__(self, op, left, right):
      # type: (Token, expr_t, expr_t) -> None
      self.op = op
      self.left = left
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Binary
      return expr.Binary(cast('Token', None), cast('expr_t', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Binary')
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
  
  class Compare(expr_t):
    _type_tag = 16
    __slots__ = ('left', 'ops', 'comparators')
  
    def __init__(self, left, ops, comparators):
      # type: (expr_t, List[Token], List[expr_t]) -> None
      self.left = left
      self.ops = ops
      self.comparators = comparators
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Compare
      return expr.Compare(cast('expr_t', None), [] if alloc_lists else cast('List[Token]', None), [] if alloc_lists else cast('List[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Compare')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.ops is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.ops:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('ops', x1))
  
      if self.comparators is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.comparators:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('comparators', x2))
  
      return out_node
  
  class FuncCall(expr_t):
    _type_tag = 17
    __slots__ = ('func', 'args')
  
    def __init__(self, func, args):
      # type: (expr_t, ArgList) -> None
      self.func = func
      self.args = args
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.FuncCall
      return expr.FuncCall(cast('expr_t', None), cast('ArgList', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.FuncCall')
      L = out_node.fields
  
      assert self.func is not None
      x0 = self.func.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('func', x0))
  
      assert self.args is not None
      x1 = self.args.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('args', x1))
  
      return out_node
  
  class IfExp(expr_t):
    _type_tag = 18
    __slots__ = ('test', 'body', 'orelse')
  
    def __init__(self, test, body, orelse):
      # type: (expr_t, expr_t, expr_t) -> None
      self.test = test
      self.body = body
      self.orelse = orelse
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.IfExp
      return expr.IfExp(cast('expr_t', None), cast('expr_t', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.IfExp')
      L = out_node.fields
  
      assert self.test is not None
      x0 = self.test.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('test', x0))
  
      assert self.body is not None
      x1 = self.body.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('body', x1))
  
      assert self.orelse is not None
      x2 = self.orelse.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('orelse', x2))
  
      return out_node
  
  class Tuple(expr_t):
    _type_tag = 19
    __slots__ = ('left', 'elts', 'ctx')
  
    def __init__(self, left, elts, ctx):
      # type: (Token, List[expr_t], expr_context_t) -> None
      self.left = left
      self.elts = elts
      self.ctx = ctx
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Tuple
      return expr.Tuple(cast('Token', None), [] if alloc_lists else cast('List[expr_t]', None), expr_context_e.Load)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Tuple')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.elts is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.elts:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('elts', x1))
  
      x2 = hnode.Leaf(expr_context_str(self.ctx), color_e.TypeName)
      L.append(Field('ctx', x2))
  
      return out_node
  
  class List(expr_t):
    _type_tag = 20
    __slots__ = ('left', 'elts', 'ctx')
  
    def __init__(self, left, elts, ctx):
      # type: (Token, List[expr_t], expr_context_t) -> None
      self.left = left
      self.elts = elts
      self.ctx = ctx
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.List
      return expr.List(cast('Token', None), [] if alloc_lists else cast('List[expr_t]', None), expr_context_e.Load)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.List')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.elts is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.elts:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('elts', x1))
  
      x2 = hnode.Leaf(expr_context_str(self.ctx), color_e.TypeName)
      L.append(Field('ctx', x2))
  
      return out_node
  
  class Dict(expr_t):
    _type_tag = 21
    __slots__ = ('left', 'keys', 'values')
  
    def __init__(self, left, keys, values):
      # type: (Token, List[expr_t], List[expr_t]) -> None
      self.left = left
      self.keys = keys
      self.values = values
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Dict
      return expr.Dict(cast('Token', None), [] if alloc_lists else cast('List[expr_t]', None), [] if alloc_lists else cast('List[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Dict')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      if self.keys is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.keys:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('keys', x1))
  
      if self.values is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.values:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('values', x2))
  
      return out_node
  
  Implicit = expr__Implicit()
  
  class ListComp(expr_t):
    _type_tag = 23
    __slots__ = ('left', 'elt', 'generators')
  
    def __init__(self, left, elt, generators):
      # type: (Token, expr_t, List[Comprehension]) -> None
      self.left = left
      self.elt = elt
      self.generators = generators
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.ListComp
      return expr.ListComp(cast('Token', None), cast('expr_t', None), [] if alloc_lists else cast('List[Comprehension]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.ListComp')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.elt is not None
      x1 = self.elt.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('elt', x1))
  
      if self.generators is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.generators:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('generators', x2))
  
      return out_node
  
  class DictComp(expr_t):
    _type_tag = 24
    __slots__ = ('left', 'key', 'value', 'generators')
  
    def __init__(self, left, key, value, generators):
      # type: (Token, expr_t, expr_t, List[Comprehension]) -> None
      self.left = left
      self.key = key
      self.value = value
      self.generators = generators
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.DictComp
      return expr.DictComp(cast('Token', None), cast('expr_t', None), cast('expr_t', None), [] if alloc_lists else cast('List[Comprehension]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.DictComp')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.key is not None
      x1 = self.key.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('key', x1))
  
      assert self.value is not None
      x2 = self.value.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('value', x2))
  
      if self.generators is not None:  # List
        x3 = hnode.Array([])
        for i3 in self.generators:
          h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
               i3.PrettyTree(do_abbrev, trav=trav))
          x3.children.append(h)
        L.append(Field('generators', x3))
  
      return out_node
  
  class GeneratorExp(expr_t):
    _type_tag = 25
    __slots__ = ('elt', 'generators')
  
    def __init__(self, elt, generators):
      # type: (expr_t, List[Comprehension]) -> None
      self.elt = elt
      self.generators = generators
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.GeneratorExp
      return expr.GeneratorExp(cast('expr_t', None), [] if alloc_lists else cast('List[Comprehension]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.GeneratorExp')
      L = out_node.fields
  
      assert self.elt is not None
      x0 = self.elt.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('elt', x0))
  
      if self.generators is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.generators:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('generators', x1))
  
      return out_node
  
  class Range(expr_t):
    _type_tag = 26
    __slots__ = ('lower', 'op', 'upper')
  
    def __init__(self, lower, op, upper):
      # type: (expr_t, Token, expr_t) -> None
      self.lower = lower
      self.op = op
      self.upper = upper
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Range
      return expr.Range(cast('expr_t', None), cast('Token', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Range')
      L = out_node.fields
  
      assert self.lower is not None
      x0 = self.lower.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('lower', x0))
  
      assert self.op is not None
      x1 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x1))
  
      assert self.upper is not None
      x2 = self.upper.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('upper', x2))
  
      return out_node
  
  class Slice(expr_t):
    _type_tag = 27
    __slots__ = ('lower', 'op', 'upper')
  
    def __init__(self, lower, op, upper):
      # type: (Optional[expr_t], Token, Optional[expr_t]) -> None
      self.lower = lower
      self.op = op
      self.upper = upper
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Slice
      return expr.Slice(cast('Optional[expr_t]', None), cast('Token', None), cast('Optional[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Slice')
      L = out_node.fields
  
      if self.lower is not None:  # Optional
        x0 = self.lower.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('lower', x0))
  
      assert self.op is not None
      x1 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x1))
  
      if self.upper is not None:  # Optional
        x2 = self.upper.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('upper', x2))
  
      return out_node
  
  class Spread(expr_t):
    _type_tag = 30
    __slots__ = ('left', 'child')
  
    def __init__(self, left, child):
      # type: (Token, expr_t) -> None
      self.left = left
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Spread
      return expr.Spread(cast('Token', None), cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Spread')
      L = out_node.fields
  
      assert self.left is not None
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))
  
      assert self.child is not None
      x1 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x1))
  
      return out_node
  
  pass

class class_literal_term_e(object):
  PosixClass = 104
  PerlClass = 105
  CharRange = 107
  CharCode = 106
  SingleQuoted = 71
  Splice = 6

_class_literal_term_str = {
  6: 'Splice',
  71: 'SingleQuoted',
  104: 'PosixClass',
  105: 'PerlClass',
  106: 'CharCode',
  107: 'CharRange',
}

def class_literal_term_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _class_literal_term_str[tag]
  if dot:
    return "class_literal_term.%s" % v
  else:
    return v

class class_literal_term_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class class_literal_term(object):
  class Splice(class_literal_term_t):
    _type_tag = 6
    __slots__ = ('name', 'var_name')
  
    def __init__(self, name, var_name):
      # type: (Token, str) -> None
      self.name = name
      self.var_name = var_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> class_literal_term.Splice
      return class_literal_term.Splice(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('class_literal_term.Splice')
      L = out_node.fields
  
      assert self.name is not None
      x0 = self.name.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('name', x0))
  
      x1 = NewLeaf(self.var_name, color_e.StringConst)
      L.append(Field('var_name', x1))
  
      return out_node
  
  pass

class char_class_term_e(object):
  PosixClass = 104
  PerlClass = 105
  CharRange = 107
  CharCode = 106

_char_class_term_str = {
  104: 'PosixClass',
  105: 'PerlClass',
  106: 'CharCode',
  107: 'CharRange',
}

def char_class_term_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _char_class_term_str[tag]
  if dot:
    return "char_class_term.%s" % v
  else:
    return v

class char_class_term_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class char_class_term(object):
  pass

class re_repeat_e(object):
  Op = 67
  Range = 2

_re_repeat_str = {
  2: 'Range',
  67: 'Op',
}

def re_repeat_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _re_repeat_str[tag]
  if dot:
    return "re_repeat.%s" % v
  else:
    return v

class re_repeat_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class re_repeat(object):
  class Range(re_repeat_t):
    _type_tag = 2
    __slots__ = ('left', 'lower', 'upper', 'right')
  
    def __init__(self, left, lower, upper, right):
      # type: (Optional[Token], str, str, Optional[Token]) -> None
      self.left = left
      self.lower = lower
      self.upper = upper
      self.right = right
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re_repeat.Range
      return re_repeat.Range(cast('Optional[Token]', None), '', '', cast('Optional[Token]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re_repeat.Range')
      L = out_node.fields
  
      if self.left is not None:  # Optional
        x0 = self.left.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('left', x0))
  
      x1 = NewLeaf(self.lower, color_e.StringConst)
      L.append(Field('lower', x1))
  
      x2 = NewLeaf(self.upper, color_e.StringConst)
      L.append(Field('upper', x2))
  
      if self.right is not None:  # Optional
        x3 = self.right.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('right', x3))
  
      return out_node
  
  pass

class re_e(object):
  Primitive = 1
  PosixClass = 104
  PerlClass = 105
  CharClassLiteral = 4
  CharClass = 5
  Splice = 6
  SingleQuoted = 71
  Repeat = 8
  Seq = 9
  Alt = 10
  Group = 11
  Capture = 12
  Backtracking = 13
  LiteralChars = 14

_re_str = {
  1: 'Primitive',
  4: 'CharClassLiteral',
  5: 'CharClass',
  6: 'Splice',
  8: 'Repeat',
  9: 'Seq',
  10: 'Alt',
  11: 'Group',
  12: 'Capture',
  13: 'Backtracking',
  14: 'LiteralChars',
  71: 'SingleQuoted',
  104: 'PosixClass',
  105: 'PerlClass',
}

def re_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _re_str[tag]
  if dot:
    return "re.%s" % v
  else:
    return v

class re_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class re(object):
  class Primitive(re_t):
    _type_tag = 1
    __slots__ = ('blame_tok', 'id')
  
    def __init__(self, blame_tok, id):
      # type: (Token, Id_t) -> None
      self.blame_tok = blame_tok
      self.id = id
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Primitive
      return re.Primitive(cast('Token', None), -1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Primitive')
      L = out_node.fields
  
      assert self.blame_tok is not None
      x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_tok', x0))
  
      x1 = hnode.Leaf(Id_str(self.id, dot=False), color_e.UserType)
      L.append(Field('id', x1))
  
      return out_node
  
  class CharClassLiteral(re_t):
    _type_tag = 4
    __slots__ = ('negated', 'terms')
  
    def __init__(self, negated, terms):
      # type: (bool, List[class_literal_term_t]) -> None
      self.negated = negated
      self.terms = terms
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.CharClassLiteral
      return re.CharClassLiteral(False, [] if alloc_lists else cast('List[class_literal_term_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.CharClassLiteral')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.negated else 'F', color_e.OtherConst)
      L.append(Field('negated', x0))
  
      if self.terms is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.terms:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('terms', x1))
  
      return out_node
  
  class CharClass(re_t):
    _type_tag = 5
    __slots__ = ('negated', 'terms')
  
    def __init__(self, negated, terms):
      # type: (bool, List[char_class_term_t]) -> None
      self.negated = negated
      self.terms = terms
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.CharClass
      return re.CharClass(False, [] if alloc_lists else cast('List[char_class_term_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.CharClass')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.negated else 'F', color_e.OtherConst)
      L.append(Field('negated', x0))
  
      if self.terms is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.terms:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('terms', x1))
  
      return out_node
  
  class Splice(re_t):
    _type_tag = 6
    __slots__ = ('name', 'var_name')
  
    def __init__(self, name, var_name):
      # type: (Token, str) -> None
      self.name = name
      self.var_name = var_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Splice
      return re.Splice(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Splice')
      L = out_node.fields
  
      assert self.name is not None
      x0 = self.name.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('name', x0))
  
      x1 = NewLeaf(self.var_name, color_e.StringConst)
      L.append(Field('var_name', x1))
  
      return out_node
  
  class Repeat(re_t):
    _type_tag = 8
    __slots__ = ('child', 'op')
  
    def __init__(self, child, op):
      # type: (re_t, re_repeat_t) -> None
      self.child = child
      self.op = op
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Repeat
      return re.Repeat(cast('re_t', None), cast('re_repeat_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Repeat')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      assert self.op is not None
      x1 = self.op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('op', x1))
  
      return out_node
  
  class Seq(re_t):
    _type_tag = 9
    __slots__ = ('children',)
  
    def __init__(self, children):
      # type: (List[re_t]) -> None
      self.children = children
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Seq
      return re.Seq([] if alloc_lists else cast('List[re_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Seq')
      L = out_node.fields
  
      if self.children is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('children', x0))
  
      return out_node
  
  class Alt(re_t):
    _type_tag = 10
    __slots__ = ('children',)
  
    def __init__(self, children):
      # type: (List[re_t]) -> None
      self.children = children
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Alt
      return re.Alt([] if alloc_lists else cast('List[re_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Alt')
      L = out_node.fields
  
      if self.children is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.children:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('children', x0))
  
      return out_node
  
  class Group(re_t):
    _type_tag = 11
    __slots__ = ('child',)
  
    def __init__(self, child):
      # type: (re_t) -> None
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Group
      return re.Group(cast('re_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Group')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      return out_node
  
  class Capture(re_t):
    _type_tag = 12
    __slots__ = ('child', 'name', 'func_name')
  
    def __init__(self, child, name, func_name):
      # type: (re_t, Optional[Token], Optional[Token]) -> None
      self.child = child
      self.name = name
      self.func_name = func_name
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Capture
      return re.Capture(cast('re_t', None), cast('Optional[Token]', None), cast('Optional[Token]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Capture')
      L = out_node.fields
  
      assert self.child is not None
      x0 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x0))
  
      if self.name is not None:  # Optional
        x1 = self.name.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('name', x1))
  
      if self.func_name is not None:  # Optional
        x2 = self.func_name.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('func_name', x2))
  
      return out_node
  
  class Backtracking(re_t):
    _type_tag = 13
    __slots__ = ('negated', 'name', 'child')
  
    def __init__(self, negated, name, child):
      # type: (bool, Token, re_t) -> None
      self.negated = negated
      self.name = name
      self.child = child
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.Backtracking
      return re.Backtracking(False, cast('Token', None), cast('re_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.Backtracking')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.negated else 'F', color_e.OtherConst)
      L.append(Field('negated', x0))
  
      assert self.name is not None
      x1 = self.name.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('name', x1))
  
      assert self.child is not None
      x2 = self.child.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('child', x2))
  
      return out_node
  
  class LiteralChars(re_t):
    _type_tag = 14
    __slots__ = ('blame_tok', 's')
  
    def __init__(self, blame_tok, s):
      # type: (Token, str) -> None
      self.blame_tok = blame_tok
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> re.LiteralChars
      return re.LiteralChars(cast('Token', None), '')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('re.LiteralChars')
      L = out_node.fields
  
      assert self.blame_tok is not None
      x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('blame_tok', x0))
  
      x1 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x1))
  
      return out_node
  
  pass

class BoolParamBox(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('b',)

  def __init__(self, b):
    # type: (bool) -> None
    self.b = b

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> BoolParamBox
    return BoolParamBox(False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('BoolParamBox')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.b else 'F', color_e.OtherConst)
    L.append(Field('b', x0))

    return out_node

class IntParamBox(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('i',)

  def __init__(self, i):
    # type: (int) -> None
    self.i = i

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> IntParamBox
    return IntParamBox(-1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('IntParamBox')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
    L.append(Field('i', x0))

    return out_node

class SourceLine(pybase.CompoundObj):
  _type_tag = 66
  __slots__ = ('line_num', 'content', 'src')

  def __init__(self, line_num, content, src):
    # type: (int, str, source_t) -> None
    self.line_num = line_num
    self.content = content
    self.src = src

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> SourceLine
    return SourceLine(-1, '', cast('source_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('SourceLine')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.line_num), color_e.OtherConst)
    L.append(Field('line_num', x0))

    x1 = NewLeaf(self.content, color_e.StringConst)
    L.append(Field('content', x1))

    assert self.src is not None
    x2 = self.src.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('src', x2))

    return out_node

class Token(loc_t, debug_frame_t, suffix_op_t, word_part_t, word_t,
            arith_expr_t, printf_part_t, y_lhs_t, re_repeat_t):
  _type_tag = 67
  __slots__ = ('id', 'length', 'col', 'line', 'tval')

  def __init__(self, id, length, col, line, tval):
    # type: (Id_t, int, int, Optional[SourceLine], Optional[str]) -> None
    self.id = id
    self.length = length
    self.col = col
    self.line = line
    self.tval = tval

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Token
    return Token(-1, -1, -1, cast('Optional[SourceLine]', None), cast('Optional[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    if do_abbrev:
      p = _Token(self)
      if p:
        return p

    out_node = NewRecord('Token')
    L = out_node.fields

    x0 = hnode.Leaf(Id_str(self.id, dot=False), color_e.UserType)
    L.append(Field('id', x0))

    x1 = hnode.Leaf(str(self.length), color_e.OtherConst)
    L.append(Field('length', x1))

    x2 = hnode.Leaf(str(self.col), color_e.OtherConst)
    L.append(Field('col', x2))

    if self.line is not None:  # Optional
      x3 = self.line.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('line', x3))

    if self.tval is not None:  # Optional
      x4 = NewLeaf(self.tval, color_e.StringConst)
      L.append(Field('tval', x4))

    return out_node

class CompoundWord(loc_t, debug_frame_t, rhs_word_t, word_t, arith_expr_t,
                   redir_param_t):
  _type_tag = 68
  __slots__ = ('parts',)

  def __init__(self, parts):
    # type: (List[word_part_t]) -> None
    self.parts = parts

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> CompoundWord
    return CompoundWord([] if alloc_lists else cast('List[word_part_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    if do_abbrev:
      p = _CompoundWord(self)
      if p:
        return p

    out_node = NewRecord('CompoundWord')
    L = out_node.fields

    if self.parts is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.parts:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('parts', x0))

    return out_node

class BracedVarSub(word_part_t, expr_t):
  _type_tag = 69
  __slots__ = ('left', 'name_tok', 'var_name', 'prefix_op', 'bracket_op',
               'suffix_op', 'right')

  def __init__(self, left, name_tok, var_name, prefix_op, bracket_op,
               suffix_op, right):
    # type: (Token, Token, str, Optional[Token], Optional[bracket_op_t], Optional[suffix_op_t], Token) -> None
    self.left = left
    self.name_tok = name_tok
    self.var_name = var_name
    self.prefix_op = prefix_op
    self.bracket_op = bracket_op
    self.suffix_op = suffix_op
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> BracedVarSub
    return BracedVarSub(cast('Token', None), cast('Token', None), '', cast('Optional[Token]', None), cast('Optional[bracket_op_t]', None), cast('Optional[suffix_op_t]', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    if do_abbrev:
      p = _BracedVarSub(self)
      if p:
        return p

    out_node = NewRecord('BracedVarSub')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    assert self.name_tok is not None
    x1 = self.name_tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('name_tok', x1))

    x2 = NewLeaf(self.var_name, color_e.StringConst)
    L.append(Field('var_name', x2))

    if self.prefix_op is not None:  # Optional
      x3 = self.prefix_op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('prefix_op', x3))

    if self.bracket_op is not None:  # Optional
      x4 = self.bracket_op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('bracket_op', x4))

    if self.suffix_op is not None:  # Optional
      x5 = self.suffix_op.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('suffix_op', x5))

    assert self.right is not None
    x6 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x6))

    return out_node

class DoubleQuoted(word_part_t, expr_t):
  _type_tag = 70
  __slots__ = ('left', 'parts', 'right')

  def __init__(self, left, parts, right):
    # type: (Token, List[word_part_t], Token) -> None
    self.left = left
    self.parts = parts
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> DoubleQuoted
    return DoubleQuoted(cast('Token', None), [] if alloc_lists else cast('List[word_part_t]', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    if do_abbrev:
      p = _DoubleQuoted(self)
      if p:
        return p

    out_node = NewRecord('DoubleQuoted')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    if self.parts is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.parts:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('parts', x1))

    assert self.right is not None
    x2 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x2))

    return out_node

class SingleQuoted(word_part_t, expr_t, class_literal_term_t, re_t):
  _type_tag = 71
  __slots__ = ('left', 'sval', 'right')

  def __init__(self, left, sval, right):
    # type: (Token, str, Token) -> None
    self.left = left
    self.sval = sval
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> SingleQuoted
    return SingleQuoted(cast('Token', None), '', cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    if do_abbrev:
      p = _SingleQuoted(self)
      if p:
        return p

    out_node = NewRecord('SingleQuoted')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    x1 = NewLeaf(self.sval, color_e.StringConst)
    L.append(Field('sval', x1))

    assert self.right is not None
    x2 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x2))

    return out_node

class SimpleVarSub(word_part_t, expr_t):
  _type_tag = 72
  __slots__ = ('tok',)

  def __init__(self, tok):
    # type: (Token) -> None
    self.tok = tok

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> SimpleVarSub
    return SimpleVarSub(cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    if do_abbrev:
      p = _SimpleVarSub(self)
      if p:
        return p

    out_node = NewRecord('SimpleVarSub')
    L = out_node.fields

    assert self.tok is not None
    x0 = self.tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('tok', x0))

    return out_node

class CommandSub(word_part_t, expr_t):
  _type_tag = 73
  __slots__ = ('left_token', 'child', 'right')

  def __init__(self, left_token, child, right):
    # type: (Token, command_t, Token) -> None
    self.left_token = left_token
    self.child = child
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> CommandSub
    return CommandSub(cast('Token', None), cast('command_t', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('CommandSub')
    L = out_node.fields

    assert self.left_token is not None
    x0 = self.left_token.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left_token', x0))

    assert self.child is not None
    x1 = self.child.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('child', x1))

    assert self.right is not None
    x2 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x2))

    return out_node

class ExprSub(word_part_t, expr_t):
  _type_tag = 74
  __slots__ = ('left', 'child', 'right')

  def __init__(self, left, child, right):
    # type: (Token, expr_t, Token) -> None
    self.left = left
    self.child = child
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ExprSub
    return ExprSub(cast('Token', None), cast('expr_t', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ExprSub')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    assert self.child is not None
    x1 = self.child.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('child', x1))

    assert self.right is not None
    x2 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x2))

    return out_node

class YshArrayLiteral(word_part_t, expr_t):
  _type_tag = 75
  __slots__ = ('left', 'words', 'right')

  def __init__(self, left, words, right):
    # type: (Token, List[word_t], Token) -> None
    self.left = left
    self.words = words
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> YshArrayLiteral
    return YshArrayLiteral(cast('Token', None), [] if alloc_lists else cast('List[word_t]', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('YshArrayLiteral')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    if self.words is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.words:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('words', x1))

    assert self.right is not None
    x2 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x2))

    return out_node

class ArgList(pybase.CompoundObj):
  _type_tag = 76
  __slots__ = ('left', 'pos_args', 'semi_tok', 'named_args', 'semi_tok2',
               'block_expr', 'right')

  def __init__(self, left, pos_args, semi_tok, named_args, semi_tok2,
               block_expr, right):
    # type: (Token, List[expr_t], Optional[Token], List[NamedArg], Optional[Token], Optional[expr_t], Token) -> None
    self.left = left
    self.pos_args = pos_args
    self.semi_tok = semi_tok
    self.named_args = named_args
    self.semi_tok2 = semi_tok2
    self.block_expr = block_expr
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ArgList
    return ArgList(cast('Token', None), [] if alloc_lists else cast('List[expr_t]', None), cast('Optional[Token]', None), [] if alloc_lists else cast('List[NamedArg]', None), cast('Optional[Token]', None), cast('Optional[expr_t]', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ArgList')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    if self.pos_args is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.pos_args:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('pos_args', x1))

    if self.semi_tok is not None:  # Optional
      x2 = self.semi_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('semi_tok', x2))

    if self.named_args is not None:  # List
      x3 = hnode.Array([])
      for i3 in self.named_args:
        h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
             i3.PrettyTree(do_abbrev, trav=trav))
        x3.children.append(h)
      L.append(Field('named_args', x3))

    if self.semi_tok2 is not None:  # Optional
      x4 = self.semi_tok2.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('semi_tok2', x4))

    if self.block_expr is not None:  # Optional
      x5 = self.block_expr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('block_expr', x5))

    assert self.right is not None
    x6 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x6))

    return out_node

class AssocPair(InitializerWord_t):
  _type_tag = 77
  __slots__ = ('key', 'value', 'has_plus')

  def __init__(self, key, value, has_plus):
    # type: (CompoundWord, CompoundWord, bool) -> None
    self.key = key
    self.value = value
    self.has_plus = has_plus

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> AssocPair
    return AssocPair(cast('CompoundWord', None), cast('CompoundWord', None), False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('AssocPair')
    L = out_node.fields

    assert self.key is not None
    x0 = self.key.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('key', x0))

    assert self.value is not None
    x1 = self.value.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('value', x1))

    x2 = hnode.Leaf('T' if self.has_plus else 'F', color_e.OtherConst)
    L.append(Field('has_plus', x2))

    return out_node

class Redir(pybase.CompoundObj):
  _type_tag = 78
  __slots__ = ('op', 'loc', 'arg')

  def __init__(self, op, loc, arg):
    # type: (Token, redir_loc_t, redir_param_t) -> None
    self.op = op
    self.loc = loc
    self.arg = arg

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Redir
    return Redir(cast('Token', None), cast('redir_loc_t', None), cast('redir_param_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Redir')
    L = out_node.fields

    assert self.op is not None
    x0 = self.op.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('op', x0))

    assert self.loc is not None
    x1 = self.loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('loc', x1))

    assert self.arg is not None
    x2 = self.arg.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('arg', x2))

    return out_node

class AssignPair(pybase.CompoundObj):
  _type_tag = 79
  __slots__ = ('left', 'lhs', 'op', 'rhs')

  def __init__(self, left, lhs, op, rhs):
    # type: (Token, sh_lhs_t, assign_op_t, rhs_word_t) -> None
    self.left = left
    self.lhs = lhs
    self.op = op
    self.rhs = rhs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> AssignPair
    return AssignPair(cast('Token', None), cast('sh_lhs_t', None), assign_op_e.Equal, cast('rhs_word_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('AssignPair')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    assert self.lhs is not None
    x1 = self.lhs.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('lhs', x1))

    x2 = hnode.Leaf(assign_op_str(self.op), color_e.TypeName)
    L.append(Field('op', x2))

    assert self.rhs is not None
    x3 = self.rhs.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('rhs', x3))

    return out_node

class EnvPair(pybase.CompoundObj):
  _type_tag = 80
  __slots__ = ('left', 'name', 'val')

  def __init__(self, left, name, val):
    # type: (Token, str, rhs_word_t) -> None
    self.left = left
    self.name = name
    self.val = val

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> EnvPair
    return EnvPair(cast('Token', None), '', cast('rhs_word_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('EnvPair')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    assert self.val is not None
    x2 = self.val.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('val', x2))

    return out_node

class CaseArm(pybase.CompoundObj):
  _type_tag = 82
  __slots__ = ('left', 'pattern', 'middle', 'action', 'right')

  def __init__(self, left, pattern, middle, action, right):
    # type: (Token, pat_t, Token, List[command_t], Optional[Token]) -> None
    self.left = left
    self.pattern = pattern
    self.middle = middle
    self.action = action
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> CaseArm
    return CaseArm(cast('Token', None), cast('pat_t', None), cast('Token', None), [] if alloc_lists else cast('List[command_t]', None), cast('Optional[Token]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('CaseArm')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    assert self.pattern is not None
    x1 = self.pattern.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('pattern', x1))

    assert self.middle is not None
    x2 = self.middle.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('middle', x2))

    if self.action is not None:  # List
      x3 = hnode.Array([])
      for i3 in self.action:
        h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
             i3.PrettyTree(do_abbrev, trav=trav))
        x3.children.append(h)
      L.append(Field('action', x3))

    if self.right is not None:  # Optional
      x4 = self.right.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('right', x4))

    return out_node

class EggexFlag(pybase.CompoundObj):
  _type_tag = 83
  __slots__ = ('negated', 'flag')

  def __init__(self, negated, flag):
    # type: (bool, Token) -> None
    self.negated = negated
    self.flag = flag

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> EggexFlag
    return EggexFlag(False, cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('EggexFlag')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.negated else 'F', color_e.OtherConst)
    L.append(Field('negated', x0))

    assert self.flag is not None
    x1 = self.flag.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('flag', x1))

    return out_node

class Eggex(pat_t, expr_t):
  _type_tag = 84
  __slots__ = ('left', 'regex', 'flags', 'trans_pref', 'canonical_flags')

  def __init__(self, left, regex, flags, trans_pref, canonical_flags):
    # type: (Token, re_t, List[EggexFlag], Optional[Token], Optional[str]) -> None
    self.left = left
    self.regex = regex
    self.flags = flags
    self.trans_pref = trans_pref
    self.canonical_flags = canonical_flags

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Eggex
    return Eggex(cast('Token', None), cast('re_t', None), [] if alloc_lists else cast('List[EggexFlag]', None), cast('Optional[Token]', None), cast('Optional[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Eggex')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    assert self.regex is not None
    x1 = self.regex.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('regex', x1))

    if self.flags is not None:  # List
      x2 = hnode.Array([])
      for i2 in self.flags:
        h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
             i2.PrettyTree(do_abbrev, trav=trav))
        x2.children.append(h)
      L.append(Field('flags', x2))

    if self.trans_pref is not None:  # Optional
      x3 = self.trans_pref.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('trans_pref', x3))

    if self.canonical_flags is not None:  # Optional
      x4 = NewLeaf(self.canonical_flags, color_e.StringConst)
      L.append(Field('canonical_flags', x4))

    return out_node

class IfArm(pybase.CompoundObj):
  _type_tag = 85
  __slots__ = ('keyword', 'cond', 'then_kw', 'action', 'then_tok')

  def __init__(self, keyword, cond, then_kw, action, then_tok):
    # type: (Token, condition_t, Optional[Token], List[command_t], Optional[Token]) -> None
    self.keyword = keyword
    self.cond = cond
    self.then_kw = then_kw
    self.action = action
    self.then_tok = then_tok

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> IfArm
    return IfArm(cast('Token', None), cast('condition_t', None), cast('Optional[Token]', None), [] if alloc_lists else cast('List[command_t]', None), cast('Optional[Token]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('IfArm')
    L = out_node.fields

    assert self.keyword is not None
    x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('keyword', x0))

    assert self.cond is not None
    x1 = self.cond.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('cond', x1))

    if self.then_kw is not None:  # Optional
      x2 = self.then_kw.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('then_kw', x2))

    if self.action is not None:  # List
      x3 = hnode.Array([])
      for i3 in self.action:
        h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
             i3.PrettyTree(do_abbrev, trav=trav))
        x3.children.append(h)
      L.append(Field('action', x3))

    if self.then_tok is not None:  # Optional
      x4 = self.then_tok.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('then_tok', x4))

    return out_node

class BraceGroup(command_t):
  _type_tag = 86
  __slots__ = ('left', 'doc_token', 'children', 'right')

  def __init__(self, left, doc_token, children, right):
    # type: (Token, Optional[Token], List[command_t], Token) -> None
    self.left = left
    self.doc_token = doc_token
    self.children = children
    self.right = right

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> BraceGroup
    return BraceGroup(cast('Token', None), cast('Optional[Token]', None), [] if alloc_lists else cast('List[command_t]', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('BraceGroup')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    if self.doc_token is not None:  # Optional
      x1 = self.doc_token.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('doc_token', x1))

    if self.children is not None:  # List
      x2 = hnode.Array([])
      for i2 in self.children:
        h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
             i2.PrettyTree(do_abbrev, trav=trav))
        x2.children.append(h)
      L.append(Field('children', x2))

    assert self.right is not None
    x3 = self.right.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('right', x3))

    return out_node

class Param(pybase.CompoundObj):
  _type_tag = 87
  __slots__ = ('blame_tok', 'name', 'type', 'default_val')

  def __init__(self, blame_tok, name, type, default_val):
    # type: (Token, str, Optional[TypeExpr], Optional[expr_t]) -> None
    self.blame_tok = blame_tok
    self.name = name
    self.type = type
    self.default_val = default_val

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Param
    return Param(cast('Token', None), '', cast('Optional[TypeExpr]', None), cast('Optional[expr_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Param')
    L = out_node.fields

    assert self.blame_tok is not None
    x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('blame_tok', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    if self.type is not None:  # Optional
      x2 = self.type.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('type', x2))

    if self.default_val is not None:  # Optional
      x3 = self.default_val.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('default_val', x3))

    return out_node

class RestParam(pybase.CompoundObj):
  _type_tag = 88
  __slots__ = ('blame_tok', 'name')

  def __init__(self, blame_tok, name):
    # type: (Token, str) -> None
    self.blame_tok = blame_tok
    self.name = name

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> RestParam
    return RestParam(cast('Token', None), '')

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('RestParam')
    L = out_node.fields

    assert self.blame_tok is not None
    x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('blame_tok', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    return out_node

class ParamGroup(pybase.CompoundObj):
  _type_tag = 89
  __slots__ = ('params', 'rest_of')

  def __init__(self, params, rest_of):
    # type: (List[Param], Optional[RestParam]) -> None
    self.params = params
    self.rest_of = rest_of

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ParamGroup
    return ParamGroup([] if alloc_lists else cast('List[Param]', None), cast('Optional[RestParam]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ParamGroup')
    L = out_node.fields

    if self.params is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.params:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('params', x0))

    if self.rest_of is not None:  # Optional
      x1 = self.rest_of.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('rest_of', x1))

    return out_node

class Proc(command_t):
  _type_tag = 90
  __slots__ = ('keyword', 'name', 'sig', 'body')

  def __init__(self, keyword, name, sig, body):
    # type: (Token, Token, proc_sig_t, command_t) -> None
    self.keyword = keyword
    self.name = name
    self.sig = sig
    self.body = body

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Proc
    return Proc(cast('Token', None), cast('Token', None), cast('proc_sig_t', None), cast('command_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Proc')
    L = out_node.fields

    assert self.keyword is not None
    x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('keyword', x0))

    assert self.name is not None
    x1 = self.name.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('name', x1))

    assert self.sig is not None
    x2 = self.sig.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('sig', x2))

    assert self.body is not None
    x3 = self.body.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('body', x3))

    return out_node

class Func(command_t):
  _type_tag = 91
  __slots__ = ('keyword', 'name', 'positional', 'named', 'body')

  def __init__(self, keyword, name, positional, named, body):
    # type: (Token, Token, Optional[ParamGroup], Optional[ParamGroup], command_t) -> None
    self.keyword = keyword
    self.name = name
    self.positional = positional
    self.named = named
    self.body = body

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Func
    return Func(cast('Token', None), cast('Token', None), cast('Optional[ParamGroup]', None), cast('Optional[ParamGroup]', None), cast('command_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Func')
    L = out_node.fields

    assert self.keyword is not None
    x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('keyword', x0))

    assert self.name is not None
    x1 = self.name.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('name', x1))

    if self.positional is not None:  # Optional
      x2 = self.positional.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('positional', x2))

    if self.named is not None:  # Optional
      x3 = self.named.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('named', x3))

    assert self.body is not None
    x4 = self.body.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('body', x4))

    return out_node

class ParsedAssignment(pybase.CompoundObj):
  _type_tag = 92
  __slots__ = ('left', 'close', 'part_offset', 'w')

  def __init__(self, left, close, part_offset, w):
    # type: (Optional[Token], Optional[Token], int, CompoundWord) -> None
    self.left = left
    self.close = close
    self.part_offset = part_offset
    self.w = w

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ParsedAssignment
    return ParsedAssignment(cast('Optional[Token]', None), cast('Optional[Token]', None), -1, cast('CompoundWord', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ParsedAssignment')
    L = out_node.fields

    if self.left is not None:  # Optional
      x0 = self.left.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('left', x0))

    if self.close is not None:  # Optional
      x1 = self.close.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('close', x1))

    x2 = hnode.Leaf(str(self.part_offset), color_e.OtherConst)
    L.append(Field('part_offset', x2))

    assert self.w is not None
    x3 = self.w.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('w', x3))

    return out_node

class VarDecl(command_t, b_command_t):
  _type_tag = 93
  __slots__ = ('keyword', 'lhs', 'rhs')

  def __init__(self, keyword, lhs, rhs):
    # type: (Optional[Token], List[NameType], Optional[expr_t]) -> None
    self.keyword = keyword
    self.lhs = lhs
    self.rhs = rhs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> VarDecl
    return VarDecl(cast('Optional[Token]', None), [] if alloc_lists else cast('List[NameType]', None), cast('Optional[expr_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('VarDecl')
    L = out_node.fields

    if self.keyword is not None:  # Optional
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))

    if self.lhs is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.lhs:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('lhs', x1))

    if self.rhs is not None:  # Optional
      x2 = self.rhs.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('rhs', x2))

    return out_node

class Mutation(command_t, b_command_t):
  _type_tag = 94
  __slots__ = ('keyword', 'lhs', 'op', 'rhs')

  def __init__(self, keyword, lhs, op, rhs):
    # type: (Token, List[y_lhs_t], Token, expr_t) -> None
    self.keyword = keyword
    self.lhs = lhs
    self.op = op
    self.rhs = rhs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Mutation
    return Mutation(cast('Token', None), [] if alloc_lists else cast('List[y_lhs_t]', None), cast('Token', None), cast('expr_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Mutation')
    L = out_node.fields

    assert self.keyword is not None
    x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('keyword', x0))

    if self.lhs is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.lhs:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('lhs', x1))

    assert self.op is not None
    x2 = self.op.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('op', x2))

    assert self.rhs is not None
    x3 = self.rhs.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('rhs', x3))

    return out_node

class ExprCommand(command_t):
  _type_tag = 95
  __slots__ = ('keyword', 'e')

  def __init__(self, keyword, e):
    # type: (Token, expr_t) -> None
    self.keyword = keyword
    self.e = e

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ExprCommand
    return ExprCommand(cast('Token', None), cast('expr_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ExprCommand')
    L = out_node.fields

    assert self.keyword is not None
    x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('keyword', x0))

    assert self.e is not None
    x1 = self.e.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('e', x1))

    return out_node

class ShFunction(command_t):
  _type_tag = 96
  __slots__ = ('keyword', 'name_tok', 'name', 'body', 'code_str')

  def __init__(self, keyword, name_tok, name, body, code_str):
    # type: (Optional[Token], Token, str, command_t, Optional[str]) -> None
    self.keyword = keyword
    self.name_tok = name_tok
    self.name = name
    self.body = body
    self.code_str = code_str

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ShFunction
    return ShFunction(cast('Optional[Token]', None), cast('Token', None), '', cast('command_t', None), cast('Optional[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ShFunction')
    L = out_node.fields

    if self.keyword is not None:  # Optional
      x0 = self.keyword.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('keyword', x0))

    assert self.name_tok is not None
    x1 = self.name_tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('name_tok', x1))

    x2 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x2))

    assert self.body is not None
    x3 = self.body.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('body', x3))

    if self.code_str is not None:  # Optional
      x4 = NewLeaf(self.code_str, color_e.StringConst)
      L.append(Field('code_str', x4))

    return out_node

class LiteralBlock(cmd_frag_t):
  _type_tag = 97
  __slots__ = ('brace_group', 'code_str')

  def __init__(self, brace_group, code_str):
    # type: (BraceGroup, Optional[str]) -> None
    self.brace_group = brace_group
    self.code_str = code_str

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> LiteralBlock
    return LiteralBlock(cast('BraceGroup', None), cast('Optional[str]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('LiteralBlock')
    L = out_node.fields

    assert self.brace_group is not None
    x0 = self.brace_group.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('brace_group', x0))

    if self.code_str is not None:  # Optional
      x1 = NewLeaf(self.code_str, color_e.StringConst)
      L.append(Field('code_str', x1))

    return out_node

class TypeExpr(pybase.CompoundObj):
  _type_tag = 98
  __slots__ = ('tok', 'name', 'params')

  def __init__(self, tok, name, params):
    # type: (Token, str, List[TypeExpr]) -> None
    self.tok = tok
    self.name = name
    self.params = params

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> TypeExpr
    return TypeExpr(cast('Token', None), '', [] if alloc_lists else cast('List[TypeExpr]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('TypeExpr')
    L = out_node.fields

    assert self.tok is not None
    x0 = self.tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('tok', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    if self.params is not None:  # List
      x2 = hnode.Array([])
      for i2 in self.params:
        h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
             i2.PrettyTree(do_abbrev, trav=trav))
        x2.children.append(h)
      L.append(Field('params', x2))

    return out_node

class NameType(pybase.CompoundObj):
  _type_tag = 99
  __slots__ = ('left', 'name', 'typ')

  def __init__(self, left, name, typ):
    # type: (Token, str, Optional[TypeExpr]) -> None
    self.left = left
    self.name = name
    self.typ = typ

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> NameType
    return NameType(cast('Token', None), '', cast('Optional[TypeExpr]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('NameType')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    if self.typ is not None:  # Optional
      x2 = self.typ.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('typ', x2))

    return out_node

class Comprehension(pybase.CompoundObj):
  _type_tag = 100
  __slots__ = ('lhs', 'iter', 'cond')

  def __init__(self, lhs, iter, cond):
    # type: (List[NameType], expr_t, Optional[expr_t]) -> None
    self.lhs = lhs
    self.iter = iter
    self.cond = cond

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Comprehension
    return Comprehension([] if alloc_lists else cast('List[NameType]', None), cast('expr_t', None), cast('Optional[expr_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Comprehension')
    L = out_node.fields

    if self.lhs is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.lhs:
        h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
             i0.PrettyTree(do_abbrev, trav=trav))
        x0.children.append(h)
      L.append(Field('lhs', x0))

    assert self.iter is not None
    x1 = self.iter.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('iter', x1))

    if self.cond is not None:  # Optional
      x2 = self.cond.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('cond', x2))

    return out_node

class NamedArg(pybase.CompoundObj):
  _type_tag = 101
  __slots__ = ('name', 'value')

  def __init__(self, name, value):
    # type: (Optional[Token], expr_t) -> None
    self.name = name
    self.value = value

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> NamedArg
    return NamedArg(cast('Optional[Token]', None), cast('expr_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('NamedArg')
    L = out_node.fields

    if self.name is not None:  # Optional
      x0 = self.name.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('name', x0))

    assert self.value is not None
    x1 = self.value.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('value', x1))

    return out_node

class Subscript(y_lhs_t, expr_t):
  _type_tag = 102
  __slots__ = ('left', 'obj', 'index')

  def __init__(self, left, obj, index):
    # type: (Token, expr_t, expr_t) -> None
    self.left = left
    self.obj = obj
    self.index = index

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Subscript
    return Subscript(cast('Token', None), cast('expr_t', None), cast('expr_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Subscript')
    L = out_node.fields

    assert self.left is not None
    x0 = self.left.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('left', x0))

    assert self.obj is not None
    x1 = self.obj.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('obj', x1))

    assert self.index is not None
    x2 = self.index.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('index', x2))

    return out_node

class Attribute(y_lhs_t, expr_t):
  _type_tag = 103
  __slots__ = ('obj', 'op', 'attr', 'attr_name', 'ctx')

  def __init__(self, obj, op, attr, attr_name, ctx):
    # type: (expr_t, Token, Token, str, expr_context_t) -> None
    self.obj = obj
    self.op = op
    self.attr = attr
    self.attr_name = attr_name
    self.ctx = ctx

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Attribute
    return Attribute(cast('expr_t', None), cast('Token', None), cast('Token', None), '', expr_context_e.Load)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Attribute')
    L = out_node.fields

    assert self.obj is not None
    x0 = self.obj.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('obj', x0))

    assert self.op is not None
    x1 = self.op.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('op', x1))

    assert self.attr is not None
    x2 = self.attr.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('attr', x2))

    x3 = NewLeaf(self.attr_name, color_e.StringConst)
    L.append(Field('attr_name', x3))

    x4 = hnode.Leaf(expr_context_str(self.ctx), color_e.TypeName)
    L.append(Field('ctx', x4))

    return out_node

class PosixClass(class_literal_term_t, char_class_term_t, re_t):
  _type_tag = 104
  __slots__ = ('negated', 'name')

  def __init__(self, negated, name):
    # type: (Optional[Token], str) -> None
    self.negated = negated
    self.name = name

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> PosixClass
    return PosixClass(cast('Optional[Token]', None), '')

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('PosixClass')
    L = out_node.fields

    if self.negated is not None:  # Optional
      x0 = self.negated.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('negated', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    return out_node

class PerlClass(class_literal_term_t, char_class_term_t, re_t):
  _type_tag = 105
  __slots__ = ('negated', 'name')

  def __init__(self, negated, name):
    # type: (Optional[Token], str) -> None
    self.negated = negated
    self.name = name

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> PerlClass
    return PerlClass(cast('Optional[Token]', None), '')

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('PerlClass')
    L = out_node.fields

    if self.negated is not None:  # Optional
      x0 = self.negated.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('negated', x0))

    x1 = NewLeaf(self.name, color_e.StringConst)
    L.append(Field('name', x1))

    return out_node

class CharCode(class_literal_term_t, char_class_term_t):
  _type_tag = 106
  __slots__ = ('blame_tok', 'i', 'u_braced')

  def __init__(self, blame_tok, i, u_braced):
    # type: (Token, int, bool) -> None
    self.blame_tok = blame_tok
    self.i = i
    self.u_braced = u_braced

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> CharCode
    return CharCode(cast('Token', None), -1, False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('CharCode')
    L = out_node.fields

    assert self.blame_tok is not None
    x0 = self.blame_tok.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('blame_tok', x0))

    x1 = hnode.Leaf(str(self.i), color_e.OtherConst)
    L.append(Field('i', x1))

    x2 = hnode.Leaf('T' if self.u_braced else 'F', color_e.OtherConst)
    L.append(Field('u_braced', x2))

    return out_node

class CharRange(class_literal_term_t, char_class_term_t):
  _type_tag = 107
  __slots__ = ('start', 'end')

  def __init__(self, start, end):
    # type: (CharCode, CharCode) -> None
    self.start = start
    self.end = end

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> CharRange
    return CharRange(cast('CharCode', None), cast('CharCode', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('CharRange')
    L = out_node.fields

    assert self.start is not None
    x0 = self.start.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('start', x0))

    assert self.end is not None
    x1 = self.end.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('end', x1))

    return out_node

class List_of_command(condition_t, List[command_t]):
  _type_tag = 81
  @staticmethod
  def New():
    # type: () -> List_of_command
    return List_of_command()

  @staticmethod
  def Take(plain_list):
    # type: (List[command_t]) -> List_of_command
    result = List_of_command(plain_list)
    del plain_list[:]
    return result

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True
    h = runtime.NewRecord('List_of_command')
    h.unnamed_fields = [c.PrettyTree(do_abbrev) for c in self]
    return h

