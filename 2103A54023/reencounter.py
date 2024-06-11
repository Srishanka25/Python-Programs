class RecentCounter:
    def __init__(self):
        self.request = collection.deque()

    def ping(self, t):
        while self.request and t -self.request[0] > 3000:
            self.request.popleft()
        self.request.append(t)
        return len(self.request)
