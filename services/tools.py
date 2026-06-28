from datetime import datetime


class ToolBox:

    def calculator(self, expression):

        try:
            return eval(expression)

        except:
            return "Invalid calculation."

    def current_time(self):

        return datetime.now().strftime("%H:%M:%S")

    def current_date(self):

        return datetime.now().strftime("%Y-%m-%d")

    def echo(self, text):

        return text

