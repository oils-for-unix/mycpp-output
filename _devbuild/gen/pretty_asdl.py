from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class doc_e(object):
  Break = 1
  Text = 2
  Indent = 3
  Group = 64
  Flat = 5
  IfFlat = 6
  Concat = 66

_doc_str = {
  1: 'Break',
  2: 'Text',
  3: 'Indent',
  5: 'Flat',
  6: 'IfFlat',
  64: 'Group',
  66: 'Concat',
}

def doc_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _doc_str[tag]
  if dot:
    return "doc.%s" % v
  else:
    return v

class doc_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class doc(object):
  class Break(doc_t):
    _type_tag = 1
    __slots__ = ('string',)
  
    def __init__(self, string):
      # type: (str) -> None
      self.string = string
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> doc.Break
      return doc.Break('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('doc.Break')
      L = out_node.fields
  
      x0 = NewLeaf(self.string, color_e.StringConst)
      L.append(Field('string', x0))
  
      return out_node
  
  class Text(doc_t):
    _type_tag = 2
    __slots__ = ('string',)
  
    def __init__(self, string):
      # type: (str) -> None
      self.string = string
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> doc.Text
      return doc.Text('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('doc.Text')
      L = out_node.fields
  
      x0 = NewLeaf(self.string, color_e.StringConst)
      L.append(Field('string', x0))
  
      return out_node
  
  class Indent(doc_t):
    _type_tag = 3
    __slots__ = ('indent', 'mdoc')
  
    def __init__(self, indent, mdoc):
      # type: (int, MeasuredDoc) -> None
      self.indent = indent
      self.mdoc = mdoc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> doc.Indent
      return doc.Indent(-1, cast('MeasuredDoc', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('doc.Indent')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.indent), color_e.OtherConst)
      L.append(Field('indent', x0))
  
      assert self.mdoc is not None
      x1 = self.mdoc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('mdoc', x1))
  
      return out_node
  
  class Flat(doc_t):
    _type_tag = 5
    __slots__ = ('mdoc',)
  
    def __init__(self, mdoc):
      # type: (MeasuredDoc) -> None
      self.mdoc = mdoc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> doc.Flat
      return doc.Flat(cast('MeasuredDoc', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('doc.Flat')
      L = out_node.fields
  
      assert self.mdoc is not None
      x0 = self.mdoc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('mdoc', x0))
  
      return out_node
  
  class IfFlat(doc_t):
    _type_tag = 6
    __slots__ = ('flat_mdoc', 'nonflat_mdoc')
  
    def __init__(self, flat_mdoc, nonflat_mdoc):
      # type: (MeasuredDoc, MeasuredDoc) -> None
      self.flat_mdoc = flat_mdoc
      self.nonflat_mdoc = nonflat_mdoc
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> doc.IfFlat
      return doc.IfFlat(cast('MeasuredDoc', None), cast('MeasuredDoc', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('doc.IfFlat')
      L = out_node.fields
  
      assert self.flat_mdoc is not None
      x0 = self.flat_mdoc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('flat_mdoc', x0))
  
      assert self.nonflat_mdoc is not None
      x1 = self.nonflat_mdoc.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('nonflat_mdoc', x1))
  
      return out_node
  
  pass

class MeasuredDoc(doc_t):
  _type_tag = 64
  __slots__ = ('doc', 'measure')

  def __init__(self, doc, measure):
    # type: (doc_t, Measure) -> None
    self.doc = doc
    self.measure = measure

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> MeasuredDoc
    return MeasuredDoc(cast('doc_t', None), cast('Measure', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('MeasuredDoc')
    L = out_node.fields

    assert self.doc is not None
    x0 = self.doc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('doc', x0))

    assert self.measure is not None
    x1 = self.measure.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('measure', x1))

    return out_node

class Measure(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('flat', 'nonflat')

  def __init__(self, flat, nonflat):
    # type: (int, int) -> None
    self.flat = flat
    self.nonflat = nonflat

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Measure
    return Measure(-1, -1)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Measure')
    L = out_node.fields

    x0 = hnode.Leaf(str(self.flat), color_e.OtherConst)
    L.append(Field('flat', x0))

    x1 = hnode.Leaf(str(self.nonflat), color_e.OtherConst)
    L.append(Field('nonflat', x1))

    return out_node

class DocFragment(pybase.CompoundObj):
  _type_tag = 67
  __slots__ = ('mdoc', 'indent', 'is_flat', 'measure')

  def __init__(self, mdoc, indent, is_flat, measure):
    # type: (MeasuredDoc, int, bool, Measure) -> None
    self.mdoc = mdoc
    self.indent = indent
    self.is_flat = is_flat
    self.measure = measure

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> DocFragment
    return DocFragment(cast('MeasuredDoc', None), -1, False, cast('Measure', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('DocFragment')
    L = out_node.fields

    assert self.mdoc is not None
    x0 = self.mdoc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('mdoc', x0))

    x1 = hnode.Leaf(str(self.indent), color_e.OtherConst)
    L.append(Field('indent', x1))

    x2 = hnode.Leaf('T' if self.is_flat else 'F', color_e.OtherConst)
    L.append(Field('is_flat', x2))

    assert self.measure is not None
    x3 = self.measure.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('measure', x3))

    return out_node

class List_Measured(doc_t, List[MeasuredDoc]):
  _type_tag = 66
  @staticmethod
  def New():
    # type: () -> List_Measured
    return List_Measured()

  @staticmethod
  def Take(plain_list):
    # type: (List[MeasuredDoc]) -> List_Measured
    result = List_Measured(plain_list)
    del plain_list[:]
    return result

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True
    h = runtime.NewRecord('List_Measured')
    h.unnamed_fields = [c.PrettyTree(do_abbrev) for c in self]
    return h

