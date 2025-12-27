from asdl import pybase

Id_t = int  # type alias for integer

class Id(object):
  Word_Compound = 1
  Arith_Semi = 2
  Arith_Comma = 3
  Arith_Plus = 4
  Arith_Minus = 5
  Arith_Star = 6
  Arith_Slash = 7
  Arith_Percent = 8
  Arith_DPlus = 9
  Arith_DMinus = 10
  Arith_DStar = 11
  Arith_LParen = 12
  Arith_RParen = 13
  Arith_LBracket = 14
  Arith_RBracket = 15
  Arith_RBrace = 16
  Arith_QMark = 17
  Arith_Colon = 18
  Arith_LessEqual = 19
  Arith_Less = 20
  Arith_GreatEqual = 21
  Arith_Great = 22
  Arith_DEqual = 23
  Arith_NEqual = 24
  Arith_DAmp = 25
  Arith_DPipe = 26
  Arith_Bang = 27
  Arith_DGreat = 28
  Arith_DLess = 29
  Arith_Amp = 30
  Arith_Pipe = 31
  Arith_Caret = 32
  Arith_Tilde = 33
  Arith_Equal = 34
  Arith_PlusEqual = 35
  Arith_MinusEqual = 36
  Arith_StarEqual = 37
  Arith_SlashEqual = 38
  Arith_PercentEqual = 39
  Arith_DGreatEqual = 40
  Arith_DLessEqual = 41
  Arith_AmpEqual = 42
  Arith_CaretEqual = 43
  Arith_PipeEqual = 44
  Eof_Real = 45
  Eof_RParen = 46
  Eof_Backtick = 47
  Undefined_Tok = 48
  Unknown_Tok = 49
  Unknown_Backslash = 50
  Unknown_DEqual = 51
  Unknown_DAmp = 52
  Unknown_DPipe = 53
  Unknown_DDot = 54
  Eol_Tok = 55
  Ignored_LineCont = 56
  Ignored_Space = 57
  Ignored_Comment = 58
  Ignored_Newline = 59
  WS_Space = 60
  Lit_Chars = 61
  Lit_CharsWithoutPrefix = 62
  Lit_VarLike = 63
  Lit_ArrayLhsOpen = 64
  Lit_ArrayLhsClose = 65
  Lit_Splice = 66
  Lit_AtLBracket = 67
  Lit_AtLBraceDot = 68
  Lit_Other = 69
  Lit_EscapedChar = 70
  Lit_BackslashDoubleQuote = 71
  Lit_LBracket = 72
  Lit_RBracket = 73
  Lit_Star = 74
  Lit_QMark = 75
  Lit_LBrace = 76
  Lit_RBrace = 77
  Lit_Comma = 78
  Lit_Equals = 79
  Lit_Dollar = 80
  Lit_DRightBracket = 81
  Lit_Tilde = 82
  Lit_Pound = 83
  Lit_TPound = 84
  Lit_TDot = 85
  Lit_Slash = 86
  Lit_Percent = 87
  Lit_Colon = 88
  Lit_Digits = 89
  Lit_At = 90
  Lit_ArithVarLike = 91
  Lit_BadBackslash = 92
  Lit_CompDummy = 93
  Lit_Number = 94
  Lit_RedirVarName = 95
  Backtick_Right = 96
  Backtick_Quoted = 97
  Backtick_DoubleQuote = 98
  Backtick_Other = 99
  History_Op = 100
  History_Num = 101
  History_Search = 102
  History_Other = 103
  Op_Newline = 104
  Op_Amp = 105
  Op_Pipe = 106
  Op_PipeAmp = 107
  Op_DAmp = 108
  Op_DPipe = 109
  Op_Semi = 110
  Op_DSemi = 111
  Op_SemiAmp = 112
  Op_DSemiAmp = 113
  Op_LParen = 114
  Op_RParen = 115
  Op_DLeftParen = 116
  Op_DRightParen = 117
  Op_Less = 118
  Op_Great = 119
  Op_Bang = 120
  Op_LBracket = 121
  Op_RBracket = 122
  Op_LBrace = 123
  Op_RBrace = 124
  Expr_Reserved = 125
  Expr_Symbol = 126
  Expr_Name = 127
  Expr_DecInt = 128
  Expr_BinInt = 129
  Expr_OctInt = 130
  Expr_HexInt = 131
  Expr_Float = 132
  Expr_Bang = 133
  Expr_Dot = 134
  Expr_DDotLessThan = 135
  Expr_DDotEqual = 136
  Expr_Colon = 137
  Expr_RArrow = 138
  Expr_RDArrow = 139
  Expr_DSlash = 140
  Expr_TEqual = 141
  Expr_NotDEqual = 142
  Expr_TildeDEqual = 143
  Expr_At = 144
  Expr_DoubleAt = 145
  Expr_Ellipsis = 146
  Expr_Dollar = 147
  Expr_NotTilde = 148
  Expr_DTilde = 149
  Expr_NotDTilde = 150
  Expr_DStarEqual = 151
  Expr_DSlashEqual = 152
  Expr_CastedDummy = 153
  Expr_Null = 154
  Expr_True = 155
  Expr_False = 156
  Expr_And = 157
  Expr_Or = 158
  Expr_Not = 159
  Expr_For = 160
  Expr_Is = 161
  Expr_In = 162
  Expr_If = 163
  Expr_Else = 164
  Expr_Capture = 165
  Expr_As = 166
  Expr_Func = 167
  Expr_Proc = 168
  Char_OneChar = 169
  Char_Stop = 170
  Char_Hex = 171
  Char_YHex = 172
  Char_Octal3 = 173
  Char_Octal4 = 174
  Char_Unicode4 = 175
  Char_SurrogatePair = 176
  Char_Unicode8 = 177
  Char_UBraced = 178
  Char_Pound = 179
  Char_AsciiControl = 180
  BashRegex_LParen = 181
  BashRegex_AllowedInParens = 182
  Eggex_Start = 183
  Eggex_End = 184
  Eggex_Dot = 185
  Redir_Less = 186
  Redir_Great = 187
  Redir_DLess = 188
  Redir_TLess = 189
  Redir_DGreat = 190
  Redir_GreatAnd = 191
  Redir_LessAnd = 192
  Redir_DLessDash = 193
  Redir_LessGreat = 194
  Redir_Clobber = 195
  Redir_AndGreat = 196
  Redir_AndDGreat = 197
  Left_DoubleQuote = 198
  Left_JDoubleQuote = 199
  Left_SingleQuote = 200
  Left_DollarSingleQuote = 201
  Left_RSingleQuote = 202
  Left_USingleQuote = 203
  Left_BSingleQuote = 204
  Left_TDoubleQuote = 205
  Left_DollarTDoubleQuote = 206
  Left_TSingleQuote = 207
  Left_RTSingleQuote = 208
  Left_UTSingleQuote = 209
  Left_BTSingleQuote = 210
  Left_Backtick = 211
  Left_DollarParen = 212
  Left_DollarBrace = 213
  Left_DollarBraceZsh = 214
  Left_DollarDParen = 215
  Left_DollarBracket = 216
  Left_AtBracket = 217
  Left_DollarDoubleQuote = 218
  Left_ProcSubIn = 219
  Left_ProcSubOut = 220
  Left_AtParen = 221
  Left_CaretParen = 222
  Left_CaretBracket = 223
  Left_CaretBrace = 224
  Left_CaretDoubleQuote = 225
  Left_ColonPipe = 226
  Left_PercentParen = 227
  Right_DoubleQuote = 228
  Right_SingleQuote = 229
  Right_Backtick = 230
  Right_DollarBrace = 231
  Right_DollarDParen = 232
  Right_DollarDoubleQuote = 233
  Right_DollarSingleQuote = 234
  Right_Subshell = 235
  Right_ShFunction = 236
  Right_CasePat = 237
  Right_Initializer = 238
  Right_ExtGlob = 239
  Right_BashRegexGroup = 240
  Right_BlockLiteral = 241
  ExtGlob_Comma = 242
  ExtGlob_At = 243
  ExtGlob_Star = 244
  ExtGlob_Plus = 245
  ExtGlob_QMark = 246
  ExtGlob_Bang = 247
  VSub_DollarName = 248
  VSub_Name = 249
  VSub_Number = 250
  VSub_Bang = 251
  VSub_At = 252
  VSub_Pound = 253
  VSub_Dollar = 254
  VSub_Star = 255
  VSub_Hyphen = 256
  VSub_QMark = 257
  VSub_Dot = 258
  VTest_ColonHyphen = 259
  VTest_Hyphen = 260
  VTest_ColonEquals = 261
  VTest_Equals = 262
  VTest_ColonQMark = 263
  VTest_QMark = 264
  VTest_ColonPlus = 265
  VTest_Plus = 266
  VOp0_Q = 267
  VOp0_E = 268
  VOp0_P = 269
  VOp0_A = 270
  VOp0_a = 271
  VOp1_Percent = 272
  VOp1_DPercent = 273
  VOp1_Pound = 274
  VOp1_DPound = 275
  VOp1_Caret = 276
  VOp1_DCaret = 277
  VOp1_Comma = 278
  VOp1_DComma = 279
  VOpYsh_Pipe = 280
  VOpYsh_Space = 281
  VOp2_Slash = 282
  VOp2_Colon = 283
  VOp2_LBracket = 284
  VOp2_RBracket = 285
  VOp3_At = 286
  VOp3_Star = 287
  Node_PostDPlus = 288
  Node_PostDMinus = 289
  Node_UnaryPlus = 290
  Node_UnaryMinus = 291
  Node_NotIn = 292
  Node_IsNot = 293
  KW_DLeftBracket = 294
  KW_Bang = 295
  KW_For = 296
  KW_While = 297
  KW_Until = 298
  KW_Do = 299
  KW_Done = 300
  KW_In = 301
  KW_Case = 302
  KW_Esac = 303
  KW_If = 304
  KW_Fi = 305
  KW_Then = 306
  KW_Else = 307
  KW_Elif = 308
  KW_Function = 309
  KW_Time = 310
  KW_Const = 311
  KW_Var = 312
  KW_SetVar = 313
  KW_SetGlobal = 314
  KW_Call = 315
  KW_Proc = 316
  KW_Typed = 317
  KW_Func = 318
  ControlFlow_Break = 319
  ControlFlow_Continue = 320
  ControlFlow_Return = 321
  ControlFlow_Exit = 322
  LookAhead_FuncParens = 323
  Glob_LBracket = 324
  Glob_RBracket = 325
  Glob_Star = 326
  Glob_QMark = 327
  Glob_Bang = 328
  Glob_Caret = 329
  Glob_EscapedChar = 330
  Glob_BadBackslash = 331
  Glob_CleanLiterals = 332
  Glob_OtherLiteral = 333
  Format_EscapedPercent = 334
  Format_Percent = 335
  Format_Flag = 336
  Format_Num = 337
  Format_Dot = 338
  Format_Type = 339
  Format_Star = 340
  Format_Time = 341
  Format_Zero = 342
  PS_Subst = 343
  PS_Octal3 = 344
  PS_LBrace = 345
  PS_RBrace = 346
  PS_Literals = 347
  PS_BadBackslash = 348
  Range_Int = 349
  Range_Char = 350
  Range_Dots = 351
  Range_Other = 352
  J8_LBracket = 353
  J8_RBracket = 354
  J8_LBrace = 355
  J8_RBrace = 356
  J8_Comma = 357
  J8_Colon = 358
  J8_Null = 359
  J8_Bool = 360
  J8_Int = 361
  J8_Float = 362
  J8_String = 363
  J8_Identifier = 364
  J8_Newline = 365
  J8_Tab = 366
  J8_LParen = 367
  J8_RParen = 368
  J8_Operator = 369
  ShNumber_Dec = 370
  ShNumber_Hex = 371
  ShNumber_Oct = 372
  ShNumber_BaseN = 373
  BoolUnary_z = 374
  BoolUnary_n = 375
  BoolUnary_o = 376
  BoolUnary_t = 377
  BoolUnary_v = 378
  BoolUnary_R = 379
  BoolUnary_a = 380
  BoolUnary_b = 381
  BoolUnary_c = 382
  BoolUnary_d = 383
  BoolUnary_e = 384
  BoolUnary_f = 385
  BoolUnary_g = 386
  BoolUnary_h = 387
  BoolUnary_k = 388
  BoolUnary_L = 389
  BoolUnary_p = 390
  BoolUnary_r = 391
  BoolUnary_s = 392
  BoolUnary_S = 393
  BoolUnary_u = 394
  BoolUnary_w = 395
  BoolUnary_x = 396
  BoolUnary_O = 397
  BoolUnary_G = 398
  BoolUnary_N = 399
  BoolUnary_true = 400
  BoolUnary_false = 401
  BoolBinary_GlobEqual = 402
  BoolBinary_GlobDEqual = 403
  BoolBinary_GlobNEqual = 404
  BoolBinary_EqualTilde = 405
  BoolBinary_ef = 406
  BoolBinary_nt = 407
  BoolBinary_ot = 408
  BoolBinary_eq = 409
  BoolBinary_ne = 410
  BoolBinary_gt = 411
  BoolBinary_ge = 412
  BoolBinary_lt = 413
  BoolBinary_le = 414
  BoolBinary_Equal = 415
  BoolBinary_DEqual = 416
  BoolBinary_NEqual = 417
  ARRAY_SIZE = 418

