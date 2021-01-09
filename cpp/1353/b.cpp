#include <functional>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, k;
        cin >> n >> k;
        vector<int> as;
        vector<int> bs;
        for (int j = 0; j < n; j++) {
            int a;
            cin >> a;
            as.push_back(a);
        }
        for (int j = 0; j < n; j++) {
            int b;
            cin >> b;
            bs.push_back(b);
        }
        sort(as.begin(), as.end());
        sort(bs.begin(), bs.end(), greater<int>());

        int total { 0 };
        for (int i = 0; i < as.size(); i++) {
            int a { as[i] };
            int b { bs[i] };
            if (i < k) {
                if (b > a) {
                    total += b;
                } else {
                    total += a;
                }
            } else {
                total += a;
            }
        }
        cout << total << endl;
    }
}
