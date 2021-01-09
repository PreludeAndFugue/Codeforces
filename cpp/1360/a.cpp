#include <iostream>

using namespace std;

int area(int, int);

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int a, b;
        cin >> a >> b;
        cout << area(a, b) << endl;
    }
}


int area(int a, int b) {
    if (a < b) {
        int c = max(2 * a, b);
        return c * c;
    } else {
        int c = max(a, 2 * b);
        return c * c;
    }
}