#include <iostream>
#include <vector>

using namespace std;

bool repet_number(int number){
    std::vector<int> digits(10, 0);
    bool check = true;
    while(number > 0){
        int digit = number % 10;
        if(digits[digit] == 0){
            digits[digit] = 1;
        } else{
            check = false;
            break;
        }
        number = number / 10;
    }
    return check;
}

int main(){
    int number1, number2;
    while(std::cin >> number1 >> number2){
        int count = 0;
        for (int i = number1; i <= number2; i++) {
            if(repet_number(i)) count++;
        }
        std::cout << count << std::endl;
    }
    return 0;
}
