# class Machine:
#     def print(self, document):
#         pass
#
#     def fax(self, document):
#         pass
#
#     def scan(self, document):
#         pass
#
# class MultiFunctionPrinter(Machine):
#     def print(self, document):
#         print("Printing ")
#
#     def fax(self, document):
#         print("Faxing")
#
#     def scan(self, document):
#         print("Scanning")
# ----------------------------------------------------------------
# 以上偉反了介面隔離原則
# 這段程式碼違反了 ISP，因為不是所有的機器都需要實現fax和scan方法
# ----------------------------------------------------------------

class Printer:
    def print(self, document):
        pass


class Fax:
    def fax(self, document):
        pass


class Scanner:
    def scan(self, document):
        pass


class MutiFunctionDevice(Printer, Fax, Scanner):
    def print(self, document):
        print("Printing")

    def fax(self, document):
        print("Faxing")
    def scan(self, document):
        print("Scanning")


