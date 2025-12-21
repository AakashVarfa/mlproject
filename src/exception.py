import sys
from src.logger import logging


def error_message_detail(error: Exception, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in Python script [{file_name}] "
        f"at line [{line_number}] "
        f"with message [{error}]"
    )


class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message



# def main():
#     try:
#         a = 1 / 0  # test error
#     except Exception as e:
#         logging.error(error_message_detail(e, sys))
#         raise CustomException(e, sys)


# if __name__ == "__main__":
#     try:
#         main()
#     except CustomException as ce:
#         print(ce)
#         logging.info("divide by zero exception caught in main")
