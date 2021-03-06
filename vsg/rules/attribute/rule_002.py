
from vsg.rules import lower_case_rule


class rule_002(lower_case_rule):
    '''
    Attribute rule 002 checks the **attribute** keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'attribute', '002', 'isAttributeKeyword', 'attribute')
        self.solution = 'Change the "attribute" keyword to lowercase.'
