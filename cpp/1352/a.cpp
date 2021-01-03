#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

vector<int> parts(int);
int_fast64_t pow(int, int);


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        auto ps = parts(n);
        cout << ps.size() << endl;
        for (int p : ps) {
            cout << p << " ";
        }
        cout << endl;
    }
}


vector<int> parts(int n) {
    vector<int> ps;
    int i = 0;
    while (n) {
        int r = n % 10;
        if (r) {
            int p = r * pow(10, i);
            ps.push_back(p);
        }
        n /= 10;
        i += 1;
    }
    return ps;
}


// https://www.learncpp.com/cpp-tutorial/5-3-modulus-and-exponentiation/
int_fast64_t pow(int base, int exp)
{
    std::int_fast64_t result{ 1 };
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}
