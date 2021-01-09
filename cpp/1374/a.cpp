#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int x, y, n;
        cin >> x >> y >> n;
        int a = n % x;
        if (a >= y) {
            cout << n + y - a << endl;
        } else {
            cout << n - x + y - a << endl;
        }
    }
}
