# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
    
        if not asteroids : return asteroids
        ret = []
        for a in asteroids :
            while ret and a < 0 < ret[-1] :
                if a + ret[-1] < 0 :
                    ret.pop()
                    continue
                elif a + ret[-1] == 0 :
                    ret.pop()
                break
            else :
                ret.append(a)
                
        return ret
        
