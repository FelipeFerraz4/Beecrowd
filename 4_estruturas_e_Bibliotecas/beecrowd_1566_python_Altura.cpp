#include <iostream>
#include <vector>
#include <sstream>
#include <string>

int main() {
    int NC;
    std::cin >> NC;

    for (int i = 0; i < NC; ++i) {
        std::vector<int> alturas(231, 0);

        int N;
        std::cin >> N;

        for (int j = 0; j < N; ++j) {
            int altura;
            std::cin >> altura;
            alturas[altura]++;
        }

        bool first = true;
        for (int altura = 20; altura <= 230; ++altura) {
            for (int count = 0; count < alturas[altura]; ++count) {
                if (!first) {
                    std::cout << " ";
                }
                std::cout << altura;
                first = false;
            }
        }
        std::cout << std::endl;
    }

    return 0;
}