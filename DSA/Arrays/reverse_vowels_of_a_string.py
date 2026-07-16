class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:

            if s[p1].lower() not in "aeiou":
                p1 += 1

            elif s[p2].lower() not in "aeiou":
                p2 -= 1

            else:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1

        return "".join(s)
