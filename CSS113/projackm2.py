import heapq
import sys

# ==========================================
# 1. Helper Class: DSU (สำหรับ Kruskal)
# ==========================================
class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, v):
        if self.parent[v] == v: return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]: self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]: self.parent[root_u] = root_v
            else: self.parent[root_v] = root_u; self.rank[root_u] += 1
            return True
        return False

# ==========================================
# 2. Main Graph Class
# ==========================================
class Graph:
    def __init__(self):
        self.adj = {}
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v, weight=1, directed=False):
        self.vertices.add(u); self.vertices.add(v)
        if u not in self.adj: self.adj[u] = []
        self.adj[u].append((v, weight))
        if not directed:
            if v not in self.adj: self.adj[v] = []
            self.adj[v].append((u, weight))
            if (weight, v, u) not in self.edges: self.edges.append((weight, u, v))

    # --- ฟังก์ชันช่วยแสดงข้อมูลจุดยอด (ตามที่คุณขอ) ---
    def print_graph_info(self):
        sorted_verts = sorted(list(self.vertices))
        print(f"Total Vertices: {len(sorted_verts)} จุด")
        print(f"Vertices List:  {sorted_verts}")

    # --- Task 1: DFS ---
    def spanning_tree_dfs(self, start_node):
        print(f"\n*** DFS Spanning Tree (Start: {start_node}) ***")
        self.print_graph_info() # แสดงจำนวนจุดและรายชื่อ
        
        tree_edges = []
        visited = set()
        visit_order = []

        def dfs(u):
            visited.add(u)
            visit_order.append(u)
            if u in self.adj:
                sorted_neighbors = sorted(self.adj[u], key=lambda x: str(x[0]))
                for v, w in sorted_neighbors:
                    if v not in visited:
                        tree_edges.append((u, v))
                        dfs(v)
        dfs(start_node)
        print(f"Traversal: {' -> '.join(visit_order)}")
        print(f"Edges: {tree_edges}")

    # --- Task 1: BFS ---
    def spanning_tree_bfs(self, start_node):
        print(f"\n*** BFS Spanning Tree (Start: {start_node}) ***")
        self.print_graph_info() # แสดงจำนวนจุดและรายชื่อ

        tree_edges = []
        visited = set([start_node])
        queue = [start_node]
        visit_order = [start_node]

        while queue:
            u = queue.pop(0)
            if u in self.adj:
                sorted_neighbors = sorted(self.adj[u], key=lambda x: str(x[0]))
                for v, w in sorted_neighbors:
                    if v not in visited:
                        visited.add(v)
                        visit_order.append(v)
                        tree_edges.append((u, v))
                        queue.append(v)
        print(f"Traversal: {' -> '.join(visit_order)}")
        print(f"Edges: {tree_edges}")

    # --- Task 2: Dijkstra ---
    def dijkstra(self, start_node, end_node):
        print(f"\n** ijkstra ({start_node} -> {end_node}) **")
        self.print_graph_info() # แสดงจำนวนจุดและรายชื่อ

        distances = {v: float('inf') for v in self.vertices}
        previous = {v: None for v in self.vertices}
        distances[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > distances[u]: continue
            if u == end_node: break
            
            if u in self.adj:
                for v, weight in self.adj[u]:
                    new_dist = distances[u] + weight
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        previous[v] = u
                        heapq.heappush(pq, (new_dist, v))
                        
        path = []; current = end_node
        if distances[end_node] == float('inf'): print("No path found."); return
        while current: path.append(current); current = previous[current]
        path.reverse()
        
        path_str = ""
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            w = next((w for n, w in self.adj[u] if n == v), 0)
            path_str += f"[{u}]-{w}-> "
        path_str += f"[{path[-1]}]"
        print(f"Path Result: {path_str}")
        print(f"Total Distance: {distances[end_node]}")

    # --- Task 3: Prim ---
    def prim_mst(self, start_node=None):
        if not self.vertices: return
        if not start_node: start_node = sorted(list(self.vertices))[0]
        print(f"\n** Prim's MST (Start: {start_node}) **")
        self.print_graph_info() # แสดงจำนวนจุดและรายชื่อ

        mst_edges = []; total_weight = 0; visited = set(); pq = []
        
        def visit(u):
            visited.add(u)
            if u in self.adj:
                for v, w in self.adj[u]:
                    if v not in visited: heapq.heappush(pq, (w, u, v))
        visit(start_node)
        while pq and len(visited) < len(self.vertices):
            w, u, v = heapq.heappop(pq)
            if v not in visited:
                mst_edges.append((u, v, w)); total_weight += w; visit(v)
        print(f"MST Edges: {mst_edges}")
        print(f"Total Weight: {total_weight}")

    # --- Task 3: Kruskal ---
    def kruskal_mst(self):
        print(f"\n** Kruskal's MST **")
        self.print_graph_info() # แสดงจำนวนจุดและรายชื่อ

        sorted_edges = sorted(self.edges)
        dsu = DSU(self.vertices)
        mst_edges = []; total_weight = 0
        for w, u, v in sorted_edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, w)); total_weight += w
        print(f"MST Edges: {mst_edges}")
        print(f"Total Weight: {total_weight}")

