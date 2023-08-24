from abc import ABC, ABCMeta


class StaticError(Exception):
    pass


class Kind(ABC):
    def __str__(self):
        return self.__class__.__name__


class Variable(Kind):
    pass


class Parameter(Kind):
    pass


class Function(Kind):
    pass


class Identifier(Kind):
    pass


class Struct(Kind):
    pass


class Field(Kind):
    pass


class Constant(Kind):
    pass


class Constructor(Kind):
    pass


class Redeclared(StaticError):
    def __init__(self, kind: Kind, identifier: str):
        self.kind = kind
        self.identifier = identifier

    def __str__(self):
        return f"Redeclared {str(self.kind)}: {self.identifier}"


class Undeclared(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Undeclared {str(self.kind)}: {self.name}"


class Invalid(StaticError):
    def __init__(self, kind: Kind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f"Invalid {str(self.kind)}: {self.name}"


class TypeMismatchInExpression(StaticError):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"Type mismatch in expression: {str(self.expr)}"


class TypeMismatchInStatement(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Type mismatch in statement: {str(self.stmt)}"


class TypeMismatchInVarDecl(StaticError):
    def __init__(self, decl):
        self.decl = decl

    def __str__(self):
        return f"Type mismatch in Variable Declaration: {str(self.decl)}"


class TypeMismatchInConstant(StaticError):
    def __init__(self, decl):
        self.decl = decl

    def __str__(self):
        return f"Type mismatch in constant: {str(self.decl)}"


class TypeMismatchInParameter(StaticError):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f"Type mismatch in parameter: {str(self.param)}"


class MustInLoop(StaticError):
    def __init__(self, stmt):
        self.stmt = stmt

    def __str__(self):
        return f"Must in loop: {str(self.stmt)}"


class IllegalArrayLiteral(StaticError):
    def __init__(self, literal):
        self.literal = literal

    def __str__(self):
        return f"Illegal array literal: {str(self.literal)}"


class FunctionNotReturn(StaticError):
    def __init__(self, func: str):
        self.func = func
    
    def __str__(self):
        return f"Function Not Return: {self.func}"


class CannotAssignToConstant(StaticError):
    def __init__(self, assign):
        self.assign = assign
    
    def __str__(self):
        return f"Cannot Assign To Constant: {str(self.assign)}"


class DefaultArgumentMissing(StaticError):
    def __init__(self, arg):
        self.arg = arg
    
    def __str__(self):
        return f"Default Argument Missing: {str(self.arg)}"


class NotImplemented(StaticError):
    def __init__(self, func):
        self.func = func
    
    def __str__(self):
        return f"Function Not Implemented: {str(self.func)}"


class InvalidReturnInConstructor(StaticError):
    def __init__(self, func):
        self.func = func
    
    def __str__(self):
        return f"Invalid Return Statement in Constructor: {str(self.func)}"


class InvalidMemberAccess(StaticError):
    def __init__(self, mem):
        self.mem = mem
    
    def __str__(self):
        return f"Invalid Member Access: {str(self.mem)}"


class IllegalOperand(StaticError):
    def __init__(self, op):
        self.op = op
    
    def __str__(self):
        return f"Illegal Operand: {str(self.op)}"


class NoEntryPoint(StaticError):
    def __str__(self):
        return "No entry point"