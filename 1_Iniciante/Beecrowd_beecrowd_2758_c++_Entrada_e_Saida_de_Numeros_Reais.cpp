#include<iostream>
#include<cmath>
#include<iomanip>

using namespace std;

int main() {
    float number1, number2;
    double number3, number4;
    
    std::cin >> number1 >> number2;
    std::cin >> number3 >> number4;
    
    std::cout << "A = " << std::fixed << std::setprecision(6) << number1;
    std::cout << ", B = " << std::fixed << std::setprecision(6) << number2 << std::endl;
    
    std::cout << "C = " << std::fixed << std::setprecision(6) << number3;
    std::cout << ", D = " << std::fixed << std::setprecision(6) << number4 << std::endl;
    
    std::cout << "A = " << std::fixed << std::setprecision(1) << number1;
    std::cout << ", B = " << std::fixed << std::setprecision(1) << number2 << std::endl;
    
    std::cout << "C = " << std::fixed << std::setprecision(1) << number3;
    std::cout << ", D = " << std::fixed << std::setprecision(1) << number4 << std::endl;

    std::cout << "A = " << std::fixed << std::setprecision(2) << number1;
    std::cout << ", B = " << std::fixed << std::setprecision(2) << number2 << std::endl;
    
    std::cout << "C = " << std::fixed << std::setprecision(2) << number3;
    std::cout << ", D = " << std::fixed << std::setprecision(2) << number4 << std::endl;
    
    std::cout << "A = " << std::fixed << std::setprecision(3) << number1;
    std::cout << ", B = " << std::fixed << std::setprecision(3) << number2 << std::endl;
    
    std::cout << "C = " << std::fixed << std::setprecision(3) << number3;
    std::cout << ", D = " << std::fixed << std::setprecision(3) << number4 << std::endl;
    
    std::cout << "A = " << std::uppercase << std::scientific << std::setprecision(3) << number1;
    std::cout << ", B = " << std::uppercase << std::scientific << std::setprecision(3) << number2 << std::endl;
    
    std::cout << "C = " << std::uppercase << std::scientific << std::setprecision(3) << number3;
    std::cout << ", D = " << std::uppercase << std::scientific << std::setprecision(3) << number4 << std::endl;
    
    std::cout << "A = " << std::fixed << std::setprecision(0) << number1;
    std::cout << ", B = " << std::fixed << std::setprecision(0) << number2 << std::endl;
    
    std::cout << "C = " << std::fixed << std::setprecision(0) << number3;
    std::cout << ", D = " << std::fixed << std::setprecision(0) << number4 << std::endl;
    
    return 0;
}
