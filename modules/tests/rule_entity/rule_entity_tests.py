
import sys
sys.path.append('..\..')
import unittest
import rule_entity
import os


class testRuleEntityMethods(unittest.TestCase):

    def test_rule_001_exists(self):
        oRule = rule_entity.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '001')

    def test_rule_001(self):
        oRule = rule_entity.rule_001()

        dExpected = [2,4]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append(' entity ')
        lLines.append('entity')
        lLines.append('     Entity  ')
        lLines.append('Entity')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_exists(self):
        oRule = rule_entity.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '002')

    def test_rule_002(self):
        oRule = rule_entity.rule_002()

        dExpected = [3,5]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append(' entity blah is')
        lLines.append('entity  blah   is')
        lLines.append('     Entity blah    is  ')
        lLines.append('Entity   blah is')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_exists(self):
        oRule = rule_entity.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '003')

    def test_rule_003(self):
        oRule = rule_entity.rule_003()

        dExpected = [4,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah is')
        lLines.append('entity  blah   is')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah    is  ')
        lLines.append('Entity   blah is')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004_exists(self):
        oRule = rule_entity.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '004')

    def test_rule_004(self):
        oRule = rule_entity.rule_004()

        dExpected = [7,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah   is')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah    is  ')
        lLines.append('Entity   blah IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005_exists(self):
        oRule = rule_entity.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '005')

    def test_rule_005(self):
        oRule = rule_entity.rule_005()

        dExpected = [4,7]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah  ')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah    ')
        lLines.append('Entity   blah IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006_exists(self):
        oRule = rule_entity.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '006')

    def test_rule_006(self):
        oRule = rule_entity.rule_006()

        dExpected = [3,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah is  ')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('Entity   blah IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007_exists(self):
        oRule = rule_entity.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '007')

    def test_rule_007(self):
        oRule = rule_entity.rule_007()

        dExpected = [4,8]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append(' entity blah iS')
        lLines.append('entity  blah   is  ')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('Entity   blah   IS')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008_exists(self):
        oRule = rule_entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '008')

    def test_rule_008(self):
        oRule = rule_entity.rule_008()

        dExpected = [12]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port (')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('    port (')
        lLines.append ('')
        lLines.append('Entity   blah   IS')
        lLines.append ('')
        lLines.append('  PORT (  ')
        lLines.append ('')
        lLines.append('Entity   blah   IS')
        lLines.append('    port (  ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009_exists(self):
        oRule = rule_entity.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '009')

    def test_rule_009(self):
        oRule = rule_entity.rule_009()

        dExpected = [4, 15]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('  port (')
        lLines.append ('')
        lLines.append('Entity   blah   IS')
        lLines.append ('')
        lLines.append('  PORT (  ')
        lLines.append ('')
        lLines.append('Entity   blah   IS')
        lLines.append('    port (  ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010_exists(self):
        oRule = rule_entity.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '010')

    def test_rule_010(self):
        oRule = rule_entity.rule_010()

        dExpected = [4]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('   ')
        lLines.append('   ')
        lLines.append('     Entity blah is   ')
        lLines.append('    port (')
        lLines.append ('')
        lLines.append('Entity   blah   IS')
        lLines.append ('')
        lLines.append('  PORT (  ')
        lLines.append ('')
        lLines.append('Entity   blah   IS')
        lLines.append('    port (  ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011_exists(self):
        oRule = rule_entity.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '011')

    def test_rule_011(self):
        oRule = rule_entity.rule_011()

        dExpected = [6,7,11]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('    port_1 : in  std_logic;')
        lLines.append('     port_2 : out std_logic;')
        lLines.append('  port_3 :  in    std_logic;')
        lLines.append('')
        lLines.append('    port_4   :   out   std_logic;')
        lLines.append('    port_5   : inout   std_logic;')
        lLines.append('   port_6    :   in std_logic;')
        lLines.append('end blah;')
        lLines.append('   ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)


    def test_rule_012_exists(self):
        oRule = rule_entity.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '012')

    def test_rule_012(self):
        oRule = rule_entity.rule_012()

        dExpected = [7,11]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('    port_1 : in  std_logic;')
        lLines.append('     port_2 : out std_logic;')
        lLines.append('  port_3 :  in    std_logic;')
        lLines.append('')
        lLines.append('    port_4   :   out   std_logic;')
        lLines.append('    port_5   : inout   std_logic;')
        lLines.append('   port_6    :   in std_logic;')
        lLines.append('end blah;')
        lLines.append('   ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013_exists(self):
        oRule = rule_entity.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '013')

    def test_rule_013(self):
        oRule = rule_entity.rule_013()

        dExpected = [6]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('    port_1 : in  std_logic;')
        lLines.append('     port_2 : out std_logic;')
        lLines.append('  port_3 :  in    std_logic;')
        lLines.append('')
        lLines.append('    port_4   :   out   std_logic;')
        lLines.append('    port_5   : inout   std_logic;')
        lLines.append('   port_6    :   in std_logic;')
        lLines.append('end blah;')
        lLines.append('   ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)


    def test_rule_014_exists(self):
        oRule = rule_entity.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '014')

    def test_rule_014(self):
        oRule = rule_entity.rule_014()

        dExpected = [5,11]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('    port_1 : in  std_logic;')
        lLines.append('     port_2 : out std_logic;')
        lLines.append('  port_3 :  in    std_logic;')
        lLines.append('')
        lLines.append('    port_4   :   out   std_logic;')
        lLines.append('    port_5   : inout   std_logic;')
        lLines.append('   port_6    :   in std_logic;')
        lLines.append('   port_7    : inout std_logic;')
        lLines.append('end blah;')
        lLines.append('   ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_exists(self):
        oRule = rule_entity.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '015')

    def test_rule_015(self):
        oRule = rule_entity.rule_015()

        dExpected = [9]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('    port_1 : in  std_logic;')
        lLines.append('     port_2 : out std_logic;')
        lLines.append('  port_3 :  in    std_logic;')
        lLines.append('')
        lLines.append('    port_4   :   out   std_logic;')
        lLines.append('    port_5   : inout   std_logic;')
        lLines.append('   port_6    :   in std_logic;')
        lLines.append('   port_7    : inout std_logic;')
        lLines.append('end blah;')
        lLines.append('   ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_016_exists(self):
        oRule = rule_entity.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '016')

    def test_rule_016(self):
        oRule = rule_entity.rule_016()

        dExpected = [10]
        lLines = []
        lLines.append('  This is a test of ending entity')
        lLines.append('   ')
        lLines.append('entity  blah   is  ')
        lLines.append('port    (')
        lLines.append('    port_1 : in  std_logic;')
        lLines.append('     port_2 : out std_logic;')
        lLines.append('  port_3 :  in    std_logic;')
        lLines.append('')
        lLines.append('    port_4   :   out   std_logic;')
        lLines.append('    port_5   : inout   std_logic;')
        lLines.append('   port_6    :   in std_logic;')
        lLines.append('   port_7    : inout std_logic;')
        lLines.append('end blah;')
        lLines.append('   ')
        oRule.analyze(lLines)
        self.assertEqual(oRule.violations, dExpected)


if __name__ == '__main__':
    unittest.main()
