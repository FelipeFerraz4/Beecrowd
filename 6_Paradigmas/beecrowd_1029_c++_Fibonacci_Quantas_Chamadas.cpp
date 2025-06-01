#include <iostream>
#include <utility>

using namespace std;

pair<unsigned long long, int> fib(int n){
    pair<unsigned long long, int> result, left, right;
    if (n == 0) return make_pair(0, 1);
    if (n == 1) return make_pair(1, 1);
    left = fib(n-1);
    right = fib(n-2);
    return make_pair(left.first + right.first, left.second + right.second + 1);
}

int main() {
    int number_test;
    std::cin >> number_test;
    for (int i = 0; i < number_test; i++) {
        int number;
        std::cin >> number;
        pair<unsigned long long, int> result = fib(number);
        std::cout << "fib(" << number << ") = " << result.second - 1 << " calls = " <<  result.first << std::endl;
    }
    return 0;
}
