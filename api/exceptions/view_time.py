from starlette import status

from api.exceptions.api_exception import APIException

class DataFetchError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Failed to fetch task data"
    description = "Failed to fetch task data from the database"

class UnexpectedDataStructure(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Unexpected data structure"
    description = "The data structure returned from the database was not as expected"