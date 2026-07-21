from datetime import datetime


class Sentence:
    """Counts words in a sentence by scanning character by character.

    A "word" ends where a non-space character is either the last
    character of the string, or is immediately followed by a space.
    """

    def __init__(self, sent):
        self.sent = sent

    def __str__(self):
        return f"{self.sent} -> {self.count_words()} words"

    def count_words(self):
        s = self.sent
        k = 0
        for i in range(len(s)):
            # A word ends at position i if:
            #   - s[i] is not a space (we're standing on a letter), AND
            #   - either this is the very last character of the string,
            #     or the next character is a space.
            #
            # Order matters here because of short-circuit evaluation:
            # `i == len(s) - 1` is checked FIRST because it's always safe
            # (just comparing two integers). Only if it's False does Python
            # move on to `s[i+1] == " "`. This guarantees s[i+1] is only
            # accessed when i is NOT the last index — so it can never
            # go out of range.
            #
            # If the order were reversed (s[i+1] first), Python would try
            # to read s[i+1] even when i is the last index, causing
            # IndexError: string index out of range.
            if s[i] != " " and (i == len(s) - 1 or s[i + 1] == " "):
                k += 1
        return k


print(f"=== Run: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
print(Sentence("Hello world from Python"))       # "Hello world from Python" -> 4 words
print(Sentence("   spaced    out   words  "))    # "   spaced    out   words  " -> 3 words
print(Sentence(""))                              # "" -> 0 words
print(Sentence("single"))                        # "single" -> 1 words