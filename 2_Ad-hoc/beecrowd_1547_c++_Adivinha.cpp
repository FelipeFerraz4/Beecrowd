#include<iostream>

using namespace std;

int main() {
    int number_test;
    std::cin >> number_test;
    
    for (int i = 0; i < number_test; i++) {
        int student, secret_number;
        std::cin >> student >> secret_number;
        int diff = 200, win = 1;
        for (int i = 0; i < student; i++) {
            int guess;
            std::cin >> guess;
            if(abs(secret_number - guess) < diff){
                win = i + 1;
                diff = abs(secret_number - guess);
            }
        }
        std::cout << win << std::endl;
    }
    return 0;
}
