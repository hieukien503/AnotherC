from Visitor import Visitor
from AST import *
from Utils import Utils
from StaticError import *


class Symbol:
    def __init__(self, name: str, typ: Type, initExpr: Expr | None = None, isConst: bool = False):
        self.name = name
        self.initExpr = initExpr
        self.isConst = isConst
        self.typ = typ
    
    def __str__(self):
        return "{}Symbol({}, {}{})".format("Const" if self.isConst else "", self.name, str(self.typ), ", " + str(self.initExpr) if self.initExpr else "")


class Func:
    def __init__(self, name: str, ret_type: Type, params: List[Symbol], body: BlockStmt | None = None):
        self.name = name
        self.ret_type = ret_type
        self.params = params
        self.body = body
    
    def __str__(self):
        if self.ret_type:
            return "FuncSymbol({}, {}, [{}]{})".format(self.name, str(self.ret_type), ", ".join([str(param) for param in self.params]), ", " + str(self.body) if self.body else "")
        return "ConstructorSymbol({}, [{}]{})".format(self.name, ", ".join([str(param) for param in self.params]), ", " + str(self.body) if self.body else "")


class StructSymbol:
    def __init__(self, name: str, attr: List[Symbol], constructors: List[Func]):
        self.name = name
        self.attr = attr
        self.constructors = constructors
    
    def __str__(self):
        return "StructSymbol({}, AttributeDecl([{}]), Constructor([{}]))".format(self.name, ", ".join([str(attr) for attr in self.attr]), ", ".join([str(constructor) for constructor in self.constructors]))


def initGlobal():
    return [Symbol("printInteger", VoidType()),
              Symbol("printFloat", VoidType()),
              Symbol("printDouble", VoidType()),
              Symbol("printChar", VoidType()),
              Symbol("printString", VoidType()),
              Symbol("printBoolean", VoidType()),
              Symbol("readString", StringType()),
              Symbol("readInteger", IntegerType()),
              Symbol("readFloat", FloatType()),
              Symbol("readDouble", DoubleType()),
              Symbol("readChar", CharType()),
              Symbol("readBoolean", BooleanType())]


def defaultValue(typ_):
        varType = type(typ_)
        if varType is IntegerType:
            return IntegerLit(0)
        elif varType is FloatType:
            return FloatLit(0.0)
        elif varType is DoubleType:
            return DoubleLit(0.0)
        elif varType is StringType:
            return StringLit("")
        elif varType is CharType:
            return CharLit('\0')
        elif varType is BooleanType:
            return BooleanLit(False)
        else:
            expr = []
            if len(typ_.dimensions) == 1:
                for x in range(typ_.dimensions[0]):
                    expr += [defaultValue(typ_.typ)]
                return ArrayLit(expr)
            else:
                dimen = typ_.dimensions
                for x in range(dimen[0]):
                    temp = defaultValue(ArrayType(dimen[1:], typ_.typ))
                    expr += [temp]
                return ArrayLit(expr)

def checkValidType(typ1, typ2, isProgram = False):
    if type(typ1) != type(typ2):
        if isProgram or (not (isinstance(typ1, DoubleType) and isinstance(typ2, (IntegerType, FloatType, DoubleType))) and not (isinstance(typ1, FloatType) and isinstance(typ2, (IntegerType, FloatType)))):
            return False
        else:
            return True
    else:
        if type(typ1) is StructType:
            return typ1.name == typ2.name
        elif type(typ1) is ArrayType:
            return typ1.dimensions == typ2.dimensions and str(typ1.typ) == str(typ2.typ)
        else:
            return True

