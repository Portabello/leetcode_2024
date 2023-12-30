"""
225. Implement Stack using Queues
Easy
5.8K
1.2K
Companies
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
"""
class MyStack:
    #stack = []
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = [x] + self.stack
        print("push", self.stack)

    def pop(self) -> int:
        if(isinstance(self.stack, int)):
            tmp = self.stack
            self.stack = None
            print("popa", self.stack)
            return tmp
        print("popb1", self.stack)
        first_elem = self.stack[0]
        self.stack.pop(0)
        print("popb2", self.stack)
        return first_elem


    def top(self) -> int:
        #print(self.stack)
        if(len(self.stack)!=0):
            return self.stack[0]
        else:
            return -1

    def empty(self) -> bool:
        print(self.stack)
        if not self.stack:
            print("empty1")
            return True
        if(isinstance(self.stack, int)):
            print("empty2")
            return False
        if len(self.stack) == 0:
            print("empty3")
            return True
        print("empty4")
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()