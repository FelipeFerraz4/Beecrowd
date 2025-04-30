#include <iostream>
#include <queue>
#include <climits>

using namespace std;

struct Node {
    int value;
    Node* leftNode;
    Node* rightNode;

    Node(int value) : value(value), leftNode(nullptr), rightNode(nullptr) {}
};

Node* insert(Node* root, int value) {
    if (root == nullptr) {
        return new Node(value);
    }

    if (value < root->value) {
        root->leftNode = insert(root->leftNode, value);
    } else if (value > root->value) {
        root->rightNode = insert(root->rightNode, value);
    }

    return root;
}

void print_min_value_per_level(Node* root) {
    if (root == nullptr) return;

    queue<Node*> q;
    q.push(root);

    int level = 0;

    while (!q.empty()) {
        int size = q.size();
        int min_value = INT_MAX;

        for (int i = 0; i < size; i++) {
            Node* currentNode = q.front();
            q.pop();

            min_value = min(min_value, currentNode->value);

            if (currentNode->leftNode) q.push(currentNode->leftNode);
            if (currentNode->rightNode) q.push(currentNode->rightNode);
        }

        cout << level << " " << min_value << endl;
        level++;
    }
}

int main() {
    int number_tests;
    cin >> number_tests;

    Node* root = nullptr;

    for (int i = 0; i < number_tests; i++) {
        int value;
        cin >> value;
        root = insert(root, value);
    }

    print_min_value_per_level(root);

    return 0;
}
