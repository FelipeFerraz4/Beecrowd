#include <iostream>
using namespace std;

int main() {
    int first_day, second_day;

    std::cin >> first_day >> second_day;

    if(second_day < 3){
        std::cout << "nova" << std::endl;
    } else if (second_day > 96){
       std::cout << "cheia" << std::endl;
    } else if (second_day < first_day) {
        std::cout << "minguante" << std::endl;
    } else {
        std::cout << "crescente" << std::endl;
    }

    return 0;
}
