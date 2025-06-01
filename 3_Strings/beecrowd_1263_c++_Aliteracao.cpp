#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
using namespace std;

int main() {
    string line;
    while(getline(cin, line)) {
        stringstream phase(line);
        string word, last_word;
        int count = 0;
        bool counted = false;

        while (phase >> word) {
            char current_letter = tolower(word[0]);
            if (!last_word.empty()) {
                char last_letter = tolower(last_word[0]);
                if (current_letter == last_letter && !counted) {
                    count++;
                    counted = true;
                } else if (current_letter != last_letter) {
                    counted = false;
                }
            }
            last_word = word;
        }
        cout << count << endl;
    }
}
