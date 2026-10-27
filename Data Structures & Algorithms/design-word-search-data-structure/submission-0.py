class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                return False

            if char in node.children:
                return dfs(node.children[char], index+1)
            return False
        return dfs(self.root, 0)
    
        
