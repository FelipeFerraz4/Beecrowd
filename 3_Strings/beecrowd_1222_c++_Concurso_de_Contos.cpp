#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int word_number, max_line, max_letter;
    while (cin >> word_number >> max_line >> max_letter) {
        vector<string> words(word_number);
        for (int i = 0; i < word_number; ++i) {
            cin >> words[i];
        }

        int lines = 1;     
        int pages = 1;     
        int current_length = 0;

        for (int i = 0; i < word_number; ++i) {
            int word_len = words[i].size();
            if (current_length == 0) {
                current_length = word_len;
            } else if (current_length + 1 + word_len <= max_letter) {
                current_length += 1 + word_len;
            } else {
                lines++;
                if (lines > max_line) {
                    pages++;
                    lines = 1;
                }
                current_length = word_len;
            }
        }

        cout << pages << endl;
    }

    return 0;
}
