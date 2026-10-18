class Twitter:
    import heapq
    def __init__(self):
        self.posts = dict()
        self.follows = dict()
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = list()
        self.posts[userId].append((self.clock, tweetId))
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []
        ans = []
        ptr = dict()
        if userId in self.posts and len(self.posts[userId])>0:
            ptr[userId]=len(self.posts[userId])-1
            heapq.heappush_max(pq, (self.posts[userId][ptr[userId]], userId))
        for following in self.follows.get(userId,set()):
            if following in self.posts and len(self.posts[following])>0:
                ptr[following]=len(self.posts[following])-1
                heapq.heappush_max(pq, (self.posts[following][ptr[following]], following))
        for _ in range(10):
            if pq is None or len(pq)==0:
                break
            post, candidate = heapq.heappop_max(pq)
            ans.append(post[1])
            ptr[candidate]=ptr[candidate]-1
            if ptr[candidate]>=0:
                heapq.heappush_max(pq, (self.posts[candidate][ptr[candidate]], candidate))
        return ans

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
 
        
