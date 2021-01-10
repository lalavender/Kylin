grammar kylin;
/*
 * parse grammer
 */

 //源文件
sourceFile
    : packageClause eos (importDecl eos)* ((functionDecl | declaration) eos)*
    ;

 //定义包
packageClause
    : 'package' IDENTIFIER
    ;
 //声明导入
importDecl
    : 'import' (importSpec | '(' (importSpec eos)* ')')
    ;
 //指定导入
importSpec
    : ('.' | IDENTIFIER)? importPath
    ;
 
//导入路径
importPath
    : string_
    ;
 //声明类型合集
declaration
    : constDecl
    | typeDecl
    | varDecl
    ;
 //常量声明
constDecl
    : 'const' (constSpec | '(' (constSpec eos)* ')')
    ;
//常量表达式
constSpec
    : identifierList (type_? '=' expressionList)?
    ;

//标识符集合
identifierList
    : IDENTIFIER (',' IDENTIFIER)*
    ;
//表达式集合
expressionList
    : expression (',' expression)*
    ;

//执行类型
typeDecl
    : 'type' (typeSpec | '(' (typeSpec eos)* ')')
    ;
//类型重命名
typeSpec
    : IDENTIFIER ASSIGN? type_
    ;

//函数声明
functionDecl
    : 'func' IDENTIFIER (signature block?)
    ;
//变量声明
varDecl
    : 'let' (varSpec | '(' (varSpec eos)* ')')
    ;
//指定变量
varSpec
    : identifierList (type_ ('=' expressionList)? | '=' expressionList)
    ;
//区域
block
    : '{' statementList? '}'
    ;
//声明列表
statementList
    : (statement eos)+
    ;
//声明表达式
statement
    : declaration
    | simpleStmt
    | returnStmt
    | breakStmt
    | continueStmt
    | gotoStmt
    | fallthroughStmt
    | block
    | ifStmt
    | switchStmt
    | forStmt
    | deferStmt
    ;
//简单声明
simpleStmt
    : expressionStmt
    | incDecStmt
    | assignment
    | shortVarDecl
    | emptyStmt
    ;
//表达式声明
expressionStmt
    : expression
    ;
//自增自减表达式
incDecStmt
    : expression (PLUS_PLUS | MINUS_MINUS)
    ;
//运算表达式
assignment
    : expressionList assign_op expressionList
    ;
//操作符
assign_op
    : ('+' | '-' | '|' | '^' | '*' | '/' | '%' | '<<' | '>>' | '&' | '&^')? '='
    ;
//变量推导声明
shortVarDecl
    : identifierList ':=' expressionList
    ;
//空声明
emptyStmt
    : ';'
    ;
//返回值声明
returnStmt
    : 'return' expressionList?
    ;
//break声明
breakStmt
    : 'break' IDENTIFIER?
    ;
//continue声明
continueStmt
    : 'continue' IDENTIFIER?
    ;
//goto声明
gotoStmt
    : 'goto' IDENTIFIER
    ;
//fallthrough声明
fallthroughStmt
    : 'fallthrough'
    ;
//defer声明
deferStmt
    : 'defer' expression
    ;
//if表达式
ifStmt
    : 'if' (simpleStmt ';')? expression block ('else' (ifStmt | block))?
    ;
//switch表达式
switchStmt
    : exprSwitchStmt
    | typeSwitchStmt
    ;
//switch表达式
exprSwitchStmt
    : 'switch' (simpleStmt ';')? expression? '{' exprCaseClause* '}'
    ;

//case 判断表达式
exprCaseClause
    : exprSwitchCase ':' statementList?
    ;
//case表达式
exprSwitchCase
    : 'case' expressionList
    | 'default'
    ;

typeSwitchStmt
    : 'switch' (simpleStmt ';')? typeSwitchGuard '{' typeCaseClause* '}'
    ;

typeSwitchGuard
    : (IDENTIFIER ':=')? primaryExpr '.' '(' 'type' ')'
    ;

typeCaseClause
    : typeSwitchCase ':' statementList?
    ;

typeSwitchCase
    : 'case' typeList
    | 'default'
    ;

