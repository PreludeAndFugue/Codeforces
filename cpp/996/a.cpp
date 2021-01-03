#include <iostream>

using namespace std;

int main() {
    constexpr int denominations[] { 100, 20, 10, 5, 1 };
    int n;
    cin >> n;

    int answer = 0;
    for (int d : denominations) {
        int c = n / d;
        if (c == 0) {
            continue;
        }
        n -= c * d;
        answer += c;
        if (n == 0) {
            break;
        }
    }

    cout << answer << endl;
}
