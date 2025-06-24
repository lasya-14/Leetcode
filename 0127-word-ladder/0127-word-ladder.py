class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dic=collections.defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pat=w[:i]+"*"+w[i+1: ]
                dic[pat].append(w)
        queue=deque([beginWord])
        visited=set([beginWord])
        count=1
        while queue:
            n=len(queue)
            for i in range(n):
                curr=queue.popleft()
                if curr==endWord:
                    return count
                for j in range(len(curr)):
                    pattern=curr[:j]+"*"+curr[j+1:]
                    for k in dic[pattern]:
                        if k not in visited:
                            visited.add(k)
                            queue.append(k)
            count+=1
        return 0
        