# multiprocessing is a in-built module which helps in Multi-Threading.
import multiprocessing
import requests
import time

def downloadFile(url , name):
    response = requests.get(url)
    with open(f"files/file{name}_{int(time.time())}.jpg" , "wb") as f:
        f.write(response.content)

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"

    pros = []

    for i in range(5):
        # downloadFile(url , i)
        download = multiprocessing.Process(target=downloadFile , args=[url , i])
        download.start()
        pros.append(download)

    for download in pros:
        download.join()

