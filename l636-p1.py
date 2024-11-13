class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        #time1 = {} #stores {ID:total_time}
        
        # 11/13/24) Wed) 1127/1134am-1204pm) tk)
        arr = [0] * n # stores total time and the index is the task ID
        stack1 = []
        # first construct the stack
        for j in logs:
            id1, task, timestamp = j.split(":") # = [id, start/end, timestamp]
            id1, timestamp = int(id1), int(timestamp)

            if task == "start":
                if stack1:
                    arr[stack1[-1][0]] += timestamp - stack1[-1][1] 
                #push onto the stack
                stack1.append([id1, timestamp]) # store [id, timestamp]
            
            else:
                #pop off the stack
                done = stack1.pop()
                arr[done[0]] += timestamp - done[1] + 1
                if stack1: 
                    stack1[-1][1] = timestamp + 1 

        return arr