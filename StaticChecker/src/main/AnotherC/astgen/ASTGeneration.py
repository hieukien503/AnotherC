from AnotherCVisitor import AnotherCVisitor
from AnotherCParser import AnotherCParser
from AST import *
from functools import *


class ASTGeneration(AnotherCVisitor):
    def visitArray_literals(self, ctx:AnotherCParser.Array_literalsContext):
        if ctx.expression_list():
            return ArrayLit(self.visit(ctx.expression_list()))
        return ArrayLit([])


    def visitLiterals(self, ctx:AnotherCParser.LiteralsContext):
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            temp = ctx.FLOAT_LIT().getText()
            if temp[-1] == 'f':
                temp = temp[:-1]
            return FloatLit(float(temp))
        elif ctx.DOUBLE_LIT():
            return DoubleLit(float(ctx.DOUBLE_LIT().getText()))
        elif ctx.STR_LIT():
            return StringLit(ctx.STR_LIT().getText())
        elif ctx.CHAR_LIT():
            return CharLit(ctx.CHAR_LIT().getText())
        elif ctx.TRUE():
            return BooleanLit(True)
        elif ctx.FALSE():
            return BooleanLit(False)
        else:
            return self.visit(ctx.array_literals())


    def visitProgram(self, ctx:AnotherCParser.ProgramContext):
        decls = []
        for x in ctx.decls():
            decl = self.visit(x)
            decls = decls + decl if type(decl) is list else decls + [decl]
        return Program(decls)


    def visitDecls(self, ctx:AnotherCParser.DeclsContext):
        if ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.struct_decl())


    def visitVardecl(self, ctx:AnotherCParser.VardeclContext):
        isConst = True if ctx.CONST() else False
        varType = self.visit(ctx.vartype())
        varlist = self.visit(ctx.var_decl_list())
        return [VarDecl(x[0], varType, x[1], isConst) for x in varlist]


    def visitVar_decl_list(self, ctx:AnotherCParser.Var_decl_listContext):
        result = []
        for index, value in enumerate(ctx.ID()):
            name = value.getText()
            expr = self.visit(ctx.expression(index)) if ctx.ASSIGN(index) else None
            result += [(name, expr)]
        return result


    def visitVartype(self, ctx:AnotherCParser.VartypeContext):
        if ctx.prim_type():
            return self.visit(ctx.prim_type())
        elif ctx.AUTO():
            return AutoType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        return self.visit(ctx.struct_type())


    def visitPrim_type(self, ctx:AnotherCParser.Prim_typeContext):
        if ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.DOUBLE():
            return DoubleType()
        elif ctx.STRING():
            return StringType()
        elif ctx.CHAR():
            return CharType()
        elif ctx.BOOL():
            return BooleanType()


    def visitArray_type(self, ctx:AnotherCParser.Array_typeContext):
        arrType = None
        if ctx.prim_type():
            arrType = self.visit(ctx.prim_type())
        else:
            arrType = self.visit(ctx.struct_type())
        dimensions = [int(x.getText()) for x in ctx.INT_LIT()]
        return ArrayType(dimensions, arrType)


    def visitFuncdecl(self, ctx:AnotherCParser.FuncdeclContext):
        functype = self.visit(ctx.functype())
        params = self.visit(ctx.paralist()) if ctx.paralist() else []
        body = None if ctx.SEMI() else self.visit(ctx.block_func())
        return FuncDecl(ctx.ID().getText(), functype, params, body)


    def visitFunctype(self, ctx:AnotherCParser.FunctypeContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.vartype())


    def visitParalist(self, ctx:AnotherCParser.ParalistContext):
        return [self.visit(x) for x in ctx.paradecl()]


    def visitParadecl(self, ctx:AnotherCParser.ParadeclContext):
        paratype = self.visit(ctx.vartype())
        initExpr = self.visit(ctx.expression()) if ctx.expression() else None
        return ParamDecl(ctx.ID().getText(), paratype, initExpr)


    def visitBlock_func(self, ctx:AnotherCParser.Block_funcContext):
        stmts = []
        for x in ctx.stmts():
            stmt = self.visit(x)
            stmts = stmts + stmt if type(stmt) is list else stmts + [stmt]
        return BlockStmt(stmts)


    def visitStmts(self, ctx:AnotherCParser.StmtsContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.statement())


    def visitStruct_decl(self, ctx:AnotherCParser.Struct_declContext):
        name = ctx.ID().getText()
        attr_list = self.visit(ctx.attribute_list())
        return StructDecl(name, attr_list[0], attr_list[1])


    def visitAttribute_list(self, ctx:AnotherCParser.Attribute_listContext):
        varDecls, constructors = [], []
        for x in ctx.no_assign_vardecl():
            varDecls += self.visit(x)
        for x in ctx.constructor():
            constructors += [self.visit(x)]
        return (varDecls, constructors)


    def visitNo_assign_vardecl(self, ctx:AnotherCParser.No_assign_vardeclContext):
        varType = self.visit(ctx.prim_type())
        return [VarDecl(x.getText(), varType, None) for x in ctx.ID()]


    def visitConstructor(self, ctx:AnotherCParser.ConstructorContext):
        if ctx.paralist():
            return FuncDecl(ctx.ID().getText(), None, self.visit(ctx.paralist()), self.visit(ctx.block_func()))
        return FuncDecl(ctx.ID().getText(), None, [], self.visit(ctx.block_func()))


    def visitStruct_type(self, ctx:AnotherCParser.Struct_typeContext):
        return StructType(ctx.ID().getText())


    def visitStatement(self, ctx:AnotherCParser.StatementContext):
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.cont_stmt():
            return self.visit(ctx.cont_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.call_func():
            return self.visit(ctx.call_func())
        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        elif ctx.do_while_stmt():
            return self.visit(ctx.do_while_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        return self.visit(ctx.block_func())


    def visitIf_stmt(self, ctx:AnotherCParser.If_stmtContext):
        cond = self.visit(ctx.expression(0))
        tstmt = self.visit(ctx.statement(0))
        else_if = []
        if len(ctx.IF()) > 1:
            for x in range(1, len(ctx.IF())):
                expr = self.visit(ctx.expression(x))
                estmt = self.visit(ctx.statement(x))
                else_if += [ElseIfStmt(expr, estmt)]
        if len(ctx.ELSE()) < len(ctx.IF()):
            return IfStmt(cond, tstmt, else_if, None)
        else:
            return IfStmt(cond, tstmt, else_if, self.visit(ctx.statement()[-1]))


    def visitFor_stmt(self, ctx:AnotherCParser.For_stmtContext):
        if ctx.single_vardecl():
            return ForStmt(self.visit(ctx.single_vardecl()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.statement()))
        return ForStmt(self.visit(ctx.assign_stmt()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.statement()))

    def visitSingle_vardecl(self, ctx:AnotherCParser.Single_vardeclContext):
        return VarDecl(ctx.ID().getText(), self.visit(ctx.vartype()), self.visit(ctx.expression()), False)


    def visitWhile_stmt(self, ctx:AnotherCParser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.statement()))


    def visitDo_while_stmt(self, ctx:AnotherCParser.Do_while_stmtContext):
        return DoWhileStmt(self.visit(ctx.expression()), self.visit(ctx.block_func()))


    def visitBreak_stmt(self, ctx:AnotherCParser.Break_stmtContext):
        return BreakStmt()


    def visitCont_stmt(self, ctx:AnotherCParser.Cont_stmtContext):
        return ContinueStmt()


    def visitReturn_stmt(self, ctx:AnotherCParser.Return_stmtContext):
        return ReturnStmt(self.visit(ctx.expression())) if ctx.expression() else ReturnStmt()


    def visitAssign_stmt(self, ctx:AnotherCParser.Assign_stmtContext):
        op = ''
        if ctx.ASSIGN():
            op = '='
        elif ctx.ADD_ASSIGN():
            op = '+='
        elif ctx.SUB_ASSIGN():
            op = '-='
        elif ctx.MUL_ASSIGN():
            op = '*='
        elif ctx.DIV_ASSIGN():
            op = '/='
        elif ctx.MOD_ASSIGN():
            op = '%='
        return AssignStmt(self.visit(ctx.scalar_var()), self.visit(ctx.expression()), op)


    def visitScalar_var(self, ctx:AnotherCParser.Scalar_varContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_cell():
            return self.visit(ctx.array_cell())
        return self.visit(ctx.member_access())


    def visitArray_cell(self, ctx:AnotherCParser.Array_cellContext):
        return ArrayCell(ctx.ID().getText(), [self.visit(x) for x in ctx.expression()])


    def visitMember_access(self, ctx:AnotherCParser.Member_accessContext):
        if ctx.ARROW():
            return MemberAccess("this", Id(ctx.ID(0).getText()))
        else:
            if len(ctx.ID()) == 2:
                return MemberAccess(ctx.ID(0).getText(), Id(ctx.ID(1).getText()))
            return MemberAccess(self.visit(ctx.array_cell()), Id(ctx.ID(0).getText()))


    def visitCall_func(self, ctx:AnotherCParser.Call_funcContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.expression_list())) if ctx.expression_list() else CallStmt(ctx.ID().getText(), [])


    def visitExpression_list(self, ctx:AnotherCParser.Expression_listContext):
        return [self.visit(x) for x in ctx.expression()]


    def visitExpression(self, ctx:AnotherCParser.ExpressionContext):
        if ctx.if_expression():
            return self.visit(ctx.if_expression())
        return self.visit(ctx.expression1())


    def visitIf_expression(self, ctx:AnotherCParser.If_expressionContext):
        return TernaryExpr(self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)), self.visit(ctx.expression1(2)))


    def visitExpression1(self, ctx:AnotherCParser.Expression1Context):
        if ctx.OR():
            return BinExpr('||', self.visit(ctx.expression1()), self.visit(ctx.expression2()))
        return self.visit(ctx.expression2())


    def visitExpression2(self, ctx:AnotherCParser.Expression2Context):
        if ctx.AND():
            return BinExpr('&&', self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        return self.visit(ctx.expression3())


    def visitExpression3(self, ctx:AnotherCParser.Expression3Context):
        temp = '==' if ctx.EQ() else ('!=' if ctx.NOT_EQ() else None)
        if temp is None:
            return self.visit(ctx.expression4())
        return BinExpr(temp, self.visit(ctx.expression3()), self.visit(ctx.expression4()))


    def visitExpression4(self, ctx:AnotherCParser.Expression4Context):
        temp = '<' if ctx.LT() else ('>' if ctx.GT() else ('<=' if ctx.LTE() else ('>=' if ctx.GTE() else None)))
        if temp is None:
            return self.visit(ctx.expression5())
        return BinExpr(temp, self.visit(ctx.expression4()), self.visit(ctx.expression5()))

    def visitExpression5(self, ctx:AnotherCParser.Expression5Context):
        temp = '+' if ctx.ADD() else ('-' if ctx.SUB() else None)
        if temp is None:
            return self.visit(ctx.expression6())
        return BinExpr(temp, self.visit(ctx.expression5()), self.visit(ctx.expression6()))


    def visitExpression6(self, ctx:AnotherCParser.Expression6Context):
        temp = '*' if ctx.MUL() else ('/' if ctx.DIV() else ('%' if ctx.MOD() else None))
        if temp is None:
            return self.visit(ctx.expression7())
        return BinExpr(temp, self.visit(ctx.expression6()), self.visit(ctx.expression7()))


    def visitExpression7(self, ctx:AnotherCParser.Expression7Context):
        temp = '!' if ctx.NEG() else ('+' if ctx.ADD() else ('-' if ctx.SUB() else None))
        if temp is None:
            return self.visit(ctx.expression8())
        return UnExpr(temp, self.visit(ctx.expression7()))


    def visitExpression8(self, ctx:AnotherCParser.Expression8Context):
        temp = '++' if ctx.INC() else ('--' if ctx.DEC() else None)
        if temp is None:
            return self.visit(ctx.expression9())
        return UnExpr(temp, self.visit(ctx.scalar_var()))


    def visitExpression9(self, ctx:AnotherCParser.Expression9Context):
        if ctx.NEW():
            return NewExpr(ctx.ID().getText(), self.visit(ctx.expression_list())) if ctx.expression_list() else NewExpr(ctx.ID().getText(), [])
        return self.visit(ctx.operands())

    def visitOperands(self, ctx:AnotherCParser.OperandsContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.scalar_var():
            return self.visit(ctx.scalar_var())
        elif ctx.literals():
            return self.visit(ctx.literals())
        return self.visit(ctx.func_call())


    def visitFunc_call(self, ctx:AnotherCParser.Func_callContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.expression_list())) if ctx.expression_list() else FuncCall(ctx.ID().getText(), [])