from collections import deque
class RecentCounter:
    def __init__(self) -> None:
        self.queue = deque()
        
    def ping(self,t):
        while self.queue and self.queue[0] < t-3000:
            self.queue.popleft
        return len(self.queue)