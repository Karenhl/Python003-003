class InputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo


userinput = 'a'

try:
    if not (userinput.isdigit()):
        raise InputError('不是数字')
except InputError as e:
    print(e)
finally:
    del userinput