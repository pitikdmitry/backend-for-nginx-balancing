from time import sleep


STATUS_CODE = {
    'OK': 200,
    'CREATED': 201,
    'NOT_FOUND': 404,
    'CONFLICT': 409
}


class UsersRepository:

    def __init__(self):
        pass

    def create(self, data):
        sleep(0.5)
        return STATUS_CODE['OK']
