import heapq
class DSU:
    def __init__(self, vertices):
        # เริ่มต้น, ทุกโหนดเป็น parent ของตัวเอง
        self.parent = {v: v for v in vertices}
        # ใช้สำหรับ Union by Rank เพื่อเพิ่มประสิทธิภาพ
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] == v:
            return v
        # Path Compression: ทำให้ทุกโหนดในทางชี้ไปยังรากโดยตรง
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by Rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                # ถ้ายศเท่ากัน, เลือกหนึ่งเป็นราก และเพิ่มยศ
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True  # คืนค่า True ถ้ารวมสำเร็จ
        return False # คืนค่า False ถ้าอยู่กลุ่มเดียวกันแล้ว (จะเกิด cycle)

# --- Main Graph Class ---
class Graph:
    def __init__(self):
        self.adj = {}
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v, weight=1, directed=False):
        self.vertices.add(u)
        self.vertices.add(v)

        # เพิ่ม u -> v
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, weight))

        if not directed:
            # ถ้าไม่มีทิศทาง, เพิ่ม v -> u ด้วย
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append((u, weight))
            
            # เพิ่มใน edge list (สำหรับ Kruskal) แค่ครั้งเดียว
            # เราเก็บ (weight, u, v)
            if (weight, v, u) not in self.edges:
                self.edges.append((weight, u, v))
        else:
            # ถ้ามีทิศทาง, Kruskal's จะใช้ไม่ได้
            # แต่เรายังเก็บข้อมูล adj list สำหรับ Dijkstra
            pass 

    # --- 1. Spanning Tree (DFS / BFS) ---

    def spanning_tree_dfs(self, start_node):
        """หา Spanning Tree ด้วย Depth-First Search"""
        print(f"--- Spanning Tree (DFS) starting from {start_node} ---")
        tree_edges = []
        visited = set()
        stack = [start_node] # ใช้ Stack สำหรับ DFS
        
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            
            if u in self.adj:
                # เพิ่มเพื่อนบ้านลง stack
                for v, weight in self.adj[u]:
                    if v not in visited:
                        # เพิ่มเส้นเชื่อมนี้เข้าต้นไม้
                        tree_edges.append((u, v))
                        stack.append(v)
        
        print(f"Edges: {tree_edges}")
        return tree_edges

    def spanning_tree_bfs(self, start_node):
        print(f"--- Spanning Tree (BFS) starting from {start_node} ---")
        tree_edges = []
        visited = set([start_node]) # Mark visited ทันทีที่เข้าคิว
        queue = [start_node] # ใช้ Queue สำหรับ BFS
        
        while queue:
            u = queue.pop(0) # ดึงจากหน้าคิว
            
            if u in self.adj:
                for v, weight in self.adj[u]:
                    if v not in visited:
                        visited.add(v)
                        # เพิ่มเส้นเชื่อมนี้เข้าต้นไม้
                        tree_edges.append((u, v))
                        queue.append(v)
        
        print(f"Edges: {tree_edges}")
        return tree_edges

    # --- 2. Dijkstra's Shortest Path ---
    
    def dijkstra(self, start_node, end_node):
        print(f"\n--- Dijkstra's Shortest Path ({start_node} to {end_node}) ---")
        
        # distances: เก็บระยะทางสั้นสุดจาก start_node ไปยังโหนดอื่นๆ
        distances = {v: float('inf') for v in self.vertices}
        # previous: เก็บโหนดก่อนหน้าในเส้นทางที่สั้นที่สุด
        previous = {v: None for v in self.vertices}
        distances[start_node] = 0
        
        # Priority Queue (min-heap) เก็บ (distance, vertex)
        pq = [(0, start_node)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # ถ้าเราดึงออกมาแล้วเจอระยะทางที่มากกว่าที่เคยบันทึกไว้, ให้ข้าม
            if current_dist > distances[u]:
                continue
                
            # ถ้าถึงปลายทางแล้ว, หยุดได้ (Optimization)
            if u == end_node:
                break
                
            if u in self.adj:
                for v, weight in self.adj[u]:
                    new_dist = distances[u] + weight
                    
                    # ถ้าเจอทางไป v ที่สั้นกว่าเดิม
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        previous[v] = u
                        heapq.heappush(pq, (new_dist, v))
                        
        # --- สร้างเส้นทางย้อนกลับ ---
        path = []
        current = end_node
        total_distance = distances[end_node]
        
        if total_distance == float('inf'):
            print(f"No path found from {start_node} to {end_node}.")
            return [], float('inf')
            
        while current is not None:
            path.append(current)
            current = previous[current]
            
        path.reverse() # กลับด้าน
        
        print(f"Path: {' -> '.join(path)}")
        print(f"Total Distance: {total_distance}")
        return path, total_distance

    # --- 3. Minimum Spanning Tree (Prim's) ---

    def prim_mst(self, start_node=None):
        """หา MST ด้วย Prim's Algorithm"""
        print("\n--- Prim's MST ---")
        if not self.vertices:
            return [], 0
            
        # เลือกโหนดเริ่มต้น (ถ้าไม่กำหนด, เลือกตัวแรก)
        if start_node is None:
            start_node = list(self.vertices)[0]
            
        mst_edges = []
        total_weight = 0
        visited = set()
        
        # Priority Queue (min-heap) เก็บ (weight, u, v)
        # (น้ำหนัก, โหนดที่อยู่ใน MST แล้ว, โหนดที่ยังไม่อยู่ใน MST)
        pq = []
        
        def visit_node(u):
            visited.add(u)
            if u in self.adj:
                for v, weight in self.adj[u]:
                    if v not in visited:
                        heapq.heappush(pq, (weight, u, v))

        # เริ่มต้น
        visit_node(start_node)
        
        while pq and len(visited) < len(self.vertices):
            # ดึงเส้นเชื่อมที่ถูกที่สุด ที่เชื่อมไปยังโหนดที่ยังไม่ visited
            weight, u, v = heapq.heappop(pq)
            
            if v not in visited:
                mst_edges.append((u, v, weight))
                total_weight += weight
                visit_node(v)
                
        print(f"Edges: {mst_edges}")
        print(f"Total Weight: {total_weight}")
        return mst_edges, total_weight

    # --- 4. Minimum Spanning Tree (Kruskal's) ---
    
    def kruskal_mst(self):
        print("\n--- Kruskal's MST ---")
        
        # 1. เรียงลำดับเส้นเชื่อมทั้งหมด (self.edges) ตามน้ำหนัก (น้อยไปมาก)
        sorted_edges = sorted(self.edges)
        
        # 2. สร้าง DSU
        dsu = DSU(self.vertices)
        
        mst_edges = []
        total_weight = 0
        
        # 3. วนลูปดูทุกเส้นเชื่อม
        for weight, u, v in sorted_edges:
            # 4. ใช้ DSU เช็คว่าการเพิ่มเส้นนี้จะเกิด cycle หรือไม่
            if dsu.union(u, v):
                # ถ้าไม่เกิด cycle (union สำเร็จ)
                mst_edges.append((u, v, weight))
                total_weight += weight
        
        print(f"Edges: {mst_edges}")
        print(f"Total Weight: {total_weight}")
        return mst_edges, total_weight
    
# --- Example Usage ---
if __name__ == "__main__":
    
    # --- ตัวอย่างข้อ 1: Spanning Tree (Test Case Page 1, Graph 1) ---
    print("="*50)
    print("TASK 1: SPANNING TREE (Graph 1)")
    print("="*50)
    g1 = Graph()

    # กราฟนี้ไม่มีน้ำหนัก (ใช้ weight=1) และไม่มีทิศทาง
    g1.add_edge('a', 'b')
    g1.add_edge('a', 'f')
    g1.add_edge('b', 'c')
    g1.add_edge('b', 'f')
    g1.add_edge('b', 'g')
    g1.add_edge('c', 'd')
    g1.add_edge('c', 'e')
    g1.add_edge('c', 'g')
    g1.add_edge('d', 'e')
    g1.add_edge('e', 'f')
    g1.add_edge('e', 'g')
    g1.add_edge('f', 'g')
    
    # โจทย์กำหนดให้เริ่มที่ 'a'
    g1.spanning_tree_dfs('a')
    g1.spanning_tree_bfs('a')


    # --- ตัวอย่างข้อ 2: Dijkstra (Test Case Page 3, Graph 1) ---
    print("\n" + "="*30)
    print("TASK 2: DIJKSTRA (Page 3, Graph 1)")
    print("="*30)
    g2 = Graph()
    g2.add_edge('a', 'b', 4)
    g2.add_edge('a', 'c', 2)
    g2.add_edge('b', 'c', 1)
    g2.add_edge('b', 'd', 5)
    g2.add_edge('c', 'd', 8)
    g2.add_edge('c', 'e', 10)
    g2.add_edge('d', 'e', 2)
    
    # โจทย์ให้หา a -> e
    g2.dijkstra('a', 'e')


    # --- ตัวอย่างข้อ 2 (แบบมีทิศทาง): Dijkstra (Test Case Page 4) ---
    print("\n" + "="*30)
    print("TASK 2: DIJKSTRA (Page 4, Directed Graph)")
    print("="*30)
    g_directed = Graph()
    # ต้องระบุ directed=True
    g_directed.add_edge('S', 'A', 2, directed=True)
    g_directed.add_edge('S', 'B', 5, directed=True)
    g_directed.add_edge('S', 'C', 3, directed=True)
    g_directed.add_edge('A', 'D', 6, directed=True)
    g_directed.add_edge('A', 'B', 2, directed=True)
    g_directed.add_edge('B', 'D', 3, directed=True)
    g_directed.add_edge('B', 'F', 6, directed=True)
    g_directed.add_edge('C', 'B', 2, directed=True)
    g_directed.add_edge('C', 'F', 7, directed=True)
    g_directed.add_edge('D', 'E', 3, directed=True)
    g_directed.add_edge('D', 'T', 6, directed=True)
    g_directed.add_edge('E', 'T', 2, directed=True)
    g_directed.add_edge('F', 'E', 3, directed=True)
    g_directed.add_edge('F', 'T', 4, directed=True)
    
    # โจทย์ให้หา S -> T
    g_directed.dijkstra('S', 'T')


    # --- ตัวอย่างข้อ 3: MST (Test Case Page 5, Graph 2) ---
    print("\n" + "="*30)
    print("TASK 3: MST (Page 5, Graph 2)")
    print("="*30)
    g3 = Graph()
    g3.add_edge('a', 'b', 2)
    g3.add_edge('a', 'f', 3)
    g3.add_edge('b', 'f', 4)
    g3.add_edge('b', 'g', 3)
    g3.add_edge('b', 'c', 3)
    g3.add_edge('c', 'g', 4)
    g3.add_edge('c', 'e', 3)
    g3.add_edge('c', 'd', 5)
    g3.add_edge('d', 'e', 4)
    g3.add_edge('e', 'g', 3)
    g3.add_edge('e', 'f', 2)
    g3.add_edge('f', 'g', 5)
    
    # โจทย์ให้หา MST ทั้งสองวิธี
    g3.prim_mst(start_node='a')
    g3.kruskal_mst()