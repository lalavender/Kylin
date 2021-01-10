# Generated from c:\Users\16904\Desktop\Kylin\src\parse\kylin.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kylinParser import kylinParser
else:
    from kylinParser import kylinParser

# This class defines a complete listener for a parse tree produced by kylinParser.
class kylinListener(ParseTreeListener):

    # Enter a parse tree produced by kylinParser#sourceFile.
    def enterSourceFile(self, ctx:kylinParser.SourceFileContext):
        pass

    # Exit a parse tree produced by kylinParser#sourceFile.
    def exitSourceFile(self, ctx:kylinParser.SourceFileContext):
        pass


    # Enter a parse tree produced by kylinParser#packageClause.
    def enterPackageClause(self, ctx:kylinParser.PackageClauseContext):
        pass

    # Exit a parse tree produced by kylinParser#packageClause.
    def exitPackageClause(self, ctx:kylinParser.PackageClauseContext):
        pass


    # Enter a parse tree produced by kylinParser#importDecl.
    def enterImportDecl(self, ctx:kylinParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#importDecl.
    def exitImportDecl(self, ctx:kylinParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#importSpec.
    def enterImportSpec(self, ctx:kylinParser.ImportSpecContext):
        pass

    # Exit a parse tree produced by kylinParser#importSpec.
    def exitImportSpec(self, ctx:kylinParser.ImportSpecContext):
        pass


    # Enter a parse tree produced by kylinParser#importPath.
    def enterImportPath(self, ctx:kylinParser.ImportPathContext):
        pass

    # Exit a parse tree produced by kylinParser#importPath.
    def exitImportPath(self, ctx:kylinParser.ImportPathContext):
        pass


    # Enter a parse tree produced by kylinParser#declaration.
    def enterDeclaration(self, ctx:kylinParser.DeclarationContext):
        pass

    # Exit a parse tree produced by kylinParser#declaration.
    def exitDeclaration(self, ctx:kylinParser.DeclarationContext):
        pass


    # Enter a parse tree produced by kylinParser#constDecl.
    def enterConstDecl(self, ctx:kylinParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#constDecl.
    def exitConstDecl(self, ctx:kylinParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#constSpec.
    def enterConstSpec(self, ctx:kylinParser.ConstSpecContext):
        pass

    # Exit a parse tree produced by kylinParser#constSpec.
    def exitConstSpec(self, ctx:kylinParser.ConstSpecContext):
        pass


    # Enter a parse tree produced by kylinParser#identifierList.
    def enterIdentifierList(self, ctx:kylinParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by kylinParser#identifierList.
    def exitIdentifierList(self, ctx:kylinParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by kylinParser#expressionList.
    def enterExpressionList(self, ctx:kylinParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by kylinParser#expressionList.
    def exitExpressionList(self, ctx:kylinParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by kylinParser#typeDecl.
    def enterTypeDecl(self, ctx:kylinParser.TypeDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#typeDecl.
    def exitTypeDecl(self, ctx:kylinParser.TypeDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#typeSpec.
    def enterTypeSpec(self, ctx:kylinParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by kylinParser#typeSpec.
    def exitTypeSpec(self, ctx:kylinParser.TypeSpecContext):
        pass


    # Enter a parse tree produced by kylinParser#functionDecl.
    def enterFunctionDecl(self, ctx:kylinParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#functionDecl.
    def exitFunctionDecl(self, ctx:kylinParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#varDecl.
    def enterVarDecl(self, ctx:kylinParser.VarDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#varDecl.
    def exitVarDecl(self, ctx:kylinParser.VarDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#varSpec.
    def enterVarSpec(self, ctx:kylinParser.VarSpecContext):
        pass

    # Exit a parse tree produced by kylinParser#varSpec.
    def exitVarSpec(self, ctx:kylinParser.VarSpecContext):
        pass


    # Enter a parse tree produced by kylinParser#block.
    def enterBlock(self, ctx:kylinParser.BlockContext):
        pass

    # Exit a parse tree produced by kylinParser#block.
    def exitBlock(self, ctx:kylinParser.BlockContext):
        pass


    # Enter a parse tree produced by kylinParser#statementList.
    def enterStatementList(self, ctx:kylinParser.StatementListContext):
        pass

    # Exit a parse tree produced by kylinParser#statementList.
    def exitStatementList(self, ctx:kylinParser.StatementListContext):
        pass


    # Enter a parse tree produced by kylinParser#statement.
    def enterStatement(self, ctx:kylinParser.StatementContext):
        pass

    # Exit a parse tree produced by kylinParser#statement.
    def exitStatement(self, ctx:kylinParser.StatementContext):
        pass


    # Enter a parse tree produced by kylinParser#simpleStmt.
    def enterSimpleStmt(self, ctx:kylinParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#simpleStmt.
    def exitSimpleStmt(self, ctx:kylinParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#expressionStmt.
    def enterExpressionStmt(self, ctx:kylinParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#expressionStmt.
    def exitExpressionStmt(self, ctx:kylinParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#incDecStmt.
    def enterIncDecStmt(self, ctx:kylinParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#incDecStmt.
    def exitIncDecStmt(self, ctx:kylinParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#assignment.
    def enterAssignment(self, ctx:kylinParser.AssignmentContext):
        pass

    # Exit a parse tree produced by kylinParser#assignment.
    def exitAssignment(self, ctx:kylinParser.AssignmentContext):
        pass


    # Enter a parse tree produced by kylinParser#assign_op.
    def enterAssign_op(self, ctx:kylinParser.Assign_opContext):
        pass

    # Exit a parse tree produced by kylinParser#assign_op.
    def exitAssign_op(self, ctx:kylinParser.Assign_opContext):
        pass


    # Enter a parse tree produced by kylinParser#shortVarDecl.
    def enterShortVarDecl(self, ctx:kylinParser.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#shortVarDecl.
    def exitShortVarDecl(self, ctx:kylinParser.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#emptyStmt.
    def enterEmptyStmt(self, ctx:kylinParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#emptyStmt.
    def exitEmptyStmt(self, ctx:kylinParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#returnStmt.
    def enterReturnStmt(self, ctx:kylinParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#returnStmt.
    def exitReturnStmt(self, ctx:kylinParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#breakStmt.
    def enterBreakStmt(self, ctx:kylinParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#breakStmt.
    def exitBreakStmt(self, ctx:kylinParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#continueStmt.
    def enterContinueStmt(self, ctx:kylinParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#continueStmt.
    def exitContinueStmt(self, ctx:kylinParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#gotoStmt.
    def enterGotoStmt(self, ctx:kylinParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#gotoStmt.
    def exitGotoStmt(self, ctx:kylinParser.GotoStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#fallthroughStmt.
    def enterFallthroughStmt(self, ctx:kylinParser.FallthroughStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#fallthroughStmt.
    def exitFallthroughStmt(self, ctx:kylinParser.FallthroughStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#deferStmt.
    def enterDeferStmt(self, ctx:kylinParser.DeferStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#deferStmt.
    def exitDeferStmt(self, ctx:kylinParser.DeferStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#ifStmt.
    def enterIfStmt(self, ctx:kylinParser.IfStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#ifStmt.
    def exitIfStmt(self, ctx:kylinParser.IfStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#switchStmt.
    def enterSwitchStmt(self, ctx:kylinParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#switchStmt.
    def exitSwitchStmt(self, ctx:kylinParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#exprSwitchStmt.
    def enterExprSwitchStmt(self, ctx:kylinParser.ExprSwitchStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#exprSwitchStmt.
    def exitExprSwitchStmt(self, ctx:kylinParser.ExprSwitchStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#exprCaseClause.
    def enterExprCaseClause(self, ctx:kylinParser.ExprCaseClauseContext):
        pass

    # Exit a parse tree produced by kylinParser#exprCaseClause.
    def exitExprCaseClause(self, ctx:kylinParser.ExprCaseClauseContext):
        pass


    # Enter a parse tree produced by kylinParser#exprSwitchCase.
    def enterExprSwitchCase(self, ctx:kylinParser.ExprSwitchCaseContext):
        pass

    # Exit a parse tree produced by kylinParser#exprSwitchCase.
    def exitExprSwitchCase(self, ctx:kylinParser.ExprSwitchCaseContext):
        pass


    # Enter a parse tree produced by kylinParser#typeSwitchStmt.
    def enterTypeSwitchStmt(self, ctx:kylinParser.TypeSwitchStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#typeSwitchStmt.
    def exitTypeSwitchStmt(self, ctx:kylinParser.TypeSwitchStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#typeSwitchGuard.
    def enterTypeSwitchGuard(self, ctx:kylinParser.TypeSwitchGuardContext):
        pass

    # Exit a parse tree produced by kylinParser#typeSwitchGuard.
    def exitTypeSwitchGuard(self, ctx:kylinParser.TypeSwitchGuardContext):
        pass


    # Enter a parse tree produced by kylinParser#typeCaseClause.
    def enterTypeCaseClause(self, ctx:kylinParser.TypeCaseClauseContext):
        pass

    # Exit a parse tree produced by kylinParser#typeCaseClause.
    def exitTypeCaseClause(self, ctx:kylinParser.TypeCaseClauseContext):
        pass


    # Enter a parse tree produced by kylinParser#typeSwitchCase.
    def enterTypeSwitchCase(self, ctx:kylinParser.TypeSwitchCaseContext):
        pass

    # Exit a parse tree produced by kylinParser#typeSwitchCase.
    def exitTypeSwitchCase(self, ctx:kylinParser.TypeSwitchCaseContext):
        pass


    # Enter a parse tree produced by kylinParser#typeList.
    def enterTypeList(self, ctx:kylinParser.TypeListContext):
        pass

    # Exit a parse tree produced by kylinParser#typeList.
    def exitTypeList(self, ctx:kylinParser.TypeListContext):
        pass


    # Enter a parse tree produced by kylinParser#forStmt.
    def enterForStmt(self, ctx:kylinParser.ForStmtContext):
        pass

    # Exit a parse tree produced by kylinParser#forStmt.
    def exitForStmt(self, ctx:kylinParser.ForStmtContext):
        pass


    # Enter a parse tree produced by kylinParser#forClause.
    def enterForClause(self, ctx:kylinParser.ForClauseContext):
        pass

    # Exit a parse tree produced by kylinParser#forClause.
    def exitForClause(self, ctx:kylinParser.ForClauseContext):
        pass


    # Enter a parse tree produced by kylinParser#rangeClause.
    def enterRangeClause(self, ctx:kylinParser.RangeClauseContext):
        pass

    # Exit a parse tree produced by kylinParser#rangeClause.
    def exitRangeClause(self, ctx:kylinParser.RangeClauseContext):
        pass


    # Enter a parse tree produced by kylinParser#type_.
    def enterType_(self, ctx:kylinParser.Type_Context):
        pass

    # Exit a parse tree produced by kylinParser#type_.
    def exitType_(self, ctx:kylinParser.Type_Context):
        pass


    # Enter a parse tree produced by kylinParser#typeName.
    def enterTypeName(self, ctx:kylinParser.TypeNameContext):
        pass

    # Exit a parse tree produced by kylinParser#typeName.
    def exitTypeName(self, ctx:kylinParser.TypeNameContext):
        pass


    # Enter a parse tree produced by kylinParser#typeLit.
    def enterTypeLit(self, ctx:kylinParser.TypeLitContext):
        pass

    # Exit a parse tree produced by kylinParser#typeLit.
    def exitTypeLit(self, ctx:kylinParser.TypeLitContext):
        pass


    # Enter a parse tree produced by kylinParser#arrayType.
    def enterArrayType(self, ctx:kylinParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#arrayType.
    def exitArrayType(self, ctx:kylinParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#arrayLength.
    def enterArrayLength(self, ctx:kylinParser.ArrayLengthContext):
        pass

    # Exit a parse tree produced by kylinParser#arrayLength.
    def exitArrayLength(self, ctx:kylinParser.ArrayLengthContext):
        pass


    # Enter a parse tree produced by kylinParser#elementType.
    def enterElementType(self, ctx:kylinParser.ElementTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#elementType.
    def exitElementType(self, ctx:kylinParser.ElementTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#pointerType.
    def enterPointerType(self, ctx:kylinParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#pointerType.
    def exitPointerType(self, ctx:kylinParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#interfaceType.
    def enterInterfaceType(self, ctx:kylinParser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#interfaceType.
    def exitInterfaceType(self, ctx:kylinParser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#listType.
    def enterListType(self, ctx:kylinParser.ListTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#listType.
    def exitListType(self, ctx:kylinParser.ListTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#mapType.
    def enterMapType(self, ctx:kylinParser.MapTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#mapType.
    def exitMapType(self, ctx:kylinParser.MapTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#channelType.
    def enterChannelType(self, ctx:kylinParser.ChannelTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#channelType.
    def exitChannelType(self, ctx:kylinParser.ChannelTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#methodSpec.
    def enterMethodSpec(self, ctx:kylinParser.MethodSpecContext):
        pass

    # Exit a parse tree produced by kylinParser#methodSpec.
    def exitMethodSpec(self, ctx:kylinParser.MethodSpecContext):
        pass


    # Enter a parse tree produced by kylinParser#functionType.
    def enterFunctionType(self, ctx:kylinParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#functionType.
    def exitFunctionType(self, ctx:kylinParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#signature.
    def enterSignature(self, ctx:kylinParser.SignatureContext):
        pass

    # Exit a parse tree produced by kylinParser#signature.
    def exitSignature(self, ctx:kylinParser.SignatureContext):
        pass


    # Enter a parse tree produced by kylinParser#result.
    def enterResult(self, ctx:kylinParser.ResultContext):
        pass

    # Exit a parse tree produced by kylinParser#result.
    def exitResult(self, ctx:kylinParser.ResultContext):
        pass


    # Enter a parse tree produced by kylinParser#parameters.
    def enterParameters(self, ctx:kylinParser.ParametersContext):
        pass

    # Exit a parse tree produced by kylinParser#parameters.
    def exitParameters(self, ctx:kylinParser.ParametersContext):
        pass


    # Enter a parse tree produced by kylinParser#parameterDecl.
    def enterParameterDecl(self, ctx:kylinParser.ParameterDeclContext):
        pass

    # Exit a parse tree produced by kylinParser#parameterDecl.
    def exitParameterDecl(self, ctx:kylinParser.ParameterDeclContext):
        pass


    # Enter a parse tree produced by kylinParser#expression.
    def enterExpression(self, ctx:kylinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by kylinParser#expression.
    def exitExpression(self, ctx:kylinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by kylinParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:kylinParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by kylinParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:kylinParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by kylinParser#unaryExpr.
    def enterUnaryExpr(self, ctx:kylinParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by kylinParser#unaryExpr.
    def exitUnaryExpr(self, ctx:kylinParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by kylinParser#conversion.
    def enterConversion(self, ctx:kylinParser.ConversionContext):
        pass

    # Exit a parse tree produced by kylinParser#conversion.
    def exitConversion(self, ctx:kylinParser.ConversionContext):
        pass


    # Enter a parse tree produced by kylinParser#operand.
    def enterOperand(self, ctx:kylinParser.OperandContext):
        pass

    # Exit a parse tree produced by kylinParser#operand.
    def exitOperand(self, ctx:kylinParser.OperandContext):
        pass


    # Enter a parse tree produced by kylinParser#literal.
    def enterLiteral(self, ctx:kylinParser.LiteralContext):
        pass

    # Exit a parse tree produced by kylinParser#literal.
    def exitLiteral(self, ctx:kylinParser.LiteralContext):
        pass


    # Enter a parse tree produced by kylinParser#basicLit.
    def enterBasicLit(self, ctx:kylinParser.BasicLitContext):
        pass

    # Exit a parse tree produced by kylinParser#basicLit.
    def exitBasicLit(self, ctx:kylinParser.BasicLitContext):
        pass


    # Enter a parse tree produced by kylinParser#integer.
    def enterInteger(self, ctx:kylinParser.IntegerContext):
        pass

    # Exit a parse tree produced by kylinParser#integer.
    def exitInteger(self, ctx:kylinParser.IntegerContext):
        pass


    # Enter a parse tree produced by kylinParser#operandName.
    def enterOperandName(self, ctx:kylinParser.OperandNameContext):
        pass

    # Exit a parse tree produced by kylinParser#operandName.
    def exitOperandName(self, ctx:kylinParser.OperandNameContext):
        pass


    # Enter a parse tree produced by kylinParser#qualifiedIdent.
    def enterQualifiedIdent(self, ctx:kylinParser.QualifiedIdentContext):
        pass

    # Exit a parse tree produced by kylinParser#qualifiedIdent.
    def exitQualifiedIdent(self, ctx:kylinParser.QualifiedIdentContext):
        pass


    # Enter a parse tree produced by kylinParser#compositeLit.
    def enterCompositeLit(self, ctx:kylinParser.CompositeLitContext):
        pass

    # Exit a parse tree produced by kylinParser#compositeLit.
    def exitCompositeLit(self, ctx:kylinParser.CompositeLitContext):
        pass


    # Enter a parse tree produced by kylinParser#literalType.
    def enterLiteralType(self, ctx:kylinParser.LiteralTypeContext):
        pass

    # Exit a parse tree produced by kylinParser#literalType.
    def exitLiteralType(self, ctx:kylinParser.LiteralTypeContext):
        pass


    # Enter a parse tree produced by kylinParser#literalValue.
    def enterLiteralValue(self, ctx:kylinParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by kylinParser#literalValue.
    def exitLiteralValue(self, ctx:kylinParser.LiteralValueContext):
        pass


    # Enter a parse tree produced by kylinParser#elementList.
    def enterElementList(self, ctx:kylinParser.ElementListContext):
        pass

    # Exit a parse tree produced by kylinParser#elementList.
    def exitElementList(self, ctx:kylinParser.ElementListContext):
        pass


    # Enter a parse tree produced by kylinParser#keyedElement.
    def enterKeyedElement(self, ctx:kylinParser.KeyedElementContext):
        pass

    # Exit a parse tree produced by kylinParser#keyedElement.
    def exitKeyedElement(self, ctx:kylinParser.KeyedElementContext):
        pass


    # Enter a parse tree produced by kylinParser#key.
    def enterKey(self, ctx:kylinParser.KeyContext):
        pass

    # Exit a parse tree produced by kylinParser#key.
    def exitKey(self, ctx:kylinParser.KeyContext):
        pass


    # Enter a parse tree produced by kylinParser#element.
    def enterElement(self, ctx:kylinParser.ElementContext):
        pass

    # Exit a parse tree produced by kylinParser#element.
    def exitElement(self, ctx:kylinParser.ElementContext):
        pass


    # Enter a parse tree produced by kylinParser#string_.
    def enterString_(self, ctx:kylinParser.String_Context):
        pass

    # Exit a parse tree produced by kylinParser#string_.
    def exitString_(self, ctx:kylinParser.String_Context):
        pass


    # Enter a parse tree produced by kylinParser#anonymousField.
    def enterAnonymousField(self, ctx:kylinParser.AnonymousFieldContext):
        pass

    # Exit a parse tree produced by kylinParser#anonymousField.
    def exitAnonymousField(self, ctx:kylinParser.AnonymousFieldContext):
        pass


    # Enter a parse tree produced by kylinParser#functionLit.
    def enterFunctionLit(self, ctx:kylinParser.FunctionLitContext):
        pass

    # Exit a parse tree produced by kylinParser#functionLit.
    def exitFunctionLit(self, ctx:kylinParser.FunctionLitContext):
        pass


    # Enter a parse tree produced by kylinParser#index.
    def enterIndex(self, ctx:kylinParser.IndexContext):
        pass

    # Exit a parse tree produced by kylinParser#index.
    def exitIndex(self, ctx:kylinParser.IndexContext):
        pass


    # Enter a parse tree produced by kylinParser#typeAssertion.
    def enterTypeAssertion(self, ctx:kylinParser.TypeAssertionContext):
        pass

    # Exit a parse tree produced by kylinParser#typeAssertion.
    def exitTypeAssertion(self, ctx:kylinParser.TypeAssertionContext):
        pass


    # Enter a parse tree produced by kylinParser#arguments.
    def enterArguments(self, ctx:kylinParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by kylinParser#arguments.
    def exitArguments(self, ctx:kylinParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by kylinParser#eos.
    def enterEos(self, ctx:kylinParser.EosContext):
        pass

    # Exit a parse tree produced by kylinParser#eos.
    def exitEos(self, ctx:kylinParser.EosContext):
        pass



del kylinParser