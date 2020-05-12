import os
import requests
import threading
from time import time

print(os.getpid())

print(os.getloadavg())

load1,load5,load15 = os.getloadavg()
print("5 minute loadavg: " , load5)
print(os.cpu_count())

if os.cpu_count() - load5 < 1:
    exit()

urls = ["​https://api.github.com​", "http://bilgisayar.mu.edu.tr/​","https://www.python.org/​", 
        "http://akrepnalan.com/ceng2034​","https://github.com/caesarsalad/wow​"]

def checkUrl(url,startTime):
    request_status_code = requests.get(url.encode("ascii","ignore")).status_code
    if request_status_code == 200:
        print(url, "url is valid.")
    else:
        print(url, "url is not valid.Status code:",request_status_code) 
    elapsed_time = time() - startTime
    print("Finished in:{:.2f} seconds".format(elapsed_time))

for url in urls:
    threading.Thread(target=checkUrl,args=(url,time())).start()

# for url in urls:
#     startTime = time()
#     request_status_code = requests.get(url.encode("ascii","ignore")).status_code
#     if request_status_code == 200:
#         print(url, "url is valid.")
#     else:
#         print(url, "url is not valid.Status code:",request_status_code) 
#     elapsed_time = time() - startTime
#     print("Finished in:{:.2f} seconds".format(elapsed_time))

