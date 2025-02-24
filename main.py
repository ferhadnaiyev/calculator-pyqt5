
from PyQt5 import QtWidgets
from calc3 import Ui_Form  
import sys

class CalculatorApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
      
        self.current_input = "" 
        self.operator = ""      
        self.operand1 = None    
        self.operand2 = None   
        
        
        self.button_0.clicked.connect(lambda: self.add_to_display("0"))
        self.button_1.clicked.connect(lambda: self.add_to_display("1"))
        self.button_2.clicked.connect(lambda: self.add_to_display("2"))
        self.button_3.clicked.connect(lambda: self.add_to_display("3"))
        self.button_4.clicked.connect(lambda: self.add_to_display("4"))
        self.button_5.clicked.connect(lambda: self.add_to_display("5"))
        self.button_6.clicked.connect(lambda: self.add_to_display("6"))
        self.button_7.clicked.connect(lambda: self.add_to_display("7"))
        self.button_8.clicked.connect(lambda: self.add_to_display("8"))
        self.button_9.clicked.connect(lambda: self.add_to_display("9"))
        self.button_dot.clicked.connect(lambda: self.add_to_display("."))
        
        
        self.button_add.clicked.connect(lambda: self.set_operator("+"))
        self.button_subtract.clicked.connect(lambda: self.set_operator("-"))
        self.button_multiply.clicked.connect(lambda: self.set_operator("*"))
        self.button_divide.clicked.connect(lambda: self.set_operator("/"))
        self.button_percentage.clicked.connect(self.calculate_percentage)
        self.button_plus_minus.clicked.connect(self.toggle_sign)
        self.button_equals.clicked.connect(self.calculate_result)
        self.button_clear.clicked.connect(self.clear_display)

    def add_to_display(self, text):
        self.current_input += text
        self.display.setText(self.current_input)

    def set_operator(self, operator):
        if self.current_input:
            self.operand1 = float(self.current_input)
            self.operator = operator
            self.current_input = ""
            self.display.setText(self.operator)

    def calculate_result(self):
        if self.current_input and self.operator:
            self.operand2 = float(self.current_input)
            result = self.perform_operation(self.operand1, self.operand2, self.operator)
            self.display.setText(str(result))
            self.current_input = str(result)
            self.operator = ""
            self.operand1 = None
            self.operand2 = None

    def perform_operation(self, operand1, operand2, operator):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2 if operand2 != 0 else "Error"
    
    def calculate_percentage(self):
        if self.current_input:
            result = float(self.current_input) / 100
            self.display.setText(str(result))
            self.current_input = str(result)

    def toggle_sign(self):
        if self.current_input:
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.display.setText(self.current_input)

    def clear_display(self):
        self.current_input = ""
        self.operator = ""
        self.operand1 = None
        self.operand2 = None
        self.display.setText("0")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

