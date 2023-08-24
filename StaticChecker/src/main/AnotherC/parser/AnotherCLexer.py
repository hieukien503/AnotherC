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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u0201\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u00a0\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\7=\u0173\n=\f=\16=\u0176\13=\3>\3>\5>\u017a")
        buf.write("\n>\3>\3>\3?\3?\3?\3?\3?\6?\u0183\n?\r?\16?\u0184\5?\u0187")
        buf.write("\n?\3@\3@\3@\3@\5@\u018d\n@\3A\3A\3A\3A\3A\3B\3B\7B\u0196")
        buf.write("\nB\fB\16B\u0199\13B\3B\3B\3B\3C\3C\7C\u01a0\nC\fC\16")
        buf.write("C\u01a3\13C\3C\3C\6C\u01a7\nC\rC\16C\u01a8\7C\u01ab\n")
        buf.write("C\fC\16C\u01ae\13C\3D\3D\7D\u01b2\nD\fD\16D\u01b5\13D")
        buf.write("\3E\5E\u01b8\nE\3E\3E\3E\3E\3E\3E\5E\u01c0\nE\3F\3F\5")
        buf.write("F\u01c4\nF\3F\6F\u01c7\nF\rF\16F\u01c8\3G\3G\3G\3G\7G")
        buf.write("\u01cf\nG\fG\16G\u01d2\13G\3G\3G\3H\3H\3H\3H\7H\u01da")
        buf.write("\nH\fH\16H\u01dd\13H\3H\3H\3H\3H\3H\3I\6I\u01e5\nI\rI")
        buf.write("\16I\u01e6\3I\3I\3J\3J\3J\3K\3K\7K\u01f0\nK\fK\16K\u01f3")
        buf.write("\13K\3K\3K\3L\3L\3L\3L\7L\u01fb\nL\fL\16L\u01fe\13L\3")
        buf.write("L\3L\4\u01db\u01fc\2M\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21")
        buf.write("\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'")
        buf.write("\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63")
        buf.write("i\64k\65m\66o\67q8s9u:w;y<{=}>\177?\u0081@\u0083A\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008dB\u008fC\u0091D\u0093")
        buf.write("E\u0095F\u0097G\3\2\f\7\2\n\f\16\17$$))^^\5\2\n\13\16")
        buf.write("\17))\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2GG")
        buf.write("gg\4\2--//\4\2\f\f\16\17\5\2\13\f\17\17\"\"\2\u020f\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u008d\3\2\2\2")
        buf.write("\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00a1\3\2\2\2\t\u00a7\3\2\2\2\13\u00ad\3\2\2\2\r")
        buf.write("\u00b2\3\2\2\2\17\u00b6\3\2\2\2\21\u00b9\3\2\2\2\23\u00c0")
        buf.write("\3\2\2\2\25\u00c5\3\2\2\2\27\u00ca\3\2\2\2\31\u00ce\3")
        buf.write("\2\2\2\33\u00d5\3\2\2\2\35\u00da\3\2\2\2\37\u00df\3\2")
        buf.write("\2\2!\u00e5\3\2\2\2#\u00ec\3\2\2\2%\u00ef\3\2\2\2\'\u00f4")
        buf.write("\3\2\2\2)\u00fb\3\2\2\2+\u0101\3\2\2\2-\u010a\3\2\2\2")
        buf.write("/\u010f\3\2\2\2\61\u0115\3\2\2\2\63\u011a\3\2\2\2\65\u011e")
        buf.write("\3\2\2\2\67\u0120\3\2\2\29\u0123\3\2\2\2;\u0125\3\2\2")
        buf.write("\2=\u0127\3\2\2\2?\u012a\3\2\2\2A\u012d\3\2\2\2C\u0130")
        buf.write("\3\2\2\2E\u0132\3\2\2\2G\u0134\3\2\2\2I\u0136\3\2\2\2")
        buf.write("K\u0138\3\2\2\2M\u013a\3\2\2\2O\u013d\3\2\2\2Q\u0140\3")
        buf.write("\2\2\2S\u0143\3\2\2\2U\u0146\3\2\2\2W\u0149\3\2\2\2Y\u014c")
        buf.write("\3\2\2\2[\u014f\3\2\2\2]\u0152\3\2\2\2_\u0155\3\2\2\2")
        buf.write("a\u0157\3\2\2\2c\u015a\3\2\2\2e\u015c\3\2\2\2g\u015e\3")
        buf.write("\2\2\2i\u0160\3\2\2\2k\u0162\3\2\2\2m\u0164\3\2\2\2o\u0166")
        buf.write("\3\2\2\2q\u0168\3\2\2\2s\u016a\3\2\2\2u\u016c\3\2\2\2")
        buf.write("w\u016e\3\2\2\2y\u0170\3\2\2\2{\u0179\3\2\2\2}\u0186\3")
        buf.write("\2\2\2\177\u018c\3\2\2\2\u0081\u018e\3\2\2\2\u0083\u0193")
        buf.write("\3\2\2\2\u0085\u019d\3\2\2\2\u0087\u01af\3\2\2\2\u0089")
        buf.write("\u01bf\3\2\2\2\u008b\u01c1\3\2\2\2\u008d\u01ca\3\2\2\2")
        buf.write("\u008f\u01d5\3\2\2\2\u0091\u01e4\3\2\2\2\u0093\u01ea\3")
        buf.write("\2\2\2\u0095\u01ed\3\2\2\2\u0097\u01f6\3\2\2\2\u0099\u009a")
        buf.write("\7^\2\2\u009a\u009b\7$\2\2\u009b\4\3\2\2\2\u009c\u00a0")
        buf.write("\n\2\2\2\u009d\u00a0\5\3\2\2\u009e\u00a0\t\3\2\2\u009f")
        buf.write("\u009c\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\6\3\2\2\2\u00a1\u00a2\7e\2\2\u00a2\u00a3\7q\2\2")
        buf.write("\u00a3\u00a4\7p\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7v")
        buf.write("\2\2\u00a6\b\3\2\2\2\u00a7\u00a8\7y\2\2\u00a8\u00a9\7")
        buf.write("j\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab\7n\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\n\3\2\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af")
        buf.write("\7w\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7q\2\2\u00b1\f")
        buf.write("\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\16\3\2\2\2\u00b6\u00b7\7f\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\20\3\2\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be")
        buf.write("\7e\2\2\u00be\u00bf\7v\2\2\u00bf\22\3\2\2\2\u00c0\u00c1")
        buf.write("\7x\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7f\2\2\u00c4\24\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7n\2\2\u00c9\26")
        buf.write("\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\30\3\2\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7i\2\2\u00d4\32\3\2\2\2\u00d5\u00d6")
        buf.write("\7e\2\2\u00d6\u00d7\7j\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7t\2\2\u00d9\34\3\2\2\2\u00da\u00db\7n\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7i\2\2\u00de\36")
        buf.write("\3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7v\2\2\u00e4 \3")
        buf.write("\2\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7w\2\2\u00e8\u00e9\7d\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\"\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7h\2\2\u00ee$\3\2\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7g\2\2\u00f3&\3")
        buf.write("\2\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa(\3\2\2\2\u00fb\u00fc\7d\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100")
        buf.write("\7m\2\2\u0100*\3\2\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108\7w\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109,\3\2\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7w\2\2\u010d\u010e\7g\2\2\u010e.\3")
        buf.write("\2\2\2\u010f\u0110\7h\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114\60")
        buf.write("\3\2\2\2\u0115\u0116\7v\2\2\u0116\u0117\7j\2\2\u0117\u0118")
        buf.write("\7k\2\2\u0118\u0119\7u\2\2\u0119\62\3\2\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7g\2\2\u011c\u011d\7y\2\2\u011d\64")
        buf.write("\3\2\2\2\u011e\u011f\7?\2\2\u011f\66\3\2\2\2\u0120\u0121")
        buf.write("\7?\2\2\u0121\u0122\7?\2\2\u01228\3\2\2\2\u0123\u0124")
        buf.write("\7>\2\2\u0124:\3\2\2\2\u0125\u0126\7@\2\2\u0126<\3\2\2")
        buf.write("\2\u0127\u0128\7>\2\2\u0128\u0129\7?\2\2\u0129>\3\2\2")
        buf.write("\2\u012a\u012b\7@\2\2\u012b\u012c\7?\2\2\u012c@\3\2\2")
        buf.write("\2\u012d\u012e\7#\2\2\u012e\u012f\7?\2\2\u012fB\3\2\2")
        buf.write("\2\u0130\u0131\7-\2\2\u0131D\3\2\2\2\u0132\u0133\7/\2")
        buf.write("\2\u0133F\3\2\2\2\u0134\u0135\7,\2\2\u0135H\3\2\2\2\u0136")
        buf.write("\u0137\7\61\2\2\u0137J\3\2\2\2\u0138\u0139\7\'\2\2\u0139")
        buf.write("L\3\2\2\2\u013a\u013b\7(\2\2\u013b\u013c\7(\2\2\u013c")
        buf.write("N\3\2\2\2\u013d\u013e\7~\2\2\u013e\u013f\7~\2\2\u013f")
        buf.write("P\3\2\2\2\u0140\u0141\7-\2\2\u0141\u0142\7-\2\2\u0142")
        buf.write("R\3\2\2\2\u0143\u0144\7/\2\2\u0144\u0145\7/\2\2\u0145")
        buf.write("T\3\2\2\2\u0146\u0147\7-\2\2\u0147\u0148\7?\2\2\u0148")
        buf.write("V\3\2\2\2\u0149\u014a\7/\2\2\u014a\u014b\7?\2\2\u014b")
        buf.write("X\3\2\2\2\u014c\u014d\7,\2\2\u014d\u014e\7?\2\2\u014e")
        buf.write("Z\3\2\2\2\u014f\u0150\7\61\2\2\u0150\u0151\7?\2\2\u0151")
        buf.write("\\\3\2\2\2\u0152\u0153\7\'\2\2\u0153\u0154\7?\2\2\u0154")
        buf.write("^\3\2\2\2\u0155\u0156\7#\2\2\u0156`\3\2\2\2\u0157\u0158")
        buf.write("\7/\2\2\u0158\u0159\7@\2\2\u0159b\3\2\2\2\u015a\u015b")
        buf.write("\7\60\2\2\u015bd\3\2\2\2\u015c\u015d\7A\2\2\u015df\3\2")
        buf.write("\2\2\u015e\u015f\7=\2\2\u015fh\3\2\2\2\u0160\u0161\7<")
        buf.write("\2\2\u0161j\3\2\2\2\u0162\u0163\7*\2\2\u0163l\3\2\2\2")
        buf.write("\u0164\u0165\7+\2\2\u0165n\3\2\2\2\u0166\u0167\7]\2\2")
        buf.write("\u0167p\3\2\2\2\u0168\u0169\7_\2\2\u0169r\3\2\2\2\u016a")
        buf.write("\u016b\7}\2\2\u016bt\3\2\2\2\u016c\u016d\7\177\2\2\u016d")
        buf.write("v\3\2\2\2\u016e\u016f\7.\2\2\u016fx\3\2\2\2\u0170\u0174")
        buf.write("\t\4\2\2\u0171\u0173\t\5\2\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175z\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017a\7\62\2")
        buf.write("\2\u0178\u017a\5\u0085C\2\u0179\u0177\3\2\2\2\u0179\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\b>\2\2\u017c")
        buf.write("|\3\2\2\2\u017d\u017e\5\u0085C\2\u017e\u017f\5\u0087D")
        buf.write("\2\u017f\u0187\3\2\2\2\u0180\u0182\7\60\2\2\u0181\u0183")
        buf.write("\t\6\2\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2")
        buf.write("\u0186\u017d\3\2\2\2\u0186\u0180\3\2\2\2\u0187~\3\2\2")
        buf.write("\2\u0188\u0189\5}?\2\u0189\u018a\7h\2\2\u018a\u018d\3")
        buf.write("\2\2\2\u018b\u018d\5\u0089E\2\u018c\u0188\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u0080\3\2\2\2\u018e\u018f\7)\2\2")
        buf.write("\u018f\u0190\5\5\3\2\u0190\u0191\7)\2\2\u0191\u0192\b")
        buf.write("A\3\2\u0192\u0082\3\2\2\2\u0193\u0197\7$\2\2\u0194\u0196")
        buf.write("\5\5\3\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019a\3\2\2\2")
        buf.write("\u0199\u0197\3\2\2\2\u019a\u019b\7$\2\2\u019b\u019c\b")
        buf.write("B\4\2\u019c\u0084\3\2\2\2\u019d\u01a1\t\7\2\2\u019e\u01a0")
        buf.write("\t\6\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01ac\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a4\u01a6\7a\2\2\u01a5\u01a7\t")
        buf.write("\6\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a4\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u0086\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01af\u01b3\7\60\2\2\u01b0\u01b2\t\6\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4\u0088\3\2\2\2\u01b5\u01b3\3")
        buf.write("\2\2\2\u01b6\u01b8\5{>\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\5\u0087D\2\u01ba")
        buf.write("\u01bb\5\u008bF\2\u01bb\u01c0\3\2\2\2\u01bc\u01bd\5{>")
        buf.write("\2\u01bd\u01be\5\u008bF\2\u01be\u01c0\3\2\2\2\u01bf\u01b7")
        buf.write("\3\2\2\2\u01bf\u01bc\3\2\2\2\u01c0\u008a\3\2\2\2\u01c1")
        buf.write("\u01c3\t\b\2\2\u01c2\u01c4\t\t\2\2\u01c3\u01c2\3\2\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01c7\t")
        buf.write("\6\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u008c\3\2\2\2\u01ca")
        buf.write("\u01cb\7\61\2\2\u01cb\u01cc\7\61\2\2\u01cc\u01d0\3\2\2")
        buf.write("\2\u01cd\u01cf\n\n\2\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\bG\5\2")
        buf.write("\u01d4\u008e\3\2\2\2\u01d5\u01d6\7\61\2\2\u01d6\u01d7")
        buf.write("\7,\2\2\u01d7\u01db\3\2\2\2\u01d8\u01da\13\2\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3")
        buf.write("\2\2\2\u01de\u01df\7,\2\2\u01df\u01e0\7\61\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01e2\bH\5\2\u01e2\u0090\3\2\2\2\u01e3")
        buf.write("\u01e5\t\13\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2")
        buf.write("\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e9\bI\5\2\u01e9\u0092\3\2\2\2\u01ea")
        buf.write("\u01eb\13\2\2\2\u01eb\u01ec\bJ\6\2\u01ec\u0094\3\2\2\2")
        buf.write("\u01ed\u01f1\7$\2\2\u01ee\u01f0\5\5\3\2\u01ef\u01ee\3")
        buf.write("\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f5\bK\7\2\u01f5\u0096\3\2\2\2\u01f6\u01f7\7\61\2\2")
        buf.write("\u01f7\u01f8\7,\2\2\u01f8\u01fc\3\2\2\2\u01f9\u01fb\13")
        buf.write("\2\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fd")
        buf.write("\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01ff\u0200\bL\b\2\u0200\u0098\3\2\2\2")
        buf.write("\27\2\u009f\u0174\u0179\u0184\u0186\u018c\u0197\u01a1")
        buf.write("\u01a8\u01ac\u01b3\u01b7\u01bf\u01c3\u01c8\u01d0\u01db")
        buf.write("\u01e6\u01f1\u01fc\t\3>\2\3A\3\3B\4\b\2\2\3J\5\3K\6\3")
        buf.write("L\7")
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
    NEW = 23
    ASSIGN = 24
    EQ = 25
    LT = 26
    GT = 27
    LTE = 28
    GTE = 29
    NOT_EQ = 30
    ADD = 31
    SUB = 32
    MUL = 33
    DIV = 34
    MOD = 35
    AND = 36
    OR = 37
    INC = 38
    DEC = 39
    ADD_ASSIGN = 40
    SUB_ASSIGN = 41
    MUL_ASSIGN = 42
    DIV_ASSIGN = 43
    MOD_ASSIGN = 44
    NEG = 45
    ARROW = 46
    DOT = 47
    QM = 48
    SEMI = 49
    COLON = 50
    LB = 51
    RB = 52
    LS = 53
    RS = 54
    LC = 55
    RC = 56
    COMMA = 57
    ID = 58
    INT_LIT = 59
    DOUBLE_LIT = 60
    FLOAT_LIT = 61
    CHAR_LIT = 62
    STR_LIT = 63
    LINE_CMT = 64
    BLOCK_CMT = 65
    WS = 66
    ERROR_CHAR = 67
    UNCLOSED_STRING = 68
    UNTERMINATED_COMMENT = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'const'", "'while'", "'auto'", "'for'", "'do'", "'struct'", 
            "'void'", "'bool'", "'int'", "'string'", "'char'", "'long'", 
            "'float'", "'double'", "'if'", "'else'", "'return'", "'break'", 
            "'continue'", "'true'", "'false'", "'this'", "'new'", "'='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'!='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'&&'", "'||'", "'++'", "'--'", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "'!'", "'->'", "'.'", "'?'", 
            "';'", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','" ]

    symbolicNames = [ "<INVALID>",
            "CONST", "WHILE", "AUTO", "FOR", "DO", "STRUCT", "VOID", "BOOL", 
            "INT", "STRING", "CHAR", "LONG", "FLOAT", "DOUBLE", "IF", "ELSE", 
            "RETURN", "BREAK", "CONTINUE", "TRUE", "FALSE", "THIS", "NEW", 
            "ASSIGN", "EQ", "LT", "GT", "LTE", "GTE", "NOT_EQ", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "AND", "OR", "INC", "DEC", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "NEG", 
            "ARROW", "DOT", "QM", "SEMI", "COLON", "LB", "RB", "LS", "RS", 
            "LC", "RC", "COMMA", "ID", "INT_LIT", "DOUBLE_LIT", "FLOAT_LIT", 
            "CHAR_LIT", "STR_LIT", "LINE_CMT", "BLOCK_CMT", "WS", "ERROR_CHAR", 
            "UNCLOSED_STRING", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DoubleQuote", "Character", "CONST", "WHILE", "AUTO", 
                  "FOR", "DO", "STRUCT", "VOID", "BOOL", "INT", "STRING", 
                  "CHAR", "LONG", "FLOAT", "DOUBLE", "IF", "ELSE", "RETURN", 
                  "BREAK", "CONTINUE", "TRUE", "FALSE", "THIS", "NEW", "ASSIGN", 
                  "EQ", "LT", "GT", "LTE", "GTE", "NOT_EQ", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "AND", "OR", "INC", "DEC", "ADD_ASSIGN", 
                  "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "NEG", "ARROW", "DOT", "QM", "SEMI", "COLON", "LB", "RB", 
                  "LS", "RS", "LC", "RC", "COMMA", "ID", "INT_LIT", "DOUBLE_LIT", 
                  "FLOAT_LIT", "CHAR_LIT", "STR_LIT", "DECIMAL", "FDec", 
                  "Scientific", "FExp", "LINE_CMT", "BLOCK_CMT", "WS", "ERROR_CHAR", 
                  "UNCLOSED_STRING", "UNTERMINATED_COMMENT" ]

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
            actions[60] = self.INT_LIT_action 
            actions[63] = self.CHAR_LIT_action 
            actions[64] = self.STR_LIT_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSED_STRING_action 
            actions[74] = self.UNTERMINATED_COMMENT_action 
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

     


