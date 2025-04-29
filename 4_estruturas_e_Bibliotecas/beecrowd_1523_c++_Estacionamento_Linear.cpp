#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <stack>
using namespace std;

int main() {
    int number_of_car, number_of_spaces, number_of_cars_in_parking_lot = 0;
    cin >> number_of_car >> number_of_spaces;
    
    while (number_of_car != 0 && number_of_spaces != 0) {
        vector<array<int, 3>> operation;
        for (int i = 0; i < number_of_car; i++) {
            int entrance, exit;
            cin >> entrance >> exit;
            operation.push_back({i, 0, entrance});
            operation.push_back({i, 1, exit});
        }

        sort(operation.begin(), operation.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
            return a[2] < b[2];
        });

        bool check = false;
        stack<int> parking_lot;
        for(int i = 0; i < operation.size(); i++) {
            if (operation[i][1] == 0) {
                if (parking_lot.size() < number_of_spaces) {
                    parking_lot.push(operation[i][0]);
                    number_of_cars_in_parking_lot++;
                } else {
                    // cout << "No parking space available for car " << operation[i][0] << endl;
                    check = true;
                    break;
                }
            } else {
                if (!parking_lot.empty()) {
                    parking_lot.pop();
                    number_of_cars_in_parking_lot--;
                } else {
                    // cout << "No car to exit from parking lot" << endl;
                    check = true;
                    break;
                }
            }
        }

        if (check) {
            cout << "Nao" << endl;
        } else {
            cout << "Sim" << endl;
        }
        
        cin >> number_of_car >> number_of_spaces;
    }
       
    return 0;
}