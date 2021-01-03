#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int a;
        int b;
        cin >> a;
        cin >> b;

        int r = a % b;
        int d = (b - r) % b;

        cout << d << endl;
    }

    cout << endl;
}
