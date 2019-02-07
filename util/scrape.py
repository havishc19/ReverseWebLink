from urllib2 import urlopen
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self):
        self.startUrl = "https://quantsoftware.gatech.edu/Machine_Learning_for_Trading_Course"
        self.graph = {}
        self.visited = {}
        self.queue = []

    def scrape(self):
        iterations = 0
        self.queue.append(self.startUrl)
        while(len(self.queue) > 0):
            iterations = iterations + 1
            print(iterations)
            if(iterations > 200):
                break
            currUrl = self.queue[0]
            # print(currUrl)
            self.visited[currUrl] = 1
            self.queue = self.queue[1:]
            try:
                html = urlopen(currUrl)
            except:
                # print("Faulty", currUrl)
                pass
            soup = BeautifulSoup(html, 'lxml')
            title = soup.title
            text = soup.get_text()
            all_links = soup.find_all("a")
            for link in all_links:
                tempLink = link.get("href")
                try:
                    if(tempLink[:4] == "http"):
                        try:
                            temp = self.visited[tempLink]
                        except:
                            #Not Visited
                            try:
                                self.graph[currUrl].append(tempLink)
                            except:
                                self.graph[currUrl] = [tempLink]
                            self.queue.append(tempLink)
                except:
                    pass
        f = open("webLink.tsv","w")
        for key in self.graph:
            print(key, len(self.graph[key]))
            for val in self.graph[key]:
                try:
                    f.write(key+"\t"+val+"\n")
                except:
                    print("Err", key,val)
        f.close()
        


if __name__ == "__main__":
    scraper = Scraper()
    scraper.scrape()

# 23280673899423

# 23280673899423

# 23280674390288

# 23280674390288
