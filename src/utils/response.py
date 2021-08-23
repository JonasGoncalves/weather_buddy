class Response:
    """
    Class responsible for endpoints responses
    """

    def success(self, message: str, data='Done'):
        status_code = 200
        response = {'data': data, 'message': message, 'code': status_code, 'success': True}
        print(response)
        return response, status_code

    def failed(self, message: str):
        status_code = 400
        response = {'message': message, 'code': status_code, 'success': False}
        print(response)
        return response, status_code

    def unauthorized(self, message: str):
        status_code = 401
        response = {'message': message, 'code': status_code, 'success': True}
        print(response)
        return response, status_code

    def not_found(self, message: str, data=None):
        status_code = 404
        response = {'data': data, 'message': message, 'code': status_code, 'success': True}
        print(response)
        return response, status_code

    def conflict(self, message: str):
        status_code = 409
        response = {'message': message, 'code': status_code, 'success': True}
        print(response)
        return response, status_code

    def internal_error(self, message: str):
        status_code = 500
        response = {'message': message, 'code': status_code, 'success': False}
        print(response)
        return response, status_code

    def custom(self, message: str, status_code: int, success: bool):
        response = {'message': message, 'code': status_code, 'success': success}
        print(response)
        return response, status_code
