#code to calculate longest substring in a string

class solution:

    def longeststr(self,s):
        n=len(s)
        maxlenght=0
        charset=set()
        left=0

        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                maxlenght=max(maxlenght,right-left+1)

            else:
                while s[right] in charset:
                   charset.remove(s[left])
                   left+=1
                charset.add(s[right])

        return maxlenght

def main():

    s='abcabcbb'
    sol=solution()
    result=sol.longeststr(s)
    print(result)

main()

