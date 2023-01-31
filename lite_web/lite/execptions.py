class NotElementsInVersionControl(Exception):
    def __init__(self):
        self.message = 'Not versions. Please create version. Path for create in Postman: POST: http://127.0.0.1:8000/'

    def __str__(self):
        return self.message
