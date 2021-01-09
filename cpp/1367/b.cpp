#include <cmath>
#include <iostream>
#include <vector>

using namespace std;


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;

        int even_count = 0;
        int misplaced_even_count = 0;

        for (int j = 0; j < n; j++) {
            int a;
            cin >> a;
            if (a % 2 == 0) {
                even_count += 1;
                if (j % 2 == 1) {
                    misplaced_even_count += 1;
                }
            }
        }

        int total_even_count = static_cast<int>(ceil(static_cast<double>(n) / 2.0));

        if (even_count != total_even_count) {
            cout << -1 << endl;
        } else {
            cout << misplaced_even_count << endl;
        }
    }
    return 0;
}
