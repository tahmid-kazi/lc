class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = sentence.split()
        # 11/21/24) Thurs) 339-347pm) tk) figured it out by myself and got it right the first try!!
        for k in range(len(words)):
            if words[k][0].lower() in vowels: #linear search O(n)
                words[k] = words[k] + "ma" + 'a'*(k+1) 
            else:
                words[k] = words[k][1:] + words[k][0] + "ma" + 'a'*(k+1)
        
        return " ".join(words)