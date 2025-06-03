#include <iostream>
#include <vector>

using namespace std;

int main(){
    int number_bank, number_debenture;
    
    while (true) {
        cin >> number_bank >> number_debenture;

        if (number_bank == 0 && number_debenture == 0)
            break;
        
        vector<int> banks(number_bank);
        
        for (int i = 0; i < number_bank; ++i) {
            cin >> banks[i];
        }

        for (int i = 0; i < number_debenture; ++i) {
            int debtor, creditor, amount;
            cin >> debtor >> creditor >> amount;
            banks[debtor - 1] -= amount;
            banks[creditor - 1] += amount;
        }

        bool possible = true;
        for (int i = 0; i < number_bank; ++i) {
            if (banks[i] < 0) {
                possible = false;
                break;
            }
        }

        cout << (possible ? "S" : "N") << endl;
    }

    return 0;
}
