grammar kylin;

/*
 * 语法规则
 */

tokens { INDENT, DEDENT }
//Note the indentation of code inside

@lexer::header{
from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

@lexer::members {
@property
def tokens(self):
    try:
        return self._tokens
    except AttributeError:
        self._tokens = []
        return self._tokens

@property
def indents(self):
    try:
        return self._indents
    except AttributeError:
        self._indents = []
        return self._indents

@property
def opened(self):
    try:
        return self._opened
    except AttributeError:
        self._opened = 0
        return self._opened

@opened.setter
def opened(self, value):
    self._opened = value

@property
def lastToken(self):
    try:
        return self._lastToken
    except AttributeError:
        self._lastToken = None
        return self._lastToken

@lastToken.setter
def lastToken(self, value):
    self._lastToken = value

def reset(self):
    super().reset()
    self.tokens = []
    self.indents = []
    self.opened = 0
    self.lastToken = None

def emitToken(self, t):
    super().emitToken(t)
    self.tokens.append(t)

def nextToken(self):
    if self._input.LA(1) == Token.EOF and self.indents:
        for i in range(len(self.tokens)-1,-1,-1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop(i)

        self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
        while self.indents:
            self.emitToken(self.createDedent())
            self.indents.pop()

        self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
    next = super().nextToken()
    if next.channel == Token.DEFAULT_CHANNEL:
        self.lastToken = next
    return next if not self.tokens else self.tokens.pop(0)

def createDedent(self):
    dedent = self.commonToken(LanguageParser.DEDENT, "")
    dedent.line = self.lastToken.line
    return dedent

def commonToken(self, type, text, indent=0):
    stop = self.getCharIndex()-1-indent
    start = (stop - len(text) + 1) if text else stop
    return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count

def atStartOfInput(self):
    return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1
}



single_input: NEWLINE | simple_stmt | compound_stmt NEWLINE;
file_input: (NEWLINE | stmt)* EOF;
eval_input: testlist NEWLINE* EOF; 





//文件导入
import_stmt: import_name | import_from;

import_name: 'import' dotted_as_names;
//注意：（'.'|'...'）是必需的，因为'...'被标记为ELLIPSIS
import_from
    : ('from' (('.' | '...')* dotted_name
    | ('.' | '...')+)
    'import' ('*' | '(' import_as_names ')'
    | import_as_names))
    ;

import_as_names
    : import_as_name (',' import_as_name)* (',')?
    ;

import_as_name: NAME ('as' NAME)?;
dotted_as_names: dotted_as_name (',' dotted_as_name)*;
dotted_as_name: dotted_name ('as' NAME)?;
dotted_name: NAME ('.' NAME)*;



//类定义表达式
classdef
    : 'class' NAME ('(' (arglist)? ')')? ':' suite
    ;

//类参数列表
arglist
    : argument (',' argument)*  (',')?
    ;

//类参数
argument
    : ( test (comp_for)?
    | test '=' test
    |'**' test
    |'*' test )
    ;

comp_for
    : 'for' exprlist 'in' or_test (comp_iter)?
    ;
comp_iter
    : comp_for
    | comp_if
    ;
comp_if: 'if' test_nocond (comp_iter)?;
test_nocond
    : or_test ;

//函数定义推导式
funcdef
    : 'func' NAME parameters ('->' type_specifier)? ':' suite
    ;
//表达式内部推导式
suite
    : simple_stmt
    | NEWLINE INDENT stmt+ DEDENT
    ;

simple_stmt
    : small_stmt (';' small_stmt)* (';')? NEWLINE
    ;

small_stmt
    : (expr_stmt
    | del_stmt
    | pass_stmt
    | flow_stmt
    | import_stmt)
    ;

expr_stmt
    : testlist_star_expr
    (annassign | augassign ( testlist)
    | testlist_star_expr)*
    ;
//
annassign: ':' test ('=' test)?;

augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' |
            '<<=' | '>>=' | '**=' | '//=');

testlist_star_expr
    : (test|star_expr) (',' (test|star_expr))* (',')?
    ;


stmt
    : simple_stmt
    | compound_stmt
    ;


//跳转表达式
flow_stmt
    : break_stmt
    | continue_stmt
    | return_stmt
    | raise_stmt
    ;

//raise表达式
raise_stmt
    : 'raise' (test ('from' test)?)?
    ;

//复合表达式
compound_stmt
    : if_stmt
    | while_stmt
    | for_stmt
    | funcdef
    | classdef
    ;

//if表达式
if_stmt
    : 'if' test ':' suite ('elif' test ':' suite)* ('else' ':' suite)?
    ;

//while表达式
while_stmt
    : 'while' test ':' suite ('else' ':' suite)?
    ;

//for表达式
for_stmt
    : 'for' exprlist 'in' testlist ':' suite ('else' ':' suite)?
    ;

//删除表达式
del_stmt: 'del' exprlist;

//
exprlist: (expr|star_expr) (',' (expr|star_expr))* (',')?;

//函数参数
parameters              : '(' (typedargslist)? ')';



//判断表达式集合
testlist: test (',' test)* (',')?;



//类型说明符
type_specifier
    :   ('void'
    |   'char'
    |   'int'
    |   'float'
    |   'double'
    |   'signed'
    |   'unsigned')
    |   enum_specifier
    |   typedef_name
    ;


typedef_name
    :   IDENTIFIER
    ;


//枚举说明符
enum_specifier
    :   'enum' IDENTIFIER? '{' enumerator_list '}'
    |   'enum' IDENTIFIER? '{' enumerator_list ',' '}'
    |   'enum' IDENTIFIER
    ;

enumerator_list
    :   enumerator
    |   enumerator_list ',' enumerator
    ;

enumerator
    :   enumeration_constant
    ;

enumeration_constant
    :   IDENTIFIER
    ;

star_expr
    : '*' expr
    ;

expr
    : xor_expr ('|' xor_expr)*;

xor_expr
    : and_expr ('^' and_expr)*;

and_expr
    : shift_expr ('&' shift_expr)*;

shift_expr
    : arith_expr (('<<'|'>>') arith_expr)*;

arith_expr
    : term (('+'|'-') term)*;

term
    : factor (('*'|'@'|'/'|'%'|'//') factor)*;

factor
    : ('+'|'-'|'~') factor
    ;




//空函数占位符
pass_stmt               : 'pass';



typedargslist
    : (tfpdef ('=' test)? (',' tfpdef ('=' test)?)* (',' (
        '*' (tfpdef)? (',' tfpdef ('=' test)?)* (',' ('**' tfpdef (',')?)?)?
    | '**' tfpdef (',')?)?)?
    | '*' (tfpdef)? (',' tfpdef ('=' test)?)* (',' ('**' tfpdef (',')?)?)?
    | '**' tfpdef (',')?);

tfpdef: NAME (':' test)?;

//判断表达式
test
    : or_test ('if' or_test 'else' test)?
    ;

//or表达式
or_test
    : and_test ('or' and_test)*
    ;

//and表达式
and_test
    : not_test ('and' not_test)*
    ;

//not表达式
not_test
    : 'not' not_test
    | comparison
    ;
//比较表达式
comparison: expr (comp_op expr)*;

//比较操作符
comp_op: '<'|'>'|'=='|'>='|'<='|'<>'|'!='|'in'|'not' 'in'|'is'|'is' 'not';

//函数返回表达式
return_stmt             : 'return' (testlist)?;

//break表达式
break_stmt              : 'break';

//continue表达式
continue_stmt           : 'continue';


/*
 * 词法规则
 */

//关键字

FUNC                   : 'func';
BREAK                  : 'break';
DEFAULT                : 'default';
CASE                   : 'case';
MAP                    : 'map';
STRUCT                 : 'struct';
CHAN                   : 'chan';
ELSE                   : 'else';
GOTO                   : 'goto';
PACKAGE                : 'package';
SWITCH                 : 'switch';
CONST                  : 'const';
IF                     : 'if';
RANGE                  : 'range';
TYPE                   : 'type';
CONTINUE               : 'continue';
FOR                    : 'for';
IMPORT                 : 'import';
RETURN                 : 'return';
LET                    : 'let';
AS                     : 'as';
//标识符
IDENTIFIER             : LETTER (LETTER | UNICODE_DIGIT)*;

//标记符号
L_PAREN                : '(';
R_PAREN                : ')';
L_CURLY                : '{';
R_CURLY                : '}';
L_BRACKET              : '[';
R_BRACKET              : ']';
ASSIGN                 : '=';
COMMA                  : ',';
SEMI                   : ';';
COLON                  : ':';
DOT                    : '.';
PLUS_PLUS              : '++';
MINUS_MINUS            : '--';
DECLARE_ASSIGN         : ':=';
ELLIPSIS               : '...';

//逻辑符号
LOGICAL_OR             : '||';
LOGICAL_AND            : '&&';
EXCLAMATION            : '!';

//关系运算符
EQUALS                 : '==';
NOT_EQUALS             : '!=';
LESS                   : '<';
LESS_OR_EQUALS         : '<=';
GREATER                : '>';
GREATER_OR_EQUALS      : '>=';

//算术运算符
OR                     : '|';
DIV                    : '/';
MOD                    : '%';
LSHIFT                 : '<<';
RSHIFT                 : '>>';
BIT_CLEAR              : '&^';

//混合运算符
PLUS                   : '+';
MINUS                  : '-';
CARET                  : '^';
STAR                   : '*';
AMPERSAND              : '&';
RECEIVE                : '<-';

NAME
 : ID_START ID_CONTINUE*
 ;



//注释和空白等忽略的信息
Whitespace
    :   [ \t]+
        -> skip
    ;

//新的一行的注释
NEWLINE
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

//块注释
BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;
//行注释
LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;


//字面量
DECIMAL_LIT            : [1-9] [0-9]*;
OCTAL_LIT              : '0' OCTAL_DIGIT*;
HEX_LIT                : '0' [xX] HEX_DIGIT+;

FLOAT_LIT              : DECIMALS ('.' DECIMALS? EXPONENT? | EXPONENT)
                       | '.' DECIMALS EXPONENT?
                       ;

IMAGINARY_LIT          : (DECIMALS | FLOAT_LIT) 'i';

//标识符开始
fragment ID_START
 : '_'
 | [A-Z]
 | [a-z]
 ;

//标识符第二个字母之后
fragment ID_CONTINUE
 : ID_START
 | [0-9]
 ;

//十进制
fragment DECIMALS
    : [0-9]+
    ;
//八进制
fragment OCTAL_DIGIT
    : [0-7]
    ;
//十六进制
fragment HEX_DIGIT
    : [0-9a-fA-F]
    ;
//指数
fragment EXPONENT
    : [eE] [+-]? DECIMALS
    ;

//unicode
fragment LETTER
    : UNICODE_LETTER
    | '_'
    ;

fragment UNICODE_DIGIT
    : [\u0030-\u0039]
    ;

fragment UNICODE_LETTER
    : [\u0041-\u005A]
    ;