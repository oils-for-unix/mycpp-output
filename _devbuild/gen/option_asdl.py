from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

option_t = int  # type alias for integer

class option_i(object):
  errexit = 1
  nounset = 2
  pipefail = 3
  inherit_errexit = 4
  nullglob = 5
  verbose_errexit = 6
  verbose_warn = 7
  allexport = 8
  noexec = 9
  xtrace = 10
  verbose = 11
  noglob = 12
  noclobber = 13
  errtrace = 14
  posix = 15
  vi = 16
  emacs = 17
  interactive = 18
  hashall = 19
  lastpipe = 20
  extglob = 21
  failglob = 22
  nocasematch = 23
  dotglob = 24
  globskipdots = 25
  extdebug = 26
  eval_unsafe_arith = 27
  ignore_flags_not_impl = 28
  ignore_shopt_not_impl = 29
  rewrite_extern = 30
  _allow_command_sub = 31
  _allow_process_sub = 32
  dynamic_scope = 33
  redefine_const = 34
  redefine_source = 35
  _running_trap = 36
  _running_hay = 37
  _no_debug_trap = 38
  _no_err_trap = 39
  strict_parse_equals = 40
  strict_parse_slice = 41
  strict_argv = 42
  strict_arith = 43
  strict_arg_parse = 44
  strict_array = 45
  strict_control_flow = 46
  strict_env_binding = 47
  strict_errexit = 48
  strict_nameref = 49
  strict_word_eval = 50
  strict_tilde = 51
  strict_glob = 52
  parse_at = 53
  parse_proc = 54
  parse_func = 55
  parse_brace = 56
  parse_bracket = 57
  parse_equals = 58
  parse_paren = 59
  parse_ysh_string = 60
  parse_triple_quote = 61
  parse_ysh_expr_sub = 62
  simple_word_eval = 63
  no_dash_glob = 64
  command_sub_errexit = 65
  process_sub_fail = 66
  xtrace_rich = 67
  no_xtrace_osh = 68
  sigpipe_status_ok = 69
  env_obj = 70
  init_ysh_globals = 71
  for_loop_frames = 72
  ysh_rewrite_extern = 73
  parse_at_all = 74
  no_parse_backslash = 75
  no_parse_backticks = 76
  no_parse_bare_word = 77
  no_parse_dbracket = 78
  no_parse_dollar = 79
  no_parse_dparen = 80
  no_parse_ignored = 81
  no_parse_osh = 82
  no_parse_sh_arith = 83
  no_parse_word_join = 84
  no_exported = 85
  no_init_globals = 86
  no_osh_builtins = 87
  simple_echo = 88
  simple_eval_builtin = 89
  simple_test_builtin = 90
  simple_trap_builtin = 91
  expand_aliases = 92
  progcomp = 93
  hostcomplete = 94
  histappend = 95
  cmdhist = 96
  assoc_expand_once = 97
  autocd = 98
  cdable_vars = 99
  cdspell = 100
  checkhash = 101
  checkjobs = 102
  checkwinsize = 103
  complete_fullquote = 104
  direxpand = 105
  dirspell = 106
  execfail = 107
  extquote = 108
  force_fignore = 109
  globasciiranges = 110
  globstar = 111
  gnu_errfmt = 112
  histreedit = 113
  histverify = 114
  huponexit = 115
  interactive_comments = 116
  lithist = 117
  localvar_inherit = 118
  localvar_unset = 119
  login_shell = 120
  mailwarn = 121
  no_empty_cmd_completion = 122
  nocaseglob = 123
  progcomp_alias = 124
  promptvars = 125
  restricted_shell = 126
  shift_verbose = 127
  sourcepath = 128
  xpg_echo = 129
  ARRAY_SIZE = 130

