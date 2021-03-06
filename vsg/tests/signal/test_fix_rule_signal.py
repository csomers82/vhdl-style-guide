import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile

class testFixRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))

    def test_fix_rule_001(self):
        oRule = signal.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = signal.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = signal.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = signal.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = signal.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = signal.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_fix_rule_007(self):
#        oRule = signal.rule_007()
#        dExpected = []
#        oRule.fix(self.oFile)
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, dExpected)

#    def test_fix_rule_008_with_no_prefixes(self):
#        oRule = signal.rule_008()
#        dExpected = []
#        oRule.fix(self.oFile)
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_008_with_prefixes(self):
#        oRule = signal.rule_008()
#        dExpected = []
#        oRule.fix(self.oFile)
#        oRule.prefixes = ['a_','b_','d_','e_']
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = signal.rule_013()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = signal.rule_010()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[12].line, '  signal   SIg : std_logic_vector(31 downto 0);')
        self.assertEqual(self.oFile.lines[16].line, '  signal sig :   std_logic_vector (31 downto 0) := (others => \'0\');')
        self.assertEqual(self.oFile.lines[20].line, '  signal b_sig100, b_sig2 :std_logic_vector (31 downto 0);')
        self.assertEqual(self.oFile.lines[23].line, '  signal w_sig1 : t_User_Defined_Type;')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = signal.rule_011()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[12].line, '  signal   SIg : std_logic_vector(31 downto 0);')
        self.assertEqual(self.oFile.lines[16].line, '  signal sig :   std_logic_vector (31 downto 0) := (others => \'0\');')
        self.assertEqual(self.oFile.lines[20].line, '  signal b_sig100, b_sig2 :std_logic_vector (31 downto 0);')
        self.assertEqual(self.oFile.lines[23].line, '  signal w_sig1 : t_user_defined_type;')
