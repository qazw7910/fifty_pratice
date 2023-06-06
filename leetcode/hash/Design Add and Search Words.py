import collections


class WordDictionary:
    def __init__(self):
        self.word_dict = collections.defaultdict(set)

    def add_word(self, word) -> None:
        self.word_dict[len(word)].add(word)

    def search_word(self, search_word: str) -> bool:
        if "." not in search_word:
            return search_word in self.word_dict[len(search_word)]

        for word in self.word_dict[len(search_word)]:
            for idx, char in enumerate(search_word):
                match = True
                if char != word[idx] and char != ".":
                    match = False
                    break
            if match :
                return True
        return False



if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    # ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
    # [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
    obj = WordDictionary()
    obj.add_word("bad")
    obj.add_word("mad")
    param_2 = obj.search_word("m..")
    param_3 = obj.search_word(".j.")
    print(param_3)