_option_str = {
  1: 'errexit',
  2: 'nounset',
  3: 'pipefail',
  4: 'inherit_errexit',
  5: 'nullglob',
  6: 'verbose_errexit',
  7: 'verbose_warn',
  8: 'allexport',
  9: 'noexec',
  10: 'xtrace',
  11: 'verbose',
  12: 'noglob',
  13: 'noclobber',
  14: 'errtrace',
  15: 'posix',
  16: 'vi',
  17: 'emacs',
  18: 'interactive',
  19: 'hashall',
  20: 'lastpipe',
  21: 'extglob',
  22: 'failglob',
  23: 'nocasematch',
  24: 'dotglob',
  25: 'globskipdots',
  26: 'extdebug',
  27: 'eval_unsafe_arith',
  28: 'ignore_flags_not_impl',
  29: 'ignore_shopt_not_impl',
  30: 'rewrite_extern',
  31: '_allow_command_sub',
  32: '_allow_process_sub',
  33: 'dynamic_scope',
  34: 'redefine_const',
  35: 'redefine_source',
  36: '_running_trap',
  37: '_running_hay',
  38: '_no_debug_trap',
  39: '_no_err_trap',
  40: 'strict_parse_equals',
  41: 'strict_parse_slice',
  42: 'strict_argv',
  43: 'strict_arith',
  44: 'strict_arg_parse',
  45: 'strict_array',
  46: 'strict_control_flow',
  47: 'strict_env_binding',
  48: 'strict_errexit',
  49: 'strict_nameref',
  50: 'strict_word_eval',
  51: 'strict_tilde',
  52: 'strict_glob',
  53: 'parse_at',
  54: 'parse_proc',
  55: 'parse_func',
  56: 'parse_brace',
  57: 'parse_bracket',
  58: 'parse_equals',
  59: 'parse_paren',
  60: 'parse_ysh_string',
  61: 'parse_triple_quote',
  62: 'parse_ysh_expr_sub',
  63: 'simple_word_eval',
  64: 'no_dash_glob',
  65: 'command_sub_errexit',
  66: 'process_sub_fail',
  67: 'xtrace_rich',
  68: 'no_xtrace_osh',
  69: 'sigpipe_status_ok',
  70: 'env_obj',
  71: 'init_ysh_globals',
  72: 'for_loop_frames',
  73: 'ysh_rewrite_extern',
  74: 'parse_at_all',
  75: 'no_parse_backslash',
  76: 'no_parse_backticks',
  77: 'no_parse_bare_word',
  78: 'no_parse_dbracket',
  79: 'no_parse_dollar',
  80: 'no_parse_dparen',
  81: 'no_parse_ignored',
  82: 'no_parse_osh',
  83: 'no_parse_sh_arith',
  84: 'no_parse_word_join',
  85: 'no_exported',
  86: 'no_init_globals',
  87: 'no_osh_builtins',
  88: 'simple_echo',
  89: 'simple_eval_builtin',
  90: 'simple_test_builtin',
  91: 'simple_trap_builtin',
  92: 'expand_aliases',
  93: 'progcomp',
  94: 'hostcomplete',
  95: 'histappend',
  96: 'cmdhist',
  97: 'assoc_expand_once',
  98: 'autocd',
  99: 'cdable_vars',
  100: 'cdspell',
  101: 'checkhash',
  102: 'checkjobs',
  103: 'checkwinsize',
  104: 'complete_fullquote',
  105: 'direxpand',
  106: 'dirspell',
  107: 'execfail',
  108: 'extquote',
  109: 'force_fignore',
  110: 'globasciiranges',
  111: 'globstar',
  112: 'gnu_errfmt',
  113: 'histreedit',
  114: 'histverify',
  115: 'huponexit',
  116: 'interactive_comments',
  117: 'lithist',
  118: 'localvar_inherit',
  119: 'localvar_unset',
  120: 'login_shell',
  121: 'mailwarn',
  122: 'no_empty_cmd_completion',
  123: 'nocaseglob',
  124: 'progcomp_alias',
  125: 'promptvars',
  126: 'restricted_shell',
  127: 'shift_verbose',
  128: 'sourcepath',
  129: 'xpg_echo',
}

