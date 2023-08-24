# Generated from main/AnotherC/parser/AnotherC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u01e3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\5\2e\n\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3r\n\3\3\4\6\4u\n\4")
        buf.write("\r\4\16\4v\3\4\3\4\3\5\3\5\3\5\5\5~\n\5\3\6\5\6\u0081")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u008a\n\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7\u0090\n\7\7\7\u0092\n\7\f\7\16\7\u0095\13")
        buf.write("\7\3\b\3\b\3\b\3\b\5\b\u009b\n\b\3\t\3\t\3\n\3\n\5\n\u00a1")
        buf.write("\n\n\3\n\3\n\3\n\6\n\u00a6\n\n\r\n\16\n\u00a7\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00ae\n\13\3\13\3\13\3\13\3\13\5\13\u00b4")
        buf.write("\n\13\3\f\3\f\5\f\u00b8\n\f\3\r\3\r\3\r\7\r\u00bd\n\r")
        buf.write("\f\r\16\r\u00c0\13\r\3\16\3\16\3\16\3\16\5\16\u00c6\n")
        buf.write("\16\3\17\3\17\6\17\u00ca\n\17\r\17\16\17\u00cb\3\17\3")
        buf.write("\17\3\20\3\20\5\20\u00d2\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\6\22\u00dd\n\22\r\22\16\22\u00de")
        buf.write("\3\23\3\23\3\23\3\23\7\23\u00e5\n\23\f\23\16\23\u00e8")
        buf.write("\13\23\3\23\3\23\3\24\3\24\3\24\5\24\u00ef\n\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\5\26\u0101\n\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u010d\n\27\f\27")
        buf.write("\16\27\u0110\13\27\3\27\3\27\3\27\5\27\u0115\n\27\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u011b\n\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\5\36\u013e\n\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \5 \u014a\n")
        buf.write(" \3!\3!\3!\3!\3!\6!\u0151\n!\r!\16!\u0152\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u015a\n\"\3\"\3\"\5\"\u015e\n\"\3#\3#\3#")
        buf.write("\5#\u0163\n#\3#\3#\3#\3$\3$\3$\7$\u016b\n$\f$\16$\u016e")
        buf.write("\13$\3%\3%\5%\u0172\n%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\7\'\u0180\n\'\f\'\16\'\u0183\13\'\3(\3(\3(")
        buf.write("\3(\3(\3(\7(\u018b\n(\f(\16(\u018e\13(\3)\3)\3)\3)\3)")
        buf.write("\3)\7)\u0196\n)\f)\16)\u0199\13)\3*\3*\3*\3*\3*\3*\7*")
        buf.write("\u01a1\n*\f*\16*\u01a4\13*\3+\3+\3+\3+\3+\3+\7+\u01ac")
        buf.write("\n+\f+\16+\u01af\13+\3,\3,\3,\3,\3,\3,\7,\u01b7\n,\f,")
        buf.write("\16,\u01ba\13,\3-\3-\3-\5-\u01bf\n-\3.\3.\3.\3.\3.\3.")
        buf.write("\5.\u01c7\n.\3/\3/\3/\3/\5/\u01cd\n/\3/\3/\5/\u01d1\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01da\n\60\3")
        buf.write("\61\3\61\3\61\5\61\u01df\n\61\3\61\3\61\3\61\2\bLNPRT")
        buf.write("V\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\n\4\2\n\r\17\20\4\2")
        buf.write("\33\33+/\4\2\34\34!!\3\2\35 \3\2\"#\3\2$&\4\2\"#\60\60")
        buf.write("\3\2)*\2\u01f6\2b\3\2\2\2\4q\3\2\2\2\6t\3\2\2\2\b}\3\2")
        buf.write("\2\2\n\u0080\3\2\2\2\f\u0086\3\2\2\2\16\u009a\3\2\2\2")
        buf.write("\20\u009c\3\2\2\2\22\u00a0\3\2\2\2\24\u00a9\3\2\2\2\26")
        buf.write("\u00b7\3\2\2\2\30\u00b9\3\2\2\2\32\u00c1\3\2\2\2\34\u00c7")
        buf.write("\3\2\2\2\36\u00d1\3\2\2\2 \u00d3\3\2\2\2\"\u00dc\3\2\2")
        buf.write("\2$\u00e0\3\2\2\2&\u00eb\3\2\2\2(\u00f3\3\2\2\2*\u0100")
        buf.write("\3\2\2\2,\u0102\3\2\2\2.\u0116\3\2\2\2\60\u0123\3\2\2")
        buf.write("\2\62\u0128\3\2\2\2\64\u012d\3\2\2\2\66\u0135\3\2\2\2")
        buf.write("8\u0138\3\2\2\2:\u013b\3\2\2\2<\u0141\3\2\2\2>\u0149\3")
        buf.write("\2\2\2@\u014b\3\2\2\2B\u015d\3\2\2\2D\u015f\3\2\2\2F\u0167")
        buf.write("\3\2\2\2H\u0171\3\2\2\2J\u0173\3\2\2\2L\u0179\3\2\2\2")
        buf.write("N\u0184\3\2\2\2P\u018f\3\2\2\2R\u019a\3\2\2\2T\u01a5\3")
        buf.write("\2\2\2V\u01b0\3\2\2\2X\u01be\3\2\2\2Z\u01c6\3\2\2\2\\")
        buf.write("\u01d0\3\2\2\2^\u01d9\3\2\2\2`\u01db\3\2\2\2bd\7:\2\2")
        buf.write("ce\5F$\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\7;\2\2g\3\3\2")
        buf.write("\2\2hr\7>\2\2ir\7@\2\2jr\7?\2\2kr\7B\2\2lr\7A\2\2mr\7")
        buf.write("\26\2\2nr\7\27\2\2or\5\2\2\2pr\7\31\2\2qh\3\2\2\2qi\3")
        buf.write("\2\2\2qj\3\2\2\2qk\3\2\2\2ql\3\2\2\2qm\3\2\2\2qn\3\2\2")
        buf.write("\2qo\3\2\2\2qp\3\2\2\2r\5\3\2\2\2su\5\b\5\2ts\3\2\2\2")
        buf.write("uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\7\2\2\3y\7")
        buf.write("\3\2\2\2z~\5\n\6\2{~\5\24\13\2|~\5 \21\2}z\3\2\2\2}{\3")
        buf.write("\2\2\2}|\3\2\2\2~\t\3\2\2\2\177\u0081\7\3\2\2\u0080\177")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0083\5\16\b\2\u0083\u0084\5\f\7\2\u0084\u0085\7\64\2")
        buf.write("\2\u0085\13\3\2\2\2\u0086\u0089\7=\2\2\u0087\u0088\7\33")
        buf.write("\2\2\u0088\u008a\5H%\2\u0089\u0087\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u0093\3\2\2\2\u008b\u008c\7<\2\2\u008c")
        buf.write("\u008f\7=\2\2\u008d\u008e\7\33\2\2\u008e\u0090\5H%\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u008b\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3")
        buf.write("\2\2\2\u0093\u0094\3\2\2\2\u0094\r\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\u009b\5\20\t\2\u0097\u009b\7\5\2\2\u0098")
        buf.write("\u009b\5\22\n\2\u0099\u009b\5(\25\2\u009a\u0096\3\2\2")
        buf.write("\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\17\3\2\2\2\u009c\u009d\t\2\2\2\u009d\21")
        buf.write("\3\2\2\2\u009e\u00a1\5\20\t\2\u009f\u00a1\5(\25\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a5\3\2\2\2")
        buf.write("\u00a2\u00a3\78\2\2\u00a3\u00a4\7>\2\2\u00a4\u00a6\79")
        buf.write("\2\2\u00a5\u00a2\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa")
        buf.write("\5\26\f\2\u00aa\u00ab\7=\2\2\u00ab\u00ad\7\66\2\2\u00ac")
        buf.write("\u00ae\5\30\r\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2")
        buf.write("\2\u00ae\u00af\3\2\2\2\u00af\u00b0\7\67\2\2\u00b0\u00b3")
        buf.write("\3\2\2\2\u00b1\u00b4\7\64\2\2\u00b2\u00b4\5\34\17\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\25\3\2\2\2\u00b5")
        buf.write("\u00b8\5\16\b\2\u00b6\u00b8\7\t\2\2\u00b7\u00b5\3\2\2")
        buf.write("\2\u00b7\u00b6\3\2\2\2\u00b8\27\3\2\2\2\u00b9\u00be\5")
        buf.write("\32\16\2\u00ba\u00bb\7<\2\2\u00bb\u00bd\5\32\16\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\31\3\2\2\2\u00c0\u00be\3\2")
        buf.write("\2\2\u00c1\u00c2\5\16\b\2\u00c2\u00c5\7=\2\2\u00c3\u00c4")
        buf.write("\7\33\2\2\u00c4\u00c6\5H%\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\33\3\2\2\2\u00c7\u00c9\7:\2\2\u00c8")
        buf.write("\u00ca\5\36\20\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2")
        buf.write("\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00ce\7;\2\2\u00ce\35\3\2\2\2\u00cf\u00d2")
        buf.write("\5\n\6\2\u00d0\u00d2\5*\26\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\37\3\2\2\2\u00d3\u00d4\7\b\2\2\u00d4")
        buf.write("\u00d5\7=\2\2\u00d5\u00d6\7:\2\2\u00d6\u00d7\5\"\22\2")
        buf.write("\u00d7\u00d8\7;\2\2\u00d8\u00d9\7\64\2\2\u00d9!\3\2\2")
        buf.write("\2\u00da\u00dd\5$\23\2\u00db\u00dd\5&\24\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df#\3\2\2\2\u00e0")
        buf.write("\u00e1\5\20\t\2\u00e1\u00e6\7=\2\2\u00e2\u00e3\7<\2\2")
        buf.write("\u00e3\u00e5\7=\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e8\3")
        buf.write("\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7\64\2\2\u00ea")
        buf.write("%\3\2\2\2\u00eb\u00ec\7=\2\2\u00ec\u00ee\7\66\2\2\u00ed")
        buf.write("\u00ef\5\30\r\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2")
        buf.write("\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\7\67\2\2\u00f1\u00f2")
        buf.write("\5\34\17\2\u00f2\'\3\2\2\2\u00f3\u00f4\7\b\2\2\u00f4\u00f5")
        buf.write("\7=\2\2\u00f5)\3\2\2\2\u00f6\u0101\5,\27\2\u00f7\u0101")
        buf.write("\5\64\33\2\u00f8\u0101\5\62\32\2\u00f9\u0101\5\66\34\2")
        buf.write("\u00fa\u0101\58\35\2\u00fb\u0101\5:\36\2\u00fc\u0101\5")
        buf.write(".\30\2\u00fd\u0101\5<\37\2\u00fe\u0101\5\34\17\2\u00ff")
        buf.write("\u0101\5D#\2\u0100\u00f6\3\2\2\2\u0100\u00f7\3\2\2\2\u0100")
        buf.write("\u00f8\3\2\2\2\u0100\u00f9\3\2\2\2\u0100\u00fa\3\2\2\2")
        buf.write("\u0100\u00fb\3\2\2\2\u0100\u00fc\3\2\2\2\u0100\u00fd\3")
        buf.write("\2\2\2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101+")
        buf.write("\3\2\2\2\u0102\u0103\7\21\2\2\u0103\u0104\5H%\2\u0104")
        buf.write("\u0105\7\65\2\2\u0105\u010e\5*\26\2\u0106\u0107\7\22\2")
        buf.write("\2\u0107\u0108\7\21\2\2\u0108\u0109\5H%\2\u0109\u010a")
        buf.write("\7\65\2\2\u010a\u010b\5*\26\2\u010b\u010d\3\2\2\2\u010c")
        buf.write("\u0106\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\u0114\3\2\2\2\u0110\u010e\3")
        buf.write("\2\2\2\u0111\u0112\7\22\2\2\u0112\u0113\7\65\2\2\u0113")
        buf.write("\u0115\5*\26\2\u0114\u0111\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115-\3\2\2\2\u0116\u0117\7\6\2\2\u0117\u011a\7\66\2")
        buf.write("\2\u0118\u011b\5\60\31\2\u0119\u011b\5<\37\2\u011a\u0118")
        buf.write("\3\2\2\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011d\7<\2\2\u011d\u011e\5H%\2\u011e\u011f\7<\2\2\u011f")
        buf.write("\u0120\5H%\2\u0120\u0121\7\67\2\2\u0121\u0122\5*\26\2")
        buf.write("\u0122/\3\2\2\2\u0123\u0124\5\16\b\2\u0124\u0125\7=\2")
        buf.write("\2\u0125\u0126\7\33\2\2\u0126\u0127\5H%\2\u0127\61\3\2")
        buf.write("\2\2\u0128\u0129\7\4\2\2\u0129\u012a\5H%\2\u012a\u012b")
        buf.write("\7\65\2\2\u012b\u012c\5*\26\2\u012c\63\3\2\2\2\u012d\u012e")
        buf.write("\7\7\2\2\u012e\u012f\5\34\17\2\u012f\u0130\7\4\2\2\u0130")
        buf.write("\u0131\7\66\2\2\u0131\u0132\5H%\2\u0132\u0133\7\67\2\2")
        buf.write("\u0133\u0134\7\64\2\2\u0134\65\3\2\2\2\u0135\u0136\7\24")
        buf.write("\2\2\u0136\u0137\7\64\2\2\u0137\67\3\2\2\2\u0138\u0139")
        buf.write("\7\25\2\2\u0139\u013a\7\64\2\2\u013a9\3\2\2\2\u013b\u013d")
        buf.write("\7\23\2\2\u013c\u013e\5H%\2\u013d\u013c\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\7\64\2")
        buf.write("\2\u0140;\3\2\2\2\u0141\u0142\5> \2\u0142\u0143\t\3\2")
        buf.write("\2\u0143\u0144\5H%\2\u0144\u0145\7\64\2\2\u0145=\3\2\2")
        buf.write("\2\u0146\u014a\7=\2\2\u0147\u014a\5@!\2\u0148\u014a\5")
        buf.write("B\"\2\u0149\u0146\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u0148")
        buf.write("\3\2\2\2\u014a?\3\2\2\2\u014b\u0150\7=\2\2\u014c\u014d")
        buf.write("\7\66\2\2\u014d\u014e\5H%\2\u014e\u014f\7\67\2\2\u014f")
        buf.write("\u0151\3\2\2\2\u0150\u014c\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153A\3\2\2")
        buf.write("\2\u0154\u0155\7\30\2\2\u0155\u0156\7\61\2\2\u0156\u015e")
        buf.write("\7=\2\2\u0157\u015a\7=\2\2\u0158\u015a\5@!\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write("\u015c\7\62\2\2\u015c\u015e\7=\2\2\u015d\u0154\3\2\2\2")
        buf.write("\u015d\u0159\3\2\2\2\u015eC\3\2\2\2\u015f\u0160\7=\2\2")
        buf.write("\u0160\u0162\7\66\2\2\u0161\u0163\5F$\2\u0162\u0161\3")
        buf.write("\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165")
        buf.write("\7\67\2\2\u0165\u0166\7\64\2\2\u0166E\3\2\2\2\u0167\u016c")
        buf.write("\5H%\2\u0168\u0169\7<\2\2\u0169\u016b\5H%\2\u016a\u0168")
        buf.write("\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016dG\3\2\2\2\u016e\u016c\3\2\2\2\u016f")
        buf.write("\u0172\5J&\2\u0170\u0172\5L\'\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172I\3\2\2\2\u0173\u0174\5L\'\2\u0174")
        buf.write("\u0175\7\63\2\2\u0175\u0176\5L\'\2\u0176\u0177\7\65\2")
        buf.write("\2\u0177\u0178\5L\'\2\u0178K\3\2\2\2\u0179\u017a\b\'\1")
        buf.write("\2\u017a\u017b\5N(\2\u017b\u0181\3\2\2\2\u017c\u017d\f")
        buf.write("\4\2\2\u017d\u017e\7(\2\2\u017e\u0180\5N(\2\u017f\u017c")
        buf.write("\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182M\3\2\2\2\u0183\u0181\3\2\2\2\u0184")
        buf.write("\u0185\b(\1\2\u0185\u0186\5P)\2\u0186\u018c\3\2\2\2\u0187")
        buf.write("\u0188\f\4\2\2\u0188\u0189\7\'\2\2\u0189\u018b\5P)\2\u018a")
        buf.write("\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018dO\3\2\2\2\u018e\u018c\3\2\2")
        buf.write("\2\u018f\u0190\b)\1\2\u0190\u0191\5R*\2\u0191\u0197\3")
        buf.write("\2\2\2\u0192\u0193\f\4\2\2\u0193\u0194\t\4\2\2\u0194\u0196")
        buf.write("\5R*\2\u0195\u0192\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198Q\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019b\b*\1\2\u019b\u019c\5T+\2\u019c\u01a2")
        buf.write("\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f\t\5\2\2\u019f")
        buf.write("\u01a1\5T+\2\u01a0\u019d\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3S\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a5\u01a6\b+\1\2\u01a6\u01a7\5V,\2\u01a7")
        buf.write("\u01ad\3\2\2\2\u01a8\u01a9\f\4\2\2\u01a9\u01aa\t\6\2\2")
        buf.write("\u01aa\u01ac\5V,\2\u01ab\u01a8\3\2\2\2\u01ac\u01af\3\2")
        buf.write("\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aeU\3")
        buf.write("\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\b,\1\2\u01b1\u01b2")
        buf.write("\5X-\2\u01b2\u01b8\3\2\2\2\u01b3\u01b4\f\4\2\2\u01b4\u01b5")
        buf.write("\t\7\2\2\u01b5\u01b7\5X-\2\u01b6\u01b3\3\2\2\2\u01b7\u01ba")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("W\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\t\b\2\2\u01bc")
        buf.write("\u01bf\5X-\2\u01bd\u01bf\5Z.\2\u01be\u01bb\3\2\2\2\u01be")
        buf.write("\u01bd\3\2\2\2\u01bfY\3\2\2\2\u01c0\u01c1\5> \2\u01c1")
        buf.write("\u01c2\t\t\2\2\u01c2\u01c7\3\2\2\2\u01c3\u01c4\t\t\2\2")
        buf.write("\u01c4\u01c7\5> \2\u01c5\u01c7\5\\/\2\u01c6\u01c0\3\2")
        buf.write("\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7[\3")
        buf.write("\2\2\2\u01c8\u01c9\7\32\2\2\u01c9\u01ca\7=\2\2\u01ca\u01cc")
        buf.write("\7\66\2\2\u01cb\u01cd\5F$\2\u01cc\u01cb\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d1\7\67\2")
        buf.write("\2\u01cf\u01d1\5^\60\2\u01d0\u01c8\3\2\2\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1]\3\2\2\2\u01d2\u01da\5> \2\u01d3\u01da")
        buf.write("\5\4\3\2\u01d4\u01da\5`\61\2\u01d5\u01d6\7\66\2\2\u01d6")
        buf.write("\u01d7\5H%\2\u01d7\u01d8\7\67\2\2\u01d8\u01da\3\2\2\2")
        buf.write("\u01d9\u01d2\3\2\2\2\u01d9\u01d3\3\2\2\2\u01d9\u01d4\3")
        buf.write("\2\2\2\u01d9\u01d5\3\2\2\2\u01da_\3\2\2\2\u01db\u01dc")
        buf.write("\7=\2\2\u01dc\u01de\7\66\2\2\u01dd\u01df\5F$\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e1\7\67\2\2\u01e1a\3\2\2\2\60dqv}\u0080\u0089\u008f")
        buf.write("\u0093\u009a\u00a0\u00a7\u00ad\u00b3\u00b7\u00be\u00c5")
        buf.write("\u00cb\u00d1\u00dc\u00de\u00e6\u00ee\u0100\u010e\u0114")
        buf.write("\u011a\u013d\u0149\u0152\u0159\u015d\u0162\u016c\u0171")
        buf.write("\u0181\u018c\u0197\u01a2\u01ad\u01b8\u01be\u01c6\u01cc")
        buf.write("\u01d0\u01d9\u01de")
        return buf.getvalue()


class AnotherCParser ( Parser ):

    grammarFileName = "AnotherC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'const'", "'while'", "'auto'", "'for'", 
                     "'do'", "'struct'", "'void'", "'bool'", "'int'", "'string'", 
                     "'char'", "'long'", "'float'", "'double'", "'if'", 
                     "'else'", "'return'", "'break'", "'continue'", "'true'", 
                     "'false'", "'this'", "'None'", "'new'", "'='", "'=='", 
                     "'<'", "'>'", "'<='", "'>='", "'!='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'&&'", "'||'", "'++'", "'--'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'!'", "'->'", 
                     "'.'", "'?'", "';'", "':'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "','" ]

    symbolicNames = [ "<INVALID>", "CONST", "WHILE", "AUTO", "FOR", "DO", 
                      "STRUCT", "VOID", "BOOL", "INT", "STRING", "CHAR", 
                      "LONG", "FLOAT", "DOUBLE", "IF", "ELSE", "RETURN", 
                      "BREAK", "CONTINUE", "TRUE", "FALSE", "THIS", "NONE", 
                      "NEW", "ASSIGN", "EQ", "LT", "GT", "LTE", "GTE", "NOT_EQ", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "INC", 
                      "DEC", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "NEG", "ARROW", "DOT", "QM", "SEMI", 
                      "COLON", "LB", "RB", "LS", "RS", "LC", "RC", "COMMA", 
                      "ID", "INT_LIT", "DOUBLE_LIT", "FLOAT_LIT", "CHAR_LIT", 
                      "STR_LIT", "LINE_CMT", "BLOCK_CMT", "WS", "ERROR_CHAR", 
                      "UNCLOSED_STRING", "UNTERMINATED_COMMENT" ]

    RULE_array_literals = 0
    RULE_literals = 1
    RULE_program = 2
    RULE_decls = 3
    RULE_vardecl = 4
    RULE_var_decl_list = 5
    RULE_vartype = 6
    RULE_prim_type = 7
    RULE_array_type = 8
    RULE_funcdecl = 9
    RULE_functype = 10
    RULE_paralist = 11
    RULE_paradecl = 12
    RULE_block_func = 13
    RULE_stmts = 14
    RULE_struct_decl = 15
    RULE_attribute_list = 16
    RULE_no_assign_vardecl = 17
    RULE_constructor = 18
    RULE_struct_type = 19
    RULE_statement = 20
    RULE_if_stmt = 21
    RULE_for_stmt = 22
    RULE_single_vardecl = 23
    RULE_while_stmt = 24
    RULE_do_while_stmt = 25
    RULE_break_stmt = 26
    RULE_cont_stmt = 27
    RULE_return_stmt = 28
    RULE_assign_stmt = 29
    RULE_scalar_var = 30
    RULE_array_cell = 31
    RULE_member_access = 32
    RULE_call_func = 33
    RULE_expression_list = 34
    RULE_expression = 35
    RULE_if_expression = 36
    RULE_expression1 = 37
    RULE_expression2 = 38
    RULE_expression3 = 39
    RULE_expression4 = 40
    RULE_expression5 = 41
    RULE_expression6 = 42
    RULE_expression7 = 43
    RULE_expression8 = 44
    RULE_expression9 = 45
    RULE_operands = 46
    RULE_func_call = 47

    ruleNames =  [ "array_literals", "literals", "program", "decls", "vardecl", 
                   "var_decl_list", "vartype", "prim_type", "array_type", 
                   "funcdecl", "functype", "paralist", "paradecl", "block_func", 
                   "stmts", "struct_decl", "attribute_list", "no_assign_vardecl", 
                   "constructor", "struct_type", "statement", "if_stmt", 
                   "for_stmt", "single_vardecl", "while_stmt", "do_while_stmt", 
                   "break_stmt", "cont_stmt", "return_stmt", "assign_stmt", 
                   "scalar_var", "array_cell", "member_access", "call_func", 
                   "expression_list", "expression", "if_expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "expression9", 
                   "operands", "func_call" ]

    EOF = Token.EOF
    CONST=1
    WHILE=2
    AUTO=3
    FOR=4
    DO=5
    STRUCT=6
    VOID=7
    BOOL=8
    INT=9
    STRING=10
    CHAR=11
    LONG=12
    FLOAT=13
    DOUBLE=14
    IF=15
    ELSE=16
    RETURN=17
    BREAK=18
    CONTINUE=19
    TRUE=20
    FALSE=21
    THIS=22
    NONE=23
    NEW=24
    ASSIGN=25
    EQ=26
    LT=27
    GT=28
    LTE=29
    GTE=30
    NOT_EQ=31
    ADD=32
    SUB=33
    MUL=34
    DIV=35
    MOD=36
    AND=37
    OR=38
    INC=39
    DEC=40
    ADD_ASSIGN=41
    SUB_ASSIGN=42
    MUL_ASSIGN=43
    DIV_ASSIGN=44
    MOD_ASSIGN=45
    NEG=46
    ARROW=47
    DOT=48
    QM=49
    SEMI=50
    COLON=51
    LB=52
    RB=53
    LS=54
    RS=55
    LC=56
    RC=57
    COMMA=58
    ID=59
    INT_LIT=60
    DOUBLE_LIT=61
    FLOAT_LIT=62
    CHAR_LIT=63
    STR_LIT=64
    LINE_CMT=65
    BLOCK_CMT=66
    WS=67
    ERROR_CHAR=68
    UNCLOSED_STRING=69
    UNTERMINATED_COMMENT=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Array_literalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(AnotherCParser.LC, 0)

        def RC(self):
            return self.getToken(AnotherCParser.RC, 0)

        def expression_list(self):
            return self.getTypedRuleContext(AnotherCParser.Expression_listContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_array_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literals" ):
                return visitor.visitArray_literals(self)
            else:
                return visitor.visitChildren(self)




    def array_literals(self):

        localctx = AnotherCParser.Array_literalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_array_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(AnotherCParser.LC)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (AnotherCParser.TRUE - 20)) | (1 << (AnotherCParser.FALSE - 20)) | (1 << (AnotherCParser.THIS - 20)) | (1 << (AnotherCParser.NONE - 20)) | (1 << (AnotherCParser.NEW - 20)) | (1 << (AnotherCParser.ADD - 20)) | (1 << (AnotherCParser.SUB - 20)) | (1 << (AnotherCParser.INC - 20)) | (1 << (AnotherCParser.DEC - 20)) | (1 << (AnotherCParser.NEG - 20)) | (1 << (AnotherCParser.LB - 20)) | (1 << (AnotherCParser.LC - 20)) | (1 << (AnotherCParser.ID - 20)) | (1 << (AnotherCParser.INT_LIT - 20)) | (1 << (AnotherCParser.DOUBLE_LIT - 20)) | (1 << (AnotherCParser.FLOAT_LIT - 20)) | (1 << (AnotherCParser.CHAR_LIT - 20)) | (1 << (AnotherCParser.STR_LIT - 20)))) != 0):
                self.state = 97
                self.expression_list()


            self.state = 100
            self.match(AnotherCParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(AnotherCParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(AnotherCParser.FLOAT_LIT, 0)

        def DOUBLE_LIT(self):
            return self.getToken(AnotherCParser.DOUBLE_LIT, 0)

        def STR_LIT(self):
            return self.getToken(AnotherCParser.STR_LIT, 0)

        def CHAR_LIT(self):
            return self.getToken(AnotherCParser.CHAR_LIT, 0)

        def TRUE(self):
            return self.getToken(AnotherCParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(AnotherCParser.FALSE, 0)

        def array_literals(self):
            return self.getTypedRuleContext(AnotherCParser.Array_literalsContext,0)


        def NONE(self):
            return self.getToken(AnotherCParser.NONE, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = AnotherCParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literals)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(AnotherCParser.INT_LIT)
                pass
            elif token in [AnotherCParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(AnotherCParser.FLOAT_LIT)
                pass
            elif token in [AnotherCParser.DOUBLE_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(AnotherCParser.DOUBLE_LIT)
                pass
            elif token in [AnotherCParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.match(AnotherCParser.STR_LIT)
                pass
            elif token in [AnotherCParser.CHAR_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.match(AnotherCParser.CHAR_LIT)
                pass
            elif token in [AnotherCParser.TRUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.match(AnotherCParser.TRUE)
                pass
            elif token in [AnotherCParser.FALSE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.match(AnotherCParser.FALSE)
                pass
            elif token in [AnotherCParser.LC]:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.array_literals()
                pass
            elif token in [AnotherCParser.NONE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 110
                self.match(AnotherCParser.NONE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AnotherCParser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.DeclsContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.DeclsContext,i)


        def getRuleIndex(self):
            return AnotherCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AnotherCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 113
                self.decls()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.CONST) | (1 << AnotherCParser.AUTO) | (1 << AnotherCParser.STRUCT) | (1 << AnotherCParser.VOID) | (1 << AnotherCParser.BOOL) | (1 << AnotherCParser.INT) | (1 << AnotherCParser.STRING) | (1 << AnotherCParser.CHAR) | (1 << AnotherCParser.FLOAT) | (1 << AnotherCParser.DOUBLE))) != 0)):
                    break

            self.state = 118
            self.match(AnotherCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(AnotherCParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(AnotherCParser.FuncdeclContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(AnotherCParser.Struct_declContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = AnotherCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decls)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.struct_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(AnotherCParser.VartypeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(AnotherCParser.Var_decl_listContext,0)


        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def CONST(self):
            return self.getToken(AnotherCParser.CONST, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = AnotherCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AnotherCParser.CONST:
                self.state = 125
                self.match(AnotherCParser.CONST)


            self.state = 128
            self.vartype()
            self.state = 129
            self.var_decl_list()
            self.state = 130
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.ID)
            else:
                return self.getToken(AnotherCParser.ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.ASSIGN)
            else:
                return self.getToken(AnotherCParser.ASSIGN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.COMMA)
            else:
                return self.getToken(AnotherCParser.COMMA, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = AnotherCParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(AnotherCParser.ID)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AnotherCParser.ASSIGN:
                self.state = 133
                self.match(AnotherCParser.ASSIGN)
                self.state = 134
                self.expression()


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AnotherCParser.COMMA:
                self.state = 137
                self.match(AnotherCParser.COMMA)

                self.state = 138
                self.match(AnotherCParser.ID)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==AnotherCParser.ASSIGN:
                    self.state = 139
                    self.match(AnotherCParser.ASSIGN)
                    self.state = 140
                    self.expression()


                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(AnotherCParser.Prim_typeContext,0)


        def AUTO(self):
            return self.getToken(AnotherCParser.AUTO, 0)

        def array_type(self):
            return self.getTypedRuleContext(AnotherCParser.Array_typeContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(AnotherCParser.Struct_typeContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = AnotherCParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vartype)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.prim_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(AnotherCParser.AUTO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.array_type()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.struct_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(AnotherCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(AnotherCParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(AnotherCParser.DOUBLE, 0)

        def STRING(self):
            return self.getToken(AnotherCParser.STRING, 0)

        def BOOL(self):
            return self.getToken(AnotherCParser.BOOL, 0)

        def CHAR(self):
            return self.getToken(AnotherCParser.CHAR, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_prim_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrim_type" ):
                return visitor.visitPrim_type(self)
            else:
                return visitor.visitChildren(self)




    def prim_type(self):

        localctx = AnotherCParser.Prim_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_prim_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.BOOL) | (1 << AnotherCParser.INT) | (1 << AnotherCParser.STRING) | (1 << AnotherCParser.CHAR) | (1 << AnotherCParser.FLOAT) | (1 << AnotherCParser.DOUBLE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(AnotherCParser.Prim_typeContext,0)


        def struct_type(self):
            return self.getTypedRuleContext(AnotherCParser.Struct_typeContext,0)


        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.LS)
            else:
                return self.getToken(AnotherCParser.LS, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.INT_LIT)
            else:
                return self.getToken(AnotherCParser.INT_LIT, i)

        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.RS)
            else:
                return self.getToken(AnotherCParser.RS, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = AnotherCParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.BOOL, AnotherCParser.INT, AnotherCParser.STRING, AnotherCParser.CHAR, AnotherCParser.FLOAT, AnotherCParser.DOUBLE]:
                self.state = 156
                self.prim_type()
                pass
            elif token in [AnotherCParser.STRUCT]:
                self.state = 157
                self.struct_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 160
                self.match(AnotherCParser.LS)
                self.state = 161
                self.match(AnotherCParser.INT_LIT)
                self.state = 162
                self.match(AnotherCParser.RS)
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AnotherCParser.LS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functype(self):
            return self.getTypedRuleContext(AnotherCParser.FunctypeContext,0)


        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def block_func(self):
            return self.getTypedRuleContext(AnotherCParser.Block_funcContext,0)


        def paralist(self):
            return self.getTypedRuleContext(AnotherCParser.ParalistContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = AnotherCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.functype()
            self.state = 168
            self.match(AnotherCParser.ID)

            self.state = 169
            self.match(AnotherCParser.LB)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.AUTO) | (1 << AnotherCParser.STRUCT) | (1 << AnotherCParser.BOOL) | (1 << AnotherCParser.INT) | (1 << AnotherCParser.STRING) | (1 << AnotherCParser.CHAR) | (1 << AnotherCParser.FLOAT) | (1 << AnotherCParser.DOUBLE))) != 0):
                self.state = 170
                self.paralist()


            self.state = 173
            self.match(AnotherCParser.RB)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.SEMI]:
                self.state = 175
                self.match(AnotherCParser.SEMI)
                pass
            elif token in [AnotherCParser.LC]:
                self.state = 176
                self.block_func()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(AnotherCParser.VartypeContext,0)


        def VOID(self):
            return self.getToken(AnotherCParser.VOID, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_functype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctype" ):
                return visitor.visitFunctype(self)
            else:
                return visitor.visitChildren(self)




    def functype(self):

        localctx = AnotherCParser.FunctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functype)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.AUTO, AnotherCParser.STRUCT, AnotherCParser.BOOL, AnotherCParser.INT, AnotherCParser.STRING, AnotherCParser.CHAR, AnotherCParser.FLOAT, AnotherCParser.DOUBLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.vartype()
                pass
            elif token in [AnotherCParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(AnotherCParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paradecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ParadeclContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ParadeclContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.COMMA)
            else:
                return self.getToken(AnotherCParser.COMMA, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = AnotherCParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.paradecl()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AnotherCParser.COMMA:
                self.state = 184
                self.match(AnotherCParser.COMMA)
                self.state = 185
                self.paradecl()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(AnotherCParser.VartypeContext,0)


        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(AnotherCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_paradecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParadecl" ):
                return visitor.visitParadecl(self)
            else:
                return visitor.visitChildren(self)




    def paradecl(self):

        localctx = AnotherCParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paradecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.vartype()
            self.state = 192
            self.match(AnotherCParser.ID)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AnotherCParser.ASSIGN:
                self.state = 193
                self.match(AnotherCParser.ASSIGN)
                self.state = 194
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(AnotherCParser.LC, 0)

        def RC(self):
            return self.getToken(AnotherCParser.RC, 0)

        def stmts(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.StmtsContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.StmtsContext,i)


        def getRuleIndex(self):
            return AnotherCParser.RULE_block_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_func" ):
                return visitor.visitBlock_func(self)
            else:
                return visitor.visitChildren(self)




    def block_func(self):

        localctx = AnotherCParser.Block_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(AnotherCParser.LC)
            self.state = 199 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 198
                self.stmts()
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.CONST) | (1 << AnotherCParser.WHILE) | (1 << AnotherCParser.AUTO) | (1 << AnotherCParser.FOR) | (1 << AnotherCParser.DO) | (1 << AnotherCParser.STRUCT) | (1 << AnotherCParser.BOOL) | (1 << AnotherCParser.INT) | (1 << AnotherCParser.STRING) | (1 << AnotherCParser.CHAR) | (1 << AnotherCParser.FLOAT) | (1 << AnotherCParser.DOUBLE) | (1 << AnotherCParser.IF) | (1 << AnotherCParser.RETURN) | (1 << AnotherCParser.BREAK) | (1 << AnotherCParser.CONTINUE) | (1 << AnotherCParser.THIS) | (1 << AnotherCParser.LC) | (1 << AnotherCParser.ID))) != 0)):
                    break

            self.state = 203
            self.match(AnotherCParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(AnotherCParser.VardeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(AnotherCParser.StatementContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = AnotherCParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmts)
        try:
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.CONST, AnotherCParser.AUTO, AnotherCParser.STRUCT, AnotherCParser.BOOL, AnotherCParser.INT, AnotherCParser.STRING, AnotherCParser.CHAR, AnotherCParser.FLOAT, AnotherCParser.DOUBLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.vardecl()
                pass
            elif token in [AnotherCParser.WHILE, AnotherCParser.FOR, AnotherCParser.DO, AnotherCParser.IF, AnotherCParser.RETURN, AnotherCParser.BREAK, AnotherCParser.CONTINUE, AnotherCParser.THIS, AnotherCParser.LC, AnotherCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(AnotherCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LC(self):
            return self.getToken(AnotherCParser.LC, 0)

        def attribute_list(self):
            return self.getTypedRuleContext(AnotherCParser.Attribute_listContext,0)


        def RC(self):
            return self.getToken(AnotherCParser.RC, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = AnotherCParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(AnotherCParser.STRUCT)
            self.state = 210
            self.match(AnotherCParser.ID)
            self.state = 211
            self.match(AnotherCParser.LC)
            self.state = 212
            self.attribute_list()
            self.state = 213
            self.match(AnotherCParser.RC)
            self.state = 214
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def no_assign_vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.No_assign_vardeclContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.No_assign_vardeclContext,i)


        def constructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ConstructorContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ConstructorContext,i)


        def getRuleIndex(self):
            return AnotherCParser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = AnotherCParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_attribute_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 218
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [AnotherCParser.BOOL, AnotherCParser.INT, AnotherCParser.STRING, AnotherCParser.CHAR, AnotherCParser.FLOAT, AnotherCParser.DOUBLE]:
                    self.state = 216
                    self.no_assign_vardecl()
                    pass
                elif token in [AnotherCParser.ID]:
                    self.state = 217
                    self.constructor()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 220 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.BOOL) | (1 << AnotherCParser.INT) | (1 << AnotherCParser.STRING) | (1 << AnotherCParser.CHAR) | (1 << AnotherCParser.FLOAT) | (1 << AnotherCParser.DOUBLE) | (1 << AnotherCParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_assign_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_type(self):
            return self.getTypedRuleContext(AnotherCParser.Prim_typeContext,0)


        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.ID)
            else:
                return self.getToken(AnotherCParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.COMMA)
            else:
                return self.getToken(AnotherCParser.COMMA, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_no_assign_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_assign_vardecl" ):
                return visitor.visitNo_assign_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def no_assign_vardecl(self):

        localctx = AnotherCParser.No_assign_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_no_assign_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.prim_type()

            self.state = 223
            self.match(AnotherCParser.ID)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AnotherCParser.COMMA:
                self.state = 224
                self.match(AnotherCParser.COMMA)
                self.state = 225
                self.match(AnotherCParser.ID)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def block_func(self):
            return self.getTypedRuleContext(AnotherCParser.Block_funcContext,0)


        def paralist(self):
            return self.getTypedRuleContext(AnotherCParser.ParalistContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = AnotherCParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(AnotherCParser.ID)
            self.state = 234
            self.match(AnotherCParser.LB)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.AUTO) | (1 << AnotherCParser.STRUCT) | (1 << AnotherCParser.BOOL) | (1 << AnotherCParser.INT) | (1 << AnotherCParser.STRING) | (1 << AnotherCParser.CHAR) | (1 << AnotherCParser.FLOAT) | (1 << AnotherCParser.DOUBLE))) != 0):
                self.state = 235
                self.paralist()


            self.state = 238
            self.match(AnotherCParser.RB)
            self.state = 239
            self.block_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(AnotherCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_struct_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_type" ):
                return visitor.visitStruct_type(self)
            else:
                return visitor.visitChildren(self)




    def struct_type(self):

        localctx = AnotherCParser.Struct_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(AnotherCParser.STRUCT)
            self.state = 242
            self.match(AnotherCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.If_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.Do_while_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.While_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.Break_stmtContext,0)


        def cont_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.Cont_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.Return_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.For_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.Assign_stmtContext,0)


        def block_func(self):
            return self.getTypedRuleContext(AnotherCParser.Block_funcContext,0)


        def call_func(self):
            return self.getTypedRuleContext(AnotherCParser.Call_funcContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AnotherCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.do_while_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.cont_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 249
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 250
                self.for_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 251
                self.assign_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 252
                self.block_func()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 253
                self.call_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.IF)
            else:
                return self.getToken(AnotherCParser.IF, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ExpressionContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.COLON)
            else:
                return self.getToken(AnotherCParser.COLON, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.StatementContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.StatementContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.ELSE)
            else:
                return self.getToken(AnotherCParser.ELSE, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = AnotherCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(AnotherCParser.IF)
            self.state = 257
            self.expression()
            self.state = 258
            self.match(AnotherCParser.COLON)
            self.state = 259
            self.statement()
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.match(AnotherCParser.ELSE)
                    self.state = 261
                    self.match(AnotherCParser.IF)
                    self.state = 262
                    self.expression()
                    self.state = 263
                    self.match(AnotherCParser.COLON)
                    self.state = 264
                    self.statement() 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 271
                self.match(AnotherCParser.ELSE)
                self.state = 272
                self.match(AnotherCParser.COLON)
                self.state = 273
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(AnotherCParser.FOR, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.COMMA)
            else:
                return self.getToken(AnotherCParser.COMMA, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ExpressionContext,i)


        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(AnotherCParser.StatementContext,0)


        def single_vardecl(self):
            return self.getTypedRuleContext(AnotherCParser.Single_vardeclContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(AnotherCParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = AnotherCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(AnotherCParser.FOR)
            self.state = 277
            self.match(AnotherCParser.LB)
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.AUTO, AnotherCParser.STRUCT, AnotherCParser.BOOL, AnotherCParser.INT, AnotherCParser.STRING, AnotherCParser.CHAR, AnotherCParser.FLOAT, AnotherCParser.DOUBLE]:
                self.state = 278
                self.single_vardecl()
                pass
            elif token in [AnotherCParser.THIS, AnotherCParser.ID]:
                self.state = 279
                self.assign_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 282
            self.match(AnotherCParser.COMMA)
            self.state = 283
            self.expression()
            self.state = 284
            self.match(AnotherCParser.COMMA)
            self.state = 285
            self.expression()
            self.state = 286
            self.match(AnotherCParser.RB)
            self.state = 287
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(AnotherCParser.VartypeContext,0)


        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(AnotherCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_single_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_vardecl" ):
                return visitor.visitSingle_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def single_vardecl(self):

        localctx = AnotherCParser.Single_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_single_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.vartype()
            self.state = 290
            self.match(AnotherCParser.ID)
            self.state = 291
            self.match(AnotherCParser.ASSIGN)
            self.state = 292
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(AnotherCParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(AnotherCParser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(AnotherCParser.StatementContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = AnotherCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(AnotherCParser.WHILE)
            self.state = 295
            self.expression()
            self.state = 296
            self.match(AnotherCParser.COLON)
            self.state = 297
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(AnotherCParser.DO, 0)

        def block_func(self):
            return self.getTypedRuleContext(AnotherCParser.Block_funcContext,0)


        def WHILE(self):
            return self.getToken(AnotherCParser.WHILE, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = AnotherCParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(AnotherCParser.DO)
            self.state = 300
            self.block_func()
            self.state = 301
            self.match(AnotherCParser.WHILE)
            self.state = 302
            self.match(AnotherCParser.LB)
            self.state = 303
            self.expression()
            self.state = 304
            self.match(AnotherCParser.RB)
            self.state = 305
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(AnotherCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = AnotherCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(AnotherCParser.BREAK)
            self.state = 308
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cont_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(AnotherCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_cont_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_stmt" ):
                return visitor.visitCont_stmt(self)
            else:
                return visitor.visitChildren(self)




    def cont_stmt(self):

        localctx = AnotherCParser.Cont_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_cont_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(AnotherCParser.CONTINUE)
            self.state = 311
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(AnotherCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = AnotherCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(AnotherCParser.RETURN)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (AnotherCParser.TRUE - 20)) | (1 << (AnotherCParser.FALSE - 20)) | (1 << (AnotherCParser.THIS - 20)) | (1 << (AnotherCParser.NONE - 20)) | (1 << (AnotherCParser.NEW - 20)) | (1 << (AnotherCParser.ADD - 20)) | (1 << (AnotherCParser.SUB - 20)) | (1 << (AnotherCParser.INC - 20)) | (1 << (AnotherCParser.DEC - 20)) | (1 << (AnotherCParser.NEG - 20)) | (1 << (AnotherCParser.LB - 20)) | (1 << (AnotherCParser.LC - 20)) | (1 << (AnotherCParser.ID - 20)) | (1 << (AnotherCParser.INT_LIT - 20)) | (1 << (AnotherCParser.DOUBLE_LIT - 20)) | (1 << (AnotherCParser.FLOAT_LIT - 20)) | (1 << (AnotherCParser.CHAR_LIT - 20)) | (1 << (AnotherCParser.STR_LIT - 20)))) != 0):
                self.state = 314
                self.expression()


            self.state = 317
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(AnotherCParser.Scalar_varContext,0)


        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(AnotherCParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(AnotherCParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(AnotherCParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(AnotherCParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(AnotherCParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(AnotherCParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = AnotherCParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.scalar_var()
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.ASSIGN) | (1 << AnotherCParser.ADD_ASSIGN) | (1 << AnotherCParser.SUB_ASSIGN) | (1 << AnotherCParser.MUL_ASSIGN) | (1 << AnotherCParser.DIV_ASSIGN) | (1 << AnotherCParser.MOD_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 321
            self.expression()
            self.state = 322
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def array_cell(self):
            return self.getTypedRuleContext(AnotherCParser.Array_cellContext,0)


        def member_access(self):
            return self.getTypedRuleContext(AnotherCParser.Member_accessContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = AnotherCParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_scalar_var)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(AnotherCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.array_cell()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.member_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_cellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.LB)
            else:
                return self.getToken(AnotherCParser.LB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ExpressionContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.RB)
            else:
                return self.getToken(AnotherCParser.RB, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_array_cell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_cell" ):
                return visitor.visitArray_cell(self)
            else:
                return visitor.visitChildren(self)




    def array_cell(self):

        localctx = AnotherCParser.Array_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_cell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(AnotherCParser.ID)
            self.state = 334 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 330
                    self.match(AnotherCParser.LB)
                    self.state = 331
                    self.expression()
                    self.state = 332
                    self.match(AnotherCParser.RB)

                else:
                    raise NoViableAltException(self)
                self.state = 336 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(AnotherCParser.THIS, 0)

        def ARROW(self):
            return self.getToken(AnotherCParser.ARROW, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.ID)
            else:
                return self.getToken(AnotherCParser.ID, i)

        def DOT(self):
            return self.getToken(AnotherCParser.DOT, 0)

        def array_cell(self):
            return self.getTypedRuleContext(AnotherCParser.Array_cellContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = AnotherCParser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_member_access)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.THIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(AnotherCParser.THIS)
                self.state = 339
                self.match(AnotherCParser.ARROW)
                self.state = 340
                self.match(AnotherCParser.ID)
                pass
            elif token in [AnotherCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 341
                    self.match(AnotherCParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 342
                    self.array_cell()
                    pass


                self.state = 345
                self.match(AnotherCParser.DOT)
                self.state = 346
                self.match(AnotherCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def SEMI(self):
            return self.getToken(AnotherCParser.SEMI, 0)

        def expression_list(self):
            return self.getTypedRuleContext(AnotherCParser.Expression_listContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = AnotherCParser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_call_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(AnotherCParser.ID)
            self.state = 350
            self.match(AnotherCParser.LB)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (AnotherCParser.TRUE - 20)) | (1 << (AnotherCParser.FALSE - 20)) | (1 << (AnotherCParser.THIS - 20)) | (1 << (AnotherCParser.NONE - 20)) | (1 << (AnotherCParser.NEW - 20)) | (1 << (AnotherCParser.ADD - 20)) | (1 << (AnotherCParser.SUB - 20)) | (1 << (AnotherCParser.INC - 20)) | (1 << (AnotherCParser.DEC - 20)) | (1 << (AnotherCParser.NEG - 20)) | (1 << (AnotherCParser.LB - 20)) | (1 << (AnotherCParser.LC - 20)) | (1 << (AnotherCParser.ID - 20)) | (1 << (AnotherCParser.INT_LIT - 20)) | (1 << (AnotherCParser.DOUBLE_LIT - 20)) | (1 << (AnotherCParser.FLOAT_LIT - 20)) | (1 << (AnotherCParser.CHAR_LIT - 20)) | (1 << (AnotherCParser.STR_LIT - 20)))) != 0):
                self.state = 351
                self.expression_list()


            self.state = 354
            self.match(AnotherCParser.RB)
            self.state = 355
            self.match(AnotherCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AnotherCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AnotherCParser.COMMA)
            else:
                return self.getToken(AnotherCParser.COMMA, i)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = AnotherCParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.expression()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AnotherCParser.COMMA:
                self.state = 358
                self.match(AnotherCParser.COMMA)
                self.state = 359
                self.expression()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_expression(self):
            return self.getTypedRuleContext(AnotherCParser.If_expressionContext,0)


        def expression1(self):
            return self.getTypedRuleContext(AnotherCParser.Expression1Context,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AnotherCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.if_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AnotherCParser.Expression1Context)
            else:
                return self.getTypedRuleContext(AnotherCParser.Expression1Context,i)


        def QM(self):
            return self.getToken(AnotherCParser.QM, 0)

        def COLON(self):
            return self.getToken(AnotherCParser.COLON, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_if_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_expression" ):
                return visitor.visitIf_expression(self)
            else:
                return visitor.visitChildren(self)




    def if_expression(self):

        localctx = AnotherCParser.If_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.expression1(0)
            self.state = 370
            self.match(AnotherCParser.QM)
            self.state = 371
            self.expression1(0)
            self.state = 372
            self.match(AnotherCParser.COLON)
            self.state = 373
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(AnotherCParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(AnotherCParser.Expression1Context,0)


        def OR(self):
            return self.getToken(AnotherCParser.OR, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AnotherCParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AnotherCParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    self.match(AnotherCParser.OR)
                    self.state = 380
                    self.expression2(0) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(AnotherCParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(AnotherCParser.Expression2Context,0)


        def AND(self):
            return self.getToken(AnotherCParser.AND, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AnotherCParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AnotherCParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    self.match(AnotherCParser.AND)
                    self.state = 391
                    self.expression3(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(AnotherCParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(AnotherCParser.Expression3Context,0)


        def EQ(self):
            return self.getToken(AnotherCParser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(AnotherCParser.NOT_EQ, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AnotherCParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AnotherCParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not(_la==AnotherCParser.EQ or _la==AnotherCParser.NOT_EQ):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.expression4(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(AnotherCParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(AnotherCParser.Expression4Context,0)


        def LT(self):
            return self.getToken(AnotherCParser.LT, 0)

        def LTE(self):
            return self.getToken(AnotherCParser.LTE, 0)

        def GT(self):
            return self.getToken(AnotherCParser.GT, 0)

        def GTE(self):
            return self.getToken(AnotherCParser.GTE, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AnotherCParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AnotherCParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.LT) | (1 << AnotherCParser.GT) | (1 << AnotherCParser.LTE) | (1 << AnotherCParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.expression5(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(AnotherCParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(AnotherCParser.Expression5Context,0)


        def ADD(self):
            return self.getToken(AnotherCParser.ADD, 0)

        def SUB(self):
            return self.getToken(AnotherCParser.SUB, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AnotherCParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.expression6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AnotherCParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    _la = self._input.LA(1)
                    if not(_la==AnotherCParser.ADD or _la==AnotherCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 424
                    self.expression6(0) 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(AnotherCParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(AnotherCParser.Expression6Context,0)


        def MUL(self):
            return self.getToken(AnotherCParser.MUL, 0)

        def DIV(self):
            return self.getToken(AnotherCParser.DIV, 0)

        def MOD(self):
            return self.getToken(AnotherCParser.MOD, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AnotherCParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AnotherCParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.MUL) | (1 << AnotherCParser.DIV) | (1 << AnotherCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 435
                    self.expression7() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(AnotherCParser.Expression7Context,0)


        def NEG(self):
            return self.getToken(AnotherCParser.NEG, 0)

        def ADD(self):
            return self.getToken(AnotherCParser.ADD, 0)

        def SUB(self):
            return self.getToken(AnotherCParser.SUB, 0)

        def expression8(self):
            return self.getTypedRuleContext(AnotherCParser.Expression8Context,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = AnotherCParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.ADD, AnotherCParser.SUB, AnotherCParser.NEG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << AnotherCParser.ADD) | (1 << AnotherCParser.SUB) | (1 << AnotherCParser.NEG))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.expression7()
                pass
            elif token in [AnotherCParser.TRUE, AnotherCParser.FALSE, AnotherCParser.THIS, AnotherCParser.NONE, AnotherCParser.NEW, AnotherCParser.INC, AnotherCParser.DEC, AnotherCParser.LB, AnotherCParser.LC, AnotherCParser.ID, AnotherCParser.INT_LIT, AnotherCParser.DOUBLE_LIT, AnotherCParser.FLOAT_LIT, AnotherCParser.CHAR_LIT, AnotherCParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.expression8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(AnotherCParser.Scalar_varContext,0)


        def INC(self):
            return self.getToken(AnotherCParser.INC, 0)

        def DEC(self):
            return self.getToken(AnotherCParser.DEC, 0)

        def expression9(self):
            return self.getTypedRuleContext(AnotherCParser.Expression9Context,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = AnotherCParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expression8)
        self._la = 0 # Token type
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.scalar_var()
                self.state = 447
                _la = self._input.LA(1)
                if not(_la==AnotherCParser.INC or _la==AnotherCParser.DEC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                _la = self._input.LA(1)
                if not(_la==AnotherCParser.INC or _la==AnotherCParser.DEC):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                self.scalar_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.expression9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(AnotherCParser.NEW, 0)

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def expression_list(self):
            return self.getTypedRuleContext(AnotherCParser.Expression_listContext,0)


        def operands(self):
            return self.getTypedRuleContext(AnotherCParser.OperandsContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)




    def expression9(self):

        localctx = AnotherCParser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expression9)
        self._la = 0 # Token type
        try:
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AnotherCParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(AnotherCParser.NEW)
                self.state = 455
                self.match(AnotherCParser.ID)
                self.state = 456
                self.match(AnotherCParser.LB)
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (AnotherCParser.TRUE - 20)) | (1 << (AnotherCParser.FALSE - 20)) | (1 << (AnotherCParser.THIS - 20)) | (1 << (AnotherCParser.NONE - 20)) | (1 << (AnotherCParser.NEW - 20)) | (1 << (AnotherCParser.ADD - 20)) | (1 << (AnotherCParser.SUB - 20)) | (1 << (AnotherCParser.INC - 20)) | (1 << (AnotherCParser.DEC - 20)) | (1 << (AnotherCParser.NEG - 20)) | (1 << (AnotherCParser.LB - 20)) | (1 << (AnotherCParser.LC - 20)) | (1 << (AnotherCParser.ID - 20)) | (1 << (AnotherCParser.INT_LIT - 20)) | (1 << (AnotherCParser.DOUBLE_LIT - 20)) | (1 << (AnotherCParser.FLOAT_LIT - 20)) | (1 << (AnotherCParser.CHAR_LIT - 20)) | (1 << (AnotherCParser.STR_LIT - 20)))) != 0):
                    self.state = 457
                    self.expression_list()


                self.state = 460
                self.match(AnotherCParser.RB)
                pass
            elif token in [AnotherCParser.TRUE, AnotherCParser.FALSE, AnotherCParser.THIS, AnotherCParser.NONE, AnotherCParser.LB, AnotherCParser.LC, AnotherCParser.ID, AnotherCParser.INT_LIT, AnotherCParser.DOUBLE_LIT, AnotherCParser.FLOAT_LIT, AnotherCParser.CHAR_LIT, AnotherCParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(AnotherCParser.Scalar_varContext,0)


        def literals(self):
            return self.getTypedRuleContext(AnotherCParser.LiteralsContext,0)


        def func_call(self):
            return self.getTypedRuleContext(AnotherCParser.Func_callContext,0)


        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(AnotherCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def getRuleIndex(self):
            return AnotherCParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = AnotherCParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_operands)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.literals()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 467
                self.match(AnotherCParser.LB)
                self.state = 468
                self.expression()
                self.state = 469
                self.match(AnotherCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AnotherCParser.ID, 0)

        def LB(self):
            return self.getToken(AnotherCParser.LB, 0)

        def RB(self):
            return self.getToken(AnotherCParser.RB, 0)

        def expression_list(self):
            return self.getTypedRuleContext(AnotherCParser.Expression_listContext,0)


        def getRuleIndex(self):
            return AnotherCParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = AnotherCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(AnotherCParser.ID)
            self.state = 474
            self.match(AnotherCParser.LB)
            self.state = 476
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (AnotherCParser.TRUE - 20)) | (1 << (AnotherCParser.FALSE - 20)) | (1 << (AnotherCParser.THIS - 20)) | (1 << (AnotherCParser.NONE - 20)) | (1 << (AnotherCParser.NEW - 20)) | (1 << (AnotherCParser.ADD - 20)) | (1 << (AnotherCParser.SUB - 20)) | (1 << (AnotherCParser.INC - 20)) | (1 << (AnotherCParser.DEC - 20)) | (1 << (AnotherCParser.NEG - 20)) | (1 << (AnotherCParser.LB - 20)) | (1 << (AnotherCParser.LC - 20)) | (1 << (AnotherCParser.ID - 20)) | (1 << (AnotherCParser.INT_LIT - 20)) | (1 << (AnotherCParser.DOUBLE_LIT - 20)) | (1 << (AnotherCParser.FLOAT_LIT - 20)) | (1 << (AnotherCParser.CHAR_LIT - 20)) | (1 << (AnotherCParser.STR_LIT - 20)))) != 0):
                self.state = 475
                self.expression_list()


            self.state = 478
            self.match(AnotherCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.expression1_sempred
        self._predicates[38] = self.expression2_sempred
        self._predicates[39] = self.expression3_sempred
        self._predicates[40] = self.expression4_sempred
        self._predicates[41] = self.expression5_sempred
        self._predicates[42] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




