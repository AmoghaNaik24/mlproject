import sys
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in Python script [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    def _init_(self, error_message, error_detail: sys):
        super()._init_(error_message)  # ✅ Correct use of super()
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def _str_(self):
        return self.error_message