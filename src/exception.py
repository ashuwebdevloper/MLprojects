import sys 
##  provides various funstions to handle exception in a better way  

def error_message_detail(error,error_detail:sys):
    _,_,error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(error_detail[0].__name__,error_detail[2].tb_lineno,str(error))
    file_name,exc_tb.tb_lineo,str(error)


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)