#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int days_number;
    while(std::cin >> days_number){
        int cost;
        std::cin >> cost;
        std::vector<int> days(days_number, 0);
        for (int i = 0; i < days_number; i++) {
            std::cin >> days[i];
        }
        int max_value_current = 0, max_value_total = 0;
        for (int i = 0; i < days_number; i++) {
            int value = days[i] - cost;
            max_value_current = max(0, max_value_current + value);
            max_value_total = max(max_value_total, max_value_current);
        }
        std::cout << max_value_total << std::endl;
    }

    return 0;
}
