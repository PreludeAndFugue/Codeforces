#include <iostream>

using namespace std;

int main() {
    int x1, x2, x3;
    cin >> x1;
    cin >> x2;
    cin >> x3;

    int x_max = max(max(x1, x2), x3);
    int x_min = min(min(x1, x2), x3);

    cout << x_max - x_min << endl;
}
