class Trie:

    def __init__(self):
        self.root=defaultdict(Trie)
        self.isWord=False
        
    def insert(self, word: str) -> None:
        cur=self
        for w in word:
            cur=cur.root[w]
        cur.isWord=True
        

    def search(self, word: str) -> bool:
        cur=self
        for w in word:
            if w not in cur.root:
                return False
            cur=cur.root[w]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur=self
        for w in prefix:
            if w not in cur.root:
                return False
            cur=cur.root[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)