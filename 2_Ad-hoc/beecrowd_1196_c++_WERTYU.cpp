#include <iostream>
#include <string>
#include <map>

std::map<char, char> keys = {
    // Linha 1
    {'1', '`'}, {'2', '1'}, {'3', '2'}, {'4', '3'}, {'5', '4'},
    {'6', '5'}, {'7', '6'}, {'8', '7'}, {'9', '8'}, {'0', '9'},
    {'-', '0'}, {'=', '-'},

    // Linha 2
    {'W', 'Q'}, {'E', 'W'}, {'R', 'E'}, {'T', 'R'}, {'Y', 'T'},
    {'U', 'Y'}, {'I', 'U'}, {'O', 'I'}, {'P', 'O'}, {'[', 'P'},
    {']', '['}, {'\\', ']'},

    // Linha 3
    {'S', 'A'}, {'D', 'S'}, {'F', 'D'}, {'G', 'F'}, {'H', 'G'},
    {'J', 'H'}, {'K', 'J'}, {'L', 'K'}, {';', 'L'}, {'\'', ';'},

    // Linha 4
    {'X', 'Z'}, {'C', 'X'}, {'V', 'C'}, {'B', 'V'}, {'N', 'B'},
    {'M', 'N'}, {',', 'M'}, {'.', ','}, {'/', '.'}
};

using namespace std;

int main(){
    string phase;
    while(getline(cin, phase)){
        for (auto& letter : phase) {
            if(letter != ' '){
                std::cout << keys[letter];
            } else {
                std::cout << " ";
            }
        }
        std::cout << "" << std::endl;
    }

    return 0;
}
