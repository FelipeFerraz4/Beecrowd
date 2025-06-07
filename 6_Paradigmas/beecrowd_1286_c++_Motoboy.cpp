#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int order_number, max_pizza;
    do{
        std::cin >> order_number;
        if(order_number == 0) break;

        cin >> max_pizza;
        vector<int> times(order_number), pizzas(order_number);

        for(int i = 0; i < order_number; i++){
            cin >> times[i] >> pizzas[i];
        }

        vector<vector<int>> dp(order_number + 1, vector<int>(max_pizza + 1, 0));

        for(int i = 1; i <= order_number; i++){
            for(int j = 1; j <= max_pizza; j++){
                dp[i][j] = dp[i-1][j];

                if(j >= pizzas[i-1]){
                    dp[i][j] = max(dp[i][j], dp[i-1][j - pizzas[i-1]] + times[i-1]);
                }
            }
        }

        cout << dp[order_number][max_pizza] << " min." << endl;

    }while(order_number != 0);

    return 0;
}
