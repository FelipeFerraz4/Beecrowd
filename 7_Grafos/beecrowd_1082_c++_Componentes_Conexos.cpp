#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

class Graph{
    private:
        std::map<char, vector<char>> adjacency_list;
        std::set<char> visited;
        int vertices_number;
    public:
        Graph(int vertices){
            vertices_number = vertices;
            for (int i = 0; i < vertices_number; i++) {
                char vertice_letter = 'a' + i;
                adjacency_list[vertice_letter] = {};
            }
        }
        
        void addEdge(char u, char v){
            adjacency_list[u].push_back(v);
            adjacency_list[v].push_back(u);
        }
        
        void dfs(char v, vector<char>& component){
            visited.insert(v);
            component.push_back(v);
            for (auto neighbor : adjacency_list[v]) {
                if(visited.find(neighbor) == visited.end()){
                    dfs(neighbor, component);
                }
            }
        }
        
        vector<vector<char>> find_components(){
            vector<vector<char>> components;
            for (int i = 0; i < vertices_number; i++) {
                char vertice = 'a' + i;
                if(visited.find(vertice) == visited.end()){
                    vector<char> component;
                    dfs(vertice, component);
                    sort(component.begin(), component.end());
                    components.push_back(component);
                }
            }
            return components;
        }
};

int main(){
    int test_number;
    std::cin >> test_number;
    for (int i = 0; i < test_number; i++) {
        int vertices_number, edges_number;
        std::cin >> vertices_number >> edges_number;
        
        Graph graph(vertices_number);
        
     for (int j = 0; j < edges_number; j++) {
         char u, v;
         std::cin >> u >> v;
         graph.addEdge(u, v);
     }
     
     vector<vector<char>> components  = graph.find_components();
     
     std::cout << "Case #" << i+1 << ":" << std::endl;
     for (const auto& component : components) {
         for (char letter : component) {
             std::cout << letter << ",";
         }
         std::cout << "" << std::endl;
     }
     std::cout << components.size() << " connected components\n" << std::endl;
    }

    return 0;
}
