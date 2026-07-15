# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.queue = []

    # Add element to the rear
    def push(self, item):
        self.queue.append(item)

    # Remove element from the front
    def pop(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue.pop(0)

    # Return front element
    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    # Return rear element
    def rear(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[-1]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Return size of queue
    def size(self):
        return len(self.queue)

    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue:", self.queue)
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if root == None:
            return ans
        
        queue = Queue()

        queue.push(root)
        ans.append([root.val])

        while queue.size() > 0:
            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)
                
            if len(level) > 0:
                ans.append(level)

        ans.reverse()
        return ans