import requests
import datetime
from .models import *
API_URL="https://account.netpap.co.ke"
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
    def checkCount(self,w):
        print(w[0].paid_count)
        print(w[0].count)
        if  w[0].count>=w[0].paid_count:
            return False
        else:
            return True
    def storeLocal(self,code,expiration_date,count):
 
   

        expiration_date=datetime.datetime.strptime(expiration_date,"%Y-%m-%d %H:%M:%S")
   

        w=Watchers()
        w.unique_code=code
        w.paid_count=count
        w.code_expiration = expiration_date
        w.save()
        return True

class RemotePermissionClass:


    def verify_code(self,code):

        r=requests.get(API_URL+"/mobflix/code/search/"+code)

        a=r.json()
        if "success" in a['status']:
            LocalPermissionClass().storeLocal(code,a['message']['expire_date'],a['message']['paid_count'])
            print(a)
            print ("successful")
            return a
        else:
            print ("Not successful")
            print(a)
            print("remote")
            return a
