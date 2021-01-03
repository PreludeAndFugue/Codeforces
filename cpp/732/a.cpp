#include <iostream>

using namespace std;

int main() {
    int k;
    int r;
    cin >> k;
    cin >> r;
    int count = 1;
    int test;
    while (true) {
        test = (count * k) % 10;
        if (test == r || test == 0) {
            cout << count << endl;
            break;
        }
        count += 1;
    }
}