def option_str(val, dot=True):
  # type: (option_t, bool) -> str
  v = _option_str[val]
  if dot:
    return "option.%s" % v
  else:
    return v

builtin_t = int  # type alias for integer

class builtin_i(object):
  colon = 1
  dot = 2
  exec_ = 3
  eval = 4
  set = 5
  shift = 6
  times = 7
  trap = 8
  unset = 9
  readonly = 10
  local = 11
  declare = 12
  typeset = 13
  export_ = 14
  true_ = 15
  false_ = 16
  try_ = 17
  assert_ = 18
  break_ = 19
  continue_ = 20
  return_ = 21
  exit = 22
  read = 23
  echo = 24
  printf = 25
  mapfile = 26
  readarray = 27
  cd = 28
  chdir = 29
  pushd = 30
  popd = 31
  dirs = 32
  pwd = 33
  source = 34
  umask = 35
  ulimit = 36
  wait = 37
  jobs = 38
  fg = 39
  bg = 40
  kill = 41
  shopt = 42
  complete = 43
  compgen = 44
  compopt = 45
  compadjust = 46
  compexport = 47
  getopts = 48
  builtin = 49
  command = 50
  type = 51
  hash = 52
  help = 53
  history = 54
  fc = 55
  alias = 56
  unalias = 57
  bind = 58
  append = 59
  write = 60
  json = 61
  json8 = 62
  pp = 63
  hay = 64
  haynode = 65
  use = 66
  error = 67
  failed = 68
  fork = 69
  forkwait = 70
  redir = 71
  fopen = 72
  shvar = 73
  ctx = 74
  invoke = 75
  runproc = 76
  boolstatus = 77
  test = 78
  bracket = 79
  push_registers = 80
  source_guard = 81
  is_main = 82
  cat = 83
  rm = 84
  sleep = 85
  ARRAY_SIZE = 86

_builtin_str = {
  1: 'colon',
  2: 'dot',
  3: 'exec_',
  4: 'eval',
  5: 'set',
  6: 'shift',
  7: 'times',
  8: 'trap',
  9: 'unset',
  10: 'readonly',
  11: 'local',
  12: 'declare',
  13: 'typeset',
  14: 'export_',
  15: 'true_',
  16: 'false_',
  17: 'try_',
  18: 'assert_',
  19: 'break_',
  20: 'continue_',
  21: 'return_',
  22: 'exit',
  23: 'read',
  24: 'echo',
  25: 'printf',
  26: 'mapfile',
  27: 'readarray',
  28: 'cd',
  29: 'chdir',
  30: 'pushd',
  31: 'popd',
  32: 'dirs',
  33: 'pwd',
  34: 'source',
  35: 'umask',
  36: 'ulimit',
  37: 'wait',
  38: 'jobs',
  39: 'fg',
  40: 'bg',
  41: 'kill',
  42: 'shopt',
  43: 'complete',
  44: 'compgen',
  45: 'compopt',
  46: 'compadjust',
  47: 'compexport',
  48: 'getopts',
  49: 'builtin',
  50: 'command',
  51: 'type',
  52: 'hash',
  53: 'help',
  54: 'history',
  55: 'fc',
  56: 'alias',
  57: 'unalias',
  58: 'bind',
  59: 'append',
  60: 'write',
  61: 'json',
  62: 'json8',
  63: 'pp',
  64: 'hay',
  65: 'haynode',
  66: 'use',
  67: 'error',
  68: 'failed',
  69: 'fork',
  70: 'forkwait',
  71: 'redir',
  72: 'fopen',
  73: 'shvar',
  74: 'ctx',
  75: 'invoke',
  76: 'runproc',
  77: 'boolstatus',
  78: 'test',
  79: 'bracket',
  80: 'push_registers',
  81: 'source_guard',
  82: 'is_main',
  83: 'cat',
  84: 'rm',
  85: 'sleep',
}

def builtin_str(val, dot=True):
  # type: (builtin_t, bool) -> str
  v = _builtin_str[val]
  if dot:
    return "builtin.%s" % v
  else:
    return v

