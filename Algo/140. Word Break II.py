class Node:
    def __init__(self):
        self.isTerminal = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
        node.isTerminal = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        t = Trie()
        for w in wordDict:
            t.insert(w)
        
        dp = dict()

        for start in range(len(s) - 1, -1, -1):
            valid_sentences = []

            node = t.root

            for end in range(start, len(s)):
                c = s[end]
                idx = ord(c) - ord('a')
                if not node.children[idx]:
                    break
                
                node = node.children[idx]
                if node.isTerminal:
                    word = s[start: end + 1]

                    if end == len(s) - 1:
                        valid_sentences.append(word)
                    else:
                        sentences_from_next_index = dp.get(end + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(
                                word + ' ' + sentence
                            )

            dp[start] = valid_sentences

        return dp.get(0, [])