_Id_str = {
  1: 'Word_Compound',
  2: 'Arith_Semi',
  3: 'Arith_Comma',
  4: 'Arith_Plus',
  5: 'Arith_Minus',
  6: 'Arith_Star',
  7: 'Arith_Slash',
  8: 'Arith_Percent',
  9: 'Arith_DPlus',
  10: 'Arith_DMinus',
  11: 'Arith_DStar',
  12: 'Arith_LParen',
  13: 'Arith_RParen',
  14: 'Arith_LBracket',
  15: 'Arith_RBracket',
  16: 'Arith_RBrace',
  17: 'Arith_QMark',
  18: 'Arith_Colon',
  19: 'Arith_LessEqual',
  20: 'Arith_Less',
  21: 'Arith_GreatEqual',
  22: 'Arith_Great',
  23: 'Arith_DEqual',
  24: 'Arith_NEqual',
  25: 'Arith_DAmp',
  26: 'Arith_DPipe',
  27: 'Arith_Bang',
  28: 'Arith_DGreat',
  29: 'Arith_DLess',
  30: 'Arith_Amp',
  31: 'Arith_Pipe',
  32: 'Arith_Caret',
  33: 'Arith_Tilde',
  34: 'Arith_Equal',
  35: 'Arith_PlusEqual',
  36: 'Arith_MinusEqual',
  37: 'Arith_StarEqual',
  38: 'Arith_SlashEqual',
  39: 'Arith_PercentEqual',
  40: 'Arith_DGreatEqual',
  41: 'Arith_DLessEqual',
  42: 'Arith_AmpEqual',
  43: 'Arith_CaretEqual',
  44: 'Arith_PipeEqual',
  45: 'Eof_Real',
  46: 'Eof_RParen',
  47: 'Eof_Backtick',
  48: 'Undefined_Tok',
  49: 'Unknown_Tok',
  50: 'Unknown_Backslash',
  51: 'Unknown_DEqual',
  52: 'Unknown_DAmp',
  53: 'Unknown_DPipe',
  54: 'Unknown_DDot',
  55: 'Eol_Tok',
  56: 'Ignored_LineCont',
  57: 'Ignored_Space',
  58: 'Ignored_Comment',
  59: 'Ignored_Newline',
  60: 'WS_Space',
  61: 'Lit_Chars',
  62: 'Lit_CharsWithoutPrefix',
  63: 'Lit_VarLike',
  64: 'Lit_ArrayLhsOpen',
  65: 'Lit_ArrayLhsClose',
  66: 'Lit_Splice',
  67: 'Lit_AtLBracket',
  68: 'Lit_AtLBraceDot',
  69: 'Lit_Other',
  70: 'Lit_EscapedChar',
  71: 'Lit_BackslashDoubleQuote',
  72: 'Lit_LBracket',
  73: 'Lit_RBracket',
  74: 'Lit_Star',
  75: 'Lit_QMark',
  76: 'Lit_LBrace',
  77: 'Lit_RBrace',
  78: 'Lit_Comma',
  79: 'Lit_Equals',
  80: 'Lit_Dollar',
  81: 'Lit_DRightBracket',
  82: 'Lit_Tilde',
  83: 'Lit_Pound',
  84: 'Lit_TPound',
  85: 'Lit_TDot',
  86: 'Lit_Slash',
  87: 'Lit_Percent',
  88: 'Lit_Colon',
  89: 'Lit_Digits',
  90: 'Lit_At',
  91: 'Lit_ArithVarLike',
  92: 'Lit_BadBackslash',
  93: 'Lit_CompDummy',
  94: 'Lit_Number',
  95: 'Lit_RedirVarName',
  96: 'Backtick_Right',
  97: 'Backtick_Quoted',
  98: 'Backtick_DoubleQuote',
  99: 'Backtick_Other',
  100: 'History_Op',
  101: 'History_Num',
  102: 'History_Search',
  103: 'History_Other',
  104: 'Op_Newline',
  105: 'Op_Amp',
  106: 'Op_Pipe',
  107: 'Op_PipeAmp',
  108: 'Op_DAmp',
  109: 'Op_DPipe',
  110: 'Op_Semi',
  111: 'Op_DSemi',
  112: 'Op_SemiAmp',
  113: 'Op_DSemiAmp',
  114: 'Op_LParen',
  115: 'Op_RParen',
  116: 'Op_DLeftParen',
  117: 'Op_DRightParen',
  118: 'Op_Less',
  119: 'Op_Great',
  120: 'Op_Bang',
  121: 'Op_LBracket',
  122: 'Op_RBracket',
  123: 'Op_LBrace',
  124: 'Op_RBrace',
  125: 'Expr_Reserved',
  126: 'Expr_Symbol',
  127: 'Expr_Name',
  128: 'Expr_DecInt',
  129: 'Expr_BinInt',
  130: 'Expr_OctInt',
  131: 'Expr_HexInt',
  132: 'Expr_Float',
  133: 'Expr_Bang',
  134: 'Expr_Dot',
  135: 'Expr_DDotLessThan',
  136: 'Expr_DDotEqual',
  137: 'Expr_Colon',
  138: 'Expr_RArrow',
  139: 'Expr_RDArrow',
  140: 'Expr_DSlash',
  141: 'Expr_TEqual',
  142: 'Expr_NotDEqual',
  143: 'Expr_TildeDEqual',
  144: 'Expr_At',
  145: 'Expr_DoubleAt',
  146: 'Expr_Ellipsis',
  147: 'Expr_Dollar',
  148: 'Expr_NotTilde',
  149: 'Expr_DTilde',
  150: 'Expr_NotDTilde',
  151: 'Expr_DStarEqual',
  152: 'Expr_DSlashEqual',
  153: 'Expr_CastedDummy',
  154: 'Expr_Null',
  155: 'Expr_True',
  156: 'Expr_False',
  157: 'Expr_And',
  158: 'Expr_Or',
  159: 'Expr_Not',
  160: 'Expr_For',
  161: 'Expr_Is',
  162: 'Expr_In',
  163: 'Expr_If',
  164: 'Expr_Else',
  165: 'Expr_Capture',
  166: 'Expr_As',
  167: 'Expr_Func',
  168: 'Expr_Proc',
  169: 'Char_OneChar',
  170: 'Char_Stop',
  171: 'Char_Hex',
  172: 'Char_YHex',
  173: 'Char_Octal3',
  174: 'Char_Octal4',
  175: 'Char_Unicode4',
  176: 'Char_SurrogatePair',
  177: 'Char_Unicode8',
  178: 'Char_UBraced',
  179: 'Char_Pound',
  180: 'Char_AsciiControl',
  181: 'BashRegex_LParen',
  182: 'BashRegex_AllowedInParens',
  183: 'Eggex_Start',
  184: 'Eggex_End',
  185: 'Eggex_Dot',
  186: 'Redir_Less',
  187: 'Redir_Great',
  188: 'Redir_DLess',
  189: 'Redir_TLess',
  190: 'Redir_DGreat',
  191: 'Redir_GreatAnd',
  192: 'Redir_LessAnd',
  193: 'Redir_DLessDash',
  194: 'Redir_LessGreat',
  195: 'Redir_Clobber',
  196: 'Redir_AndGreat',
  197: 'Redir_AndDGreat',
  198: 'Left_DoubleQuote',
  199: 'Left_JDoubleQuote',
  200: 'Left_SingleQuote',
  201: 'Left_DollarSingleQuote',
  202: 'Left_RSingleQuote',
  203: 'Left_USingleQuote',
  204: 'Left_BSingleQuote',
  205: 'Left_TDoubleQuote',
  206: 'Left_DollarTDoubleQuote',
  207: 'Left_TSingleQuote',
  208: 'Left_RTSingleQuote',
  209: 'Left_UTSingleQuote',
  210: 'Left_BTSingleQuote',
  211: 'Left_Backtick',
  212: 'Left_DollarParen',
  213: 'Left_DollarBrace',
  214: 'Left_DollarBraceZsh',
  215: 'Left_DollarDParen',
  216: 'Left_DollarBracket',
  217: 'Left_AtBracket',
  218: 'Left_DollarDoubleQuote',
  219: 'Left_ProcSubIn',
  220: 'Left_ProcSubOut',
  221: 'Left_AtParen',
  222: 'Left_CaretParen',
  223: 'Left_CaretBracket',
  224: 'Left_CaretBrace',
  225: 'Left_CaretDoubleQuote',
  226: 'Left_ColonPipe',
  227: 'Left_PercentParen',
  228: 'Right_DoubleQuote',
  229: 'Right_SingleQuote',
  230: 'Right_Backtick',
  231: 'Right_DollarBrace',
  232: 'Right_DollarDParen',
  233: 'Right_DollarDoubleQuote',
  234: 'Right_DollarSingleQuote',
  235: 'Right_Subshell',
  236: 'Right_ShFunction',
  237: 'Right_CasePat',
  238: 'Right_Initializer',
  239: 'Right_ExtGlob',
  240: 'Right_BashRegexGroup',
  241: 'Right_BlockLiteral',
  242: 'ExtGlob_Comma',
  243: 'ExtGlob_At',
  244: 'ExtGlob_Star',
  245: 'ExtGlob_Plus',
  246: 'ExtGlob_QMark',
  247: 'ExtGlob_Bang',
  248: 'VSub_DollarName',
  249: 'VSub_Name',
  250: 'VSub_Number',
  251: 'VSub_Bang',
  252: 'VSub_At',
  253: 'VSub_Pound',
  254: 'VSub_Dollar',
  255: 'VSub_Star',
  256: 'VSub_Hyphen',
  257: 'VSub_QMark',
  258: 'VSub_Dot',
  259: 'VTest_ColonHyphen',
  260: 'VTest_Hyphen',
  261: 'VTest_ColonEquals',
  262: 'VTest_Equals',
  263: 'VTest_ColonQMark',
  264: 'VTest_QMark',
  265: 'VTest_ColonPlus',
  266: 'VTest_Plus',
  267: 'VOp0_Q',
  268: 'VOp0_E',
  269: 'VOp0_P',
  270: 'VOp0_A',
  271: 'VOp0_a',
  272: 'VOp1_Percent',
  273: 'VOp1_DPercent',
  274: 'VOp1_Pound',
  275: 'VOp1_DPound',
  276: 'VOp1_Caret',
  277: 'VOp1_DCaret',
  278: 'VOp1_Comma',
  279: 'VOp1_DComma',
  280: 'VOpYsh_Pipe',
  281: 'VOpYsh_Space',
  282: 'VOp2_Slash',
  283: 'VOp2_Colon',
  284: 'VOp2_LBracket',
  285: 'VOp2_RBracket',
  286: 'VOp3_At',
  287: 'VOp3_Star',
  288: 'Node_PostDPlus',
  289: 'Node_PostDMinus',
  290: 'Node_UnaryPlus',
  291: 'Node_UnaryMinus',
  292: 'Node_NotIn',
  293: 'Node_IsNot',
  294: 'KW_DLeftBracket',
  295: 'KW_Bang',
  296: 'KW_For',
  297: 'KW_While',
  298: 'KW_Until',
  299: 'KW_Do',
  300: 'KW_Done',
  301: 'KW_In',
  302: 'KW_Case',
  303: 'KW_Esac',
  304: 'KW_If',
  305: 'KW_Fi',
  306: 'KW_Then',
  307: 'KW_Else',
  308: 'KW_Elif',
  309: 'KW_Function',
  310: 'KW_Time',
  311: 'KW_Const',
  312: 'KW_Var',
  313: 'KW_SetVar',
  314: 'KW_SetGlobal',
  315: 'KW_Call',
  316: 'KW_Proc',
  317: 'KW_Typed',
  318: 'KW_Func',
  319: 'ControlFlow_Break',
  320: 'ControlFlow_Continue',
  321: 'ControlFlow_Return',
  322: 'ControlFlow_Exit',
  323: 'LookAhead_FuncParens',
  324: 'Glob_LBracket',
  325: 'Glob_RBracket',
  326: 'Glob_Star',
  327: 'Glob_QMark',
  328: 'Glob_Bang',
  329: 'Glob_Caret',
  330: 'Glob_EscapedChar',
  331: 'Glob_BadBackslash',
  332: 'Glob_CleanLiterals',
  333: 'Glob_OtherLiteral',
  334: 'Format_EscapedPercent',
  335: 'Format_Percent',
  336: 'Format_Flag',
  337: 'Format_Num',
  338: 'Format_Dot',
  339: 'Format_Type',
  340: 'Format_Star',
  341: 'Format_Time',
  342: 'Format_Zero',
  343: 'PS_Subst',
  344: 'PS_Octal3',
  345: 'PS_LBrace',
  346: 'PS_RBrace',
  347: 'PS_Literals',
  348: 'PS_BadBackslash',
  349: 'Range_Int',
  350: 'Range_Char',
  351: 'Range_Dots',
  352: 'Range_Other',
  353: 'J8_LBracket',
  354: 'J8_RBracket',
  355: 'J8_LBrace',
  356: 'J8_RBrace',
  357: 'J8_Comma',
  358: 'J8_Colon',
  359: 'J8_Null',
  360: 'J8_Bool',
  361: 'J8_Int',
  362: 'J8_Float',
  363: 'J8_String',
  364: 'J8_Identifier',
  365: 'J8_Newline',
  366: 'J8_Tab',
  367: 'J8_LParen',
  368: 'J8_RParen',
  369: 'J8_Operator',
  370: 'ShNumber_Dec',
  371: 'ShNumber_Hex',
  372: 'ShNumber_Oct',
  373: 'ShNumber_BaseN',
  374: 'BoolUnary_z',
  375: 'BoolUnary_n',
  376: 'BoolUnary_o',
  377: 'BoolUnary_t',
  378: 'BoolUnary_v',
  379: 'BoolUnary_R',
  380: 'BoolUnary_a',
  381: 'BoolUnary_b',
  382: 'BoolUnary_c',
  383: 'BoolUnary_d',
  384: 'BoolUnary_e',
  385: 'BoolUnary_f',
  386: 'BoolUnary_g',
  387: 'BoolUnary_h',
  388: 'BoolUnary_k',
  389: 'BoolUnary_L',
  390: 'BoolUnary_p',
  391: 'BoolUnary_r',
  392: 'BoolUnary_s',
  393: 'BoolUnary_S',
  394: 'BoolUnary_u',
  395: 'BoolUnary_w',
  396: 'BoolUnary_x',
  397: 'BoolUnary_O',
  398: 'BoolUnary_G',
  399: 'BoolUnary_N',
  400: 'BoolUnary_true',
  401: 'BoolUnary_false',
  402: 'BoolBinary_GlobEqual',
  403: 'BoolBinary_GlobDEqual',
  404: 'BoolBinary_GlobNEqual',
  405: 'BoolBinary_EqualTilde',
  406: 'BoolBinary_ef',
  407: 'BoolBinary_nt',
  408: 'BoolBinary_ot',
  409: 'BoolBinary_eq',
  410: 'BoolBinary_ne',
  411: 'BoolBinary_gt',
  412: 'BoolBinary_ge',
  413: 'BoolBinary_lt',
  414: 'BoolBinary_le',
  415: 'BoolBinary_Equal',
  416: 'BoolBinary_DEqual',
  417: 'BoolBinary_NEqual',
}

