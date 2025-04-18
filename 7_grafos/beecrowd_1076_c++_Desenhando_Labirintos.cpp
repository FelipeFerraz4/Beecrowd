#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int number_of_cases;
    cin >> number_of_cases;

    while (number_of_cases--) {
        int start, number_of_nodes, number_of_edges;
        cin >> start >> number_of_nodes >> number_of_edges;

        vector<vector<bool>> graph(number_of_nodes, vector<bool>(number_of_nodes, false));

        for (int i = 0; i < number_of_edges; ++i) {
            int u, v;
            cin >> u >> v;
            graph[u][v] = true;
            graph[v][u] = true;
        }

        int result = 0;
        for (int i = 0; i < number_of_nodes; ++i) {
            for (int j = 0; j < number_of_nodes; ++j) {
                if (graph[i][j]) {
                    result++;
                }
            }
        }

        cout << result << endl;
    }

    return 0;
}