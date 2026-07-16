class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)          # Convert string to list (strings are immutable)

        start = 0
        n = len(s)

        for end in range(n + 1):

            # End of a word
            if end == n or s[end] == ' ':
                left = start
                right = end - 1

                # Reverse the current word
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1

                start = end + 1

        return "".join(s)