typeList
    : (type_ | NONE) (',' (type_ | NONE))*
    ;

//for 表达式
forStmt
    : 'for' (expression | forClause | rangeClause)? block
    ;
//for 判断条件
forClause
    : simpleStmt? ';' expression? ';' simpleStmt?
    ;
//range判断
rangeClause
    : (expressionList '=' | identifierList ':=')? 'range' expression
    ;
//定义类型
type_
    : typeName
    | typeLit
    | '(' type_ ')'
    ;
//定义类型名称
typeName
    : IDENTIFIER
    | qualifiedIdent
    ;

//类型集合
typeLit
    : arrayType
    | pointerType
    | functionType
    | interfaceType
    | listType
    | mapType
    | channelType
    ;
//数组类型
arrayType
    : '[' arrayLength ']' elementType
    ;
//数组长度
arrayLength
    : expression
    ;
//数组元素类型
elementType
    : type_
    ;
//指针类型
pointerType
    : '*' type_
    ;
//接口类型
interfaceType
    : 'interface' '{' (methodSpec eos)* '}'
    ;
//切片类型
listType
    : '[' ']' elementType
    ;

// It's possible to replace `type` with more restricted typeLit list and also pay attention to nil maps
//字典类型
mapType
    : 'map' '[' type_ ']' elementType
    ;
//通道类型
channelType
    : ('chan' | 'chan' '<-' | '<-' 'chan') elementType
    ;
//方法
methodSpec
    : {noTerminatorAfterParams(2)}? IDENTIFIER parameters result
    | typeName
    | IDENTIFIER parameters
    ;
//函数类型
functionType
    : 'func' signature
    ;
//函数参数
signature
    : {noTerminatorAfterParams(1)}? parameters result
    | parameters
    ;
//返回值
result
    : parameters
    | type_
    ;
//参数
parameters
    : '(' (parameterDecl (COMMA parameterDecl)* COMMA?)? ')'
    ;
//参数声明
parameterDecl
    : identifierList? '...'? type_
    ;
//基本表达式
expression
    : primaryExpr
    | unaryExpr
    | expression ('*' | '/' | '%' | '<<' | '>>' | '&' | '&^') expression
    | expression ('+' | '-' | '|' | '^') expression
    | expression ('==' | '!=' | '<' | '<=' | '>' | '>=') expression
    | expression '&&' expression
    | expression '||' expression
    ;
//主要表达式
primaryExpr
    : operand
    | conversion
    | primaryExpr ( DOT IDENTIFIER
                  | index
                  | typeAssertion
                  | arguments)
    ;
//一元表达式
unaryExpr
    : primaryExpr
    | ('+' | '-' | '!' | '^' | '*' | '&' | '<-') expression
    ;
//类型转换
conversion
    : type_ '(' expression ','? ')'
    ;
//操作符
operand
    : literal
    | operandName
    | '(' expression ')'
    ;
//字面量
literal
    : basicLit
    | compositeLit
    | functionLit
    ;
//基本类型
basicLit
    : NONE
    | integer
    | string_
    | FLOAT_LIT
    | IMAGINARY_LIT
    | RUNE_LIT
    ;
//整形
integer
    : DECIMAL_LIT
    | OCTAL_LIT
    | HEX_LIT
    | IMAGINARY_LIT
    | RUNE_LIT
    ;

operandName
    : IDENTIFIER
    | qualifiedIdent
    ;

qualifiedIdent
    : IDENTIFIER '.' IDENTIFIER
    ;

compositeLit
    : literalType literalValue
    ;
//字面量类型
literalType
    :
    | arrayType
    | '[' '...' ']' elementType
    | listType
    | mapType
    | typeName
    ;
//字面量的值
literalValue
    : '{' (elementList ','?)? '}'
    ;
//元素集合
elementList
    : keyedElement (',' keyedElement)*
    ;

keyedElement
    : (key ':')? element
    ;
//关键字
key
    : IDENTIFIER
    | expression
    | literalValue
    ;
//元素
element
    : expression
    | literalValue
    ;

string_
    : RAW_STRING_LIT
    | INTERPRETED_STRING_LIT
    ;

