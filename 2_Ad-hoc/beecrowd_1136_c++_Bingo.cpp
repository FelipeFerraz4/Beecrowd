#include <iostream>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int numbers, ball;

    while (cin >> numbers >> ball) {
        if (numbers == 0 && ball == 0) {
            break;
        }

        vector<int> bingo_numbers(ball);
        for (int i = 0; i < ball; i++) {
            cin >> bingo_numbers[i];
        }

        set<int> numbers_possible;

        for (int i = 0; i < ball; i++) {
            for (int j = 0; j < ball; j++) {
                numbers_possible.insert(abs(bingo_numbers[i] - bingo_numbers[j]));
            }
        }

        bool bingo = true;
        for (int i = 0; i <= numbers; i++) {
            if (numbers_possible.find(i) == numbers_possible.end()) {
                bingo = false;
                break;
            }
        }

        cout << (bingo ? "Y" : "N") << endl;
    }

    return 0;
}
