#include <vector>
#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
public:
    Node* root = nullptr;

    void insert(int value) {
        root = insertRec(root, value);
    }

    void inOrder(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        inOrder(node->left, result);
        result.push_back(node->value);
        inOrder(node->right, result);
    }

    void preOrder(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        result.push_back(node->value);
        preOrder(node->left, result);
        preOrder(node->right, result);
    }

    void postOrder(Node* node, vector<int>& result) {
        if (node == nullptr) return;
        postOrder(node->left, result);
        postOrder(node->right, result);
        result.push_back(node->value);
    }

private:
    Node* insertRec(Node* node, int value) {
        if (node == nullptr) return new Node(value);
        if (value < node->value)
            node->left = insertRec(node->left, value);
        else
            node->right = insertRec(node->right, value);
        return node;
    }
};

void printVector(const vector<int>& vec, const string& label) {
    cout << label;
    for (size_t i = 0; i < vec.size(); i++) {
        if (i > 0) cout << " ";
        cout << vec[i];
    }
    cout << endl;
}

int main() {
    int numberCases;
    cin >> numberCases;
    for (int i = 0; i < numberCases; i++) {
        int size;
        cin >> size;
        BinaryTree tree;
        for (int j = 0; j < size; j++) {
            int value;
            cin >> value;
            tree.insert(value);
        }
        vector<int> inOrderResult, preOrderResult, postOrderResult;
        tree.inOrder(tree.root, inOrderResult);
        tree.preOrder(tree.root, preOrderResult);
        tree.postOrder(tree.root, postOrderResult);

        cout << "Case " << i + 1 << ":\n";
        printVector(preOrderResult, "Pre.: ");
        printVector(inOrderResult, "In..: ");
        printVector(postOrderResult, "Post: ");
        cout << endl;
    }

    return 0;
}
