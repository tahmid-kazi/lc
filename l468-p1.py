class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # 1010 to 1057pm) 11/9/24) Sat) tk)
        # first determine if its an IPv4 or an IPv6 string that you're splitting
        is_ipv4 = True if "." in queryIP else False

        #now determine if the string is valid by string splitting
        if is_ipv4:
            #IPv4 checks
            ip_split = queryIP.split(".") # this splits it into an array of substr
            if len(ip_split) != 4: # 1st check
                return "Neither"
            for j in ip_split: 
                if j == "": return "Neither" # 2nd check
                #check for leading zeros (3rd check)
                if len(j)>1 and j[0] == "0":
                    return "Neither"
                for k in j: #check for any goofy characters (4th check)
                    if not k.isdigit():
                        return "Neither"
                if int(j) > 255: # 5th check
                    return "Neither"
            return "IPv4"
        
        else:
            #IPv6 checks
                #check for leading zeros
            ip_split = queryIP.split(":")
            if len(ip_split) != 8: # 1st check
                return "Neither"
            for j in ip_split: 
                if j == "": return "Neither" # 2nd check
                if len(j) > 4: return "Neither" # 3rd check
                for k in j:
                    if not (k.isdigit() or k.lower() in 'abcdef'):  # 4th check: valid hex digits
                        return "Neither"

        #then return the IPv4 or IPv6 status msg
            return "IPv6"