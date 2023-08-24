from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *
from CodeGenError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                ]]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(Visitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = 'AnotherC'
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.classEnv = []
        self.strCode = []
        
    def visitIntegerType(self, ast, o):
        return IntegerType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBooleanType(self, ast, o):
        return BooleanType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitArrayType(self, ast, o):
        return ArrayType(ast.dimensions, self.visit(ast.typ, o))
    
    def visitAutoType(self, ast, o):
        return AutoType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitCharType(self, ast, o):
        return CharType()
    
    def visitStructType(self, ast, o):
        return StructType(ast.name)
    
    def visitDoubleType(self, ast, o):
        return DoubleType()

    def visitBinExpr(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        e1c += + ("" if not isinstance(ast.left, ArrayCell) else self.emit.emitALOAD(e1t, o.frame))
        e2c += + ("" if not isinstance(ast.left, ArrayCell) else self.emit.emitALOAD(e2t, o.frame))
        if ast.op == '+':
            if isinstance(e1t, StringType):
                if isinstance (ast.left, StringLit) and isinstance(ast.right, (StringLit, CharLit)):
                    o.frame.pop()
                    o.frame.pop()
                    return self.visit(StringLit(ast.left.val + ast.right.val), o)
                else:
                    if self.strCode == []:
                        self.strCode += [self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/toString", MType([], StringType()), o.frame)]
                        code = self.emit.emitNEW("java/lang/StringBuilder", o.frame) + self.emit.emitDUP(o.frame) + e1c
                        code += self.emit.emitINVOKESPECIAL(o.frame, "java/lang/StringBuilder/<init>", MType([StringType()], VoidType()))
                        self.strCode.insert(0, code)
                    self.strCode.insert(-1, e2c + self.emit.emitINVOKEVIRTUAL("java/lang/StringBuilder/append", MType([e2t], "Ljava/lang/StringBuilder;"), o.frame))
                    return "", StringType()
            else:
                if isinstance(e1t, DoubleType) or isinstance(e2t, DoubleType):
                    if (isinstance(ast.left, DoubleLit) and isinstance(ast.right, (DoubleLit, IntegerLit, FloatLit))) or (isinstance(ast.right, DoubleLit) and isinstance(ast.left, (DoubleLit, IntegerLit, FloatLit))):
                        return self.visit(DoubleLit(ast.left.val + ast.right.val), o)
                    
                    e1c += self.emit.emitI2D(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e1t, FloatType) and isinstance(e2t, DoubleType) else e1c)
                    e2c += self.emit.emitI2D(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e2t, FloatType) and isinstance(e1t, DoubleType) else e2c)
                    return e1c + e2c + self.emit.emitADDOP(ast.op, DoubleType(), o.frame), DoubleType()
                
                elif isinstance(e1t, FloatType) or isinstance(e2t, FloatType):
                    if (isinstance(ast.left, FloatLit) and isinstance(ast.right, (IntegerLit, FloatLit))) or (isinstance(ast.right, FloatLit) and isinstance(ast.left, (IntegerLit, FloatLit))):
                        return self.visit(FloatLit(ast.left.val + ast.right.val), o)
                    
                    e1c += self.emit.emitI2F(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, FloatType) else e1c
                    e2c += self.emit.emitI2F(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, FloatType) else e2c
                    return e1c + e2c + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
                
                else:
                    if isinstance(ast.left, IntegerLit) and isinstance(ast.right, IntegerLit):
                        return self.visit(IntegerLit(ast.left.val + ast.right.val), o)
                
                    return e1c + e2c + self.emit.emitADDOP(ast.op, IntegerType(), o.frame), IntegerType()
                
        elif ast.op == '-':
            if isinstance(e1t, DoubleType) or isinstance(e2t, DoubleType):
                if (isinstance(ast.left, DoubleLit) and isinstance(ast.right, (DoubleLit, IntegerLit, FloatLit))) or (isinstance(ast.right, DoubleLit) and isinstance(ast.left, (DoubleLit, IntegerLit, FloatLit))):
                    return self.visit(DoubleLit(ast.left.val - ast.right.val), o)
                    
                e1c += self.emit.emitI2D(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e1t, FloatType) and isinstance(e2t, DoubleType) else e1c)
                e2c += self.emit.emitI2D(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e2t, FloatType) and isinstance(e1t, DoubleType) else e2c)
                return e1c + e2c + self.emit.emitADDOP(ast.op, DoubleType(), o.frame), DoubleType()
                
            elif isinstance(e1t, FloatType) or isinstance(e2t, FloatType):
                if (isinstance(ast.left, FloatLit) and isinstance(ast.right, (IntegerLit, FloatLit))) or (isinstance(ast.right, FloatLit) and isinstance(ast.left, (IntegerLit, FloatLit))):
                    return self.visit(FloatLit(ast.left.val - ast.right.val), o)
                
                e1c += self.emit.emitI2F(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, FloatType) else e1c
                e2c += self.emit.emitI2F(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, FloatType) else e2c
                return e1c + e2c + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
            
            else:
                if isinstance(ast.left, IntegerLit) and isinstance(ast.right, IntegerLit):
                    return self.visit(IntegerLit(ast.left.val - ast.right.val), o)
                
                return e1c + e2c + self.emit.emitADDOP(ast.op, IntegerType(), o.frame), IntegerType()
        
        elif ast.op in ['*', '/']:
            if isinstance(e1t, DoubleType) or isinstance(e2t, DoubleType):
                if (isinstance(ast.left, DoubleLit) and isinstance(ast.right, (DoubleLit, IntegerLit, FloatLit))) or (isinstance(ast.right, DoubleLit) and isinstance(ast.left, (DoubleLit, IntegerLit, FloatLit))):
                    return self.visit(DoubleLit(ast.left.val * ast.right.val), o) if ast.op == '*' else self.visit(DoubleLit(ast.left.val / ast.right.val), o)
                    
                e1c += self.emit.emitI2D(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e1t, FloatType) and isinstance(e2t, DoubleType) else e1c)
                e2c += self.emit.emitI2D(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e2t, FloatType) and isinstance(e1t, DoubleType) else e2c)
                return e1c + e2c + self.emit.emitMULOP(ast.op, DoubleType(), o.frame), DoubleType()
                
            elif isinstance(e1t, FloatType) or isinstance(e2t, FloatType):
                if (isinstance(ast.left, FloatLit) and isinstance(ast.right, (IntegerLit, FloatLit))) or (isinstance(ast.right, FloatLit) and isinstance(ast.left, (IntegerLit, FloatLit))):
                    return self.visit(FloatLit(ast.left.val * ast.right.val), o) if ast.op == '*' else self.visit(FloatLit(ast.left.val / ast.right.val), o)
                
                e1c += self.emit.emitI2F(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, FloatType) else e1c
                e2c += self.emit.emitI2F(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, FloatType) else e2c
                return e1c + e2c + self.emit.emitMULOP(ast.op, FloatType(), o.frame), FloatType()
            
            else:
                if isinstance(ast.left, IntegerLit) and isinstance(ast.right, IntegerLit):
                    return self.visit(IntegerLit(ast.left.val - ast.right.val), o) if ast.op == '*' else self.visit(IntegerLit(ast.left.val / ast.right.val), o)
                
                return e1c + e2c + self.emit.emitMULOP(ast.op, IntegerType(), o.frame), IntegerType()
        
        elif ast.op == '%':
            return e1c + e2c + self.emit.emitMOD(o.frame), IntegerType()
        
        elif ast.op == '&&':
            label1 = o.frame.getNewLabel()
            label2 = o.frame.getNewLabel()
            e1c = e1c + self.emit.emitIFTRUE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitGOTO(label2, o.frame)
            e2c = self.emit.emitLABEL(label1, o.frame) + e2c + self.emit.emitLABEL(label2, o.frame)
            return e1c + e2c, BooleanType()
        
        elif ast.op == '||':
            label1 = o.frame.getNewLabel()
            label2 = o.frame.getNewLabel()
            e1c = e1c + self.emit.emitIFFALSE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitGOTO(label2, o.frame)
            e2c = self.emit.emitLABEL(label1, o.frame) + e2c + self.emit.emitLABEL(label2, o.frame)
            return e1c + e2c, BooleanType()
        
        elif ast.op in ['<', '>', '<=', '>=']:
            if isinstance(e1t, DoubleType) or isinstance(e2t, DoubleType):
                e1c += self.emit.emitI2D(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e1t, FloatType) and isinstance(e2t, DoubleType) else e1c)
                e2c += self.emit.emitI2D(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e2t, FloatType) and isinstance(e1t, DoubleType) else e2c)
                return e1c + e2c + self.emit.emitREOP(ast.op, DoubleType(), o.frame), DoubleType()
                
            elif isinstance(e1t, FloatType) or isinstance(e2t, FloatType):
                e1c += self.emit.emitI2F(o.frame) if isinstance(e1t, IntegerType) and isinstance(e2t, FloatType) else e1c
                e2c += self.emit.emitI2F(o.frame) if isinstance(e2t, IntegerType) and isinstance(e1t, FloatType) else e2c
                return e1c + e2c + self.emit.emitREOP(ast.op, FloatType(), o.frame), FloatType()
            
            else:
                return e1c + e2c + self.emit.emitREOP(ast.op, IntegerType(), o.frame), IntegerType()

    def visitUnExpr(self, ast, o):
        ec, et = self.visit(ast.val, o)
        if ast.op == '!':
            return ec + self.emit.emitNOT(et, o.frame), et
        elif ast.op == '+':
            return ec, et
        elif ast.op == '-':
            return ec + self.emit.emitNEGOP(et, o.frame), et
        else:
            if not isinstance(ast.val, Id):
                raise IllegalOperandException(str(ast.val))
            
            if not isinstance(et, IntegerType):
                self.visit(AssignStmt(ast.val, BinExpr(ast.op[0], ast.val, IntegerLit(1))), o)

            else:
                for lst in o.sym:
                    sym = self.lookup(ast.val.name, lst, lambda x: x.name)
                    if sym is not None:
                        if isinstance(sym.value, Index):
                            return self.emit.emitIINC(sym.value.value, (1 if ast.op == '++' else - 1)), IntegerType()
                        else:
                            self.visit(AssignStmt(ast.val, BinExpr(ast.op[0], ast.val, IntegerLit(1))), o)
                        
                    
    def visitTernaryExpr(self, ast, o):
        e1c, e1t = self.visit(ast.expr1, o)
        e2c, e2t = self.visit(ast.texpr, o)
        e3c, e3t = self.visit(ast.fexpr, o)
        rt = None
        if isinstance(e2t, DoubleType) or isinstance(e3t, DoubleType):
            e2c += self.emit.emitI2D(o.frame) if isinstance(e2t, IntegerType) and isinstance(e3t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e2t, FloatType) and isinstance(e3t, DoubleType) else e2c)
            e3c += self.emit.emitI2D(o.frame) if isinstance(e3t, IntegerType) and isinstance(e2t, DoubleType) else (self.emit.emitF2D(o.frame) if isinstance(e3t, FloatType) and isinstance(e2t, DoubleType) else e3c)
            rt = DoubleType()
        elif isinstance(e1t, FloatType) or isinstance(e2t, FloatType):
            e2c += self.emit.emitI2F(o.frame) if isinstance(e2t, IntegerType) and isinstance(e3t, FloatType) else e2c
            e3c += self.emit.emitI2F(o.frame) if isinstance(e3t, IntegerType) and isinstance(e2t, FloatType) else e3c
            rt = FloatType()
        else:
            rt = IntegerType()

        label1 = o.frame.getNewLabel()
        label2 = o.frame.getNewLabel()
        e1c += self.emit.emitIFFALSE(label1, o.frame) + e2c + self.emit.emitGOTO(label2, o.frame)
        e1c += self.emit.emitLABEL(label1, o.frame) + e3c + self.emit.emitLABEL(label2, o.frame)
        return e1c, rt

    def visitId(self, ast, o): pass

    def visitArrayCell(self, ast, o): pass

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
    
    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()
    
    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST('\"' + ast.val + '\"', StringType(), o.frame), StringType()
    
    def visitBooleanLit(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.val).lower(), BooleanType(), o.frame), BooleanType()
    
    def visitArrayLit(self, ast, o): pass

    def visitDoubleLit(self, ast, o):
        return self.emit.emitPUSHDCONST(str(ast.val), o.frame), DoubleType()
    
    def visitMemberAccess(self, ast, o): pass

    def visitCharLit(self, ast, o):
        return self.emit.emitPUSHICONST(ord(ast.val), o.frame), CharType()
    
    def visitNewExpr(self, ast, o): pass

    def visitFuncCall(self, ast, o): pass

    def visitAssignStmt(self, ast, o): pass

    def visitBlockStmt(self, ast, o): pass

    def visitIfStmt(self, ast, o): pass

    def visitForStmt(self, ast, o): pass

    def visitWhileStmt(self, ast, o): pass

    def visitDoWhileStmt(self, ast, o): pass

    def visitBreakStmt(self, ast, o): pass

    def visitContinueStmt(self, ast, o): pass

    def visitReturnStmt(self, ast, o): pass

    def visitCallStmt(self, ast, o): pass

    def visitVarDecl(self, ast, o): pass

    def visitParamDecl(self, ast, o): pass

    def visitFuncDecl(self, ast, o): pass
        
    def visitStructDecl(self, ast, o):
        self.className = ast.name
        emitter = self.emit
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java/lang/Object"))
        attrSym = []
        attrSym = [self.visit(x, o) for x in ast.varDecls]
        constructorSym = []
        for constructor in ast.constructors:
            self.visit(FuncDecl("<init>", None, constructor.params, constructor.body))
            constructorSym += [constructor]
        self.classEnv += [(ast.name, attrSym, constructorSym)]
        self.emit.emitEPILOG()
        self.emit = emitter

    def visitProgram(self, ast, o): pass