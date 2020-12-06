# Generated from c:\Users\16904\Desktop\Kylin\src\parse\kylin.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kylinParser import kylinParser
else:
    from kylinParser import kylinParser

# This class defines a complete listener for a parse tree produced by kylinParser.
class kylinListener(ParseTreeListener):

    # Enter a parse tree produced by kylinParser#single_input.
    def enterSingle_input(self, ctx:kylinParser.Single_inputContext):
        pass

    # Exit a parse tree produced by kylinParser#single_input.
    def exitSingle_input(self, ctx:kylinParser.Single_inputContext):
        pass


    # Enter a parse tree produced by kylinParser#file_input.
    def enterFile_input(self, ctx:kylinParser.File_inputContext):
        pass

    # Exit a parse tree produced by kylinParser#file_input.
    def exitFile_input(self, ctx:kylinParser.File_inputContext):
        pass


    # Enter a parse tree produced by kylinParser#eval_input.
    def enterEval_input(self, ctx:kylinParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by kylinParser#eval_input.
    def exitEval_input(self, ctx:kylinParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by kylinParser#decorator.
    def enterDecorator(self, ctx:kylinParser.DecoratorContext):
        pass

    # Exit a parse tree produced by kylinParser#decorator.
    def exitDecorator(self, ctx:kylinParser.DecoratorContext):
        pass


    # Enter a parse tree produced by kylinParser#decorators.
    def enterDecorators(self, ctx:kylinParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by kylinParser#decorators.
    def exitDecorators(self, ctx:kylinParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by kylinParser#decorated.
    def enterDecorated(self, ctx:kylinParser.DecoratedContext):
        pass

    # Exit a parse tree produced by kylinParser#decorated.
    def exitDecorated(self, ctx:kylinParser.DecoratedContext):
        pass


    # Enter a parse tree produced by kylinParser#async_funcdef.
    def enterAsync_funcdef(self, ctx:kylinParser.Async_funcdefContext):
        pass

    # Exit a parse tree produced by kylinParser#async_funcdef.
    def exitAsync_funcdef(self, ctx:kylinParser.Async_funcdefContext):
        pass


    # Enter a parse tree produced by kylinParser#funcdef.
    def enterFuncdef(self, ctx:kylinParser.FuncdefContext):
        pass

    # Exit a parse tree produced by kylinParser#funcdef.
    def exitFuncdef(self, ctx:kylinParser.FuncdefContext):
        pass


    # Enter a parse tree produced by kylinParser#parameters.
    def enterParameters(self, ctx:kylinParser.ParametersContext):
        pass

    # Exit a parse tree produced by kylinParser#parameters.
    def exitParameters(self, ctx:kylinParser.ParametersContext):
        pass


    # Enter a parse tree produced by kylinParser#typedargslist.
    def enterTypedargslist(self, ctx:kylinParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by kylinParser#typedargslist.
    def exitTypedargslist(self, ctx:kylinParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by kylinParser#tfpdef.
    def enterTfpdef(self, ctx:kylinParser.TfpdefContext):
        pass

    # Exit a parse tree produced by kylinParser#tfpdef.
    def exitTfpdef(self, ctx:kylinParser.TfpdefContext):
        pass


    # Enter a parse tree produced by kylinParser#varargslist.
    def enterVarargslist(self, ctx:kylinParser.VarargslistContext):
        pass

    # Exit a parse tree produced by kylinParser#varargslist.
    def exitVarargslist(self, ctx:kylinParser.VarargslistContext):
        pass


    # Enter a parse tree produced by kylinParser#vfpdef.
    def enterVfpdef(self, ctx:kylinParser.VfpdefContext):
        pass

    # Exit a parse tree produced by kylinParser#vfpdef.
    def exitVfpdef(self, ctx:kylinParser.VfpdefContext):
        pass


    # Enter a parse tree produced by kylinParser#stmt.
    def enterStmt(self, ctx:kylinParser.StmtContext):
        pass

    # Exit a parse tree produced by kylinParser#stmt.
    def exitStmt(self, ctx:kylinParser.StmtContext):
        pass


    # Enter a parse tree produced by kylinParser#simple_stmt.
    def enterSimple_stmt(self, ctx:kylinParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#simple_stmt.
    def exitSimple_stmt(self, ctx:kylinParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#small_stmt.
    def enterSmall_stmt(self, ctx:kylinParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#small_stmt.
    def exitSmall_stmt(self, ctx:kylinParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#expr_stmt.
    def enterExpr_stmt(self, ctx:kylinParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#expr_stmt.
    def exitExpr_stmt(self, ctx:kylinParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#annassign.
    def enterAnnassign(self, ctx:kylinParser.AnnassignContext):
        pass

    # Exit a parse tree produced by kylinParser#annassign.
    def exitAnnassign(self, ctx:kylinParser.AnnassignContext):
        pass


    # Enter a parse tree produced by kylinParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:kylinParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:kylinParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#augassign.
    def enterAugassign(self, ctx:kylinParser.AugassignContext):
        pass

    # Exit a parse tree produced by kylinParser#augassign.
    def exitAugassign(self, ctx:kylinParser.AugassignContext):
        pass


    # Enter a parse tree produced by kylinParser#del_stmt.
    def enterDel_stmt(self, ctx:kylinParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#del_stmt.
    def exitDel_stmt(self, ctx:kylinParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#pass_stmt.
    def enterPass_stmt(self, ctx:kylinParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#pass_stmt.
    def exitPass_stmt(self, ctx:kylinParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#flow_stmt.
    def enterFlow_stmt(self, ctx:kylinParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#flow_stmt.
    def exitFlow_stmt(self, ctx:kylinParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#break_stmt.
    def enterBreak_stmt(self, ctx:kylinParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#break_stmt.
    def exitBreak_stmt(self, ctx:kylinParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#continue_stmt.
    def enterContinue_stmt(self, ctx:kylinParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#continue_stmt.
    def exitContinue_stmt(self, ctx:kylinParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#return_stmt.
    def enterReturn_stmt(self, ctx:kylinParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#return_stmt.
    def exitReturn_stmt(self, ctx:kylinParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#yield_stmt.
    def enterYield_stmt(self, ctx:kylinParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#yield_stmt.
    def exitYield_stmt(self, ctx:kylinParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#raise_stmt.
    def enterRaise_stmt(self, ctx:kylinParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#raise_stmt.
    def exitRaise_stmt(self, ctx:kylinParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#import_stmt.
    def enterImport_stmt(self, ctx:kylinParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#import_stmt.
    def exitImport_stmt(self, ctx:kylinParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#import_name.
    def enterImport_name(self, ctx:kylinParser.Import_nameContext):
        pass

    # Exit a parse tree produced by kylinParser#import_name.
    def exitImport_name(self, ctx:kylinParser.Import_nameContext):
        pass


    # Enter a parse tree produced by kylinParser#import_from.
    def enterImport_from(self, ctx:kylinParser.Import_fromContext):
        pass

    # Exit a parse tree produced by kylinParser#import_from.
    def exitImport_from(self, ctx:kylinParser.Import_fromContext):
        pass


    # Enter a parse tree produced by kylinParser#import_as_name.
    def enterImport_as_name(self, ctx:kylinParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by kylinParser#import_as_name.
    def exitImport_as_name(self, ctx:kylinParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by kylinParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:kylinParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by kylinParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:kylinParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by kylinParser#import_as_names.
    def enterImport_as_names(self, ctx:kylinParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by kylinParser#import_as_names.
    def exitImport_as_names(self, ctx:kylinParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by kylinParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:kylinParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by kylinParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:kylinParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by kylinParser#dotted_name.
    def enterDotted_name(self, ctx:kylinParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by kylinParser#dotted_name.
    def exitDotted_name(self, ctx:kylinParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by kylinParser#global_stmt.
    def enterGlobal_stmt(self, ctx:kylinParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#global_stmt.
    def exitGlobal_stmt(self, ctx:kylinParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:kylinParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:kylinParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#assert_stmt.
    def enterAssert_stmt(self, ctx:kylinParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#assert_stmt.
    def exitAssert_stmt(self, ctx:kylinParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#compound_stmt.
    def enterCompound_stmt(self, ctx:kylinParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#compound_stmt.
    def exitCompound_stmt(self, ctx:kylinParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#async_stmt.
    def enterAsync_stmt(self, ctx:kylinParser.Async_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#async_stmt.
    def exitAsync_stmt(self, ctx:kylinParser.Async_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#if_stmt.
    def enterIf_stmt(self, ctx:kylinParser.If_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#if_stmt.
    def exitIf_stmt(self, ctx:kylinParser.If_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#while_stmt.
    def enterWhile_stmt(self, ctx:kylinParser.While_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#while_stmt.
    def exitWhile_stmt(self, ctx:kylinParser.While_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#for_stmt.
    def enterFor_stmt(self, ctx:kylinParser.For_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#for_stmt.
    def exitFor_stmt(self, ctx:kylinParser.For_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#try_stmt.
    def enterTry_stmt(self, ctx:kylinParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#try_stmt.
    def exitTry_stmt(self, ctx:kylinParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#with_stmt.
    def enterWith_stmt(self, ctx:kylinParser.With_stmtContext):
        pass

    # Exit a parse tree produced by kylinParser#with_stmt.
    def exitWith_stmt(self, ctx:kylinParser.With_stmtContext):
        pass


    # Enter a parse tree produced by kylinParser#with_item.
    def enterWith_item(self, ctx:kylinParser.With_itemContext):
        pass

    # Exit a parse tree produced by kylinParser#with_item.
    def exitWith_item(self, ctx:kylinParser.With_itemContext):
        pass


    # Enter a parse tree produced by kylinParser#except_clause.
    def enterExcept_clause(self, ctx:kylinParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by kylinParser#except_clause.
    def exitExcept_clause(self, ctx:kylinParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by kylinParser#suite.
    def enterSuite(self, ctx:kylinParser.SuiteContext):
        pass

    # Exit a parse tree produced by kylinParser#suite.
    def exitSuite(self, ctx:kylinParser.SuiteContext):
        pass


    # Enter a parse tree produced by kylinParser#test.
    def enterTest(self, ctx:kylinParser.TestContext):
        pass

    # Exit a parse tree produced by kylinParser#test.
    def exitTest(self, ctx:kylinParser.TestContext):
        pass


    # Enter a parse tree produced by kylinParser#test_nocond.
    def enterTest_nocond(self, ctx:kylinParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by kylinParser#test_nocond.
    def exitTest_nocond(self, ctx:kylinParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by kylinParser#lambdef.
    def enterLambdef(self, ctx:kylinParser.LambdefContext):
        pass

    # Exit a parse tree produced by kylinParser#lambdef.
    def exitLambdef(self, ctx:kylinParser.LambdefContext):
        pass


    # Enter a parse tree produced by kylinParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:kylinParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by kylinParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:kylinParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by kylinParser#or_test.
    def enterOr_test(self, ctx:kylinParser.Or_testContext):
        pass

    # Exit a parse tree produced by kylinParser#or_test.
    def exitOr_test(self, ctx:kylinParser.Or_testContext):
        pass


    # Enter a parse tree produced by kylinParser#and_test.
    def enterAnd_test(self, ctx:kylinParser.And_testContext):
        pass

    # Exit a parse tree produced by kylinParser#and_test.
    def exitAnd_test(self, ctx:kylinParser.And_testContext):
        pass


    # Enter a parse tree produced by kylinParser#not_test.
    def enterNot_test(self, ctx:kylinParser.Not_testContext):
        pass

    # Exit a parse tree produced by kylinParser#not_test.
    def exitNot_test(self, ctx:kylinParser.Not_testContext):
        pass


    # Enter a parse tree produced by kylinParser#comparison.
    def enterComparison(self, ctx:kylinParser.ComparisonContext):
        pass

    # Exit a parse tree produced by kylinParser#comparison.
    def exitComparison(self, ctx:kylinParser.ComparisonContext):
        pass


    # Enter a parse tree produced by kylinParser#comp_op.
    def enterComp_op(self, ctx:kylinParser.Comp_opContext):
        pass

    # Exit a parse tree produced by kylinParser#comp_op.
    def exitComp_op(self, ctx:kylinParser.Comp_opContext):
        pass


    # Enter a parse tree produced by kylinParser#star_expr.
    def enterStar_expr(self, ctx:kylinParser.Star_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#star_expr.
    def exitStar_expr(self, ctx:kylinParser.Star_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#expr.
    def enterExpr(self, ctx:kylinParser.ExprContext):
        pass

    # Exit a parse tree produced by kylinParser#expr.
    def exitExpr(self, ctx:kylinParser.ExprContext):
        pass


    # Enter a parse tree produced by kylinParser#xor_expr.
    def enterXor_expr(self, ctx:kylinParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#xor_expr.
    def exitXor_expr(self, ctx:kylinParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#and_expr.
    def enterAnd_expr(self, ctx:kylinParser.And_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#and_expr.
    def exitAnd_expr(self, ctx:kylinParser.And_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#shift_expr.
    def enterShift_expr(self, ctx:kylinParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#shift_expr.
    def exitShift_expr(self, ctx:kylinParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#arith_expr.
    def enterArith_expr(self, ctx:kylinParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#arith_expr.
    def exitArith_expr(self, ctx:kylinParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#term.
    def enterTerm(self, ctx:kylinParser.TermContext):
        pass

    # Exit a parse tree produced by kylinParser#term.
    def exitTerm(self, ctx:kylinParser.TermContext):
        pass


    # Enter a parse tree produced by kylinParser#factor.
    def enterFactor(self, ctx:kylinParser.FactorContext):
        pass

    # Exit a parse tree produced by kylinParser#factor.
    def exitFactor(self, ctx:kylinParser.FactorContext):
        pass


    # Enter a parse tree produced by kylinParser#power.
    def enterPower(self, ctx:kylinParser.PowerContext):
        pass

    # Exit a parse tree produced by kylinParser#power.
    def exitPower(self, ctx:kylinParser.PowerContext):
        pass


    # Enter a parse tree produced by kylinParser#atom_expr.
    def enterAtom_expr(self, ctx:kylinParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#atom_expr.
    def exitAtom_expr(self, ctx:kylinParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#atom.
    def enterAtom(self, ctx:kylinParser.AtomContext):
        pass

    # Exit a parse tree produced by kylinParser#atom.
    def exitAtom(self, ctx:kylinParser.AtomContext):
        pass


    # Enter a parse tree produced by kylinParser#testlist_comp.
    def enterTestlist_comp(self, ctx:kylinParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by kylinParser#testlist_comp.
    def exitTestlist_comp(self, ctx:kylinParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by kylinParser#trailer.
    def enterTrailer(self, ctx:kylinParser.TrailerContext):
        pass

    # Exit a parse tree produced by kylinParser#trailer.
    def exitTrailer(self, ctx:kylinParser.TrailerContext):
        pass


    # Enter a parse tree produced by kylinParser#subscriptlist.
    def enterSubscriptlist(self, ctx:kylinParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by kylinParser#subscriptlist.
    def exitSubscriptlist(self, ctx:kylinParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by kylinParser#subscript.
    def enterSubscript(self, ctx:kylinParser.SubscriptContext):
        pass

    # Exit a parse tree produced by kylinParser#subscript.
    def exitSubscript(self, ctx:kylinParser.SubscriptContext):
        pass


    # Enter a parse tree produced by kylinParser#sliceop.
    def enterSliceop(self, ctx:kylinParser.SliceopContext):
        pass

    # Exit a parse tree produced by kylinParser#sliceop.
    def exitSliceop(self, ctx:kylinParser.SliceopContext):
        pass


    # Enter a parse tree produced by kylinParser#exprlist.
    def enterExprlist(self, ctx:kylinParser.ExprlistContext):
        pass

    # Exit a parse tree produced by kylinParser#exprlist.
    def exitExprlist(self, ctx:kylinParser.ExprlistContext):
        pass


    # Enter a parse tree produced by kylinParser#testlist.
    def enterTestlist(self, ctx:kylinParser.TestlistContext):
        pass

    # Exit a parse tree produced by kylinParser#testlist.
    def exitTestlist(self, ctx:kylinParser.TestlistContext):
        pass


    # Enter a parse tree produced by kylinParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:kylinParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by kylinParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:kylinParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by kylinParser#classdef.
    def enterClassdef(self, ctx:kylinParser.ClassdefContext):
        pass

    # Exit a parse tree produced by kylinParser#classdef.
    def exitClassdef(self, ctx:kylinParser.ClassdefContext):
        pass


    # Enter a parse tree produced by kylinParser#arglist.
    def enterArglist(self, ctx:kylinParser.ArglistContext):
        pass

    # Exit a parse tree produced by kylinParser#arglist.
    def exitArglist(self, ctx:kylinParser.ArglistContext):
        pass


    # Enter a parse tree produced by kylinParser#argument.
    def enterArgument(self, ctx:kylinParser.ArgumentContext):
        pass

    # Exit a parse tree produced by kylinParser#argument.
    def exitArgument(self, ctx:kylinParser.ArgumentContext):
        pass


    # Enter a parse tree produced by kylinParser#comp_iter.
    def enterComp_iter(self, ctx:kylinParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by kylinParser#comp_iter.
    def exitComp_iter(self, ctx:kylinParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by kylinParser#comp_for.
    def enterComp_for(self, ctx:kylinParser.Comp_forContext):
        pass

    # Exit a parse tree produced by kylinParser#comp_for.
    def exitComp_for(self, ctx:kylinParser.Comp_forContext):
        pass


    # Enter a parse tree produced by kylinParser#comp_if.
    def enterComp_if(self, ctx:kylinParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by kylinParser#comp_if.
    def exitComp_if(self, ctx:kylinParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by kylinParser#encoding_decl.
    def enterEncoding_decl(self, ctx:kylinParser.Encoding_declContext):
        pass

    # Exit a parse tree produced by kylinParser#encoding_decl.
    def exitEncoding_decl(self, ctx:kylinParser.Encoding_declContext):
        pass


    # Enter a parse tree produced by kylinParser#yield_expr.
    def enterYield_expr(self, ctx:kylinParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by kylinParser#yield_expr.
    def exitYield_expr(self, ctx:kylinParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by kylinParser#yield_arg.
    def enterYield_arg(self, ctx:kylinParser.Yield_argContext):
        pass

    # Exit a parse tree produced by kylinParser#yield_arg.
    def exitYield_arg(self, ctx:kylinParser.Yield_argContext):
        pass



del kylinParser