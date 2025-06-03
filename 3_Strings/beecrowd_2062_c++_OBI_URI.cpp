#include <iostream>
#include <string>

using namespace std;

int main(){
    int number_words;
    cin >> number_words;

    string word;
    for (int i = 1; i <= number_words; ++i) {
        cin >> word;

        if (word.size() == 3 && (word.rfind("OB", 0) == 0 || word.rfind("UR", 0) == 0)) {
            word[2] = 'I';
        }

        if (i == number_words) {
            cout << word << endl;
        } else {
            cout << word << " ";
        }
    }

    return 0;
}
