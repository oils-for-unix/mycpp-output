from asdl import pybase
from mycpp import mops
from typing import Optional, List, Tuple, Dict, Any, cast, TYPE_CHECKING
from _devbuild.gen.id_kind_asdl import Id_str

if TYPE_CHECKING:
  from _devbuild.gen.id_kind_asdl import Id_t
  from _devbuild.gen.syntax_asdl import loc_t, Token, expr_t, word_t, command_t, CompoundWord, DoubleQuoted, ArgList, re_t, redir_loc_t, proc_sig_t, Func
  from _devbuild.gen.value_asdl import value_t, Obj

from asdl import runtime  # For runtime.NO_SPID
from asdl.runtime import NewRecord, NewLeaf, TraversalState
from _devbuild.gen.hnode_asdl import color_e, hnode, hnode_e, hnode_t, Field

class cmd_value_e(object):
  Argv = 1
  Assign = 2

_cmd_value_str = {
  1: 'Argv',
  2: 'Assign',
}

def cmd_value_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _cmd_value_str[tag]
  if dot:
    return "cmd_value.%s" % v
  else:
    return v

class cmd_value_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class cmd_value(object):
  class Argv(cmd_value_t):
    _type_tag = 1
    __slots__ = ('argv', 'arg_locs', 'is_last_cmd', 'self_obj', 'proc_args')
  
    def __init__(self, argv, arg_locs, is_last_cmd, self_obj, proc_args):
      # type: (List[str], List[CompoundWord], bool, Optional[Obj], Optional[ProcArgs]) -> None
      self.argv = argv
      self.arg_locs = arg_locs
      self.is_last_cmd = is_last_cmd
      self.self_obj = self_obj
      self.proc_args = proc_args
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> cmd_value.Argv
      return cmd_value.Argv([] if alloc_lists else cast('List[str]', None), [] if alloc_lists else cast('List[CompoundWord]', None), False, cast('Optional[Obj]', None), cast('Optional[ProcArgs]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('cmd_value.Argv')
      L = out_node.fields
  
      if self.argv is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.argv:
          x0.children.append(NewLeaf(i0, color_e.StringConst))
        L.append(Field('argv', x0))
  
      if self.arg_locs is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.arg_locs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
               i1.PrettyTree(do_abbrev, trav=trav))
          x1.children.append(h)
        L.append(Field('arg_locs', x1))
  
      x2 = hnode.Leaf('T' if self.is_last_cmd else 'F', color_e.OtherConst)
      L.append(Field('is_last_cmd', x2))
  
      if self.self_obj is not None:  # Optional
        x3 = self.self_obj.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('self_obj', x3))
  
      if self.proc_args is not None:  # Optional
        x4 = self.proc_args.PrettyTree(do_abbrev, trav=trav)
        L.append(Field('proc_args', x4))
  
      return out_node
  
  class Assign(cmd_value_t):
    _type_tag = 2
    __slots__ = ('builtin_id', 'argv', 'arg_locs', 'pairs')
  
    def __init__(self, builtin_id, argv, arg_locs, pairs):
      # type: (int, List[str], List[CompoundWord], List[AssignArg]) -> None
      self.builtin_id = builtin_id
      self.argv = argv
      self.arg_locs = arg_locs
      self.pairs = pairs
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> cmd_value.Assign
      return cmd_value.Assign(-1, [] if alloc_lists else cast('List[str]', None), [] if alloc_lists else cast('List[CompoundWord]', None), [] if alloc_lists else cast('List[AssignArg]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('cmd_value.Assign')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.builtin_id), color_e.OtherConst)
      L.append(Field('builtin_id', x0))
  
      if self.argv is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.argv:
          x1.children.append(NewLeaf(i1, color_e.StringConst))
        L.append(Field('argv', x1))
  
      if self.arg_locs is not None:  # List
        x2 = hnode.Array([])
        for i2 in self.arg_locs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i2 is None else
               i2.PrettyTree(do_abbrev, trav=trav))
          x2.children.append(h)
        L.append(Field('arg_locs', x2))
  
      if self.pairs is not None:  # List
        x3 = hnode.Array([])
        for i3 in self.pairs:
          h = (hnode.Leaf("_", color_e.OtherConst) if i3 is None else
               i3.PrettyTree(do_abbrev, trav=trav))
          x3.children.append(h)
        L.append(Field('pairs', x3))
  
      return out_node
  
  pass

class part_value_e(object):
  String = 66
  Array = 2
  ExtGlob = 3

_part_value_str = {
  2: 'Array',
  3: 'ExtGlob',
  66: 'String',
}

def part_value_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _part_value_str[tag]
  if dot:
    return "part_value.%s" % v
  else:
    return v

class part_value_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class part_value(object):
  class Array(part_value_t):
    _type_tag = 2
    __slots__ = ('strs', 'quoted')
  
    def __init__(self, strs, quoted):
      # type: (List[str], bool) -> None
      self.strs = strs
      self.quoted = quoted
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> part_value.Array
      return part_value.Array([] if alloc_lists else cast('List[str]', None), False)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('part_value.Array')
      L = out_node.fields
  
      if self.strs is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.strs:
          x0.children.append(NewLeaf(i0, color_e.StringConst))
        L.append(Field('strs', x0))
  
      x1 = hnode.Leaf('T' if self.quoted else 'F', color_e.OtherConst)
      L.append(Field('quoted', x1))
  
      return out_node
  
  class ExtGlob(part_value_t):
    _type_tag = 3
    __slots__ = ('part_vals',)
  
    def __init__(self, part_vals):
      # type: (List[part_value_t]) -> None
      self.part_vals = part_vals
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> part_value.ExtGlob
      return part_value.ExtGlob([] if alloc_lists else cast('List[part_value_t]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('part_value.ExtGlob')
      L = out_node.fields
  
      if self.part_vals is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.part_vals:
          h = (hnode.Leaf("_", color_e.OtherConst) if i0 is None else
               i0.PrettyTree(do_abbrev, trav=trav))
          x0.children.append(h)
        L.append(Field('part_vals', x0))
  
      return out_node
  
  pass

class coerced_t(pybase.SimpleObj):
  pass

class coerced_e(object):
  Int = coerced_t(1)
  Float = coerced_t(2)
  Neither = coerced_t(3)

_coerced_str = {
  1: 'Int',
  2: 'Float',
  3: 'Neither',
}

def coerced_str(val, dot=True):
  # type: (coerced_t, bool) -> str
  v = _coerced_str[val]
  if dot:
    return "coerced.%s" % v
  else:
    return v

class scope_t(pybase.SimpleObj):
  pass

class scope_e(object):
  Shopt = scope_t(1)
  Dynamic = scope_t(2)
  LocalOrGlobal = scope_t(3)
  LocalOnly = scope_t(4)
  GlobalOnly = scope_t(5)

_scope_str = {
  1: 'Shopt',
  2: 'Dynamic',
  3: 'LocalOrGlobal',
  4: 'LocalOnly',
  5: 'GlobalOnly',
}

def scope_str(val, dot=True):
  # type: (scope_t, bool) -> str
  v = _scope_str[val]
  if dot:
    return "scope.%s" % v
  else:
    return v

class a_index_e(object):
  Str = 1
  Int = 2

_a_index_str = {
  1: 'Str',
  2: 'Int',
}

def a_index_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _a_index_str[tag]
  if dot:
    return "a_index.%s" % v
  else:
    return v

class a_index_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class a_index(object):
  class Str(a_index_t):
    _type_tag = 1
    __slots__ = ('s',)
  
    def __init__(self, s):
      # type: (str) -> None
      self.s = s
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> a_index.Str
      return a_index.Str('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('a_index.Str')
      L = out_node.fields
  
      x0 = NewLeaf(self.s, color_e.StringConst)
      L.append(Field('s', x0))
  
      return out_node
  
  class Int(a_index_t):
    _type_tag = 2
    __slots__ = ('i',)
  
    def __init__(self, i):
      # type: (int) -> None
      self.i = i
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> a_index.Int
      return a_index.Int(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('a_index.Int')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.i), color_e.OtherConst)
      L.append(Field('i', x0))
  
      return out_node
  
  pass

class redirect_arg_e(object):
  Path = 1
  CopyFd = 2
  MoveFd = 3
  CloseFd = 4
  HereDoc = 5

_redirect_arg_str = {
  1: 'Path',
  2: 'CopyFd',
  3: 'MoveFd',
  4: 'CloseFd',
  5: 'HereDoc',
}

def redirect_arg_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _redirect_arg_str[tag]
  if dot:
    return "redirect_arg.%s" % v
  else:
    return v

class redirect_arg_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class redirect_arg__CloseFd(redirect_arg_t):
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

    out_node = NewRecord('redirect_arg.CloseFd')
    L = out_node.fields

    return out_node

class redirect_arg(object):
  class Path(redirect_arg_t):
    _type_tag = 1
    __slots__ = ('filename',)
  
    def __init__(self, filename):
      # type: (str) -> None
      self.filename = filename
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redirect_arg.Path
      return redirect_arg.Path('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redirect_arg.Path')
      L = out_node.fields
  
      x0 = NewLeaf(self.filename, color_e.StringConst)
      L.append(Field('filename', x0))
  
      return out_node
  
  class CopyFd(redirect_arg_t):
    _type_tag = 2
    __slots__ = ('target_fd',)
  
    def __init__(self, target_fd):
      # type: (int) -> None
      self.target_fd = target_fd
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redirect_arg.CopyFd
      return redirect_arg.CopyFd(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redirect_arg.CopyFd')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.target_fd), color_e.OtherConst)
      L.append(Field('target_fd', x0))
  
      return out_node
  
  class MoveFd(redirect_arg_t):
    _type_tag = 3
    __slots__ = ('target_fd',)
  
    def __init__(self, target_fd):
      # type: (int) -> None
      self.target_fd = target_fd
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redirect_arg.MoveFd
      return redirect_arg.MoveFd(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redirect_arg.MoveFd')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.target_fd), color_e.OtherConst)
      L.append(Field('target_fd', x0))
  
      return out_node
  
  CloseFd = redirect_arg__CloseFd()
  
  class HereDoc(redirect_arg_t):
    _type_tag = 5
    __slots__ = ('body',)
  
    def __init__(self, body):
      # type: (str) -> None
      self.body = body
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> redirect_arg.HereDoc
      return redirect_arg.HereDoc('')
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('redirect_arg.HereDoc')
      L = out_node.fields
  
      x0 = NewLeaf(self.body, color_e.StringConst)
      L.append(Field('body', x0))
  
      return out_node
  
  pass

class job_state_t(pybase.SimpleObj):
  pass

class job_state_e(object):
  Running = job_state_t(1)
  Exited = job_state_t(2)
  Stopped = job_state_t(3)

_job_state_str = {
  1: 'Running',
  2: 'Exited',
  3: 'Stopped',
}

def job_state_str(val, dot=True):
  # type: (job_state_t, bool) -> str
  v = _job_state_str[val]
  if dot:
    return "job_state.%s" % v
  else:
    return v

class wait_status_e(object):
  Proc = 1
  Pipeline = 2
  Cancelled = 3

_wait_status_str = {
  1: 'Proc',
  2: 'Pipeline',
  3: 'Cancelled',
}

def wait_status_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _wait_status_str[tag]
  if dot:
    return "wait_status.%s" % v
  else:
    return v

class wait_status_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class wait_status(object):
  class Proc(wait_status_t):
    _type_tag = 1
    __slots__ = ('state', 'code')
  
    def __init__(self, state, code):
      # type: (job_state_t, int) -> None
      self.state = state
      self.code = code
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> wait_status.Proc
      return wait_status.Proc(job_state_e.Running, -1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('wait_status.Proc')
      L = out_node.fields
  
      x0 = hnode.Leaf(job_state_str(self.state), color_e.TypeName)
      L.append(Field('state', x0))
  
      x1 = hnode.Leaf(str(self.code), color_e.OtherConst)
      L.append(Field('code', x1))
  
      return out_node
  
  class Pipeline(wait_status_t):
    _type_tag = 2
    __slots__ = ('state', 'codes')
  
    def __init__(self, state, codes):
      # type: (job_state_t, List[int]) -> None
      self.state = state
      self.codes = codes
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> wait_status.Pipeline
      return wait_status.Pipeline(job_state_e.Running, [] if alloc_lists else cast('List[int]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('wait_status.Pipeline')
      L = out_node.fields
  
      x0 = hnode.Leaf(job_state_str(self.state), color_e.TypeName)
      L.append(Field('state', x0))
  
      if self.codes is not None:  # List
        x1 = hnode.Array([])
        for i1 in self.codes:
          x1.children.append(hnode.Leaf(str(i1), color_e.OtherConst))
        L.append(Field('codes', x1))
  
      return out_node
  
  class Cancelled(wait_status_t):
    _type_tag = 3
    __slots__ = ('sig_num',)
  
    def __init__(self, sig_num):
      # type: (int) -> None
      self.sig_num = sig_num
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> wait_status.Cancelled
      return wait_status.Cancelled(-1)
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('wait_status.Cancelled')
      L = out_node.fields
  
      x0 = hnode.Leaf(str(self.sig_num), color_e.OtherConst)
      L.append(Field('sig_num', x0))
  
      return out_node
  
  pass

class flow_t(pybase.SimpleObj):
  pass

class flow_e(object):
  Nothing = flow_t(1)
  Break = flow_t(2)
  Raise = flow_t(3)

_flow_str = {
  1: 'Nothing',
  2: 'Break',
  3: 'Raise',
}

def flow_str(val, dot=True):
  # type: (flow_t, bool) -> str
  v = _flow_str[val]
  if dot:
    return "flow.%s" % v
  else:
    return v

class span_t(pybase.SimpleObj):
  pass

class span_e(object):
  Black = span_t(1)
  Delim = span_t(2)
  Backslash = span_t(3)

_span_str = {
  1: 'Black',
  2: 'Delim',
  3: 'Backslash',
}

def span_str(val, dot=True):
  # type: (span_t, bool) -> str
  v = _span_str[val]
  if dot:
    return "span.%s" % v
  else:
    return v

emit_t = int  # type alias for integer

class emit_i(object):
  Part = 1
  Delim = 2
  Empty = 3
  Escape = 4
  Nothing = 5
  ARRAY_SIZE = 6

_emit_str = {
  1: 'Part',
  2: 'Delim',
  3: 'Empty',
  4: 'Escape',
  5: 'Nothing',
}

def emit_str(val, dot=True):
  # type: (emit_t, bool) -> str
  v = _emit_str[val]
  if dot:
    return "emit.%s" % v
  else:
    return v

state_t = int  # type alias for integer

class state_i(object):
  Invalid = 1
  Start = 2
  DE_White1 = 3
  DE_Gray = 4
  DE_White2 = 5
  Black = 6
  Backslash = 7
  Done = 8
  ARRAY_SIZE = 9

_state_str = {
  1: 'Invalid',
  2: 'Start',
  3: 'DE_White1',
  4: 'DE_Gray',
  5: 'DE_White2',
  6: 'Black',
  7: 'Backslash',
  8: 'Done',
}

def state_str(val, dot=True):
  # type: (state_t, bool) -> str
  v = _state_str[val]
  if dot:
    return "state.%s" % v
  else:
    return v

char_kind_t = int  # type alias for integer

class char_kind_i(object):
  DE_White = 1
  DE_Gray = 2
  Black = 3
  Backslash = 4
  Sentinel = 5
  ARRAY_SIZE = 6

_char_kind_str = {
  1: 'DE_White',
  2: 'DE_Gray',
  3: 'Black',
  4: 'Backslash',
  5: 'Sentinel',
}

def char_kind_str(val, dot=True):
  # type: (char_kind_t, bool) -> str
  v = _char_kind_str[val]
  if dot:
    return "char_kind.%s" % v
  else:
    return v

class error_code_t(pybase.SimpleObj):
  pass

class error_code_e(object):
  OK = error_code_t(1)
  IndexOutOfRange = error_code_t(2)

_error_code_str = {
  1: 'OK',
  2: 'IndexOutOfRange',
}

def error_code_str(val, dot=True):
  # type: (error_code_t, bool) -> str
  v = _error_code_str[val]
  if dot:
    return "error_code.%s" % v
  else:
    return v

class flag_type_t(pybase.SimpleObj):
  pass

class flag_type_e(object):
  Bool = flag_type_t(1)
  Int = flag_type_t(2)
  Float = flag_type_t(3)
  Str = flag_type_t(4)

_flag_type_str = {
  1: 'Bool',
  2: 'Int',
  3: 'Float',
  4: 'Str',
}

def flag_type_str(val, dot=True):
  # type: (flag_type_t, bool) -> str
  v = _flag_type_str[val]
  if dot:
    return "flag_type.%s" % v
  else:
    return v

class trace_e(object):
  External = 1
  CommandSub = 2
  ForkWait = 3
  Fork = 4
  PipelinePart = 5
  ProcessSub = 6
  HereDoc = 7

_trace_str = {
  1: 'External',
  2: 'CommandSub',
  3: 'ForkWait',
  4: 'Fork',
  5: 'PipelinePart',
  6: 'ProcessSub',
  7: 'HereDoc',
}

def trace_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _trace_str[tag]
  if dot:
    return "trace.%s" % v
  else:
    return v

class trace_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class trace__CommandSub(trace_t):
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

    out_node = NewRecord('trace.CommandSub')
    L = out_node.fields

    return out_node

class trace__ForkWait(trace_t):
  _type_tag = 3
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

    out_node = NewRecord('trace.ForkWait')
    L = out_node.fields

    return out_node

class trace__Fork(trace_t):
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

    out_node = NewRecord('trace.Fork')
    L = out_node.fields

    return out_node

class trace__PipelinePart(trace_t):
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

    out_node = NewRecord('trace.PipelinePart')
    L = out_node.fields

    return out_node

class trace__ProcessSub(trace_t):
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

    out_node = NewRecord('trace.ProcessSub')
    L = out_node.fields

    return out_node

class trace__HereDoc(trace_t):
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

    out_node = NewRecord('trace.HereDoc')
    L = out_node.fields

    return out_node

class trace(object):
  class External(trace_t):
    _type_tag = 1
    __slots__ = ('argv',)
  
    def __init__(self, argv):
      # type: (List[str]) -> None
      self.argv = argv
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> trace.External
      return trace.External([] if alloc_lists else cast('List[str]', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('trace.External')
      L = out_node.fields
  
      if self.argv is not None:  # List
        x0 = hnode.Array([])
        for i0 in self.argv:
          x0.children.append(NewLeaf(i0, color_e.StringConst))
        L.append(Field('argv', x0))
  
      return out_node
  
  CommandSub = trace__CommandSub()
  
  ForkWait = trace__ForkWait()
  
  Fork = trace__Fork()
  
  PipelinePart = trace__PipelinePart()
  
  ProcessSub = trace__ProcessSub()
  
  HereDoc = trace__HereDoc()
  
  pass

class word_style_t(pybase.SimpleObj):
  pass

class word_style_e(object):
  Expr = word_style_t(1)
  Unquoted = word_style_t(2)
  DQ = word_style_t(3)
  SQ = word_style_t(4)

_word_style_str = {
  1: 'Expr',
  2: 'Unquoted',
  3: 'DQ',
  4: 'SQ',
}

def word_style_str(val, dot=True):
  # type: (word_style_t, bool) -> str
  v = _word_style_str[val]
  if dot:
    return "word_style.%s" % v
  else:
    return v

class comp_action_t(pybase.SimpleObj):
  pass

class comp_action_e(object):
  Other = comp_action_t(1)
  FileSystem = comp_action_t(2)
  BashFunc = comp_action_t(3)

_comp_action_str = {
  1: 'Other',
  2: 'FileSystem',
  3: 'BashFunc',
}

def comp_action_str(val, dot=True):
  # type: (comp_action_t, bool) -> str
  v = _comp_action_str[val]
  if dot:
    return "comp_action.%s" % v
  else:
    return v

class trap_action_e(object):
  Ignored = 1
  Command = 2

_trap_action_str = {
  1: 'Ignored',
  2: 'Command',
}

def trap_action_str(tag, dot=True):
  # type: (int, bool) -> str
  v = _trap_action_str[tag]
  if dot:
    return "trap_action.%s" % v
  else:
    return v

class trap_action_t(pybase.CompoundObj):
  def tag(self):
    # type: () -> int
    return self._type_tag

class trap_action__Ignored(trap_action_t):
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

    out_node = NewRecord('trap_action.Ignored')
    L = out_node.fields

    return out_node

class trap_action(object):
  Ignored = trap_action__Ignored()
  
  class Command(trap_action_t):
    _type_tag = 2
    __slots__ = ('c',)
  
    def __init__(self, c):
      # type: (command_t) -> None
      self.c = c
  
    @staticmethod
    def CreateNull(alloc_lists=False):
      # type: () -> trap_action.Command
      return trap_action.Command(cast('command_t', None))
  
    def PrettyTree(self, do_abbrev, trav=None):
      # type: (bool, Optional[TraversalState]) -> hnode_t
      trav = trav or TraversalState()
      heap_id = id(self)
      if heap_id in trav.seen:
        return hnode.AlreadySeen(heap_id)
      trav.seen[heap_id] = True
  
      out_node = NewRecord('trap_action.Command')
      L = out_node.fields
  
      assert self.c is not None
      x0 = self.c.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('c', x0))
  
      return out_node
  
  pass

class AssignArg(pybase.CompoundObj):
  _type_tag = 64
  __slots__ = ('var_name', 'rval', 'plus_eq', 'blame_word')

  def __init__(self, var_name, rval, plus_eq, blame_word):
    # type: (str, Optional[value_t], bool, CompoundWord) -> None
    self.var_name = var_name
    self.rval = rval
    self.plus_eq = plus_eq
    self.blame_word = blame_word

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> AssignArg
    return AssignArg('', cast('Optional[value_t]', None), False, cast('CompoundWord', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('AssignArg')
    L = out_node.fields

    x0 = NewLeaf(self.var_name, color_e.StringConst)
    L.append(Field('var_name', x0))

    if self.rval is not None:  # Optional
      x1 = self.rval.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('rval', x1))

    x2 = hnode.Leaf('T' if self.plus_eq else 'F', color_e.OtherConst)
    L.append(Field('plus_eq', x2))

    assert self.blame_word is not None
    x3 = self.blame_word.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('blame_word', x3))

    return out_node

class ProcArgs(pybase.CompoundObj):
  _type_tag = 65
  __slots__ = ('typed_args', 'pos_args', 'named_args', 'block_arg')

  def __init__(self, typed_args, pos_args, named_args, block_arg):
    # type: (ArgList, Optional[List[value_t]], Optional[Dict[str, value_t]], Optional[value_t]) -> None
    self.typed_args = typed_args
    self.pos_args = pos_args
    self.named_args = named_args
    self.block_arg = block_arg

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> ProcArgs
    return ProcArgs(cast('ArgList', None), cast('Optional[List[value_t]]', None), cast('Optional[Dict[str, value_t]]', None), cast('Optional[value_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('ProcArgs')
    L = out_node.fields

    assert self.typed_args is not None
    x0 = self.typed_args.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('typed_args', x0))

    if self.pos_args is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.pos_args:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('pos_args', x1))

    if self.named_args is not None:  # Dict
      unnamed2 = []  # type: List[hnode_t]
      x2 = hnode.Record("", "{", "}", [], unnamed2)
      for k2, v2 in self.named_args.iteritems():
        unnamed2.append(NewLeaf(k2, color_e.StringConst))
        unnamed2.append(v2.PrettyTree(do_abbrev, trav=trav))
      L.append(Field('named_args', x2))

    if self.block_arg is not None:  # Optional
      x3 = self.block_arg.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('block_arg', x3))

    return out_node

class Piece(part_value_t):
  _type_tag = 66
  __slots__ = ('s', 'quoted', 'do_split')

  def __init__(self, s, quoted, do_split):
    # type: (str, bool, bool) -> None
    self.s = s
    self.quoted = quoted
    self.do_split = do_split

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Piece
    return Piece('', False, False)

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Piece')
    L = out_node.fields

    x0 = NewLeaf(self.s, color_e.StringConst)
    L.append(Field('s', x0))

    x1 = hnode.Leaf('T' if self.quoted else 'F', color_e.OtherConst)
    L.append(Field('quoted', x1))

    x2 = hnode.Leaf('T' if self.do_split else 'F', color_e.OtherConst)
    L.append(Field('do_split', x2))

    return out_node

class VarSubState(pybase.CompoundObj):
  _type_tag = 67
  __slots__ = ('join_array', 'h_value', 'array_ref')

  def __init__(self, join_array, h_value, array_ref):
    # type: (bool, value_t, Token) -> None
    self.join_array = join_array
    self.h_value = h_value
    self.array_ref = array_ref

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> VarSubState
    return VarSubState(False, cast('value_t', None), cast('Token', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('VarSubState')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.join_array else 'F', color_e.OtherConst)
    L.append(Field('join_array', x0))

    assert self.h_value is not None
    x1 = self.h_value.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('h_value', x1))

    assert self.array_ref is not None
    x2 = self.array_ref.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('array_ref', x2))

    return out_node

class Cell(pybase.CompoundObj):
  _type_tag = 68
  __slots__ = ('exported', 'readonly', 'nameref', 'val')

  def __init__(self, exported, readonly, nameref, val):
    # type: (bool, bool, bool, value_t) -> None
    self.exported = exported
    self.readonly = readonly
    self.nameref = nameref
    self.val = val

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> Cell
    return Cell(False, False, False, cast('value_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('Cell')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.exported else 'F', color_e.OtherConst)
    L.append(Field('exported', x0))

    x1 = hnode.Leaf('T' if self.readonly else 'F', color_e.OtherConst)
    L.append(Field('readonly', x1))

    x2 = hnode.Leaf('T' if self.nameref else 'F', color_e.OtherConst)
    L.append(Field('nameref', x2))

    assert self.val is not None
    x3 = self.val.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('val', x3))

    return out_node

class VTestPlace(pybase.CompoundObj):
  _type_tag = 69
  __slots__ = ('name', 'index')

  def __init__(self, name, index):
    # type: (Optional[str], Optional[a_index_t]) -> None
    self.name = name
    self.index = index

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> VTestPlace
    return VTestPlace(cast('Optional[str]', None), cast('Optional[a_index_t]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('VTestPlace')
    L = out_node.fields

    if self.name is not None:  # Optional
      x0 = NewLeaf(self.name, color_e.StringConst)
      L.append(Field('name', x0))

    if self.index is not None:  # Optional
      x1 = self.index.PrettyTree(do_abbrev, trav=trav)
      L.append(Field('index', x1))

    return out_node

class RedirValue(pybase.CompoundObj):
  _type_tag = 70
  __slots__ = ('op_id', 'op_loc', 'loc', 'arg')

  def __init__(self, op_id, op_loc, loc, arg):
    # type: (Id_t, loc_t, redir_loc_t, redirect_arg_t) -> None
    self.op_id = op_id
    self.op_loc = op_loc
    self.loc = loc
    self.arg = arg

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> RedirValue
    return RedirValue(-1, cast('loc_t', None), cast('redir_loc_t', None), cast('redirect_arg_t', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('RedirValue')
    L = out_node.fields

    x0 = hnode.Leaf(Id_str(self.op_id, dot=False), color_e.UserType)
    L.append(Field('op_id', x0))

    assert self.op_loc is not None
    x1 = self.op_loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('op_loc', x1))

    assert self.loc is not None
    x2 = self.loc.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('loc', x2))

    assert self.arg is not None
    x3 = self.arg.PrettyTree(do_abbrev, trav=trav)
    L.append(Field('arg', x3))

    return out_node

class StatusArray(pybase.CompoundObj):
  _type_tag = 71
  __slots__ = ('codes', 'locs')

  def __init__(self, codes, locs):
    # type: (Optional[List[int]], Optional[List[loc_t]]) -> None
    self.codes = codes
    self.locs = locs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> StatusArray
    return StatusArray(cast('Optional[List[int]]', None), cast('Optional[List[loc_t]]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('StatusArray')
    L = out_node.fields

    if self.codes is not None:  # List
      x0 = hnode.Array([])
      for i0 in self.codes:
        x0.children.append(hnode.Leaf(str(i0), color_e.OtherConst))
      L.append(Field('codes', x0))

    if self.locs is not None:  # List
      x1 = hnode.Array([])
      for i1 in self.locs:
        h = (hnode.Leaf("_", color_e.OtherConst) if i1 is None else
             i1.PrettyTree(do_abbrev, trav=trav))
        x1.children.append(h)
      L.append(Field('locs', x1))

    return out_node

class CommandStatus(pybase.CompoundObj):
  _type_tag = 72
  __slots__ = ('check_errexit', 'show_code', 'pipe_negated', 'pipe_status',
               'pipe_locs')

  def __init__(self, check_errexit, show_code, pipe_negated, pipe_status,
               pipe_locs):
    # type: (bool, bool, bool, Optional[List[int]], Optional[List[loc_t]]) -> None
    self.check_errexit = check_errexit
    self.show_code = show_code
    self.pipe_negated = pipe_negated
    self.pipe_status = pipe_status
    self.pipe_locs = pipe_locs

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> CommandStatus
    return CommandStatus(False, False, False, cast('Optional[List[int]]', None), cast('Optional[List[loc_t]]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('CommandStatus')
    L = out_node.fields

    x0 = hnode.Leaf('T' if self.check_errexit else 'F', color_e.OtherConst)
    L.append(Field('check_errexit', x0))

    x1 = hnode.Leaf('T' if self.show_code else 'F', color_e.OtherConst)
    L.append(Field('show_code', x1))

    x2 = hnode.Leaf('T' if self.pipe_negated else 'F', color_e.OtherConst)
    L.append(Field('pipe_negated', x2))

    if self.pipe_status is not None:  # List
      x3 = hnode.Array([])
      for i3 in self.pipe_status:
        x3.children.append(hnode.Leaf(str(i3), color_e.OtherConst))
      L.append(Field('pipe_status', x3))

    if self.pipe_locs is not None:  # List
      x4 = hnode.Array([])
      for i4 in self.pipe_locs:
        h = (hnode.Leaf("_", color_e.OtherConst) if i4 is None else
             i4.PrettyTree(do_abbrev, trav=trav))
        x4.children.append(h)
      L.append(Field('pipe_locs', x4))

    return out_node

class HayNode(pybase.CompoundObj):
  _type_tag = 73
  __slots__ = ('children',)

  def __init__(self, children):
    # type: (Dict[str, HayNode]) -> None
    self.children = children

  @staticmethod
  def CreateNull(alloc_lists=False):
    # type: () -> HayNode
    return HayNode(cast('Dict[str, HayNode]', None))

  def PrettyTree(self, do_abbrev, trav=None):
    # type: (bool, Optional[TraversalState]) -> hnode_t
    trav = trav or TraversalState()
    heap_id = id(self)
    if heap_id in trav.seen:
      return hnode.AlreadySeen(heap_id)
    trav.seen[heap_id] = True

    out_node = NewRecord('HayNode')
    L = out_node.fields

    if self.children is not None:  # Dict
      unnamed0 = []  # type: List[hnode_t]
      x0 = hnode.Record("", "{", "}", [], unnamed0)
      for k0, v0 in self.children.iteritems():
        unnamed0.append(NewLeaf(k0, color_e.StringConst))
        unnamed0.append(v0.PrettyTree(do_abbrev, trav=trav))
      L.append(Field('children', x0))

    return out_node

