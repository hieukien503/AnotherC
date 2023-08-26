grammar AnotherC;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

/* Fragments */
fragment DoubleQuote: '\\"';
fragment Character: ~[\b\f\r\t'"\\] | DoubleQuote | [\b\f\r\t']; 


/* Keywords */
CONST: 'const';
WHILE: 'while';
AUTO: 'auto';
FOR: 'for';
DO: 'do';
STRUCT: 'struct';
VOID: 'void';
BOOL: 'bool';
INT: 'int';
STRING: 'string';
CHAR: 'char';
LONG: 'long';
FLOAT: 'float';
DOUBLE: 'double';
IF: 'if';
ELSE: 'else';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
TRUE: 'true';
FALSE: 'false';
THIS: 'this';
NEW: 'new';

/* Operators */
ASSIGN: '=';
EQ: '==';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NOT_EQ: '!=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
AND: '&&';
OR: '||';
INC: '++';
DEC: '--';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
NEG: '!';
ARROW: '->';
DOT: '.';

/* Seperators */
QM: '?';
SEMI: ';';
COLON: ':';
LB: '(';
RB: ')';
LS: '[';
RS: ']';
LC: '{';
RC: '}';
COMMA: ',';

/* Identifiers */
ID: [a-zA-Z_][a-zA-Z0-9_]*;

/* Literals */
INT_LIT: ('0' | DECIMAL) {self.text = self.text.replace('_', '')};
DOUBLE_LIT: DECIMAL FDec | ('.'[0-9]+);
FLOAT_LIT: DOUBLE_LIT 'f' | Scientific;
CHAR_LIT: '\'' Character '\'' {self.text = self.text[1:-1]};
STR_LIT: '"' Character* '"' {
self.text = self.text[1:-1]
for idx, value in enumerate(self.text):
    if ord(value) not in [0, 8, 9, 10, 12, 13] and ord(value) not in range(32, 127):
        raise IllegalEscape(self.text[:idx])
    if ord(value) == 10:
        raise UnclosedString(self.text[:idx])
};
fragment DECIMAL: [1-9][0-9]*('_'[0-9]+)*;
fragment FDec: '.' [0-9]*;
fragment Scientific: (INT_LIT? FDec FExp) | (INT_LIT FExp);
fragment FExp: [eE][+-]?[0-9]+;
array_literals: LC expression_list? RC;
literals: INT_LIT | FLOAT_LIT | DOUBLE_LIT | STR_LIT | CHAR_LIT | TRUE | FALSE | array_literals;

program: decls+ EOF;
decls: vardecl | funcdecl | struct_decl;

/* Variable declaration */
vardecl: CONST? vartype var_decl_list SEMI;
var_decl_list: ID (ASSIGN expression)? (COMMA (ID (ASSIGN expression)?))*;
vartype: prim_type | AUTO | array_type | struct_type;
prim_type: INT | FLOAT | DOUBLE | STRING | BOOL | CHAR;
array_type: (prim_type | struct_type) (LS INT_LIT RS)+;

/* Function declaration */
funcdecl: functype ID (LB paralist? RB) (SEMI | block_func);
functype: vartype | VOID;
paralist: paradecl (COMMA paradecl)*;
paradecl: vartype ID (ASSIGN expression)?;
block_func: LC stmts* RC;
stmts: vardecl | statement;

/* Struct Declaration */
struct_decl: STRUCT ID LC attribute_list RC SEMI;
attribute_list: (no_assign_vardecl | constructor)*;
no_assign_vardecl: prim_type (ID (COMMA ID)*) SEMI;
constructor: ID LB paralist? RB block_func;
struct_type: STRUCT ID;

/* Statements */
statement: if_stmt | do_while_stmt | while_stmt | break_stmt | cont_stmt | return_stmt | for_stmt | assign_stmt | block_func | call_func;
if_stmt: IF expression COLON statement (ELSE IF expression COLON statement)* (ELSE COLON statement)?;
for_stmt: FOR LB (single_vardecl | assign_stmt) COMMA expression COMMA expression RB statement;
single_vardecl: vartype ID ASSIGN expression;
while_stmt: WHILE expression COLON statement;
do_while_stmt: DO block_func WHILE LB expression RB SEMI;
break_stmt: BREAK SEMI;
cont_stmt: CONTINUE SEMI;
return_stmt: RETURN expression? SEMI;
assign_stmt: scalar_var (ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN) expression SEMI;
scalar_var: ID | array_cell | member_access;
array_cell: ID (LS expression RS)+;
member_access: (THIS ARROW ID) | ((ID | array_cell) DOT ID);
call_func: ID LB expression_list? RB SEMI;
expression_list: expression (COMMA expression)*;

/* Expression */
expression: if_expression | expression1;
if_expression: expression1 QM expression1 COLON expression1;
expression1: expression1 OR expression2 | expression2;
expression2: expression2 AND expression3 | expression3;
expression3: expression3 (EQ | NOT_EQ) expression4 | expression4;
expression4: expression4 (LT | LTE | GT | GTE) expression5 | expression5;
expression5: expression5 (ADD | SUB) expression6 | expression6;
expression6: expression6 (MUL | DIV | MOD) expression7 | expression7;
expression7: (NEG | ADD | SUB) expression7 | expression8;
expression8: (scalar_var (INC | DEC)) | ((INC | DEC) scalar_var) | expression9;
expression9: NEW ID LB expression_list? RB | operands;
operands: scalar_var | literals | func_call | (LB expression RB);
func_call: ID LB expression_list? RB;

/* Comments */
LINE_CMT: '//' ~[\n\r\f]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .{ raise ErrorToken(self.text) };
UNCLOSED_STRING: '"' Character* {
raise UnclosedString(self.text[1:])
};
UNTERMINATED_COMMENT: '/*' .*? {
raise UnterminatedComment(self.text)
};
