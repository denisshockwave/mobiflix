from .models import *

class ErrorLogger:
    def storeError(self,payload):
        e=ErrorLog()
        e.name=payload['name']
        e.message=payload['message']
        e.save()
