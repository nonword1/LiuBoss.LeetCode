class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        while x != 0 or y !=0:
            x,resx = x //2, x%2
            y,resy = y//2, y%2
            if resx!= resy:
                dis +=1
        return dis

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
