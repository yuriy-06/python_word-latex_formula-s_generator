import copy
class ReportNumber:
    """
    задумка такая, если указано свойство word_description, оформлять отчет по правилам Ворд,
    если указано latex_description - оформлять latex_description
def test_add():
    a = ReportNumber(5, word_description = 'a_1')
    b = ReportNumber(6, word_description = 'b_1')
    c = a + b
    return c
test_add().report() => '(a_1 + b_1) = (5 + 6) = 11'
def test_pow():
    a = ReportNumber(5, word_description = 'a_1')
    b = ReportNumber(6, word_description = 'b_1')
    c = b**2
    return c
test_pow().report() => 'b_1^2 = 6**2 = 36'
    """
    def __init__(self, value, word_description=None, latex_description=None, stack=None):
        self.word_description = word_description
        self.latex_description = latex_description
        self.value = value
        self.otput_report_number_obj = None
        self.stack = stack
        self.value_description = None
        
    def word_output(self, new_value, output_description, obj2, value_description):
        self.otput_report_number_obj = copy.copy(self)
        self.otput_report_number_obj.value = new_value
        self.otput_report_number_obj.word_description = output_description
        self.otput_report_number_obj.stack=[self, obj2]
        self.otput_report_number_obj.value_description = value_description 
        
    def latex_output(self, new_value, output_description, obj2, value_description):
        self.otput_report_number_obj = copy.copy(self)
        self.otput_report_number_obj.value = new_value
        self.otput_report_number_obj.latex_description = output_description
        self.otput_report_number_obj.stack=[self, obj2]
        self.otput_report_number_obj.value_description = value_description 

    def operation_template(self, string_word_operation, string_latex_operation, obj2, new_value, value_description):
        if self.word_description is not None:
            try:
                output_description = string_word_operation.format(self.word_description, obj2.word_description)
            except:  # на случай если obj2 окажется числом в операции возведение в степень, или другой
                output_description = string_word_operation.format(self.word_description, obj2)
            self.word_output(new_value, output_description, obj2, value_description)
        if self.latex_description is not None:
            try:
                output_description = string_latex_operation.format(self.latex_description, obj2.latex_description)
            except:
                output_description = string_latex_operation.format(self.latex_description, obj2)
            self.latex_output(new_value, output_description, obj2, value_description)
        return self.otput_report_number_obj
    
    def __add__(self, obj2):
        """
        сначала идет строка word_description,
        затем latex_description
        """
        try:
            new_value = self.value + obj2.value
            value_description = '({} + {})'.format(self.value, obj2.value)
        except:
            new_value = self.value + obj2
            value_description = '({} + {})'.format(self.value, obj2)
        return self.operation_template('({} + {})', '({} + {})', obj2, new_value, value_description)

    def __sub__(self, obj2):  # вычитание
        try:
            new_value = self.value - obj2.value
            value_description = '({} - {})'.format(self.value, obj2.value)
        except:
            new_value = self.value - obj2
            value_description = '({} - {})'.format(self.value, obj2)
        return self.operation_template('({} - {})', '({} - {})', obj2, new_value, value_description)

    def __mul__(self, obj2):  # умножение
        try:
            new_value = self.value * obj2.value
            value_description = '{} * {}'.format(self.value, obj2.value)
        except:
            new_value = self.value * obj2
            value_description = '({} * {})'.format(self.value, obj2)
        return self.operation_template('{} times {}', '{} \\times {}', obj2, new_value, value_description)

    def __truediv__(self, obj2):  # деление
        try:
            new_value = self.value / obj2.value
            value_description = '{} / {}'.format(self.value, obj2.value)
        except:
            new_value = self.value / obj2
            value_description = '{} / {}'.format(self.value, obj2)
        return self.operation_template('{} over {}', '\\frac{}{}', obj2, new_value, value_description)

    def __pow__(self, obj2):  # возведение в степень
        try:
            new_value = self.value**obj2.value
            value_description = '{}**{}'.format(self.value, obj2.value)
        except:
            new_value = self.value**obj2
            value_description = '{}**{}'.format(self.value, obj2)
        return self.operation_template('{}^{}', '{}^{}', obj2, new_value, value_description)
    
    def report(self):
        if self.word_description is not None:
            report = '{} = {} = {}'.format(self.word_description, self.value_description, self.value)
        if self.latex_description is not None:
            report = '{} = {} = {}'.format(self.latex_description, self.value_description, self.value)
        return report