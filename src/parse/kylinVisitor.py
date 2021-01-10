# Generated from c:\Users\16904\Desktop\Kylin\src\parse\kylin.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kylinParser import kylinParser
else:
    from kylinParser import kylinParser

# This class defines a complete generic visitor for a parse tree produced by kylinParser.

class kylinVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by kylinParser#sourceFile.
    def visitSourceFile(self, ctx:kylinParser.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#packageClause.
    def visitPackageClause(self, ctx:kylinParser.PackageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#importDecl.
    def visitImportDecl(self, ctx:kylinParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#importSpec.
    def visitImportSpec(self, ctx:kylinParser.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#importPath.
    def visitImportPath(self, ctx:kylinParser.ImportPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#declaration.
    def visitDeclaration(self, ctx:kylinParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#constDecl.
    def visitConstDecl(self, ctx:kylinParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#constSpec.
    def visitConstSpec(self, ctx:kylinParser.ConstSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#identifierList.
    def visitIdentifierList(self, ctx:kylinParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#expressionList.
    def visitExpressionList(self, ctx:kylinParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeDecl.
    def visitTypeDecl(self, ctx:kylinParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeSpec.
    def visitTypeSpec(self, ctx:kylinParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#functionDecl.
    def visitFunctionDecl(self, ctx:kylinParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#varDecl.
    def visitVarDecl(self, ctx:kylinParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#varSpec.
    def visitVarSpec(self, ctx:kylinParser.VarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#block.
    def visitBlock(self, ctx:kylinParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#statementList.
    def visitStatementList(self, ctx:kylinParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#statement.
    def visitStatement(self, ctx:kylinParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#simpleStmt.
    def visitSimpleStmt(self, ctx:kylinParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#expressionStmt.
    def visitExpressionStmt(self, ctx:kylinParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#incDecStmt.
    def visitIncDecStmt(self, ctx:kylinParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#assignment.
    def visitAssignment(self, ctx:kylinParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#assign_op.
    def visitAssign_op(self, ctx:kylinParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:kylinParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#emptyStmt.
    def visitEmptyStmt(self, ctx:kylinParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#returnStmt.
    def visitReturnStmt(self, ctx:kylinParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#breakStmt.
    def visitBreakStmt(self, ctx:kylinParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#continueStmt.
    def visitContinueStmt(self, ctx:kylinParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#gotoStmt.
    def visitGotoStmt(self, ctx:kylinParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#fallthroughStmt.
    def visitFallthroughStmt(self, ctx:kylinParser.FallthroughStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#deferStmt.
    def visitDeferStmt(self, ctx:kylinParser.DeferStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#ifStmt.
    def visitIfStmt(self, ctx:kylinParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#switchStmt.
    def visitSwitchStmt(self, ctx:kylinParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#exprSwitchStmt.
    def visitExprSwitchStmt(self, ctx:kylinParser.ExprSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#exprCaseClause.
    def visitExprCaseClause(self, ctx:kylinParser.ExprCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#exprSwitchCase.
    def visitExprSwitchCase(self, ctx:kylinParser.ExprSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeSwitchStmt.
    def visitTypeSwitchStmt(self, ctx:kylinParser.TypeSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeSwitchGuard.
    def visitTypeSwitchGuard(self, ctx:kylinParser.TypeSwitchGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeCaseClause.
    def visitTypeCaseClause(self, ctx:kylinParser.TypeCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeSwitchCase.
    def visitTypeSwitchCase(self, ctx:kylinParser.TypeSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeList.
    def visitTypeList(self, ctx:kylinParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#forStmt.
    def visitForStmt(self, ctx:kylinParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#forClause.
    def visitForClause(self, ctx:kylinParser.ForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#rangeClause.
    def visitRangeClause(self, ctx:kylinParser.RangeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#type_.
    def visitType_(self, ctx:kylinParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeName.
    def visitTypeName(self, ctx:kylinParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeLit.
    def visitTypeLit(self, ctx:kylinParser.TypeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#arrayType.
    def visitArrayType(self, ctx:kylinParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#arrayLength.
    def visitArrayLength(self, ctx:kylinParser.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#elementType.
    def visitElementType(self, ctx:kylinParser.ElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#pointerType.
    def visitPointerType(self, ctx:kylinParser.PointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#interfaceType.
    def visitInterfaceType(self, ctx:kylinParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#listType.
    def visitListType(self, ctx:kylinParser.ListTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#mapType.
    def visitMapType(self, ctx:kylinParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#channelType.
    def visitChannelType(self, ctx:kylinParser.ChannelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#methodSpec.
    def visitMethodSpec(self, ctx:kylinParser.MethodSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#functionType.
    def visitFunctionType(self, ctx:kylinParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#signature.
    def visitSignature(self, ctx:kylinParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#result.
    def visitResult(self, ctx:kylinParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#parameters.
    def visitParameters(self, ctx:kylinParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#parameterDecl.
    def visitParameterDecl(self, ctx:kylinParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#expression.
    def visitExpression(self, ctx:kylinParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:kylinParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#unaryExpr.
    def visitUnaryExpr(self, ctx:kylinParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#conversion.
    def visitConversion(self, ctx:kylinParser.ConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#operand.
    def visitOperand(self, ctx:kylinParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#literal.
    def visitLiteral(self, ctx:kylinParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#basicLit.
    def visitBasicLit(self, ctx:kylinParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#integer.
    def visitInteger(self, ctx:kylinParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#operandName.
    def visitOperandName(self, ctx:kylinParser.OperandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#qualifiedIdent.
    def visitQualifiedIdent(self, ctx:kylinParser.QualifiedIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#compositeLit.
    def visitCompositeLit(self, ctx:kylinParser.CompositeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#literalType.
    def visitLiteralType(self, ctx:kylinParser.LiteralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#literalValue.
    def visitLiteralValue(self, ctx:kylinParser.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#elementList.
    def visitElementList(self, ctx:kylinParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#keyedElement.
    def visitKeyedElement(self, ctx:kylinParser.KeyedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#key.
    def visitKey(self, ctx:kylinParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#element.
    def visitElement(self, ctx:kylinParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#string_.
    def visitString_(self, ctx:kylinParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#anonymousField.
    def visitAnonymousField(self, ctx:kylinParser.AnonymousFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#functionLit.
    def visitFunctionLit(self, ctx:kylinParser.FunctionLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#index.
    def visitIndex(self, ctx:kylinParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#typeAssertion.
    def visitTypeAssertion(self, ctx:kylinParser.TypeAssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#arguments.
    def visitArguments(self, ctx:kylinParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kylinParser#eos.
    def visitEos(self, ctx:kylinParser.EosContext):
        return self.visitChildren(ctx)



del kylinParser