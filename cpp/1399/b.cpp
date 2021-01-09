#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<long long> get_gifts(int);

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<long long> as = get_gifts(n);
        vector<long long> bs = get_gifts(n);
        long long a_min = *min_element(as.begin(), as.end());
        long long b_min = *min_element(bs.begin(), bs.end());
        long long moves { 0 };
        for (int j = 0; j < n; j++) {
            long long a;
            long long b;
            a = as.at(j);
            b = bs.at(j);
            long long a_diff = a - a_min;
            long long b_diff = b - b_min;
            long long max_diff = max(a_diff, b_diff);
            moves += max_diff;
        }
        cout << moves << endl;
    }
}


vector<long long> get_gifts(int n) {
    vector<long long> as;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        as.push_back(a);
    }
    return as;
}
