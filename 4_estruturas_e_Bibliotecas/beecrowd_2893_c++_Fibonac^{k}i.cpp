#include <iostream>
#include <vector>

using namespace std;

int main() {
    int number_of_cases;
    const int mod = 1000007;

    cin >> number_of_cases;
    for(int i = 0; i < number_of_cases; i++) {
        int k, n;
        cin >> k >> n;

        if (n <= k) {
            cout << n - 1 << endl;
            continue;
        }

        vector<int> fib(n + 1, 0);
        long long int sum = 0;

        for (int j = 0; j < k; j++) {
            fib[j] = j;
            sum = (sum + fib[j]) % mod;
        }

        for (int j = k; j <= n; j++) {
            fib[j] = sum;
            sum = (sum - fib[j - k] + fib[j] + mod) % mod;
        }

        cout << fib[n - 1] << endl;
    }

    return 0;
}