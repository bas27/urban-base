from threading import Thread
import requests


class Getter(Thread):

    res = []

    def __init__(self, url):
        self.url = url
        super().__init__()

    def run(self):
        response = requests.get(self.url)
        Getter.res.append(response.json())

threads = []
num_genres = 5

for i in range(num_genres):
    thread = Getter('https://binaryjazz.us/wp-json/genrenator/v1/genre/')
    thread.start()
    threads.append(thread)


for t in threads:
    t.join()

print(Getter.res)
assert len(Getter.res) == num_genres
# g = Getter()
# g.start()