# ==========================================
# 3. TEST CASES (ครบทุกรูปตามไฟล์ PDF)
# ==========================================
if __name__ == "__main__":
    
    # ---------------------------------------------------
    # TASK 1: Spanning Tree (4 รูปย่อย)
    # ---------------------------------------------------
    print("\n" + "="*50 + "\n" + " "*7 + "[TASK 1] SPANNING TREE (DFS/BFS)\n" + "="*50)
    
    # 1.1 Grid 3x3 (รูปบนสุด)
    g1_1 = Graph()
    g1_1.add_edge('a','b'); g1_1.add_edge('b','c'); g1_1.add_edge('c','d'); g1_1.add_edge('d','e')
    g1_1.add_edge('e','f'); g1_1.add_edge('f','g'); g1_1.add_edge('g','h'); g1_1.add_edge('h','a')
    g1_1.add_edge('b','i'); g1_1.add_edge('d','i'); g1_1.add_edge('f','i'); g1_1.add_edge('h','i')
    print("\n--- 1.1 ---")
    g1_1.spanning_tree_dfs('a')
    
    # 1.2 Hexagon (รูปหกเหลี่ยม)
    g1_2 = Graph()
    g1_2.add_edge('a','b'); g1_2.add_edge('a','f'); g1_2.add_edge('b','c'); g1_2.add_edge('b','g')
    g1_2.add_edge('b','f'); g1_2.add_edge('c','d'); g1_2.add_edge('c','e'); g1_2.add_edge('c','g')
    g1_2.add_edge('d','e'); g1_2.add_edge('e','f'); g1_2.add_edge('e','g'); g1_2.add_edge('f','g')
    print("\n--- 1.2 ---")
    g1_2.spanning_tree_bfs('a')

    # 1.3 Pentagon Star (K5)
    g1_3 = Graph()
    for u in 'abcde':
        for v in 'abcde':
            if u < v: g1_3.add_edge(u, v)
    print("\n--- 1.3 ---")
    g1_3.spanning_tree_dfs('a')

    # 1.4 Multi-Block (รูปล่างสุด)
    g1_4 = Graph()
    g1_4.add_edge('a','b'); g1_4.add_edge('a','d'); g1_4.add_edge('b','c'); g1_4.add_edge('b','d')
    g1_4.add_edge('c','d'); g1_4.add_edge('c','e'); g1_4.add_edge('c','g')
    g1_4.add_edge('d','e'); g1_4.add_edge('e','f'); g1_4.add_edge('e','g'); g1_4.add_edge('f','g')
    g1_4.add_edge('g','j'); g1_4.add_edge('g','k'); g1_4.add_edge('g','h')
    g1_4.add_edge('h','i'); g1_4.add_edge('h','k'); g1_4.add_edge('i','j'); g1_4.add_edge('i','k')
    g1_4.add_edge('j','k')
    print("\n--- 1.4 ---")
    g1_4.spanning_tree_bfs('a')

    # ---------------------------------------------------
    # TASK 2: Dijkstra (4 รูปย่อย)
    # ---------------------------------------------------
    print("\n" + "="*50 + "\n" + " "*15 + "[TASK 2] DIJKSTRA\n" + "="*50)

    # 2.1 Page 3 Graph 1 (บน)
    g2_1 = Graph()
    g2_1.add_edge('a','b',4); g2_1.add_edge('a','c',2); g2_1.add_edge('b','c',1)
    g2_1.add_edge('b','d',5); g2_1.add_edge('c','d',8); g2_1.add_edge('c','e',10); g2_1.add_edge('d','e',2)
    g2_1.dijkstra('a', 'e')

    # 2.2 Page 3 Graph 2 (กลาง)
    g2_2 = Graph()
    g2_2.add_edge('a','b',6); g2_2.add_edge('a','e',5); g2_2.add_edge('a','c',7)
    g2_2.add_edge('b','c',2); g2_2.add_edge('b','d',5); g2_2.add_edge('c','e',1)
    g2_2.add_edge('c','d',3); g2_2.add_edge('e','d',2)
    g2_2.dijkstra('a', 'd')
    
    # 2.3 Page 3 Graph 3 (ล่าง)
    g2_3 = Graph()
    g2_3.add_edge('a','b',10); g2_3.add_edge('a','c',5); g2_3.add_edge('b','c',3)
    g2_3.add_edge('b','d',2); g2_3.add_edge('c','e',9); g2_3.add_edge('d','e',4)
    g2_3.add_edge('d','f',6); g2_3.add_edge('e','f',7)
    g2_3.dijkstra('a', 'f')

    # 2.4 Page 4 Directed Graph
    g_dir = Graph()
    g_dir.add_edge('S','A',2,True); g_dir.add_edge('S','B',5,True); g_dir.add_edge('S','C',3,True)
    g_dir.add_edge('A','D',6,True); g_dir.add_edge('A','B',2,True); g_dir.add_edge('B','D',3,True)
    g_dir.add_edge('B','F',6,True); g_dir.add_edge('C','B',2,True); g_dir.add_edge('C','F',7,True)
    g_dir.add_edge('D','E',3,True); g_dir.add_edge('D','T',6,True); g_dir.add_edge('E','T',2,True)
    g_dir.add_edge('F','E',3,True); g_dir.add_edge('F','T',4,True)
    g_dir.dijkstra('S', 'T')

    # ---------------------------------------------------
    # TASK 3: MST (Prim & Kruskal)
    # ---------------------------------------------------
    print("\n" + "="*50 + "\n" + " "*7 + "[TASK 3] MST (Prim's & Kruskal's)\n" + "="*50)

    # 3.1 Page 5 Graph 2 (ขวาบน - หกเหลี่ยม)
    g3_1 = Graph()
    g3_1.add_edge('a','b',2); g3_1.add_edge('a','f',3); g3_1.add_edge('b','f',4); g3_1.add_edge('b','g',3)
    g3_1.add_edge('b','c',3); g3_1.add_edge('c','g',4); g3_1.add_edge('c','e',3); g3_1.add_edge('c','d',5)
    g3_1.add_edge('d','e',4); g3_1.add_edge('e','g',3); g3_1.add_edge('e','f',2); g3_1.add_edge('f','g',5)
    print("\n--- MST Graph 1 ---")
    g3_1.prim_mst('a')
    g3_1.kruskal_mst()

    # 3.2 Page 5 Graph 3 (ซ้ายล่าง - สี่เหลี่ยมกากบาท)
    g3_2 = Graph()
    g3_2.add_edge('a','b',1); g3_2.add_edge('a','d',2); g3_2.add_edge('a','e',3); g3_2.add_edge('b','c',2)
    g3_2.add_edge('b','e',2); g3_2.add_edge('c','d',3); g3_2.add_edge('c','e',4); g3_2.add_edge('d','e',1)
    print("\n--- MST Graph 2 ---")
    g3_2.prim_mst('a')
    
    # 3.3 Page 5 Graph 4 (ขวาล่าง - บ้าน)
    g3_3 = Graph()
    g3_3.add_edge('a','b',1); g3_3.add_edge('a','e',2); g3_3.add_edge('b','c',3); g3_3.add_edge('b','d',4)
    g3_3.add_edge('b','e',3); g3_3.add_edge('c','d',3); g3_3.add_edge('c','e',2); g3_3.add_edge('d','e',1)
    print("\n--- MST Graph 3 ---")
    g3_3.kruskal_mst()

    print("\n" + "="*50 + "\n" + " "*17 + "END OF TESTS" )
    print("="*50)