def Id_str(val, dot=True):
  # type: (Id_t, bool) -> str
  v = _Id_str[val]
  if dot:
    return "Id.%s" % v
  else:
    return v

class Kind_t(pybase.SimpleObj):
  pass

class Kind(object):
  Word = Kind_t(1)
  Arith = Kind_t(2)
  Eof = Kind_t(3)
  Undefined = Kind_t(4)
  Unknown = Kind_t(5)
  Eol = Kind_t(6)
  Ignored = Kind_t(7)
  WS = Kind_t(8)
  Lit = Kind_t(9)
  Backtick = Kind_t(10)
  History = Kind_t(11)
  Op = Kind_t(12)
  Expr = Kind_t(13)
  Char = Kind_t(14)
  BashRegex = Kind_t(15)
  Eggex = Kind_t(16)
  Redir = Kind_t(17)
  Left = Kind_t(18)
  Right = Kind_t(19)
  ExtGlob = Kind_t(20)
  VSub = Kind_t(21)
  VTest = Kind_t(22)
  VOp0 = Kind_t(23)
  VOp1 = Kind_t(24)
  VOpYsh = Kind_t(25)
  VOp2 = Kind_t(26)
  VOp3 = Kind_t(27)
  Node = Kind_t(28)
  KW = Kind_t(29)
  ControlFlow = Kind_t(30)
  LookAhead = Kind_t(31)
  Glob = Kind_t(32)
  Format = Kind_t(33)
  PS = Kind_t(34)
  Range = Kind_t(35)
  J8 = Kind_t(36)
  ShNumber = Kind_t(37)
  BoolUnary = Kind_t(38)
  BoolBinary = Kind_t(39)

_Kind_str = {
  1: 'Word',
  2: 'Arith',
  3: 'Eof',
  4: 'Undefined',
  5: 'Unknown',
  6: 'Eol',
  7: 'Ignored',
  8: 'WS',
  9: 'Lit',
  10: 'Backtick',
  11: 'History',
  12: 'Op',
  13: 'Expr',
  14: 'Char',
  15: 'BashRegex',
  16: 'Eggex',
  17: 'Redir',
  18: 'Left',
  19: 'Right',
  20: 'ExtGlob',
  21: 'VSub',
  22: 'VTest',
  23: 'VOp0',
  24: 'VOp1',
  25: 'VOpYsh',
  26: 'VOp2',
  27: 'VOp3',
  28: 'Node',
  29: 'KW',
  30: 'ControlFlow',
  31: 'LookAhead',
  32: 'Glob',
  33: 'Format',
  34: 'PS',
  35: 'Range',
  36: 'J8',
  37: 'ShNumber',
  38: 'BoolUnary',
  39: 'BoolBinary',
}

def Kind_str(val, dot=True):
  # type: (Kind_t, bool) -> str
  v = _Kind_str[val]
  if dot:
    return "Kind.%s" % v
  else:
    return v

