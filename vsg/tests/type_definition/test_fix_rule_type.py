
import os
import unittest

from vsg.rules import type_definition
from vsg import vhdlFile

class testFixRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'type_test_input.vhd'))

    def test_fix_rule_001(self):
        oRule = type_definition.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = type_definition.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = type_definition.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = type_definition.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = type_definition.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = type_definition.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[36].line, '  type a is (--This is a comment')
        self.assertEqual(self.oFile.lines[134].line, '  type memory_type_is_name is array (DEPTH - 1 downto 0) of STD_LOGIC_VECTOR(WIDTH-1 downto 0);')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = type_definition.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = type_definition.rule_008()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = type_definition.rule_009()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[6].line, '   type a is (')
        self.assertEqual(self.oFile.lines[7].line, ' B, C,')

    def test_fix_rule_010(self):
        oRule = type_definition.rule_010()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = type_definition.rule_011()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = type_definition.rule_013()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[13].line, '  type interface is record')
