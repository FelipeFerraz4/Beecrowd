#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

int main(){
    int days_number;
    std::cin >> days_number;
    double total_kg = 0; 
    double total_value = 0.00; 
    
    for (int i = 0; i < days_number; i++) {
        double value;
        std::cin >> value;
        
        string line;
        std::cin.ignore();
        getline(cin, line);
        stringstream fruits(line);
        
        int amount = 0;
        string fruit;
        while(fruits >> fruit){
            amount++;
        }
        total_value += value;
        total_kg += amount;
        
        std::cout << "day " << i+1 << ": " << amount << " kg" << std::endl;
    }
    
    std::cout << std::fixed << std::setprecision(2) << double(total_kg/days_number) << " kg by day" << std::endl;
    std::cout << "R$ " << std::fixed << std::setprecision(2) << (total_value/days_number) << " by day" << std::endl;
    
    return 0;
}
