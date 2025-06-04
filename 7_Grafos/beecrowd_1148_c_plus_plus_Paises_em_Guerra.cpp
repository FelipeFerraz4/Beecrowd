#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

const int INFINITE = INT_MAX;

struct Edge {
    int destination;
    int time;
    Edge(int dest, int t) : destination(dest), time(t) {}
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int city_count, agreement_count;
        cin >> city_count >> agreement_count;

        if (city_count == 0 && agreement_count == 0) break;

        vector<vector<Edge>> communication_graph(city_count + 1);

        for (int i = 0; i < agreement_count; ++i) {
            int origin, destination, travel_time;
            cin >> origin >> destination >> travel_time;

            bool has_reverse = false;
            for (const auto& edge : communication_graph[destination]) {
                if (edge.destination == origin) {
                    has_reverse = true;
                    break;
                }
            }

            if (has_reverse) {
                auto& edges_from_destination = communication_graph[destination];
                for (auto edge_iterator = edges_from_destination.begin(); edge_iterator != edges_from_destination.end(); ++edge_iterator) {
                    if (edge_iterator->destination == origin) {
                        edges_from_destination.erase(edge_iterator);
                        break;
                    }
                }

                communication_graph[origin].emplace_back(destination, 0);
                communication_graph[destination].emplace_back(origin, 0);
            } else {
                communication_graph[origin].emplace_back(destination, travel_time);
            }
        }

        vector<vector<int>> shortest_times(city_count + 1, vector<int>(city_count + 1, INFINITE));

        for (int start_city = 1; start_city <= city_count; ++start_city) {
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> time_queue;
            shortest_times[start_city][start_city] = 0;
            time_queue.push({0, start_city});

            while (!time_queue.empty()) {
                int current_time = time_queue.top().first;
                int current_city = time_queue.top().second;
                time_queue.pop();

                if (current_time > shortest_times[start_city][current_city]) continue;

                for (const auto& edge : communication_graph[current_city]) {
                    int next_city = edge.destination;
                    int travel_time = edge.time;

                    if (shortest_times[start_city][current_city] + travel_time < shortest_times[start_city][next_city]) {
                        shortest_times[start_city][next_city] = shortest_times[start_city][current_city] + travel_time;
                        time_queue.push({shortest_times[start_city][next_city], next_city});
                    }
                }
            }
        }

        int query_count;
        cin >> query_count;

        for (int i = 0; i < query_count; ++i) {
            int from_city, to_city;
            cin >> from_city >> to_city;

            if (shortest_times[from_city][to_city] == INFINITE) {
                cout << "Nao e possivel entregar a carta\n";
            } else {
                cout << shortest_times[from_city][to_city] << "\n";
            }
        }

        cout << "\n";
    }

    return 0;
}
