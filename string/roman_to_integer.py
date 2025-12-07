# A Roman numeral year string is converted into an integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        iv = 0
        letter = 0
        temp_iv = 0
        for letter in range(len(s)-1):
            if rom_dict[s[letter]] < rom_dict[s[letter+1]]:
                iv -= rom_dict[s[letter]]
            else:
                iv += rom_dict[s[letter]]
        iv += rom_dict[s[-1]]
        return iv
