from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class h8_id_t(pybase.SimpleObj):
  pass

class h8_id(object):
  Decl = h8_id_t(1)
  Comment = h8_id_t(2)
  CommentBegin = h8_id_t(3)
  Processing = h8_id_t(4)
  ProcessingBegin = h8_id_t(5)
  CData = h8_id_t(6)
  CDataBegin = h8_id_t(7)
  StartTag = h8_id_t(8)
  StartEndTag = h8_id_t(9)
  EndTag = h8_id_t(10)
  DecChar = h8_id_t(11)
  HexChar = h8_id_t(12)
  CharEntity = h8_id_t(13)
  RawData = h8_id_t(14)
  HtmlCData = h8_id_t(15)
  BadAmpersand = h8_id_t(16)
  BadGreaterThan = h8_id_t(17)
  BadLessThan = h8_id_t(18)
  Invalid = h8_id_t(19)
  EndOfStream = h8_id_t(20)
  DoubleQuote = h8_id_t(21)
  SingleQuote = h8_id_t(22)

_h8_id_str = {
  1: 'Decl',
  2: 'Comment',
  3: 'CommentBegin',
  4: 'Processing',
  5: 'ProcessingBegin',
  6: 'CData',
  7: 'CDataBegin',
  8: 'StartTag',
  9: 'StartEndTag',
  10: 'EndTag',
  11: 'DecChar',
  12: 'HexChar',
  13: 'CharEntity',
  14: 'RawData',
  15: 'HtmlCData',
  16: 'BadAmpersand',
  17: 'BadGreaterThan',
  18: 'BadLessThan',
  19: 'Invalid',
  20: 'EndOfStream',
  21: 'DoubleQuote',
  22: 'SingleQuote',
}

def h8_id_str(val, dot=True):
  # type: (h8_id_t, bool) -> str
  v = _h8_id_str[val]
  if dot:
    return "h8_id.%s" % v
  else:
    return v

class attr_name_t(pybase.SimpleObj):
  pass

class attr_name(object):
  Ok = attr_name_t(1)
  Done = attr_name_t(2)
  Invalid = attr_name_t(3)

_attr_name_str = {
  1: 'Ok',
  2: 'Done',
  3: 'Invalid',
}

def attr_name_str(val, dot=True):
  # type: (attr_name_t, bool) -> str
  v = _attr_name_str[val]
  if dot:
    return "attr_name.%s" % v
  else:
    return v

class h8_val_id_t(pybase.SimpleObj):
  pass

class h8_val_id(object):
  UnquotedVal = h8_val_id_t(1)
  DoubleQuote = h8_val_id_t(2)
  SingleQuote = h8_val_id_t(3)
  NoMatch = h8_val_id_t(4)

_h8_val_id_str = {
  1: 'UnquotedVal',
  2: 'DoubleQuote',
  3: 'SingleQuote',
  4: 'NoMatch',
}

def h8_val_id_str(val, dot=True):
  # type: (h8_val_id_t, bool) -> str
  v = _h8_val_id_str[val]
  if dot:
    return "h8_val_id.%s" % v
  else:
    return v

class attr_value_t(pybase.SimpleObj):
  pass

class attr_value_e(object):
  Missing = attr_value_t(1)
  Empty = attr_value_t(2)
  Unquoted = attr_value_t(3)
  DoubleQuoted = attr_value_t(4)
  SingleQuoted = attr_value_t(5)

_attr_value_str = {
  1: 'Missing',
  2: 'Empty',
  3: 'Unquoted',
  4: 'DoubleQuoted',
  5: 'SingleQuoted',
}

def attr_value_str(val, dot=True):
  # type: (attr_value_t, bool) -> str
  v = _attr_value_str[val]
  if dot:
    return "attr_value.%s" % v
  else:
    return v

class h8_tag_id_t(pybase.SimpleObj):
  pass

class h8_tag_id(object):
  TagName = h8_tag_id_t(1)
  AttrName = h8_tag_id_t(2)
  UnquotedValue = h8_tag_id_t(3)
  QuotedValue = h8_tag_id_t(4)
  MissingValue = h8_tag_id_t(5)

_h8_tag_id_str = {
  1: 'TagName',
  2: 'AttrName',
  3: 'UnquotedValue',
  4: 'QuotedValue',
  5: 'MissingValue',
}

def h8_tag_id_str(val, dot=True):
  # type: (h8_tag_id_t, bool) -> str
  v = _h8_tag_id_str[val]
  if dot:
    return "h8_tag_id.%s" % v
  else:
    return v

