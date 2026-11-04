class Twitter:

    def __init__(self):
        self.time = 0
        self.user = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.user.get(userId):
            self.user[userId] = []
        self.user[userId].append([self.time,tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        minHeap = []
        for followee in self.following[userId]:
            if followee in self.user:
                for p in self.user[followee]:
                    heapq.heappush(minHeap, p)
                    if len(minHeap) > 10:
                        heapq.heappop(minHeap)
        result = []
        while minHeap:
            result.append(heapq.heappop(minHeap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.following.get(followerId):
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following.get(followerId):
            self.following[followerId].remove(followeeId)
