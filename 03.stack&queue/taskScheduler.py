# Taks Scheduler.py
# https://leetcode.com/problems/task-scheduler

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        task_counts = Counter(tasks).values()
        max_v = max(task_counts)
        max_c = task_counts.count(max_v)
        count = 0
        
        res = (max_v-1)*(n+1) + max_c
        
        return max(res, len(tasks))
