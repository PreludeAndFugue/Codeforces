#include <iostream>

using namespace std;

int nearest(int, int, int);

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int x, y, n;
        cin >> x >> y >> n;
        cout << nearest(x, y, n);
    }
}


int nearest(int x, int y, int n) {
    int a = n % x;
    if (a >= y) {
        return n + y - a;
    } else {
        return n - x + y - a;
    }
}
