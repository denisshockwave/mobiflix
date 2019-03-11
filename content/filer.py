import os,pathlib, threading

from .models import *
from django.conf import settings
from .ErrorLogger import *
error=ErrorLogger()

class Crawler:

    
    def all_files(self,directory):
        for path, dirs, files in os.walk(directory):
            for f in files:
                yield os.path.join(path, f)

    
    def begin(self, dir):
        #check if app is allowed to upload from directory
        # if not self.checkUploadFromDirectoryPermissions(file_path):
        #     #store Error in errors table in database
        #     error.storeError({"name":"UPLOAD DIRECTORY PERMISSION","message":"App does not have permissions to read directory"})
        if not self.checkIfCorrectDirectory(dir):
            error.storeError({"name": "INCORRECT DIRECTORY",
                              "message": "You have entered the incorrect url with content to crawl"})


        video_files = [f for f in self.all_files(dir)
            if f.endswith(('.mp4', '.flv', '.avi', '.mov', '.wmv', '.MP4', '.mkv'))]
        c=Content.objects.all()
        print (video_files)
        for file in video_files:
            # Convert file-names to urls
            file_url = pathlib.Path(file).as_uri().split("/media/uploads")
            try:
                rel_url = "/uploads" + file_url[1]
            except:
                error.storeError({"name": "UNEXPECTED URL.",
                                  "message": "The was a problem "+file_url})
                return False


            print (rel_url)
            if not self.checkIfUrlIndexBefore(c, rel_url):
                #storeUrl in content database
                print ("store url")
                
                self.storeUrl(rel_url)
            else:
                #Skip
                continue

    
    
    def checkIfUrlIndexBefore(self,c,url):
        #check if url exists in database
        print ("URL BEING ANALYZED")
        print (url)
        u = c.filter(video_url=url)
        if u.exists():
            print ("TRUE")
            return True
        else:
            print("fALSE")
            return False

    
    def storeUrl(self,url):
        #check if url exists in database
       c = Content()
       c.video_url=url
       c.name=self.getName(url)
       c.save()
    def getName(self,url):
        u=url.split("/")
        print (u)
        return  u[2].replace(".","_")

    # 
    # def checkUploadFromDirectoryPermissions(self,file_path):
    #     pass
    
    
    def checkIfCorrectDirectory(self,file_path):
        correct = settings.MEDIA_ROOT + '/uploads'

        print (correct)
        print  (file_path)
        if correct == file_path:
            return True
        else:
            return False


class ThreadingDaemon(object):
    """ 
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, dir="/media"):
        """ Constructor
       
        """
        
        self.dir = dir

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        Crawler().begin(self.dir) 



