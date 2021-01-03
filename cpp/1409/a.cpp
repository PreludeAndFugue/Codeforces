#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    int a;
    int b;
    for (int i = 0; i < t; i++) {
        cin >> a;
        cin >> b;
        int d = abs(b - a);
        int x = d / 10;
        x += d % 10 == 0 ? 0 : 1;
        cout << x << endl;
    }
}
