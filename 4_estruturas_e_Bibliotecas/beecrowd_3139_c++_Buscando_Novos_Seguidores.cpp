#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    long long followers, min_followers;
    cin >> followers >> min_followers;

    vector<long long> last_30_days(30);
    long long sum = 0;

    for (int i = 0; i < 30; i++) {
        cin >> last_30_days[i];
        sum += last_30_days[i];
    }

    int days = 0;
    int indices = 0;

    while (followers < min_followers) {
        long long new_followers = ceil(sum / 30.0);
        followers += new_followers;
        sum -= last_30_days[indices];
        sum += new_followers;
        last_30_days[indices] = new_followers;
        indices = (indices + 1) % 30;
        days++;
    }

    cout << days << endl;

    return 0;
}
