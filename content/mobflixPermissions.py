import requests
import datetime
from .models import *
API_URL="http://netpap.co.ke"
class LocalPermissionClass:
    def checkIfWatcher(self,code):

        w=Watchers.objects.filter(unique_code=code)
        if w.exists():
            return w
        else:
            return False
    def checkExpiry(self,w):
        current_tym=datetime.datetime.now()

        w=w.filter(code_expiration__gt=current_tym)
        if w.exists():
            return True #still active
        else:
            return False

    def storeLocal(self,code,expiration_date):
        expiration_date=datetime.datetime.strptime(expiration_date,"%Y-%m-%dT%H:%M:%SZ")

        w=Watchers()
        w.unique_code=code
        w.code_expiration=datetime.datetime.strftime(expiration_date,"%Y-%m-%d %H:%M")
        w.save()
        return True

class RemotePermissionClass:


    def verify_code(self,code):

        r=requests.get(API_URL+"/mobflix/code/search/"+code)
        print r.text
        a=r.json()
        if "success" in a['status']:
            LocalPermissionClass().storeLocal(code,a['message']['expire_date'])
            return a
        else:
            return a
