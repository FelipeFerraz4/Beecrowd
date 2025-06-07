#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int test_number;
    cin >> test_number;
    for(int k = 0; k < test_number; k++){
        int projectiles_number, max_weight, castle_life;
        cin >> projectiles_number;
        vector<int> damage_powers(projectiles_number), weights(projectiles_number);
        for(int i = 0; i < projectiles_number; i++){
            cin >> damage_powers[i] >> weights[i];
        }
        cin >> max_weight;
        cin >> castle_life;

        vector<vector<int>> dp(projectiles_number+1, vector<int>(max_weight+1, 0));

        for(int i = 1; i <= projectiles_number; i++){
            for(int j = 1; j <= max_weight; j++){
                dp[i][j] = dp[i-1][j];

                if(j >= weights[i-1]){
                    dp[i][j] = max(dp[i][j], dp[i-1][j - weights[i-1]] + damage_powers[i-1]);
                }
            }
        }

        int damage = dp[projectiles_number][max_weight];
        if(damage >= castle_life){
            cout << "Missao completada com sucesso" << endl;
        } else {
            cout << "Falha na missao" << endl;
        }
    }

    return 0;
}
