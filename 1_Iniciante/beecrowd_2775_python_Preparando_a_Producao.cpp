#include <iostream>
#include <vector>
#include <utility>

using namespace std;

long long mergeAndCount(vector<pair<int, int>>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<pair<int, int>> L(n1), R(n2);
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[mid + 1 + i];

    long long cost = 0;
    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i].first <= R[j].first) {
            arr[k++] = L[i++];
        } else {
            // R[j] deve passar por todos os L[i...n1-1]
            for (int p = i; p < n1; ++p)
                cost += L[p].second + R[j].second;
            arr[k++] = R[j++];
        }
    }

    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];

    return cost;
}

long long mergeSortAndCount(vector<pair<int, int>>& arr, int left, int right) {
    long long totalCost = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        totalCost += mergeSortAndCount(arr, left, mid);
        totalCost += mergeSortAndCount(arr, mid + 1, right);
        totalCost += mergeAndCount(arr, left, mid, right);
    }
    return totalCost;
}

int main() {
    int N;
    while (cin >> N) {
        vector<int> pacotes(N), tempos(N);
        for (int i = 0; i < N; ++i)
            cin >> pacotes[i];
        for (int i = 0; i < N; ++i)
            cin >> tempos[i];

        vector<pair<int, int>> dados(N);
        for (int i = 0; i < N; ++i)
            dados[i] = {pacotes[i], tempos[i]};

        cout << mergeSortAndCount(dados, 0, N - 1) << endl;
    }

    return 0;
}
