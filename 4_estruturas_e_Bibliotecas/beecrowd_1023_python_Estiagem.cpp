#include <vector>
#include <map>
#include <cmath>
#include <iomanip>

class Lugar {
public:
    int pessoas;
    int consumo;
    double cmedio;

    Lugar(int p, int c) : pessoas(p), consumo(c) {
        cmedio = static_cast<double>(consumo) / pessoas;
    }
};

int main() {
    int num = 0;  // Contador de casos
    while (true) {
        int n;
        std::cin >> n;
        if (n == 0) {
            break;
        }

        std::vector<Lugar> lugares;
        int total_pessoas = 0;
        int total_consumo = 0;

        for (int i = 0; i < n; ++i) {
            int pessoas, consumo;
            std::cin >> pessoas >> consumo;
            total_pessoas += pessoas;
            total_consumo += consumo;
            lugares.push_back(Lugar(pessoas, consumo));
        }
        std::sort(lugares.begin(), lugares.end(), [](const Lugar& a, const Lugar& b) {
            return std::floor(a.cmedio) < std::floor(b.cmedio);
        });

        num++;
        if (num > 1) {
            std::cout << std::endl;
        }

        std::cout << "Cidade# " << num << ":" << std::endl;

        std::map<int, int> agrupados;
        for (const Lugar& lugar : lugares) {
            int cmedio_truncado = std::floor(lugar.cmedio);
            agrupados[cmedio_truncado] += lugar.pessoas;
        }

        for (auto it = agrupados.begin(); it != agrupados.end(); ++it) {
            if (it != agrupados.begin()) {
                std::cout << " ";
            }
            std::cout << it->second << "-" << it->first;
        }
        std::cout << std::endl;

        double consumo_medio = static_cast<double>(total_consumo) / total_pessoas;
        consumo_medio = std::floor(consumo_medio * 100) / 100;
        std::cout << std::fixed << std::setprecision(2) << "Consumo medio: " << consumo_medio << " m3." << std::endl;
    }

    return 0;
}