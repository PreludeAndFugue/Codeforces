#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> as;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        as.push_back(a);
    }
    int a_max = 0;
    for (int a : as) {
        if (a > a_max) {
            a_max = a;
        }
    }
    int total { 0 };
    for (int a : as) {
        total += a_max - a;
    }
    cout << total << endl;
}
