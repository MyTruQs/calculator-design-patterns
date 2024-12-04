# 400 -> Bad Request
# 422 -> Unprocessable Entity

class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
        
try:
    print('Estou no bloco try')
    raise HttpUnprocessableEntityError('Estou lançando a exception')
except Exception as exception:
    print('Estou no tratamento de erro')
    print(exception.message)
    print(exception.name)
    print(exception.status_code)