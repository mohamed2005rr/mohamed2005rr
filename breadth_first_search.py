from collections import deque

# =========================
# 1) تعريف الجراف
# =========================
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'E': ['G', 'H']
}

# =========================
# 2) BFS Function
# =========================
def bfs(start, goal):

    # queue = FIFO = First In First Out
    queue = deque([start])

    # visited لتجنب التكرار
    visited = []

    print("Traversal Order (BFS):")

    # =========================
    # 3) Loop الرئيسي
    # =========================
    while queue:

        # نخرج أول عنصر
        node = queue.popleft()

        # لو مش زرناه قبل كده
        if node not in visited:

            visited.append(node)

            # طباعة الزيارة
            print(node, end=" ")

            # لو وصلنا الهدف
            if node == goal:
                print("\n\nGoal Found!")
                return

            # جلب الجيران
            for neighbor in graph.get(node, []):

                if neighbor not in visited:
                    queue.append(neighbor)

    print("\nGoal Not Found")


# =========================
# 4) تشغيل الخوارزمية
# =========================
bfs('S', 'G')