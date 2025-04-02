import sys
import logging

# Configure logging
logging.basicConfig(
    filename="error.log",
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def format_error(error, error_detail: sys):
    """Formats the error message with filename and line number."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in file [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Log the error
    logging.error(error_message)

    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        """Custom Exception class that formats and logs errors."""
        super().__init__(str(error))
        self.error_message = format_error(error, error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will cause ZeroDivisionError
    except Exception as e:
        logging.info("An error occurred")
        raise CustomException(e, sys)