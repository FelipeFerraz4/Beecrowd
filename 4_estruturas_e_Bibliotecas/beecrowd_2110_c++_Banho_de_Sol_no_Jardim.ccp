#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

const double PI = acos(-1.0);
const double TOTAL_MINUTES = 960.0;

int main() {
    int N, L, D;

    while (cin >> N >> L >> D) {
        vector<int> h(N);
        int garden = -1;

        for (int i = 0; i < N; ++i) {
            cin >> h[i];
            if (h[i] == 0)
                garden = i;
        }

        double maxLeftAngle = 0.0;
        for (int i = 0; i < garden; ++i) {
            int dist = (garden - i) * (L + D);
            if (h[i] > 0) {
                double angle = atan((double)h[i] / dist);
                if (angle > maxLeftAngle)
                    maxLeftAngle = angle;
            }
        }

        double maxRightAngle = 0.0;
        for (int i = garden + 1; i < N; ++i) {
            int dist = (i - garden) * (L + D);
            if (h[i] > 0) {
                double angle = atan((double)h[i] / dist);
                if (angle > maxRightAngle)
                    maxRightAngle = angle;
            }
        }

        // ângulo total entre nascer e pôr do sol = pi rad (180 graus)
        // ângulo de sol útil = pi - (maxLeftAngle + maxRightAngle)
        double sunAngle = PI - (maxLeftAngle + maxRightAngle);

        double sunMinutes = sunAngle * (TOTAL_MINUTES / PI); // regra de 3

        cout << fixed << setprecision(2) << sunMinutes << endl;
    }

    return 0;
}
