from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class expr_e(object):
  Concatenation = 1
  Disjunction = 2
  Conjunction = 3
  Negation = 4
  True_ = 5
  False_ = 6
  PathTest = 7
  StatTest = 8
  DeleteAction = 9
  PruneAction = 10
  QuitAction = 11
  PrintAction = 12
  LsAction = 13
  ExecAction = 14

_expr_str = {
  1: 'Concatenation',
  2: 'Disjunction',
  3: 'Conjunction',
  4: 'Negation',
  5: 'True_',
  6: 'False_',
  7: 'PathTest',
  8: 'StatTest',
  9: 'DeleteAction',
  10: 'PruneAction',
  11: 'QuitAction',
  12: 'PrintAction',
  13: 'LsAction',
  14: 'ExecAction',
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

class expr__True_(expr_t):
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

    out_node = NewRecord('expr.True_')
    L = out_node.fields

    return out_node

class expr__False_(expr_t):
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

    out_node = NewRecord('expr.False_')
    L = out_node.fields

    return out_node

class expr__DeleteAction(expr_t):
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

    out_node = NewRecord('expr.DeleteAction')
    L = out_node.fields

    return out_node

class expr__PruneAction(expr_t):
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

    out_node = NewRecord('expr.PruneAction')
    L = out_node.fields

    return out_node

class expr__QuitAction(expr_t):
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

    out_node = NewRecord('expr.QuitAction')
    L = out_node.fields

    return out_node

class expr(object):
  class Concatenation(expr_t):
    _type_tag = 1
    __slots__ = ('exprs',)
  
    def __init__(self, exprs):
      # type: (List[expr_t]) -> None
      self.exprs = exprs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Concatenation
      return expr.Concatenation([] if alloc_lists else cast('List[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Concatenation')
      L = out_node.fields
  
      if self.exprs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.exprs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('exprs', x0))
  
      return out_node
  
  class Disjunction(expr_t):
    _type_tag = 2
    __slots__ = ('exprs',)
  
    def __init__(self, exprs):
      # type: (List[expr_t]) -> None
      self.exprs = exprs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Disjunction
      return expr.Disjunction([] if alloc_lists else cast('List[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Disjunction')
      L = out_node.fields
  
      if self.exprs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.exprs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('exprs', x0))
  
      return out_node
  
  class Conjunction(expr_t):
    _type_tag = 3
    __slots__ = ('exprs',)
  
    def __init__(self, exprs):
      # type: (List[expr_t]) -> None
      self.exprs = exprs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Conjunction
      return expr.Conjunction([] if alloc_lists else cast('List[expr_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Conjunction')
      L = out_node.fields
  
      if self.exprs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.exprs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('exprs', x0))
  
      return out_node
  
  class Negation(expr_t):
    _type_tag = 4
    __slots__ = ('expr',)
  
    def __init__(self, expr):
      # type: (expr_t) -> None
      self.expr = expr
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.Negation
      return expr.Negation(cast('expr_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.Negation')
      L = out_node.fields
  
      assert self.expr is not None
      x0 = self.expr.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('expr', x0))
  
      return out_node
  
  True_ = expr__True_()
  
  False_ = expr__False_()
  
  class PathTest(expr_t):
    _type_tag = 7
    __slots__ = ('a', 'p')
  
    def __init__(self, a, p):
      # type: (pathAccessor_t, predicate_t) -> None
      self.a = a
      self.p = p
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.PathTest
      return expr.PathTest(pathAccessor_e.FullPath, cast('predicate_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.PathTest')
      L = out_node.fields
  
      x0 = hnode.Leaf(pathAccessor_str(self.a), color_e.TypeName)
      L.append(Field('a', x0))
  
      assert self.p is not None
      x1 = self.p.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('p', x1))
  
      return out_node
  
  class StatTest(expr_t):
    _type_tag = 8
    __slots__ = ('a', 'p')
  
    def __init__(self, a, p):
      # type: (statAccessor_t, predicate_t) -> None
      self.a = a
      self.p = p
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.StatTest
      return expr.StatTest(statAccessor_e.AccessTime, cast('predicate_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.StatTest')
      L = out_node.fields
  
      x0 = hnode.Leaf(statAccessor_str(self.a), color_e.TypeName)
      L.append(Field('a', x0))
  
      assert self.p is not None
      x1 = self.p.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('p', x1))
  
      return out_node
  
  DeleteAction = expr__DeleteAction()
  
  PruneAction = expr__PruneAction()
  
  QuitAction = expr__QuitAction()
  
  class PrintAction(expr_t):
    _type_tag = 12
    __slots__ = ('file', 'format')
  
    def __init__(self, file, format):
      # type: (Optional[str], Optional[str]) -> None
      self.file = file
      self.format = format
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.PrintAction
      return expr.PrintAction(cast('Optional[str]', None), cast('Optional[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.PrintAction')
      L = out_node.fields
  
      if self.file is not None:  # Optional
        x0 = NewLeaf(self.file, color_e.StringConst)
        L.append(Field('file', x0))
  
      if self.format is not None:  # Optional
        x1 = NewLeaf(self.format, color_e.StringConst)
        L.append(Field('format', x1))
  
      return out_node
  
  class LsAction(expr_t):
    _type_tag = 13
    __slots__ = ('file',)
  
    def __init__(self, file):
      # type: (Optional[str]) -> None
      self.file = file
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.LsAction
      return expr.LsAction(cast('Optional[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.LsAction')
      L = out_node.fields
  
      if self.file is not None:  # Optional
        x0 = NewLeaf(self.file, color_e.StringConst)
        L.append(Field('file', x0))
  
      return out_node
  
  class ExecAction(expr_t):
    _type_tag = 14
    __slots__ = ('batch', 'dir', 'ok', 'argv')
  
    def __init__(self, batch, dir, ok, argv):
      # type: (bool, bool, bool, List[str]) -> None
      self.batch = batch
      self.dir = dir
      self.ok = ok
      self.argv = argv
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> expr.ExecAction
      return expr.ExecAction(False, False, False, [] if alloc_lists else cast('List[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('expr.ExecAction')
      L = out_node.fields
  
      x0 = hnode.Leaf('T' if self.batch else 'F', color_e.OtherConst)
      L.append(Field('batch', x0))
  
      x1 = hnode.Leaf('T' if self.dir else 'F', color_e.OtherConst)
      L.append(Field('dir', x1))
  
      x2 = hnode.Leaf('T' if self.ok else 'F', color_e.OtherConst)
      L.append(Field('ok', x2))
  
      if self.argv is not None:  # List
        x3 = hnode.Array([])
        for i3 in self.argv:
          x3.children.append(NewLeaf(i3, color_e.StringConst))
        L.append(Field('argv', x3))
  
      return out_node
  
  pass

class pathAccessor_t(pybase.SimpleObj):
  pass

class pathAccessor_e(object):
  FullPath = pathAccessor_t(1)
  Filename = pathAccessor_t(2)

_pathAccessor_str = {
  1: 'FullPath',
  2: 'Filename',
}

def pathAccessor_str(val, dot=True):
  # type: (pathAccessor_t, bool) -> str
  v = _pathAccessor_str[val]
  if dot:
    return "pathAccessor.%s" % v
  else:
    return v

class statAccessor_t(pybase.SimpleObj):
  pass

class statAccessor_e(object):
  AccessTime = statAccessor_t(1)
  CreationTime = statAccessor_t(2)
  ModificationTime = statAccessor_t(3)
  Filesystem = statAccessor_t(4)
  Inode = statAccessor_t(5)
  LinkCount = statAccessor_t(6)
  Mode = statAccessor_t(7)
  Filetype = statAccessor_t(8)
  Uid = statAccessor_t(9)
  Gid = statAccessor_t(10)
  Username = statAccessor_t(11)
  Groupname = statAccessor_t(12)
  Size = statAccessor_t(13)

_statAccessor_str = {
  1: 'AccessTime',
  2: 'CreationTime',
  3: 'ModificationTime',
  4: 'Filesystem',
  5: 'Inode',
  6: 'LinkCount',
  7: 'Mode',
  8: 'Filetype',
  9: 'Uid',
  10: 'Gid',
  11: 'Username',
  12: 'Groupname',
  13: 'Size',
}

def statAccessor_str(val, dot=True):
  # type: (statAccessor_t, bool) -> str
  v = _statAccessor_str[val]
  if dot:
    return "statAccessor.%s" % v
  else:
    return v

class predicate_e(object):
  EQ = 1
  GE = 2
  LE = 3
  StringMatch = 4
  GlobMatch = 5
  RegexMatch = 6
  Readable = 7
  Writable = 8
  Executable = 9

_predicate_str = {
  1: 'EQ',
  2: 'GE',
  3: 'LE',
  4: 'StringMatch',
  5: 'GlobMatch',
  6: 'RegexMatch',
  7: 'Readable',
  8: 'Writable',
  9: 'Executable',
}

def predicate_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _predicate_str[tag]
  if dot:
    return "predicate.%s" % v
  else:
    return v

class predicate_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class predicate__Readable(predicate_t):
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

    out_node = NewRecord('predicate.Readable')
    L = out_node.fields

    return out_node

class predicate__Writable(predicate_t):
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

    out_node = NewRecord('predicate.Writable')
    L = out_node.fields

    return out_node

class predicate__Executable(predicate_t):
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

    out_node = NewRecord('predicate.Executable')
    L = out_node.fields

    return out_node

class predicate(object):
  class EQ(predicate_t):
    _type_tag = 1
    __slots__ = ('n',)
  
    def __init__(self, n):
      # type: (int) -> None
      self.n = n
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> predicate.EQ
      return predicate.EQ(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('predicate.EQ')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.n), color_e.OtherConst)
      L.append(Field('n', x0))
  
      return out_node
  
  class GE(predicate_t):
    _type_tag = 2
    __slots__ = ('n',)
  
    def __init__(self, n):
      # type: (int) -> None
      self.n = n
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> predicate.GE
      return predicate.GE(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('predicate.GE')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.n), color_e.OtherConst)
      L.append(Field('n', x0))
  
      return out_node
  
  class LE(predicate_t):
    _type_tag = 3
    __slots__ = ('n',)
  
    def __init__(self, n):
      # type: (int) -> None
      self.n = n
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> predicate.LE
      return predicate.LE(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('predicate.LE')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.n), color_e.OtherConst)
      L.append(Field('n', x0))
  
      return out_node
  
  class StringMatch(predicate_t):
    _type_tag = 4
    __slots__ = ('str', 'ignoreCase')
  
    def __init__(self, str, ignoreCase):
      # type: (str, bool) -> None
      self.str = str
      self.ignoreCase = ignoreCase
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> predicate.StringMatch
      return predicate.StringMatch('', False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('predicate.StringMatch')
      L = out_node.fields
  
      x0 = NewLeaf(self.str, color_e.StringConst)
      L.append(Field('str', x0))
  
      x1 = hnode.Leaf('T' if self.ignoreCase else 'F', color_e.OtherConst)
      L.append(Field('ignoreCase', x1))
  
      return out_node
  
  class GlobMatch(predicate_t):
    _type_tag = 5
    __slots__ = ('glob', 'ignoreCase')
  
    def __init__(self, glob, ignoreCase):
      # type: (str, bool) -> None
      self.glob = glob
      self.ignoreCase = ignoreCase
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> predicate.GlobMatch
      return predicate.GlobMatch('', False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('predicate.GlobMatch')
      L = out_node.fields
  
      x0 = NewLeaf(self.glob, color_e.StringConst)
      L.append(Field('glob', x0))
  
      x1 = hnode.Leaf('T' if self.ignoreCase else 'F', color_e.OtherConst)
      L.append(Field('ignoreCase', x1))
  
      return out_node
  
  class RegexMatch(predicate_t):
    _type_tag = 6
    __slots__ = ('re', 'ignoreCase')
  
    def __init__(self, re, ignoreCase):
      # type: (str, bool) -> None
      self.re = re
      self.ignoreCase = ignoreCase
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> predicate.RegexMatch
      return predicate.RegexMatch('', False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('predicate.RegexMatch')
      L = out_node.fields
  
      x0 = NewLeaf(self.re, color_e.StringConst)
      L.append(Field('re', x0))
  
      x1 = hnode.Leaf('T' if self.ignoreCase else 'F', color_e.OtherConst)
      L.append(Field('ignoreCase', x1))
  
      return out_node
  
  Readable = predicate__Readable()
  
  Writable = predicate__Writable()
  
  Executable = predicate__Executable()
  
  pass

