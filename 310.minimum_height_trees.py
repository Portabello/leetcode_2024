'''
310. Minimum Height Trees
Attempted
Medium
Topics
Companies
Hint

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]



Constraints:

    1 <= n <= 2 * 104
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    All the pairs (ai, bi) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.

'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        hs = {}
        for x in edges:
            if x[0] in hs:
                hs[x[0]].append(x[1])
            else:
                hs[x[0]] = [x[1]]
            if x[1] in hs:
                hs[x[1]].append(x[0])
            else:
                hs[x[1]] = [x[0]]
        #print(hs)


        min_dist = [float('inf')]

        def findPathDistance(node, target, edges, visited, dist):
            #print(node, visited, dist)
            cur_node = node
            if cur_node == target:
                min_dist[0] = min(min_dist[0], dist)

            #for edge in edges:
            #    if edge not in visited and cur_node in edge:
            #        t = edge[::]
            #        t.remove(cur_node)
            #        new_visited = visited + [edge]
            #        findPathDistance(t[0], target, edges, new_visited, dist+1)

            edge = hs[cur_node]
            for j in edge:
                if j not in visited:
                    new_visited = visited + [j]
                    findPathDistance(j, target, edges, new_visited, dist+1)
        '''
        def findPathDistance(node, target, edges, visited, dist):
            from collections import deque
            queue = deque([(node, 0)])
            visited = set([node])
            while queue:
                cur_node, cur_dist = queue.popleft()
                if cur_node == target:
                    min_dist[0] = min(min_dist[0], cur_dist)
                    return
                for neighbor in hs.get(cur_node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, cur_dist + 1))
        '''
        #findPathDistance(0,3,edges,[],0)
        #print(min_dist)
        min_spanning_tree = float('inf')
        min_spanning_tree_root = []
        #check each node as root
        for node in range(n):
            #for each node as root
            #iterate through all the distances to other nodes and find the max
            max_tree_len = 0
            for target in range(n):
                #reset min_dist global
                min_dist[0] = float('inf')

                if target != node:
                    findPathDistance(node,target,edges,[],0)
                    max_tree_len = max(max_tree_len, min_dist[0])
            if max_tree_len == min_spanning_tree:
                min_spanning_tree_root.append(node)
            elif max_tree_len < min_spanning_tree:
                min_spanning_tree = max_tree_len
                min_spanning_tree_root = [node]
        return min_spanning_tree_root
