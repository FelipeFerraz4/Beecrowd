#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int tests_number;
    std::cin >> tests_number;
    for (int i = 0; i < tests_number; i++) {
        int comands_number, position = 0;
        std::cin >> comands_number;
        vector<int> comands(comands_number, 0);
        for (int j = 0; j < comands_number; j++) {
            string comand_type;
            std::cin >> comand_type;
            if(comand_type == "LEFT"){
                comands[j] = -1;
                position--;
            } else if (comand_type == "RIGHT"){
                comands[j] = 1;
                position++;
            } else if(comand_type == "SAME"){
                int position_comand;
                string aux;
                std::cin >> aux >> position_comand;
                comands[j] = comands[position_comand - 1];
                position += comands[position_comand - 1];
            }
        }
        std::cout << position << std::endl;
    }
    return 0;
}
