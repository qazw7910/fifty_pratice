# class Logger:
#     def log(self, message):
#         print(f"Log: {message}")
#
#
# class UserService:
#     def __init__(self):
#         self.logger = Logger()
#
#     def register(self, username, password):
#         try:
#             print(f"User {username} registered successfully")
#             self.logger.log(f"User {username} registered successfully")
#         except Exception as e:
#             print(f"Error: {e}")
#             self.logger.log(f"Error: {e}")
# ----------------------------------------------------------------
# 在這個例子中，UserService直接創建Logger物件。這個設計違反了依賴反轉原則，因為UserService的高層次模組直接依賴Logger這個低層次模組。
#
# 以下為修復過後的範例：
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Log: {message}")


class UserService:
    def __init__(self, logger=Logger):
        self.logger = logger

    def register(self, name, password):
        try:
            print(f"User {name} registered successfully")
            self.logger.log(f"User {name} registered successfully")
        except Exception as e:
            print(f"Error: {e}")
            self.logger.log(f"Error: {e}")


if __name__ == "__main__":
    logger = ConsoleLogger()
    service = UserService(logger)
    service.register('ray', 'gd')