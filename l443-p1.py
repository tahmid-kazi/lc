class Solution:
    def compress(self, chars: List[str]) -> int:
        # 11/21/24) Thurs) 145-203pm) tk) 1st problem of the day
        # you have to modify the chars in place (two pointers, fast and slow)
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
            
            if count > 1: #now add the count next to the char
                for c in str(count):
                    chars[write] = c
                    write += 1
        # while the resultant chars array will have stray chars on the end, it doesnt matter because we only care about the char count of the compressed string. if you wanted to return the compressed string you can also just do chars[0:write]
        return write 