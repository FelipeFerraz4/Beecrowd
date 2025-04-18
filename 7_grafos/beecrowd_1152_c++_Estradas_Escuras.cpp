#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, w;

    Edge(int u, int v, int w) : u(u), v(v), w(w) {}

    bool operator<(const Edge& other) const {
        return w < other.w;
    }
};

vector<int> parent;

int find(int u) {
    if (parent[u] != u) {
        parent[u] = find(parent[u]);
    }
    return parent[u];
}

bool unite(int u, int v) {
    int rootU = find(u);
    int rootV = find(v);
    if (rootU != rootV) {
        parent[rootU] = rootV;
        return true;
    }
    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(true) {
        int joints_number, roads_number;
        cin >> joints_number >> roads_number;
        
        if (joints_number == 0 && roads_number == 0) {
            break;
        }

        vector<Edge> edges;
        int total_cost = 0;

        for(int i = 0; i < roads_number; ++i) {
            int u, v, w;
            cin >> u >> v >> w;
            edges.emplace_back(u, v, w);
            total_cost += w;
        }

        sort(edges.begin(), edges.end());
        parent.resize(joints_number);

        for(int i = 0; i < joints_number; ++i) {
            parent[i] = i;
        }

        int mst_cost = 0;

        for(const auto& edge : edges) {
            if (unite(edge.u, edge.v)) {
                mst_cost += edge.w;
            }
        }

        cout << total_cost - mst_cost << endl;
    }

    return 0;
}
