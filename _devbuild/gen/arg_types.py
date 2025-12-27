
from _devbuild.gen.value_asdl import value, value_e, value_t
from frontend.args import _Attributes
from mycpp import mops
from typing import cast, Dict, Optional


class bind(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.P = cast(value.Bool, attrs['P']).b  # type: bool
    self.S = cast(value.Bool, attrs['S']).b  # type: bool
    self.V = cast(value.Bool, attrs['V']).b  # type: bool
    self.X = cast(value.Bool, attrs['X']).b  # type: bool
    val4 = attrs['f']
    self.f = None if val4.tag() == value_e.Undef else cast(value.Str, val4).s  # type: Optional[str]
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    val6 = attrs['m']
    self.m = None if val6.tag() == value_e.Undef else cast(value.Str, val6).s  # type: Optional[str]
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    val8 = attrs['q']
    self.q = None if val8.tag() == value_e.Undef else cast(value.Str, val8).s  # type: Optional[str]
    val9 = attrs['r']
    self.r = None if val9.tag() == value_e.Undef else cast(value.Str, val9).s  # type: Optional[str]
    self.s = cast(value.Bool, attrs['s']).b  # type: bool
    val11 = attrs['u']
    self.u = None if val11.tag() == value_e.Undef else cast(value.Str, val11).s  # type: Optional[str]
    self.v = cast(value.Bool, attrs['v']).b  # type: bool
    val13 = attrs['x']
    self.x = None if val13.tag() == value_e.Undef else cast(value.Str, val13).s  # type: Optional[str]


class cd(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.L = cast(value.Bool, attrs['L']).b  # type: bool
    self.P = cast(value.Bool, attrs['P']).b  # type: bool


class command(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.V = cast(value.Bool, attrs['V']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    self.v = cast(value.Bool, attrs['v']).b  # type: bool


class compadjust(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['n']
    self.n = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]
    self.s = cast(value.Bool, attrs['s']).b  # type: bool


class compexport(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['begin']
    self.begin = mops.BigInt(-1) if val0.tag() == value_e.Undef else cast(value.Int, val0).i  # type: mops.BigInt
    val1 = attrs['c']
    self.c = None if val1.tag() == value_e.Undef else cast(value.Str, val1).s  # type: Optional[str]
    val2 = attrs['end']
    self.end = mops.BigInt(-1) if val2.tag() == value_e.Undef else cast(value.Int, val2).i  # type: mops.BigInt
    val3 = attrs['format']
    self.format = None if val3.tag() == value_e.Undef else cast(value.Str, val3).s  # type: Optional[str]


class compgen(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['C']
    self.C = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]
    val1 = attrs['F']
    self.F = None if val1.tag() == value_e.Undef else cast(value.Str, val1).s  # type: Optional[str]
    val2 = attrs['P']
    self.P = None if val2.tag() == value_e.Undef else cast(value.Str, val2).s  # type: Optional[str]
    val3 = attrs['S']
    self.S = None if val3.tag() == value_e.Undef else cast(value.Str, val3).s  # type: Optional[str]
    val4 = attrs['W']
    self.W = None if val4.tag() == value_e.Undef else cast(value.Str, val4).s  # type: Optional[str]
    val5 = attrs['X']
    self.X = None if val5.tag() == value_e.Undef else cast(value.Str, val5).s  # type: Optional[str]


class complete(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['C']
    self.C = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]
    self.D = cast(value.Bool, attrs['D']).b  # type: bool
    self.E = cast(value.Bool, attrs['E']).b  # type: bool
    val3 = attrs['F']
    self.F = None if val3.tag() == value_e.Undef else cast(value.Str, val3).s  # type: Optional[str]
    val4 = attrs['P']
    self.P = None if val4.tag() == value_e.Undef else cast(value.Str, val4).s  # type: Optional[str]
    val5 = attrs['S']
    self.S = None if val5.tag() == value_e.Undef else cast(value.Str, val5).s  # type: Optional[str]
    val6 = attrs['W']
    self.W = None if val6.tag() == value_e.Undef else cast(value.Str, val6).s  # type: Optional[str]
    val7 = attrs['X']
    self.X = None if val7.tag() == value_e.Undef else cast(value.Str, val7).s  # type: Optional[str]


class dirs(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.c = cast(value.Bool, attrs['c']).b  # type: bool
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    self.v = cast(value.Bool, attrs['v']).b  # type: bool


class echo(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.e = cast(value.Bool, attrs['e']).b  # type: bool
    self.n = cast(value.Bool, attrs['n']).b  # type: bool


class export_(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.f = cast(value.Bool, attrs['f']).b  # type: bool
    self.n = cast(value.Bool, attrs['n']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool


class fc(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['e']
    self.e = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    self.n = cast(value.Bool, attrs['n']).b  # type: bool
    self.r = cast(value.Bool, attrs['r']).b  # type: bool


class hash(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.r = cast(value.Bool, attrs['r']).b  # type: bool


class history(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.a = cast(value.Bool, attrs['a']).b  # type: bool
    self.c = cast(value.Bool, attrs['c']).b  # type: bool
    val2 = attrs['d']
    self.d = mops.BigInt(-1) if val2.tag() == value_e.Undef else cast(value.Int, val2).i  # type: mops.BigInt
    self.r = cast(value.Bool, attrs['r']).b  # type: bool


class invoke(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.builtin = cast(value.Bool, attrs['builtin']).b  # type: bool
    self.extern_ = cast(value.Bool, attrs['extern_']).b  # type: bool
    self.proc = cast(value.Bool, attrs['proc']).b  # type: bool
    self.sh_func = cast(value.Bool, attrs['sh_func']).b  # type: bool
    self.show = cast(value.Bool, attrs['show']).b  # type: bool


class jobs(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.debug = cast(value.Bool, attrs['debug']).b  # type: bool
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool


class json_write(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['indent']
    self.indent = mops.BigInt(-1) if val0.tag() == value_e.Undef else cast(value.Int, val0).i  # type: mops.BigInt


class kill(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.L = cast(value.Bool, attrs['L']).b  # type: bool
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    val2 = attrs['n']
    self.n = None if val2.tag() == value_e.Undef else cast(value.Str, val2).s  # type: Optional[str]
    val3 = attrs['s']
    self.s = None if val3.tag() == value_e.Undef else cast(value.Str, val3).s  # type: Optional[str]


class main(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['ast_format']
    self.ast_format = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]
    val1 = attrs['c']
    self.c = None if val1.tag() == value_e.Undef else cast(value.Str, val1).s  # type: Optional[str]
    self.completion_demo = cast(value.Bool, attrs['completion_demo']).b  # type: bool
    val3 = attrs['completion_display']
    self.completion_display = None if val3.tag() == value_e.Undef else cast(value.Str, val3).s  # type: Optional[str]
    val4 = attrs['debug_file']
    self.debug_file = None if val4.tag() == value_e.Undef else cast(value.Str, val4).s  # type: Optional[str]
    self.do_lossless = cast(value.Bool, attrs['do_lossless']).b  # type: bool
    self.headless = cast(value.Bool, attrs['headless']).b  # type: bool
    self.help = cast(value.Bool, attrs['help']).b  # type: bool
    self.i = cast(value.Bool, attrs['i']).b  # type: bool
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    val10 = attrs['location_start_line']
    self.location_start_line = mops.BigInt(-1) if val10.tag() == value_e.Undef else cast(value.Int, val10).i  # type: mops.BigInt
    val11 = attrs['location_str']
    self.location_str = None if val11.tag() == value_e.Undef else cast(value.Str, val11).s  # type: Optional[str]
    self.login = cast(value.Bool, attrs['login']).b  # type: bool
    self.norc = cast(value.Bool, attrs['norc']).b  # type: bool
    self.print_status = cast(value.Bool, attrs['print_status']).b  # type: bool
    val15 = attrs['rcdir']
    self.rcdir = None if val15.tag() == value_e.Undef else cast(value.Str, val15).s  # type: Optional[str]
    val16 = attrs['rcfile']
    self.rcfile = None if val16.tag() == value_e.Undef else cast(value.Str, val16).s  # type: Optional[str]
    val17 = attrs['tool']
    self.tool = None if val17.tag() == value_e.Undef else cast(value.Str, val17).s  # type: Optional[str]
    self.version = cast(value.Bool, attrs['version']).b  # type: bool
    self.xtrace_to_debug_file = cast(value.Bool, attrs['xtrace_to_debug_file']).b  # type: bool


class mapfile(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.t = cast(value.Bool, attrs['t']).b  # type: bool


class new_var(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.A = cast(value.Bool, attrs['A']).b  # type: bool
    self.F = cast(value.Bool, attrs['F']).b  # type: bool
    self.a = cast(value.Bool, attrs['a']).b  # type: bool
    self.f = cast(value.Bool, attrs['f']).b  # type: bool
    self.g = cast(value.Bool, attrs['g']).b  # type: bool
    self.i = cast(value.Bool, attrs['i']).b  # type: bool
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    val7 = attrs['n']
    self.n = None if val7.tag() == value_e.Undef else cast(value.Str, val7).s  # type: Optional[str]
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    val9 = attrs['r']
    self.r = None if val9.tag() == value_e.Undef else cast(value.Str, val9).s  # type: Optional[str]
    self.u = cast(value.Bool, attrs['u']).b  # type: bool
    val11 = attrs['x']
    self.x = None if val11.tag() == value_e.Undef else cast(value.Str, val11).s  # type: Optional[str]


class printf(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['v']
    self.v = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]


class pwd(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.L = cast(value.Bool, attrs['L']).b  # type: bool
    self.P = cast(value.Bool, attrs['P']).b  # type: bool


class read(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['N']
    self.N = mops.BigInt(-1) if val0.tag() == value_e.Undef else cast(value.Int, val0).i  # type: mops.BigInt
    self.Z = cast(value.Bool, attrs['Z']).b  # type: bool
    val2 = attrs['a']
    self.a = None if val2.tag() == value_e.Undef else cast(value.Str, val2).s  # type: Optional[str]
    self.all = cast(value.Bool, attrs['all']).b  # type: bool
    val4 = attrs['d']
    self.d = None if val4.tag() == value_e.Undef else cast(value.Str, val4).s  # type: Optional[str]
    val5 = attrs['n']
    self.n = mops.BigInt(-1) if val5.tag() == value_e.Undef else cast(value.Int, val5).i  # type: mops.BigInt
    val6 = attrs['num_bytes']
    self.num_bytes = mops.BigInt(-1) if val6.tag() == value_e.Undef else cast(value.Int, val6).i  # type: mops.BigInt
    val7 = attrs['p']
    self.p = None if val7.tag() == value_e.Undef else cast(value.Str, val7).s  # type: Optional[str]
    self.r = cast(value.Bool, attrs['r']).b  # type: bool
    self.raw_line = cast(value.Bool, attrs['raw_line']).b  # type: bool
    self.s = cast(value.Bool, attrs['s']).b  # type: bool
    val11 = attrs['t']
    self.t = -1.0 if val11.tag() == value_e.Undef else cast(value.Float, val11).f  # type: float
    val12 = attrs['u']
    self.u = mops.BigInt(-1) if val12.tag() == value_e.Undef else cast(value.Int, val12).i  # type: mops.BigInt
    self.with_eol = cast(value.Bool, attrs['with_eol']).b  # type: bool


class readonly(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.A = cast(value.Bool, attrs['A']).b  # type: bool
    self.a = cast(value.Bool, attrs['a']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool


class rm(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.f = cast(value.Bool, attrs['f']).b  # type: bool


class runproc(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.h = cast(value.Bool, attrs['h']).b  # type: bool


class shopt(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.o = cast(value.Bool, attrs['o']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    self.q = cast(value.Bool, attrs['q']).b  # type: bool
    self.s = cast(value.Bool, attrs['s']).b  # type: bool
    self.u = cast(value.Bool, attrs['u']).b  # type: bool


class source(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.builtin = cast(value.Bool, attrs['builtin']).b  # type: bool


class trap(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.add = cast(value.Bool, attrs['add']).b  # type: bool
    self.ignore = cast(value.Bool, attrs['ignore']).b  # type: bool
    self.l = cast(value.Bool, attrs['l']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    self.remove = cast(value.Bool, attrs['remove']).b  # type: bool


class try_(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['assign']
    self.assign = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]


class type(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.P = cast(value.Bool, attrs['P']).b  # type: bool
    self.a = cast(value.Bool, attrs['a']).b  # type: bool
    self.f = cast(value.Bool, attrs['f']).b  # type: bool
    self.p = cast(value.Bool, attrs['p']).b  # type: bool
    self.t = cast(value.Bool, attrs['t']).b  # type: bool


class ulimit(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.H = cast(value.Bool, attrs['H']).b  # type: bool
    self.S = cast(value.Bool, attrs['S']).b  # type: bool
    self.a = cast(value.Bool, attrs['a']).b  # type: bool
    self.all = cast(value.Bool, attrs['all']).b  # type: bool
    self.c = cast(value.Bool, attrs['c']).b  # type: bool
    self.d = cast(value.Bool, attrs['d']).b  # type: bool
    self.f = cast(value.Bool, attrs['f']).b  # type: bool
    self.n = cast(value.Bool, attrs['n']).b  # type: bool
    self.s = cast(value.Bool, attrs['s']).b  # type: bool
    self.t = cast(value.Bool, attrs['t']).b  # type: bool
    self.v = cast(value.Bool, attrs['v']).b  # type: bool


class unalias(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.a = cast(value.Bool, attrs['a']).b  # type: bool


class unset(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.f = cast(value.Bool, attrs['f']).b  # type: bool
    self.v = cast(value.Bool, attrs['v']).b  # type: bool


class use(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.extern_ = cast(value.Bool, attrs['extern_']).b  # type: bool


class wait(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    self.all = cast(value.Bool, attrs['all']).b  # type: bool
    self.n = cast(value.Bool, attrs['n']).b  # type: bool
    self.verbose = cast(value.Bool, attrs['verbose']).b  # type: bool


class write(object):
  def __init__(self, attrs):
    # type: (Dict[str, value_t]) -> None

    val0 = attrs['end']
    self.end = None if val0.tag() == value_e.Undef else cast(value.Str, val0).s  # type: Optional[str]
    self.j8 = cast(value.Bool, attrs['j8']).b  # type: bool
    self.json = cast(value.Bool, attrs['json']).b  # type: bool
    self.n = cast(value.Bool, attrs['n']).b  # type: bool
    val4 = attrs['sep']
    self.sep = None if val4.tag() == value_e.Undef else cast(value.Str, val4).s  # type: Optional[str]