anonymousField
    : '*'? typeName
    ;

functionLit
    : 'func' signature block // function
    ;

index
    : '[' expression ']'
    ;
//类型断言
typeAssertion
    : '.' '(' type_ ')'
    ;
//参数
arguments
    : '(' ((expressionList | type_ (',' expressionList)?) '...'? ','?)? ')'
    ;
//方法调用

//结束符
eos
    : ';'
    | EOF
    ;

/*
 * 词法分析
 */
BREAK                  : 'break';
DEFAULT                : 'default';
FUNC                   : 'func';
INTERFACE              : 'interface';
CASE                   : 'case';
DEFER                  : 'defer';
MAP                    : 'map';
CHAN                   : 'chan';
ELSE                   : 'else';
GOTO                   : 'goto';
PACKAGE                : 'package';
SWITCH                 : 'switch';
CONST                  : 'const';
FALLTHROUGH            : 'fallthrough';
IF                     : 'if';
RANGE                  : 'range';
TYPE                   : 'type';
CONTINUE               : 'continue';
FOR                    : 'for';
IMPORT                 : 'import';
RETURN                 : 'return';
LET                    : 'let';
TRUE                   : 'true';
FALSE                  : 'false';
NONE                   : 'none';

IDENTIFIER             : LETTER (LETTER | UNICODE_DIGIT)*;

// Punctuation

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

// Logical

LOGICAL_OR             : '||';
LOGICAL_AND            : '&&';

// Relation operators

EQUALS                 : '==';
NOT_EQUALS             : '!=';
LESS                   : '<';
LESS_OR_EQUALS         : '<=';
GREATER                : '>';
GREATER_OR_EQUALS      : '>=';

// Arithmetic operators

OR                     : '|';
DIV                    : '/';
MOD                    : '%';
LSHIFT                 : '<<';
RSHIFT                 : '>>';
BIT_CLEAR              : '&^';

// 一元操作符
EXCLAMATION            : '!';

// 混合操作符
PLUS                   : '+';
MINUS                  : '-';
CARET                  : '^';
STAR                   : '*';
AMPERSAND              : '&';
RECEIVE                : '<-';

// 数字字面量
DECIMAL_LIT            : [1-9] [0-9]*;
OCTAL_LIT              : '0' OCTAL_DIGIT*;
HEX_LIT                : '0' [xX] HEX_DIGIT+;

FLOAT_LIT              : DECIMALS ('.' DECIMALS? EXPONENT? | EXPONENT)
                       | '.' DECIMALS EXPONENT?
                       ;

IMAGINARY_LIT          : (DECIMALS | FLOAT_LIT) 'i';

// 符文文字
RUNE_LIT               : '\'' (~[\n\\] | ESCAPED_VALUE) '\'';

//字符串
RAW_STRING_LIT         : '`' ~'`'*                      '`';
INTERPRETED_STRING_LIT : '"' (~["\\] | ESCAPED_VALUE)*  '"';

//隐藏
WS                     : [ \t]+             -> channel(HIDDEN);
COMMENT                : '/*' .*? '*/'      -> channel(HIDDEN);
TERMINATOR             : [\r\n]+            -> channel(HIDDEN);
LINE_COMMENT           : '//' ~[\r\n]*      -> channel(HIDDEN);

// Fragments
fragment ESCAPED_VALUE
    : '\\' ('u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
           | 'U' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
           | [abfnrtv\\'"]
           | OCTAL_DIGIT OCTAL_DIGIT OCTAL_DIGIT
           | 'x' HEX_DIGIT HEX_DIGIT)
    ;

fragment DECIMALS
    : [0-9]+
    ;

fragment OCTAL_DIGIT
    : [0-7]
    ;

fragment HEX_DIGIT
    : [0-9a-fA-F]
    ;

fragment EXPONENT
    : [eE] [+-]? DECIMALS
    ;

fragment LETTER
    : UNICODE_LETTER
    | '_'
    ;

//unicode 数字
fragment UNICODE_DIGIT
    : [\u0030-\u0039]
    ;
//unicode 集合
fragment UNICODE_LETTER
    : [\u0041-\u005A]
    ;
