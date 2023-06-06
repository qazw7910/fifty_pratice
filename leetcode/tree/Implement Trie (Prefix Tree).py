class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie1:

    def __init__(self):
        self.trie_root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.trie_root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.trie_root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie_root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


class Trie2:
    def __init__(self):
        self.trie_root = {}
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self.trie_root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur[self.is_word] = True

    def search(self, word: str) -> bool:
        cur = self.trie_root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return True if self.is_word in cur else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie_root
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    # ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    # [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    obj = Trie2()
    obj.insert("apple")
    param_2 = obj.search("apple")
    param_3 = obj.startsWith("app")
    print(param_3)
