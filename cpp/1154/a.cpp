#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> ns;
    int n;
    for (int i = 0; i < 4; i++) {
        cin >> n;
        ns.push_back(n);
    }
    sort(ns.begin(), ns.end());
    int a = ns.at(3) - ns.at(0);
    int b = ns.at(1) - a;
    int c = ns.at(2) - a;
    cout << a << " " << b << " " << c << endl;
}
