#include<iostream>
#include <cmath>

using namespace std;

int main() {
    int r1, x1, y1, r2, x2, y2;
    while(std::cin >> r1 >> x1 >> y1 >> r2 >> x2 >> y2){
        double distance_between_center = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
        if (distance_between_center + r2 <= r1){
            cout << "RICO" << endl;
        } else {
            cout << "MORTO" << endl;
        }
    }
    return 0;
}
