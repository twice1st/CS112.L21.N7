#include <bits/stdc++.h>

int n, a[10101][10101];

using namespace std;

struct Node {
    Node* parent;
    int pathCost;
    int cost;
    int workerID;
    int jobID;
    bool assigned[10101];
};

Node* newNode(int x, int y, bool assigned[], Node* parent) {
    Node* node = new Node;
    for (int j = 0; j < n; j++)
        node->assigned[j] = assigned[j];
    node->assigned[y] = true;
    node->parent = parent;
    node->workerID = x;
    node->jobID = y;
    return node;
}

int calculateCost(int costMatrix[10101][10101], int x, int y, bool assigned[]){
    int cost = 0;
    bool available[n] = {true};
    for (int i = x + 1; i < n; i++){
        int min = INT_MAX, minIndex = -1;
        for (int j = 0; j < n; j++){
            if (!assigned[j] && available[j] && costMatrix[i][j] < min){
                minIndex = j;
                min = costMatrix[i][j];
            }
        }
        cost += min;
        available[minIndex] = false;
    }
    return cost;
}

struct comp{
    bool operator()(const Node* lhs, const Node* rhs) const {
        return lhs->cost > rhs->cost;
    }
};
int getResult(int n, int a[10101][10101]){
    priority_queue<Node*, std::vector<Node*>, comp> pq;
    bool assigned[n] = {false};
    Node* root = newNode(-1, -1, assigned, NULL);
    root->pathCost = root->cost = 0;
    root->workerID = -1;
    pq.push(root);
    while (!pq.empty()){
      Node* min = pq.top();
      pq.pop();
      int i = min->workerID + 1;
      if (i == n){
          return min->cost;
      }
      for (int j = 0; j < n; j++){
        if (!min->assigned[j]){
          Node* child = newNode(i, j, min->assigned, min);
          child->pathCost = min->pathCost + a[i][j];
          child->cost = child->pathCost +
            calculateCost(a, i, j, child->assigned);
          pq.push(child);
        }
      }
    }
    return 0;
}

int main(){
    cin >> n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            cin >> a[i][j];
    cout << getResult(n, a);
    return 0;
}
