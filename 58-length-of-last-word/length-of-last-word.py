class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        point = len(s) -1
        word = ""

        for i in range(len(s) - 1, -1, -1):
            if s[point] != " ":
                word += s[point]
                point -= 1
            elif s[point] == " ":
                break
        return len(word)
