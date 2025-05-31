#include<iostream>
#include<string>
using namespace std;

int main() {
    string frase1, frase2;
    while(getline(cin, frase1) && getline(cin, frase2)){
        int max_size = 0;
        for(int i = 0; i < frase1.size(); i++){
            for (int j = 0; j < frase2.size(); j++) {
                if(frase1[i] == frase2[j]){
                    int size = 1;
                    int index1 = i + 1;
                    int index2 = j + 1;
                    while(index1 < frase1.size() && index2 < frase2.size()){
                        if(frase1[index1] == frase2[index2]) {
                            size++;
                            index1++;
                            index2++;
                        } else {
                            break;
                        }
                    }
                    if (size > max_size) max_size = size;
                }
            }
        }
        std::cout << max_size << std::endl;
    }
}