class StaticChecker (Visitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.global_env = [initGlobal()]
        self.stage = 0
        self.kept_ast = []
        self.in_struct = False
        self.current_struct = None
        self.inLoop = 0
        self.inConstructor = False
        self.func_ast = None
        self.return_list = []
        self.inIf = 0
        self.hasReturn = False
        self.func_return = False

    def check(self):
        self.visit(self.ast, self.global_env)
    

    def visitProgram(self, ast, param):
        decls = []
        for decl in ast.decls:
            if isinstance(decl, (VarDecl, StructDecl)):
                param = self.visit(decl, param)
            else:
                if decl.body is None:
                    decls += [decl]
                else:
                    flag = False
                    for x in range(len(decls)):
                        if decls[x].name == decl.name and decls[x].body is None:
                            flag = True
                            params1, params2 = decl.params, decls[x].params
                            if len(params1) != len(params2):
                                raise Redeclared(Function(), decl.name)
                            
                            para_lst = []
                            for y in range(len(params1)):
                                if not checkValidType(params1[y].typ, params2[y].typ, True):
                                    raise Redeclared(Function(), decl.name) 
       
                                if params1[y].initExpr is not None and params2[y].initExpr is not None:
                                    raise Invalid(Parameter(), params1[y].name)
                                
                                if params2[y].initExpr is None:
                                    para_lst += [params1[y]]
                                else:
                                    para_lst += [ParamDecl(params1[y].name, params1[y].typ, params2[y].initExpr)]
                                    
                            decls[x] = FuncDecl(decl.name, decl.return_type, para_lst, decl.body)
                            break
                    
                    if not flag:
                        decls += [decl]

        for decl in decls:
            if decl.body is None:
                raise NotImplemented(decl.name)
            else:
                param = self.visit(decl, param)
        
        flag = False
        for decl in decls:
            if decl.name == 'main' and type(decl.return_type) is VoidType and len(decl.params) == 0:
                flag = True
                break
        
        if not flag:
            raise NoEntryPoint()
        
    
    def visitVarDecl(self, ast, param):
        if self.lookup(ast.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name) if not self.in_struct else Redeclared(Field(), ast.name) 
        
        if isinstance(ast.typ, AutoType):
            if ast.init is None:
                raise Invalid(Variable(), ast.name)
            else:
                expType = self.visit(ast.init, param)
                param[0] += [Symbol(ast.name, expType, ast.init, ast.isConst)]
        else:
            if ast.isConst:
                if ast.init is None:
                    raise Invalid(Constant(), ast.name)
                else:
                    expType, varType = self.visit(ast.init, param), self.visit(ast.typ, param)
                    if not checkValidType(varType, expType):
                        raise TypeMismatchInConstant(ast)
                    param[0] += [Symbol(ast.name, expType, ast.init, ast.isConst)]
            else:
                if ast.init:
                    expType, varType = self.visit(ast.init, param), self.visit(ast.typ, param)
                    if not checkValidType(varType, expType):
                        raise TypeMismatchInVarDecl(ast)
                    
                    param[0] += [Symbol(ast.name, varType, ast.init, ast.isConst)]
                else:
                    varType = self.visit(ast.typ, param)
                    param[0] += [Symbol(ast.name, varType, ast.init, ast.isConst)]
        
        return param
    

    def visitFuncDecl(self, ast, param):

        self.func_ast = ast
        self.func_return = False
        if self.lookup(ast.name, param[-1], lambda x: x.name) is not None:
            if ast.return_type is not None:
                raise Redeclared(Function(), ast.name)
        
        func_type = self.visit(ast.return_type, param) if ast.return_type else None
        self.inConstructor = True if func_type is None else False
        params: List[Symbol] = []
        for param_decl in ast.params:
            if self.lookup(param_decl.name, params, lambda x: x.name) is not None:
                raise Redeclared(Parameter(), param_decl.name)
            
            para_typ = None
            if isinstance(param_decl.typ, AutoType):
                if param_decl.initExpr is not None:
                    para_typ = self.visit(param_decl.initExpr, param)
                else:
                    para_typ = AutoType()
            else:
                if param_decl.initExpr:
                    para_typ, expType = self.visit(param_decl.typ, param), self.visit(param_decl.initExpr, param)
                    if not checkValidType(para_typ, expType):
                        raise TypeMismatchInParameter(param_decl)
                else:
                    para_typ = self.visit(param_decl.typ, param)

            params += [Symbol(param_decl.name, para_typ, param_decl.initExpr)]
        
        for x in range(len(params)):
            if params[x].initExpr is not None:
                if x + 1 < len(params) and params[x + 1].initExpr is None:
                    raise DefaultArgumentMissing(ParamDecl(params[x + 1].name, params[x + 1].typ, params[x + 1].initExpr))

        param = [params] + param
        param[-1] += [Func(ast.name, func_type, params, ast.body)]
                
        for param_decl in params:
            if isinstance(param_decl.typ, AutoType):
                return param
             
        param = self.visit(ast.body, param)
        if self.func_return and self.inConstructor:
            raise InvalidReturnInConstructor(ast)
        
        self.inConstructor = False
        if func_type is not None:
            if isinstance(func_type, AutoType):
                if not self.func_return:
                    raise FunctionNotReturn(ast.name)
                typ = self.return_list[0][1]
                for value in self.return_list:
                    if type(value[1]) != type(typ):
                        raise Invalid(Function(), ast.name)
                for x in range(len(param[-1])):
                    if isinstance(param[-1][x], Func) and param[-1][x].name == ast.name:
                        param[-1][x].ret_type = typ
            else:
                if not isinstance(func_type, VoidType):
                    if not self.func_return:
                        raise FunctionNotReturn(ast.name)
                    
                    for value in self.return_list:
                        if not checkValidType(func_type, value[1]):
                            raise TypeMismatchInStatement(value[0])
                else:
                    if self.return_list != []:
                        for value in self.return_list:
                            if not isinstance(value[1], VoidType):
                                raise TypeMismatchInStatement(value[0])
            
            for idx in range(len(param[-1])):
                if isinstance(param[-1][idx], Func) and param[-1][idx].name == ast.name:
                    param[-1][idx].typ = func_type

        self.return_list = []
        self.func_return = False
        return param
    

    def visitStructDecl(self, ast, param):
        if self.lookup(ast.name, param[-1], lambda x: x.name) is not None:
            raise Redeclared(Struct(), ast.name)
        
        self.in_struct = True
        self.current_struct = ast.name
        attrs = [[]] + [[decl for decl in param[-1]]]
        attr_list, cons_list = [], []
        for attr in ast.varDecls:
            attrs = self.visit(attr, attrs)
            attr_list += [Symbol(attr.name, self.visit(attr.typ, param), attr.init, attr.isConst)]

        if ast.constructors == []:
            body = []
            for attr in attr_list:
                body += [AssignStmt(MemberAccess('this', Id(attr.name)), defaultValue(attr.typ), '=')]
            
            attrs = self.visit(FuncDecl(ast.name, None, [], BlockStmt(body)), attrs)
            cons_list += [Func(ast.name, None, [], body)]

        else:
            for idx, constructor in enumerate(ast.constructors):
                if constructor.name != ast.name:
                    raise Invalid(Constructor(), constructor)
                attrs = self.visit(constructor, attrs)
                for x in ast.constructors[(idx + 1):]:
                    len1, len2 = len(constructor.params), len(x.params)
                    if len1 == len2:
                        raise Redeclared(Constructor(), x)
                    else:
                        if len1 < len2:
                            if (len1 == 0 and x.params[len1].initExpr is not None) or x.params[len2 - len1].initExpr is not None:
                                raise Invalid(Constructor(), constructor)
                        else:
                            if (len2 == 0 and constructor.params[len2].initExpr is not None) or constructor.params[len2 - len1].initExpr is not None:
                                raise Invalid(Constructor(), x)
                cons_list += [Func(constructor.name, None, constructor.params, constructor.body)]

        param[-1] += [StructSymbol(ast.name, attr_list, cons_list)]
        self.in_struct = False
        return param
    
    def visitBinExpr(self, ast, param):
        left_typ, right_typ = self.visit(ast.left, param), self.visit(ast.right, param)
        if ast.op == '+':
            if isinstance(left_typ, StringType):
                if type(ast.left) is StringLit:
                    if isinstance(right_typ, StringType):
                        return StringType()
                else:
                    if isinstance(right_typ, (CharType, StringType)):
                        return StringType()
                    
            elif isinstance(left_typ, (IntegerType, FloatType, DoubleType)) and isinstance(right_typ, (IntegerType, FloatType, DoubleType)):
                if isinstance(left_typ, IntegerType) and isinstance(right_typ, IntegerType):
                    return IntegerType()
                elif (isinstance(left_typ, FloatType) and isinstance(right_typ, (FloatType, IntegerType))) or (isinstance(right_typ, FloatType) and isinstance(left_typ, (FloatType, IntegerType))):
                    return FloatType()
                else:
                    return DoubleType()
                
        elif ast.op in ['-', '*', '/', '%']:
            if isinstance(left_typ, (IntegerType, FloatType, DoubleType)) and isinstance(right_typ, (IntegerType, FloatType, DoubleType)):
                if isinstance(left_typ, IntegerType) and isinstance(right_typ, IntegerType):
                    return IntegerType()
                elif (isinstance(left_typ, FloatType) and isinstance(right_typ, (FloatType, IntegerType))) or (isinstance(right_typ, FloatType) and isinstance(left_typ, (FloatType, IntegerType))):
                    return FloatType()
                else:
                    return DoubleType()
                
        elif ast.op in ['&&', '||']:
            if isinstance(left_typ, BooleanType) and isinstance(right_typ, BooleanType):
                return BooleanType()

        else:
            if isinstance(left_typ, (IntegerType, FloatType, DoubleType)) and isinstance(right_typ, (IntegerType, FloatType, DoubleType)):
                return BooleanType()
            
        raise TypeMismatchInExpression(ast)


    def visitUnExpr(self, ast, param):
        expType = self.visit(ast.val, param)
        if ast.op == '!':
            if isinstance(expType, BooleanType):
                return BooleanType()
        
        else:
            if isinstance(ast.val, Id):
                for sym in param:
                    temp = self.lookup(ast.val.name, sym, lambda x: x.name)
                    if isinstance(temp, Symbol) and temp.isConst == True:
                        raise IllegalOperand(ast.val)

            if isinstance(expType, (FloatType, DoubleType, IntegerType)):
                return expType
        
        raise TypeMismatchInExpression(ast)

    def visitTernaryExpr(self, ast, param):
        cond_expr = self.visit(ast.expr1, param)
        if not isinstance(cond_expr, BooleanType):
            raise TypeMismatchInExpression(ast)
        
        typ1, typ2 = self.visit(ast.texpr, param), self.visit(ast.fexpr, param)
        if isinstance(typ1, (IntegerType, FloatType, DoubleType)) and isinstance(typ2, (IntegerType, FloatType, DoubleType)):
            if isinstance(typ1, IntegerType) and isinstance(typ2, IntegerType):
                return IntegerType()
            elif (isinstance(typ2, FloatType) and isinstance(typ2, (FloatType, IntegerType))) or (isinstance(typ2, FloatType) and isinstance(typ1, (FloatType, IntegerType))):
                return FloatType()
            else:
                return DoubleType()
        else:
            if not checkValidType(typ1, typ2, True):
                raise TypeMismatchInExpression(ast)
                
            return typ1

    def visitId(self, ast, param):
        for para in param:
            temp = self.lookup(ast.name, para, lambda x: x.name)
            if temp is not None:
                return temp.typ
        
        raise Undeclared(Identifier(), ast.name)
            

    def visitArrayCell(self, ast, param):
        for x in param:
            for y in x:
                if isinstance(y, Symbol):
                    if ast.name == y.name:
                        if not isinstance(y.typ, ArrayType):
                            raise TypeMismatchInExpression(ast)
                        else:
                            if len(y.typ.dimensions) < len(ast.cell):
                                raise TypeMismatchInExpression(ast)
                            for t in ast.cell:
                                typ = self.visit(t, param)
                                if not isinstance(typ, IntegerType):
                                    raise TypeMismatchInExpression(t)
                        dimen = y.typ.dimensions[len(ast.cell):] if len(ast.cell) < len(y.typ.dimensions) else []
                        return y.typ.typ if dimen == [] else ArrayType(dimen, y.typ.typ)
        raise Undeclared(Variable(), ast.name)
    
    def visitParamDecl(self, ast, param):
        return param
    
    def visitIntegerType(self, ast, param):
        return IntegerType()
    
    def visitFloatType(self, ast, param):
        return FloatType()
    
    def visitBooleanType(self, ast, param):
        return BooleanType()
    
    def visitStringType(self, ast, param):
        return StringType()
    
    def visitArrayType(self, ast, param):
        return ArrayType(ast.dimensions, self.visit(ast.typ, param))
    
    def visitAutoType(self, ast, param):
        return AutoType()
    
    def visitVoidType(self, ast, param):
        return VoidType()
    
    def visitCharType(self, ast, param):
        return CharType()
    
    def visitStructType(self, ast, param):
        return StructType(ast.name)
    
    def visitDoubleType(self, ast, param):
        return DoubleType()

    def visitIntegerLit(self, ast, param):
        return IntegerType()
    
    def visitFloatLit(self, ast, param):
        return FloatType()
    
    def visitStringLit(self, ast, param):
        return StringType()
    
    def visitBooleanLit(self, ast, param):
        return BooleanType()
    
    def visitArrayLit(self, ast, param):
        self.kept_ast += [ast]
        if ast.explist == []:
            return ArrayType([0], AtomicType)
        
        first_type = self.visit(ast.explist[0], param)
        for x in ast.explist[1:]:
            temp = self.visit(x, param)
            if not checkValidType(first_type, temp, True):
                raise IllegalArrayLiteral(self.kept_ast[0])

        self.kept_ast = self.kept_ast[:-1]
        if isinstance(first_type, (IntegerType, FloatType, StringType, BooleanType, CharType, DoubleType, StructType)):
            return ArrayType([len(ast.explist)], first_type)
        return ArrayType([len(ast.explist)] + first_type.dimensions, first_type.typ)
    
    def visitDoubleLit(self, ast, param):
        return DoubleType()
    
    def visitMemberAccess(self, ast, param):
        firstType = None
        if type(ast.firstExpr) is not str:
            if self.inConstructor is True:
                raise InvalidMemberAccess(ast)
            
        elif ast.firstExpr == 'this':
            if self.inConstructor == False:
                raise InvalidMemberAccess(ast)
            
        else:
            flag = False
            for para in param:
                temp = self.lookup(ast.firstExpr, para, lambda x: x.name)
                if temp is not None:
                    if type(temp) is not Symbol or (type(temp) is Symbol and not isinstance(temp.typ, StructType)):
                        raise TypeMismatchInExpression(ast)
                    flag = True
                    firstType = temp.typ
                    break
                    
            if not flag:
                raise Undeclared(Identifier(), ast.firstExpr)
        

        if (ast.firstExpr == 'this'):
            temp = self.lookup(ast.secondExpr.name, param[1], lambda x: x.name)
        else:
            struct_sym = self.lookup(firstType.name, self.global_env[-1], lambda x: x.name)
            if struct_sym is not None:
                temp = self.lookup(ast.secondExpr.name, struct_sym.attr, lambda x: x.name)
            else:
                raise Undeclared(Struct(), firstType.name)

        if temp is None:
            raise Undeclared(Field(), ast.secondExpr.name)
        else:
            return temp.typ
    
    def visitCharLit(self, ast, param):
        return CharType()
  
    def visitNewExpr(self, ast, param):
        if self.lookup(ast.structName, param[-1], lambda x: x.name) is None:
            raise Undeclared(Struct(), ast.structName)
        
        for x in param[-1]:
            if type(x) is StructSymbol and x.name == ast.structName:
                flag = False
                for constructor in x.constructors:
                    if len(constructor.params) >= len(ast.param):
                        flag = True
                        for y in range(len(ast.param)):
                            para_typ, arg_typ = self.visit(constructor.params[y].typ, param), self.visit(ast.param[y], param)
                            if not checkValidType(para_typ, arg_typ):
                                raise TypeMismatchInExpression(ast.param[y])
                                    
                        break
        
                if not flag:
                    raise TypeMismatchInExpression(ast)
                
        return StructType(ast.structName)

    def visitFuncCall(self, ast, param):
        if ast.name == "readString":
            if len(ast.args) == 0:
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)
            
        if ast.name == "readFloat":
            if len(ast.args) == 0:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)
            
        if ast.name == "readDouble":
            if len(ast.args) == 0:
                return DoubleType()
            else:
                raise TypeMismatchInExpression(ast)
            
        if ast.name == "readInteger":
            if len(ast.args) == 0:
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ast)
            
        if ast.name == "readChar":
            if len(ast.args) == 0:
                return CharType()
            else:
                raise TypeMismatchInExpression(ast)
            
        if ast.name == "readBoolean":
            if len(ast.args) == 0:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
            
        hasAutoParam = False
        for para in param:
            func_call = self.lookup(ast.name, para, lambda x: x.name)
            if func_call is not None:
                if not isinstance(func_call, Func):
                    raise TypeMismatchInExpression(ast)
                para_list, arg_list = func_call.params, ast.args
                para_decls = []
                if len(arg_list) > len(para_list):
                    raise TypeMismatchInExpression(ast)
                else:
                    for idx, value in enumerate(arg_list):
                        argType = self.visit(value, param)
                        if isinstance(para_list[idx].typ, AutoType):
                            hasAutoParam = True
                            para_decls += [ParamDecl(para_list[idx].name, argType, para_list[idx].initExpr)]
                        else:
                            if not checkValidType(para_list[idx].typ, argType):
                                raise TypeMismatchInExpression(ast)
                            else:
                                para_decls += [ParamDecl(para_list[idx].name, para_list[idx].typ, para_list[idx].initExpr)]

                    temp = para_list[len(arg_list):]
                    for value in temp:
                        if value.initExpr is None:
                            raise TypeMismatchInExpression(ast)
                        else:
                            if isinstance(value.typ, AutoType):
                                hasAutoParam = True
                                expType = self.visit(value.initExpr, param)
                                para_decls += [ParamDecl(value.name, expType, value.initExpr)]
                            else:
                                para_decls += [ParamDecl(value.name, value.typ, value.initExpr)]
                    
                    if hasAutoParam:
                        for x in range(len(param[-1])):
                            if isinstance(param[-1][x], Func) and param[-1][x].name == func_call.name:
                                param[-1].pop(x)
                                break
                        
                        save_stage = self.stage
                        self.stage = 0
                        param = self.visit(FuncDecl(func_call.name, func_call.ret_type, para_decls, func_call.body), param)
                        func_call = self.lookup(ast.name, param[-1], lambda x: x.name)
                        self.stage = save_stage

                    return func_call.ret_type
        
        raise Undeclared(Function(), ast.name)

    def visitAssignStmt(self, ast, param):
        if ast.op in ['+=', '-=', '*=', '/=', '%=']:
            return self.visit(AssignStmt(ast.lhs, BinExpr(ast.op[0], ast.lhs, ast.rhs)), param)
        
        if isinstance(ast.lhs, (ArrayCell, Id)):
            for para in param:
                temp = self.lookup(ast.lhs.name, para, lambda x: x.name)
                if temp is not None:
                    if temp.isConst:
                        raise CannotAssignToConstant(ast)
        
        elif isinstance(ast.lhs, MemberAccess):
            for para in param:
                temp = self.lookup(ast.lhs.firstExpr, para, lambda x: x.name)
                if temp is not None:
                    if temp.isConst:
                        raise CannotAssignToConstant(ast)
                    
        rhs_type, lhs_type = self.visit(ast.rhs, param), self.visit(ast.lhs, param)
        if isinstance(lhs_type, (VoidType, ArrayType, StructType)):
            raise TypeMismatchInStatement(ast)
        
        if type(rhs_type) != type(lhs_type):
            if not (isinstance(lhs_type, (FloatType, DoubleType)) and isinstance(rhs_type, (IntegerType, FloatType, DoubleType))):
                raise TypeMismatchInStatement(ast)
        
        return param

    def visitBlockStmt(self, ast, param):
        self.stage += 1
        param = param if len(param) != self.stage else [[]] + param
        for stmt in ast.body:
            if isinstance(stmt, (ForStmt, WhileStmt, DoWhileStmt)):
                self.inLoop += 1
                param = self.visit(stmt, param)
                self.inLoop -= 1
            else:
                if isinstance(stmt, ReturnStmt):
                    if self.stage == 1:
                        self.func_return = True
                param = self.visit(stmt, param)
        
        self.stage -= 1
        param = param[1:]
        return param
    
    def visitIfStmt(self, ast, param):
        cond_expr = self.visit(ast.cond, param)
        if not isinstance(cond_expr, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        param = self.visit(ast.tstmt, param)
        self.hasReturn = self.return_list != []
        
        if ast.estmt != []:
            for estmt in ast.estmt:
                cond_expr = self.visit(estmt.cond, param)
                if not isinstance(cond_expr, BooleanType):
                    raise TypeMismatchInStatement(ast)
                
                param = self.visit(estmt.stmt, param)

        if ast.fstmt is not None:
            if not self.hasReturn:
                param = self.visit(ast.fstmt, param)
            else:
                if isinstance(ast.fstmt, BlockStmt):
                    for stmt in ast.fstmt:
                        param = self.visit(stmt, param)
                else:
                    if isinstance(ast.fstmt, ReturnStmt):
                        if self.stage == 1:
                            self.func_return = True
                    param = self.visit(ast.fstmt, param)

        return param

    def visitForStmt(self, ast, param):
        ori_len = len(param)
        param = [[]] + param if type(ast.init) is VarDecl else param
        if type(ast.init) is VarDecl:
            varType, expType = self.visit(ast.init.typ, param), self.visit(ast.init.init, param)
            if not isinstance(varType, IntegerType) or not isinstance(expType, IntegerType):
                raise TypeMismatchInVarDecl(ast.init)
            else:
                param[0] += [Symbol(ast.init.name, varType, ast.init.init, ast.init.isConst)]
        else:
            rhs_type, lhs_type = self.visit(ast.init.rhs, param), self.visit(ast.init.lhs, param)
            if not isinstance(rhs_type, IntegerType) or not isinstance(lhs_type, IntegerType):
                raise TypeMismatchInStatement(ast.init)
        
        cond_expr = self.visit(ast.cond, param)
        if not isinstance(cond_expr, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        upd_expr = self.visit(ast.upd, param)
        if not isinstance(upd_expr, IntegerType):
            raise TypeMismatchInStatement(ast)
        
        self.stage = self.stage + (0 if isinstance(ast.stmt, BlockStmt) else 1)
        param = self.visit(ast.stmt, param)
        self.stage = self.stage - (0 if isinstance(ast.stmt, BlockStmt) else 1)
        if ori_len - len(param) != 0:
            param = param[1:]

        return param

    def visitWhileStmt(self, ast, param):
        cond_expr = self.visit(ast.cond, param)
        if not isinstance(cond_expr, BooleanType):
            raise TypeMismatchInStatement(ast)
        
        self.stage = self.stage + (0 if isinstance(ast.stmt, BlockStmt) else 1)
        param = self.visit(ast.stmt, param)
        self.stage = self.stage - (0 if isinstance(ast.stmt, BlockStmt) else 1)
        return param

    def visitDoWhileStmt(self, ast, param):
        param = self.visit(ast.stmt, param)
        cond_expr = self.visit(ast.cond, param)
        if not isinstance(cond_expr, BooleanType):
            raise TypeMismatchInStatement(ast)
        return param
        
    def visitBreakStmt(self, ast, param):
        if self.inLoop == 0:
            raise MustInLoop(ast)
        
        return param
        
    def visitContinueStmt(self, ast, param):
        if self.inLoop == 0:
            raise MustInLoop(ast)
        
        return param
        
    def visitReturnStmt(self, ast, param):
        if ast.expr:
            self.return_list += [(ast, self.visit(ast.expr, param))]
        else:
            self.return_list += [(ast, VoidType())]

        return param
    
    def visitCallStmt(self, ast, param):
        if ast.name == "printString":
            if len(ast.args) == 1:
                expType = self.visit(ast.args[0], param)
                if isinstance(expType, StringType):
                    return param
            raise TypeMismatchInStatement(ast)
            
        if ast.name == "printFloat":
            if len(ast.args) == 1:
                expType = self.visit(ast.args[0], param)
                if isinstance(expType, (FloatType, IntegerType)):
                    return param
            raise TypeMismatchInStatement(ast)
            
        if ast.name == "printDouble":
            if len(ast.args) == 1:
                expType = self.visit(ast.args[0], param)
                if isinstance(expType, (DoubleType, FloatType, IntegerType)):
                    return param
            raise TypeMismatchInStatement(ast)
            
        if ast.name == "printInteger":
            if len(ast.args) == 1:
                expType = self.visit(ast.args[0], param)
                if isinstance(expType, IntegerType):
                    return param
            raise TypeMismatchInStatement(ast)
            
        if ast.name == "printChar":
            if len(ast.args) == 1:
                expType = self.visit(ast.args[0], param)
                if isinstance(expType, CharType):
                    return param
            raise TypeMismatchInStatement(ast)
            
        if ast.name == "readBoolean":
            if len(ast.args) == 1:
                expType = self.visit(ast.args[0], param)
                if isinstance(expType, BooleanType):
                    return param
            raise TypeMismatchInStatement(ast)
            
        hasAutoParam = False
        for para in param:
            func_call = self.lookup(ast.name, para, lambda x: x.name)
            if func_call is not None:
                if not isinstance(func_call, Func):
                    raise TypeMismatchInExpression(ast)
                
                if not isinstance(func_call.ret_type, VoidType):
                    raise TypeMismatchInStatement(ast)
                
                para_list, arg_list = func_call.params, ast.args
                para_decls = []
                if len(arg_list) > len(para_list):
                    raise TypeMismatchInExpression(ast)
                else:
                    for idx, value in enumerate(arg_list):
                        argType = self.visit(value, param)
                        if isinstance(para_list[idx].typ, AutoType):
                            hasAutoParam = True
                            para_decls += [ParamDecl(para_list[idx].name, argType, para_list[idx].initExpr)]
                        else:
                            if not checkValidType(para_list[idx].typ, argType):
                                raise TypeMismatchInExpression(ast)
                            else:
                                para_decls += [ParamDecl(para_list[idx].name, para_list[idx].typ, para_list[idx].initExpr)]

                    temp = para_list[len(arg_list):]
                    for value in temp:
                        if value.initExpr is None:
                            raise TypeMismatchInExpression(ast)
                        else:
                            if isinstance(value.typ, AutoType):
                                hasAutoParam = True
                                expType = self.visit(value.initExpr, param)
                                para_decls += [ParamDecl(value.name, expType, value.initExpr)]
                            else:
                                para_decls += [ParamDecl(value.name, value.typ, value.initExpr)]
                    
                    if hasAutoParam:
                        for x in range(len(param[-1])):
                            if isinstance(param[-1][x], Func) and param[-1][x].name == func_call.name:
                                param[-1].pop(x)
                                break
                        
                        save_stage = self.stage
                        self.stage = 0
                        param = self.visit(FuncDecl(func_call.name, func_call.ret_type, para_decls, func_call.body), param)
                        self.stage = save_stage

                    return param
        
        raise Undeclared(Function(), ast.name)
