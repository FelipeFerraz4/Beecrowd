#include <iostream>
#include <map>
#include <string>
#include <set>

using namespace std;

int main() {
    string killer, victim;
    map<string, int> kill_count;
    set<string> dead;

    while(cin >> killer >> victim) {
        kill_count[killer]++;
        dead.insert(victim);
    }

    cout << "HALL OF MURDERERS" << endl;

    for(const auto& entry : kill_count) {
        if (dead.find(entry.first) == dead.end()) {
            cout << entry.first << " " << entry.second << endl;
        }
    }
    return 0;
}