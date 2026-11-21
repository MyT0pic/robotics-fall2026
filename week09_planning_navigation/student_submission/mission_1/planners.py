"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    # Frontier is a queue
    frontier = deque([ctx.start])
    parent = {ctx.start: None}

    # Case where either endpoint is a wall cell
    if(ctx.grid[ctx.start[0]][ctx.start[1]] == 1 or ctx.grid[ctx.goal[0]][ctx.goal[1]] == 1):
        return []

    # Case where start = goal; no need to expand
    if(ctx.start == ctx.goal):
        return [ctx.start]

    # While there's still candidates
    while len(frontier) > 0:

        # Getting and removing the next cell from the queue
        current = frontier.popleft()

        # nxt is a legal (row, column) neighbor
        for nxt in ctx.expand(current, len(frontier) + 1):

            # Skips discovered cells
            if nxt in parent:
                continue
        
            # Record the parent cell for undiscovered cell
            parent[nxt] = current

            # Add to the frontier/queue
            frontier.append(nxt)

            # Stop when goal is discovered
            if nxt == ctx.goal:
                return reconstruct(parent, ctx.goal)

    # Return empty route
    return []
        




def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    # Frontier is a stack
    frontier = [ctx.start]
    parent = {ctx.start: None}

    # Case where either endpoint is a wall cell
    if(ctx.grid[ctx.start[0]][ctx.start[1]] == 1 or ctx.grid[ctx.goal[0]][ctx.goal[1]] == 1):
        return []

    # Case where start = goal; no need to expand
    if(ctx.start == ctx.goal):
        return [ctx.start]

    # While there's still candidates
    while len(frontier) > 0:

        # Getting and removing the most recent cell from the stack
        current = frontier.pop()

        # nxt is a legal (row, column) neighbor
        for nxt in ctx.expand(current, len(frontier) + 1):

            # Skips discovered cells
            if nxt in parent:
                continue
        
            # Record the parent cell for undiscovered cell
            parent[nxt] = current

            # Add to the frontier/stack
            frontier.append(nxt)

            # Stop when goal is discovered
            if nxt == ctx.goal:
                return reconstruct(parent, ctx.goal)

    # Return empty route
    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    depth_count = 0

    # Case where either endpoint is a wall cell
    if(ctx.grid[ctx.start[0]][ctx.start[1]] == 1 or ctx.grid[ctx.goal[0]][ctx.goal[1]] == 1):
        return []

    # Case where start = goal; no need to expand
    if(ctx.start == ctx.goal):
        return [ctx.start]
    
    # Runner will handle the resouce limit
    while depth_count < len(ctx.grid[0]) + len(ctx.grid):
    
        # New set of parents with each increasing depth
        parent = {ctx.start: None}
        # Frontier is a stack
        frontier = [ctx.start]

        # While there's still candidates
        while len(frontier) > 0:
        
            # Getting and removing the most recent cell from the stack
            current = frontier.pop()

            # nxt is a legal (row, column) neighbor
            for nxt in ctx.expand(current, len(frontier) + 1):

                # Skips discovered cells
                if nxt in parent:
                    continue
                # Skips cells longer than the depth level
                elif (abs(ctx.start[0] - current[0]) + abs((ctx.start[1] - current[1])) > depth_count):
                    continue
        
                # Record the parent cell for undiscovered cell
                parent[nxt] = current

                # Add to the frontier/stack
                frontier.append(nxt)

                # Stop when goal is discovered
                if nxt == ctx.goal:
                    return reconstruct(parent, ctx.goal)
        

        # Incrementing the next depth level
        depth_count+=1
    
    
    # Return empty route
    return []


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    # Frontier is a priority heap
    frontier = []
    heappush(frontier, (0 + ctx.heuristic(ctx.start), 0, ctx.start))
    parent = {ctx.start: None}
    lowest_g = 0

    # Case where either endpoint is a wall cell
    if(ctx.grid[ctx.start[0]][ctx.start[1]] == 1 or ctx.grid[ctx.goal[0]][ctx.goal[1]] == 1):
        return []

    # Case where start = goal; no need to expand
    if(ctx.start == ctx.goal):
        return [ctx.start]

    # While there's still candidates
    while len(frontier) > 0:

            # Getting and removing the most recent cell from the top of min-heap
            priority, g_cost, current = frontier.heappop()

            # Stop when goal is discovered
            if current == ctx.goal:
                return reconstruct(parent, ctx.goal)

            # nxt is a legal (row, column) neighbor
            for nxt in ctx.expand(current, len(frontier) + 1):

                # New best g_cost
                if(g_cost + 1 < lowest_g):
                {
                    lowest_g = g_cost + 1

                    # Record the parent cell for undiscovered cell
                    parent[nxt] = current

                    # Add to the frontier/min-heap
                    frontier.heappush(frontier, (lowest_g + ctx.heuristic(current), lowest_g, nxt))
                }

# Return empty route
return []
