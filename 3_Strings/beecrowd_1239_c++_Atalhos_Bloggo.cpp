#include<iostream>
#include<string>
using namespace std;

int main() {
    string phase;
    while(getline(cin, phase)){
        bool italic = false, bold = false;
        for (int i = 0; i < phase.size(); i++) {
            if(phase[i] == '_'){
                if(italic) {
                    phase.replace(i, 1, "</i>");
                    italic = false;
                } else {
                    phase.replace(i, 1, "<i>");
                    italic = true;
                }
            }
            if(phase[i] == '*'){
                if(bold) {
                    phase.replace(i, 1, "</b>");
                    bold = false;
                } else {
                    phase.replace(i, 1, "<b>");
                    bold = true;
                }
            }
        }
        std::cout << phase << std::endl;
    }
}
