#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int m;
    int a;
    for (int i = 0; i < n; i++) {
        cin >> m;
        a = m / 2;
        cout << m - a - 1 << endl;
    }
}
