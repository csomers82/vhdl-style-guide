
from vsg import rule
from vsg import fix
from vsg import check


class rule_011(rule.rule):
    '''If rule 011 checks for an empty line after the "else" keyword.'''

    def __init__(self):
        rule.rule.__init__(self, 'if', '011')
        self.solution = 'Remove blank line(s) after the "else" keyword.'
        self.phase = 3

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isElseKeyword and not oLine.isEndIfKeyword:
                check.is_no_blank_line_after(self, oFile, iLineNumber, 'isCaseKeyword')

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.remove_blank_lines_below(self, oFile, iLineNumber, 'isCaseKeyword')
