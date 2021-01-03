#include <iostream>

using namespace std;

int main() {
    constexpr int t = 240;
    int n;
    int k;
    cin >> n;
    cin >> k;
    int r = t - k;
    int count = 0;
    for (int i = 1; i <= n; i++) {
        r -= 5 * i;
        if (r >= 0) {
            count += 1;
        } else {
            break;
        }
    }
    cout << count << endl;
}
