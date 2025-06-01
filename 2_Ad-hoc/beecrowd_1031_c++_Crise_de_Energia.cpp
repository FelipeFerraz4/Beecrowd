#include <iostream> 
#include <vector>
using namespace std;

int find_minimum_m(int n) {
    int m = 1;
    while (true) {
        vector<int> regions;
        for (int i = 1; i <= n; i++) {
            regions.push_back(i);
        }

        int index = 0;

        regions.erase(regions.begin());

        index = (index + m - 1) % regions.size();

        bool valid = true;
        while (regions.size() > 1) {
            int eliminated = regions[index];
            regions.erase(regions.begin() + index);
            if (eliminated == 13) {
                valid = false;
                break;
            }
            index = (index + m - 1) % regions.size();
        }

        if (valid && regions[0] == 13) {
            return m;
        }

        m++;
    }
}

int main() {
    int n;
    while (cin >> n && n != 0) {
        cout << find_minimum_m(n) << endl;
    }
    return 0;
}
