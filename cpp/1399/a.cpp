#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_test();
bool test(vector<int>);

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        vector<int> as = get_test();
        if (test(as)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}


vector<int> get_test() {
    int n;
    cin >> n;
    vector<int> as;
    int a;
    for (int j = 0; j < n; j++) {
        cin >> a;
        as.push_back(a);
    }
    return as;
}


bool test(vector<int> as) {
    sort(as.begin(), as.end());
    for (int i = 0; i < as.size() - 1; i++) {
        if (as.at(i + 1) - as.at(i) > 1) {
            return false;
        }
    }
    return true;
}
