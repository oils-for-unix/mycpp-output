from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class bool_arg_type_t(pybase.SimpleObj):
  pass

class bool_arg_type_e(object):
  Undefined = bool_arg_type_t(1)
  Path = bool_arg_type_t(2)
  Int = bool_arg_type_t(3)
  Str = bool_arg_type_t(4)
  Other = bool_arg_type_t(5)

_bool_arg_type_str = {
  1: 'Undefined',
  2: 'Path',
  3: 'Int',
  4: 'Str',
  5: 'Other',
}

def bool_arg_type_str(val, dot=True):
  # type: (bool_arg_type_t, bool) -> str
  v = _bool_arg_type_str[val]
  if dot:
    return "bool_arg_type.%s" % v
  else:
    return v

class redir_arg_type_t(pybase.SimpleObj):
  pass

class redir_arg_type_e(object):
  Path = redir_arg_type_t(1)
  Desc = redir_arg_type_t(2)

_redir_arg_type_str = {
  1: 'Path',
  2: 'Desc',
}

def redir_arg_type_str(val, dot=True):
  # type: (redir_arg_type_t, bool) -> str
  v = _redir_arg_type_str[val]
  if dot:
    return "redir_arg_type.%s" % v
  else:
    return v

opt_group_t = int  # type alias for integer

class opt_group_i(object):
  StrictAll = 1
  YshUpgrade = 2
  YshAll = 3
  ARRAY_SIZE = 4

_opt_group_str = {
  1: 'StrictAll',
  2: 'YshUpgrade',
  3: 'YshAll',
}

def opt_group_str(val, dot=True):
  # type: (opt_group_t, bool) -> str
  v = _opt_group_str[val]
  if dot:
    return "opt_group.%s" % v
  else:
    return v

class lex_mode_t(pybase.SimpleObj):
  pass

class lex_mode_e(object):
  Undefined = lex_mode_t(1)
  Comment = lex_mode_t(2)
  ShCommand = lex_mode_t(3)
  ShCommandFakeBrack = lex_mode_t(4)
  Backtick = lex_mode_t(5)
  DBracket = lex_mode_t(6)
  SQ_Raw = lex_mode_t(7)
  DQ = lex_mode_t(8)
  SQ_C = lex_mode_t(9)
  J8_Str = lex_mode_t(10)
  Arith = lex_mode_t(11)
  ExtGlob = lex_mode_t(12)
  VSub_1 = lex_mode_t(13)
  VSub_2 = lex_mode_t(14)
  VSub_ArgUnquoted = lex_mode_t(15)
  VSub_ArgDQ = lex_mode_t(16)
  VSub_Zsh = lex_mode_t(17)
  BashRegex = lex_mode_t(18)
  BashRegexFakeInner = lex_mode_t(19)
  FuncParens = lex_mode_t(20)
  PrintfOuter = lex_mode_t(21)
  PrintfPercent = lex_mode_t(22)
  Expr = lex_mode_t(23)

_lex_mode_str = {
  1: 'Undefined',
  2: 'Comment',
  3: 'ShCommand',
  4: 'ShCommandFakeBrack',
  5: 'Backtick',
  6: 'DBracket',
  7: 'SQ_Raw',
  8: 'DQ',
  9: 'SQ_C',
  10: 'J8_Str',
  11: 'Arith',
  12: 'ExtGlob',
  13: 'VSub_1',
  14: 'VSub_2',
  15: 'VSub_ArgUnquoted',
  16: 'VSub_ArgDQ',
  17: 'VSub_Zsh',
  18: 'BashRegex',
  19: 'BashRegexFakeInner',
  20: 'FuncParens',
  21: 'PrintfOuter',
  22: 'PrintfPercent',
  23: 'Expr',
}

def lex_mode_str(val, dot=True):
  # type: (lex_mode_t, bool) -> str
  v = _lex_mode_str[val]
  if dot:
    return "lex_mode.%s" % v
  else:
    return v

class word_mode_t(pybase.SimpleObj):
  pass

class word_mode_e(object):
  ShCommand = word_mode_t(1)
  ShCommandBrack = word_mode_t(2)
  DBracket = word_mode_t(3)
  BashRegex = word_mode_t(4)

_word_mode_str = {
  1: 'ShCommand',
  2: 'ShCommandBrack',
  3: 'DBracket',
  4: 'BashRegex',
}

def word_mode_str(val, dot=True):
  # type: (word_mode_t, bool) -> str
  v = _word_mode_str[val]
  if dot:
    return "word_mode.%s" % v
  else:
    return v

class cmd_mode_t(pybase.SimpleObj):
  pass

class cmd_mode_e(object):
  Shell = cmd_mode_t(1)
  Func = cmd_mode_t(2)
  Proc = cmd_mode_t(3)

_cmd_mode_str = {
  1: 'Shell',
  2: 'Func',
  3: 'Proc',
}

def cmd_mode_str(val, dot=True):
  # type: (cmd_mode_t, bool) -> str
  v = _cmd_mode_str[val]
  if dot:
    return "cmd_mode.%s" % v
  else:
    return v

