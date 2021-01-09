#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<int> ss;
        for (int j = 0; j < n; j++) {
            int s;
            cin >> s;
            ss.push_back(s);
        }
        sort(ss.begin(), ss.end());
        int min_diff { 2000 };
        for (int j = 0; j < n - 1; j++) {
            int diff = abs(ss.at(j) - ss.at(j + 1));
            if (diff < min_diff) {
                min_diff = diff;
            }
        }
        cout << min_diff << endl;
    }
}
