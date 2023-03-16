class NoElementsInVersionControl(Exception):
    def __init__(self):
        self.message = 'No versions present. Please create version. Path to create in Postman: ' \
                       'POST: http://127.0.0.1:8000/'

    def __str__(self):
        return self.message
