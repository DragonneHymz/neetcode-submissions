class TrieNode():
    def __init__(self):
        self.word = None
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def addword(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = word
    
    def dfs(self,r,c,node,board,found):
            #base case check bounds and if marked or not in children
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or board[r][c] == "#" or board[r][c] not in node.children:
                return
            
            #move to node
            char = board[r][c]
            node = node.children[char]

            #if found, add to found and remove word
            if node.word:
                found.append(node.word)
                node.word = None
            
            #mark board as checked
            board[r][c] = "#"
            
            #check all four directions
            self.dfs(r-1,c,node,board,found)
            self.dfs(r+1,c,node,board,found)
            self.dfs(r,c-1,node,board,found)
            self.dfs(r,c+1,node,board,found)

            #remove mark for backtracking
            board[r][c] = char


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #add word list into trie
        trie = Trie()
        for word in words:
            trie.addword(word)

        found = []
        #search the list
        for r in range(len(board)):
            for c in range(len(board[r])):
                trie.dfs(r,c,trie.root,board,found)

        #return found
        return found