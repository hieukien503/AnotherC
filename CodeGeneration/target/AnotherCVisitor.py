# Generated from main/AnotherC/parser/AnotherC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AnotherCParser import AnotherCParser
else:
    from AnotherCParser import AnotherCParser

# This class defines a complete generic visitor for a parse tree produced by AnotherCParser.

class AnotherCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AnotherCParser#array_literals.
    def visitArray_literals(self, ctx:AnotherCParser.Array_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#literals.
    def visitLiterals(self, ctx:AnotherCParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#program.
    def visitProgram(self, ctx:AnotherCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#decls.
    def visitDecls(self, ctx:AnotherCParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#vardecl.
    def visitVardecl(self, ctx:AnotherCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#var_decl_list.
    def visitVar_decl_list(self, ctx:AnotherCParser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#vartype.
    def visitVartype(self, ctx:AnotherCParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#prim_type.
    def visitPrim_type(self, ctx:AnotherCParser.Prim_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#array_type.
    def visitArray_type(self, ctx:AnotherCParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#funcdecl.
    def visitFuncdecl(self, ctx:AnotherCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#functype.
    def visitFunctype(self, ctx:AnotherCParser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#paralist.
    def visitParalist(self, ctx:AnotherCParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#paradecl.
    def visitParadecl(self, ctx:AnotherCParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#block_func.
    def visitBlock_func(self, ctx:AnotherCParser.Block_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#stmts.
    def visitStmts(self, ctx:AnotherCParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#struct_decl.
    def visitStruct_decl(self, ctx:AnotherCParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#attribute_list.
    def visitAttribute_list(self, ctx:AnotherCParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#no_assign_vardecl.
    def visitNo_assign_vardecl(self, ctx:AnotherCParser.No_assign_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#constructor.
    def visitConstructor(self, ctx:AnotherCParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#struct_type.
    def visitStruct_type(self, ctx:AnotherCParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#statement.
    def visitStatement(self, ctx:AnotherCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#if_stmt.
    def visitIf_stmt(self, ctx:AnotherCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#for_stmt.
    def visitFor_stmt(self, ctx:AnotherCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#single_vardecl.
    def visitSingle_vardecl(self, ctx:AnotherCParser.Single_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#while_stmt.
    def visitWhile_stmt(self, ctx:AnotherCParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:AnotherCParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#break_stmt.
    def visitBreak_stmt(self, ctx:AnotherCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#cont_stmt.
    def visitCont_stmt(self, ctx:AnotherCParser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#return_stmt.
    def visitReturn_stmt(self, ctx:AnotherCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#assign_stmt.
    def visitAssign_stmt(self, ctx:AnotherCParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#scalar_var.
    def visitScalar_var(self, ctx:AnotherCParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#array_cell.
    def visitArray_cell(self, ctx:AnotherCParser.Array_cellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#member_access.
    def visitMember_access(self, ctx:AnotherCParser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#call_func.
    def visitCall_func(self, ctx:AnotherCParser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression_list.
    def visitExpression_list(self, ctx:AnotherCParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression.
    def visitExpression(self, ctx:AnotherCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#if_expression.
    def visitIf_expression(self, ctx:AnotherCParser.If_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression1.
    def visitExpression1(self, ctx:AnotherCParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression2.
    def visitExpression2(self, ctx:AnotherCParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression3.
    def visitExpression3(self, ctx:AnotherCParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression4.
    def visitExpression4(self, ctx:AnotherCParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression5.
    def visitExpression5(self, ctx:AnotherCParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression6.
    def visitExpression6(self, ctx:AnotherCParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression7.
    def visitExpression7(self, ctx:AnotherCParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression8.
    def visitExpression8(self, ctx:AnotherCParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#expression9.
    def visitExpression9(self, ctx:AnotherCParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#operands.
    def visitOperands(self, ctx:AnotherCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnotherCParser#func_call.
    def visitFunc_call(self, ctx:AnotherCParser.Func_callContext):
        return self.visitChildren(ctx)



del AnotherCParser