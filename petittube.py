import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time

class petittube:
    def __init__(self, iterations):
        self.iterations = iterations
    def get_random_video(self):
        req = requests.get("https://petittube.com/")
        if req.status_code == 200:
            source = req.text
            bs = BeautifulSoup(source, 'html.parser')
            iframe = bs.select('iframe')
            return iframe[0]['src']
        else:
            raise Exception("Unable to connect to petittube.com, check your Internet connection.")                

    def petittube(self):
        result = []
        for i in range(self.iterations):
            result.append(self.get_random_video())
        return result

    def petittube_multithreaded(self, max_workers=5, sleep=1):
        def aux(sleep=sleep):
            time.sleep(sleep)
            return self.get_random_video()
        result = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(aux) for _ in range(self.iterations)]
            for future in futures:
                result.append(future.result())
        return result

def format(link):
    link = link.split('?')[0]
    link = link.split('/')
    watchcode = link[len(link)-1]
    result = "https://www.youtube.com/watch?v=" + watchcode
    return result

if __name__ == "__main__":
    tube = petittube(30)
    for link in tube.petittube():
        print(format(link))
    # for link in tube.petittube_multithreaded(5,2):
    #     print(link)
    
