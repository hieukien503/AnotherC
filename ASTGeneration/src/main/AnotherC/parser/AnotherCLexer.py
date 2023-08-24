# Generated from main/AnotherC/parser/AnotherC.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u0208\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u00a2\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\7>\u017a\n>\f")
        buf.write(">\16>\u017d\13>\3?\3?\5?\u0181\n?\3?\3?\3@\3@\3@\3@\3")
        buf.write("@\6@\u018a\n@\r@\16@\u018b\5@\u018e\n@\3A\3A\3A\3A\5A")
        buf.write("\u0194\nA\3B\3B\3B\3B\3B\3C\3C\7C\u019d\nC\fC\16C\u01a0")
        buf.write("\13C\3C\3C\3C\3D\3D\7D\u01a7\nD\fD\16D\u01aa\13D\3D\3")
        buf.write("D\6D\u01ae\nD\rD\16D\u01af\7D\u01b2\nD\fD\16D\u01b5\13")
        buf.write("D\3E\3E\7E\u01b9\nE\fE\16E\u01bc\13E\3F\5F\u01bf\nF\3")
        buf.write("F\3F\3F\3F\3F\3F\5F\u01c7\nF\3G\3G\5G\u01cb\nG\3G\6G\u01ce")
        buf.write("\nG\rG\16G\u01cf\3H\3H\3H\3H\7H\u01d6\nH\fH\16H\u01d9")
        buf.write("\13H\3H\3H\3I\3I\3I\3I\7I\u01e1\nI\fI\16I\u01e4\13I\3")
        buf.write("I\3I\3I\3I\3I\3J\6J\u01ec\nJ\rJ\16J\u01ed\3J\3J\3K\3K")
        buf.write("\3K\3L\3L\7L\u01f7\nL\fL\16L\u01fa\13L\3L\3L\3M\3M\3M")
        buf.write("\3M\7M\u0202\nM\fM\16M\u0205\13M\3M\3M\4\u01e2\u0203\2")
        buf.write("N\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31")
        buf.write("\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27\61")
        buf.write("\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O")
        buf.write("\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67q8s")
        buf.write("9u:w;y<{=}>\177?\u0081@\u0083A\u0085B\u0087\2\u0089\2")
        buf.write("\u008b\2\u008d\2\u008fC\u0091D\u0093E\u0095F\u0097G\u0099")
        buf.write("H\3\2\f\7\2\n\f\16\17$$))^^\5\2\n\13\16\17))\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2GGgg\4\2--//\4\2")
        buf.write("\f\f\16\17\5\2\13\f\17\17\"\"\2\u0216\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u00a1\3\2\2")
        buf.write("\2\7\u00a3\3\2\2\2\t\u00a9\3\2\2\2\13\u00af\3\2\2\2\r")
        buf.write("\u00b4\3\2\2\2\17\u00b8\3\2\2\2\21\u00bb\3\2\2\2\23\u00c2")
        buf.write("\3\2\2\2\25\u00c7\3\2\2\2\27\u00cc\3\2\2\2\31\u00d0\3")
        buf.write("\2\2\2\33\u00d7\3\2\2\2\35\u00dc\3\2\2\2\37\u00e1\3\2")
        buf.write("\2\2!\u00e7\3\2\2\2#\u00ee\3\2\2\2%\u00f1\3\2\2\2\'\u00f6")
        buf.write("\3\2\2\2)\u00fd\3\2\2\2+\u0103\3\2\2\2-\u010c\3\2\2\2")
        buf.write("/\u0111\3\2\2\2\61\u0117\3\2\2\2\63\u011c\3\2\2\2\65\u0121")
        buf.write("\3\2\2\2\67\u0125\3\2\2\29\u0127\3\2\2\2;\u012a\3\2\2")
        buf.write("\2=\u012c\3\2\2\2?\u012e\3\2\2\2A\u0131\3\2\2\2C\u0134")
        buf.write("\3\2\2\2E\u0137\3\2\2\2G\u0139\3\2\2\2I\u013b\3\2\2\2")
        buf.write("K\u013d\3\2\2\2M\u013f\3\2\2\2O\u0141\3\2\2\2Q\u0144\3")
        buf.write("\2\2\2S\u0147\3\2\2\2U\u014a\3\2\2\2W\u014d\3\2\2\2Y\u0150")
        buf.write("\3\2\2\2[\u0153\3\2\2\2]\u0156\3\2\2\2_\u0159\3\2\2\2")
        buf.write("a\u015c\3\2\2\2c\u015e\3\2\2\2e\u0161\3\2\2\2g\u0163\3")
        buf.write("\2\2\2i\u0165\3\2\2\2k\u0167\3\2\2\2m\u0169\3\2\2\2o\u016b")
        buf.write("\3\2\2\2q\u016d\3\2\2\2s\u016f\3\2\2\2u\u0171\3\2\2\2")
        buf.write("w\u0173\3\2\2\2y\u0175\3\2\2\2{\u0177\3\2\2\2}\u0180\3")
        buf.write("\2\2\2\177\u018d\3\2\2\2\u0081\u0193\3\2\2\2\u0083\u0195")
        buf.write("\3\2\2\2\u0085\u019a\3\2\2\2\u0087\u01a4\3\2\2\2\u0089")
        buf.write("\u01b6\3\2\2\2\u008b\u01c6\3\2\2\2\u008d\u01c8\3\2\2\2")
        buf.write("\u008f\u01d1\3\2\2\2\u0091\u01dc\3\2\2\2\u0093\u01eb\3")
        buf.write("\2\2\2\u0095\u01f1\3\2\2\2\u0097\u01f4\3\2\2\2\u0099\u01fd")
        buf.write("\3\2\2\2\u009b\u009c\7^\2\2\u009c\u009d\7$\2\2\u009d\4")
        buf.write("\3\2\2\2\u009e\u00a2\n\2\2\2\u009f\u00a2\5\3\2\2\u00a0")
        buf.write("\u00a2\t\3\2\2\u00a1\u009e\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a0\3\2\2\2\u00a2\6\3\2\2\2\u00a3\u00a4\7e\2")
        buf.write("\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7p\2\2\u00a6\u00a7\7")
        buf.write("u\2\2\u00a7\u00a8\7v\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7")
        buf.write("y\2\2\u00aa\u00ab\7j\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\n\3\2\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3")
        buf.write("\7q\2\2\u00b3\f\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7t\2\2\u00b7\16\3\2\2\2\u00b8\u00b9")
        buf.write("\7f\2\2\u00b9\u00ba\7q\2\2\u00ba\20\3\2\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7v\2\2\u00c1\22")
        buf.write("\3\2\2\2\u00c2\u00c3\7x\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7f\2\2\u00c6\24\3\2\2\2\u00c7\u00c8")
        buf.write("\7d\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7n\2\2\u00cb\26\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\u00cf\7v\2\2\u00cf\30\3\2\2\2\u00d0\u00d1")
        buf.write("\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7i\2\2\u00d6\32")
        buf.write("\3\2\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7j\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7t\2\2\u00db\34\3\2\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7i\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6 \3\2\2\2\u00e7\u00e8\7f\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\u00ed\7g\2\2\u00ed\"\3\2\2\2\u00ee\u00ef")
        buf.write("\7k\2\2\u00ef\u00f0\7h\2\2\u00f0$\3\2\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5&\3\2\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7p\2\2\u00fc(\3\2\2\2\u00fd\u00fe")
        buf.write("\7d\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7c\2\2\u0101\u0102\7m\2\2\u0102*\3\2\2\2\u0103\u0104")
        buf.write("\7e\2\2\u0104\u0105\7q\2\2\u0105\u0106\7p\2\2\u0106\u0107")
        buf.write("\7v\2\2\u0107\u0108\7k\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7g\2\2\u010b,\3\2\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d\u010e\7t\2\2\u010e\u010f\7w\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110.\3\2\2\2\u0111\u0112\7h\2\2\u0112\u0113")
        buf.write("\7c\2\2\u0113\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116\60\3\2\2\2\u0117\u0118\7v\2\2\u0118\u0119")
        buf.write("\7j\2\2\u0119\u011a\7k\2\2\u011a\u011b\7u\2\2\u011b\62")
        buf.write("\3\2\2\2\u011c\u011d\7P\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7p\2\2\u011f\u0120\7g\2\2\u0120\64\3\2\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7g\2\2\u0123\u0124\7y\2\2\u0124\66")
        buf.write("\3\2\2\2\u0125\u0126\7?\2\2\u01268\3\2\2\2\u0127\u0128")
        buf.write("\7?\2\2\u0128\u0129\7?\2\2\u0129:\3\2\2\2\u012a\u012b")
        buf.write("\7>\2\2\u012b<\3\2\2\2\u012c\u012d\7@\2\2\u012d>\3\2\2")
        buf.write("\2\u012e\u012f\7>\2\2\u012f\u0130\7?\2\2\u0130@\3\2\2")
        buf.write("\2\u0131\u0132\7@\2\2\u0132\u0133\7?\2\2\u0133B\3\2\2")
        buf.write("\2\u0134\u0135\7#\2\2\u0135\u0136\7?\2\2\u0136D\3\2\2")
        buf.write("\2\u0137\u0138\7-\2\2\u0138F\3\2\2\2\u0139\u013a\7/\2")
        buf.write("\2\u013aH\3\2\2\2\u013b\u013c\7,\2\2\u013cJ\3\2\2\2\u013d")
        buf.write("\u013e\7\61\2\2\u013eL\3\2\2\2\u013f\u0140\7\'\2\2\u0140")
        buf.write("N\3\2\2\2\u0141\u0142\7(\2\2\u0142\u0143\7(\2\2\u0143")
        buf.write("P\3\2\2\2\u0144\u0145\7~\2\2\u0145\u0146\7~\2\2\u0146")
        buf.write("R\3\2\2\2\u0147\u0148\7-\2\2\u0148\u0149\7-\2\2\u0149")
        buf.write("T\3\2\2\2\u014a\u014b\7/\2\2\u014b\u014c\7/\2\2\u014c")
        buf.write("V\3\2\2\2\u014d\u014e\7-\2\2\u014e\u014f\7?\2\2\u014f")
        buf.write("X\3\2\2\2\u0150\u0151\7/\2\2\u0151\u0152\7?\2\2\u0152")
        buf.write("Z\3\2\2\2\u0153\u0154\7,\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("\\\3\2\2\2\u0156\u0157\7\61\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("^\3\2\2\2\u0159\u015a\7\'\2\2\u015a\u015b\7?\2\2\u015b")
        buf.write("`\3\2\2\2\u015c\u015d\7#\2\2\u015db\3\2\2\2\u015e\u015f")
        buf.write("\7/\2\2\u015f\u0160\7@\2\2\u0160d\3\2\2\2\u0161\u0162")
        buf.write("\7\60\2\2\u0162f\3\2\2\2\u0163\u0164\7A\2\2\u0164h\3\2")
        buf.write("\2\2\u0165\u0166\7=\2\2\u0166j\3\2\2\2\u0167\u0168\7<")
        buf.write("\2\2\u0168l\3\2\2\2\u0169\u016a\7*\2\2\u016an\3\2\2\2")
        buf.write("\u016b\u016c\7+\2\2\u016cp\3\2\2\2\u016d\u016e\7]\2\2")
        buf.write("\u016er\3\2\2\2\u016f\u0170\7_\2\2\u0170t\3\2\2\2\u0171")
        buf.write("\u0172\7}\2\2\u0172v\3\2\2\2\u0173\u0174\7\177\2\2\u0174")
        buf.write("x\3\2\2\2\u0175\u0176\7.\2\2\u0176z\3\2\2\2\u0177\u017b")
        buf.write("\t\4\2\2\u0178\u017a\t\5\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c|\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0181\7\62\2")
        buf.write("\2\u017f\u0181\5\u0087D\2\u0180\u017e\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\b?\2\2\u0183")
        buf.write("~\3\2\2\2\u0184\u0185\5\u0087D\2\u0185\u0186\5\u0089E")
        buf.write("\2\u0186\u018e\3\2\2\2\u0187\u0189\7\60\2\2\u0188\u018a")
        buf.write("\t\6\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2")
        buf.write("\u018d\u0184\3\2\2\2\u018d\u0187\3\2\2\2\u018e\u0080\3")
        buf.write("\2\2\2\u018f\u0190\5\177@\2\u0190\u0191\7h\2\2\u0191\u0194")
        buf.write("\3\2\2\2\u0192\u0194\5\u008bF\2\u0193\u018f\3\2\2\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194\u0082\3\2\2\2\u0195\u0196\7)\2\2")
        buf.write("\u0196\u0197\5\5\3\2\u0197\u0198\7)\2\2\u0198\u0199\b")
        buf.write("B\3\2\u0199\u0084\3\2\2\2\u019a\u019e\7$\2\2\u019b\u019d")
        buf.write("\5\5\3\2\u019c\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1\u01a2\7$\2\2\u01a2\u01a3\b")
        buf.write("C\4\2\u01a3\u0086\3\2\2\2\u01a4\u01a8\t\7\2\2\u01a5\u01a7")
        buf.write("\t\6\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01b3\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ad\7a\2\2\u01ac\u01ae\t")
        buf.write("\6\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1")
        buf.write("\u01ab\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u0088\3\2\2\2\u01b5\u01b3\3")
        buf.write("\2\2\2\u01b6\u01ba\7\60\2\2\u01b7\u01b9\t\6\2\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01ba\u01bb\3\2\2\2\u01bb\u008a\3\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bd\u01bf\5}?\2\u01be\u01bd\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\5\u0089E\2\u01c1")
        buf.write("\u01c2\5\u008dG\2\u01c2\u01c7\3\2\2\2\u01c3\u01c4\5}?")
        buf.write("\2\u01c4\u01c5\5\u008dG\2\u01c5\u01c7\3\2\2\2\u01c6\u01be")
        buf.write("\3\2\2\2\u01c6\u01c3\3\2\2\2\u01c7\u008c\3\2\2\2\u01c8")
        buf.write("\u01ca\t\b\2\2\u01c9\u01cb\t\t\2\2\u01ca\u01c9\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ce\t")
        buf.write("\6\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u008e\3\2\2\2\u01d1")
        buf.write("\u01d2\7\61\2\2\u01d2\u01d3\7\61\2\2\u01d3\u01d7\3\2\2")
        buf.write("\2\u01d4\u01d6\n\n\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d9")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8")
        buf.write("\u01da\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01db\bH\5\2")
        buf.write("\u01db\u0090\3\2\2\2\u01dc\u01dd\7\61\2\2\u01dd\u01de")
        buf.write("\7,\2\2\u01de\u01e2\3\2\2\2\u01df\u01e1\13\2\2\2\u01e0")
        buf.write("\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e2\u01e0\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e2\3")
        buf.write("\2\2\2\u01e5\u01e6\7,\2\2\u01e6\u01e7\7\61\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e9\bI\5\2\u01e9\u0092\3\2\2\2\u01ea")
        buf.write("\u01ec\t\13\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ed\3\2\2")
        buf.write("\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f0\bJ\5\2\u01f0\u0094\3\2\2\2\u01f1")
        buf.write("\u01f2\13\2\2\2\u01f2\u01f3\bK\6\2\u01f3\u0096\3\2\2\2")
        buf.write("\u01f4\u01f8\7$\2\2\u01f5\u01f7\5\5\3\2\u01f6\u01f5\3")
        buf.write("\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9")
        buf.write("\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fb")
        buf.write("\u01fc\bL\7\2\u01fc\u0098\3\2\2\2\u01fd\u01fe\7\61\2\2")
        buf.write("\u01fe\u01ff\7,\2\2\u01ff\u0203\3\2\2\2\u0200\u0202\13")
        buf.write("\2\2\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0206\u0207\bM\b\2\u0207\u009a\3\2\2\2")
        buf.write("\27\2\u00a1\u017b\u0180\u018b\u018d\u0193\u019e\u01a8")
        buf.write("\u01af\u01b3\u01ba\u01be\u01c6\u01ca\u01cf\u01d7\u01e2")
        buf.write("\u01ed\u01f8\u0203\t\3?\2\3B\3\3C\4\b\2\2\3K\5\3L\6\3")
        buf.write("M\7")
        return buf.getvalue()


class AnotherCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CONST = 1
    WHILE = 2
    AUTO = 3
    FOR = 4
    DO = 5
    STRUCT = 6
    VOID = 7
    BOOL = 8
    INT = 9
    STRING = 10
    CHAR = 11
    LONG = 12
    FLOAT = 13
    DOUBLE = 14
    IF = 15
    ELSE = 16
    RETURN = 17
    BREAK = 18
    CONTINUE = 19
    TRUE = 20
    FALSE = 21
    THIS = 22
    NONE = 23
    NEW = 24
    ASSIGN = 25
    EQ = 26
    LT = 27
    GT = 28
    LTE = 29
    GTE = 30
    NOT_EQ = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV = 35
    MOD = 36
    AND = 37
    OR = 38
    INC = 39
    DEC = 40
    ADD_ASSIGN = 41
    SUB_ASSIGN = 42
    MUL_ASSIGN = 43
    DIV_ASSIGN = 44
    MOD_ASSIGN = 45
    NEG = 46
    ARROW = 47
    DOT = 48
    QM = 49
    SEMI = 50
    COLON = 51
    LB = 52
    RB = 53
    LS = 54
    RS = 55
    LC = 56
    RC = 57
    COMMA = 58
    ID = 59
    INT_LIT = 60
    DOUBLE_LIT = 61
    FLOAT_LIT = 62
    CHAR_LIT = 63
    STR_LIT = 64
    LINE_CMT = 65
    BLOCK_CMT = 66
    WS = 67
    ERROR_CHAR = 68
    UNCLOSED_STRING = 69
    UNTERMINATED_COMMENT = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'const'", "'while'", "'auto'", "'for'", "'do'", "'struct'", 
            "'void'", "'bool'", "'int'", "'string'", "'char'", "'long'", 
            "'float'", "'double'", "'if'", "'else'", "'return'", "'break'", 
            "'continue'", "'true'", "'false'", "'this'", "'None'", "'new'", 
            "'='", "'=='", "'<'", "'>'", "'<='", "'>='", "'!='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'++'", "'--'", 
            "'+='", "'-='", "'*='", "'/='", "'%='", "'!'", "'->'", "'.'", 
            "'?'", "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "CONST", "WHILE", "AUTO", "FOR", "DO", "STRUCT", "VOID", "BOOL", 
            "INT", "STRING", "CHAR", "LONG", "FLOAT", "DOUBLE", "IF", "ELSE", 
            "RETURN", "BREAK", "CONTINUE", "TRUE", "FALSE", "THIS", "NONE", 
            "NEW", "ASSIGN", "EQ", "LT", "GT", "LTE", "GTE", "NOT_EQ", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "AND", "OR", "INC", "DEC", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "NEG", 
            "ARROW", "DOT", "QM", "SEMI", "COLON", "LB", "RB", "LS", "RS", 
            "LC", "RC", "COMMA", "ID", "INT_LIT", "DOUBLE_LIT", "FLOAT_LIT", 
            "CHAR_LIT", "STR_LIT", "LINE_CMT", "BLOCK_CMT", "WS", "ERROR_CHAR", 
            "UNCLOSED_STRING", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DoubleQuote", "Character", "CONST", "WHILE", "AUTO", 
                  "FOR", "DO", "STRUCT", "VOID", "BOOL", "INT", "STRING", 
                  "CHAR", "LONG", "FLOAT", "DOUBLE", "IF", "ELSE", "RETURN", 
                  "BREAK", "CONTINUE", "TRUE", "FALSE", "THIS", "NONE", 
                  "NEW", "ASSIGN", "EQ", "LT", "GT", "LTE", "GTE", "NOT_EQ", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "INC", 
                  "DEC", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "NEG", "ARROW", "DOT", "QM", "SEMI", "COLON", 
                  "LB", "RB", "LS", "RS", "LC", "RC", "COMMA", "ID", "INT_LIT", 
                  "DOUBLE_LIT", "FLOAT_LIT", "CHAR_LIT", "STR_LIT", "DECIMAL", 
                  "FDec", "Scientific", "FExp", "LINE_CMT", "BLOCK_CMT", 
                  "WS", "ERROR_CHAR", "UNCLOSED_STRING", "UNTERMINATED_COMMENT" ]

    grammarFileName = "AnotherC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.INT_LIT_action 
            actions[64] = self.CHAR_LIT_action 
            actions[65] = self.STR_LIT_action 
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.UNCLOSED_STRING_action 
            actions[75] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def CHAR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            self.text = self.text[1:-1]
            for idx, value in enumerate(self.text):
                if ord(value) not in [0, 8, 9, 10, 12, 13] and ord(value) not in range(32, 127):
                    raise IllegalEscape(self.text[:idx])
                if ord(value) == 10:
                    raise UnclosedString(self.text[:idx])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text) 
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            raise UnclosedString(self.text[1:])

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            raise UnterminatedComment(self.text)

     


