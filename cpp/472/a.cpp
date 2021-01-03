#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int x;
    int y;
    if (n % 2) {
        x = 9;
        y = n - x;
    } else {
        x = 8;
        y = n - 8;
    }
    cout << x << " " << y << endl;
}
