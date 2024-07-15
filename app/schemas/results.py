class Result:
    def __init__(self, success: bool, message: str = None):
        self.success = success
        self.message = message

class SuccessResult(Result):
    def __init__(self, message: str = None):
        super().__init__(True, message)

class DataResult(Result):
    def __init__(self, data, success: bool, message: str = None):
        super().__init__(success, message)
        self.data = data

class SuccessDataResult(DataResult):
    def __init__(self, data=None, message: str = None):
        super().__init__(data, True, message)

class ErrorResult(Result):
    def __init__(self, message: str = None):
        super().__init__(False, message)

class ErrorDataResult(DataResult):
    def __init__(self, data=None, message: str = None):
        super().__init__(data, False, message)