#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    int number_tests;
    cin >> number_tests;

    while (number_tests != 0) {
        map<string, int> teams;

        for (int i = 0; i < number_tests; i++) {
            string team_name;
            cin >> team_name;

            int team_score;
            cin >> team_score;

            teams[team_name] += team_score;
        }

        for (int i = 0; i < number_tests / 2; i++) {
            string first_team, second_team, score;
            cin >> first_team >> score >> second_team;

            int first_team_score = stoi(score.substr(0, score.find('-')));
            int second_team_score = stoi(score.substr(score.find('-') + 1));

            teams[first_team] += first_team_score * 3;
            teams[second_team] += second_team_score * 3;

            if (first_team_score > second_team_score) {
                teams[first_team] += 5;
            } else if (first_team_score < second_team_score) {
                teams[second_team] += 5;
            } else {
                teams[first_team] += 1;
                teams[second_team] += 1;
            }
        }

        string winner_team = teams.begin()->first;
        int max_score = teams.begin()->second;

        for (auto it = teams.begin(); it != teams.end(); ++it) {
            if (it->second > max_score) {
                max_score = it->second;
                winner_team = it->first;
            }
        }

        if (winner_team == "Sport") {
            cout << "O Sport foi o campeao com " << max_score << " pontos :D\n" << endl;
        } else {
            cout << "O Sport nao foi o campeao. O time campeao foi o " << winner_team << " com " << max_score << " pontos :(\n" << endl;
        }

        cin >> number_tests;
    }

    return 0;
}
