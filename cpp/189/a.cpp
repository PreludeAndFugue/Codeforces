#include <iostream>


int test(int n, int a, int b, int c) {
    if (a == 1 || b == 1 || c == 1) {
        return n;
    }
    if (a == 2 || b == 2 || c == 2) {
        if (n % 2 == 0) {
            return n / 2;
        }
    }
    int m = 0;
    for (int i = 0; i <= n/a; i++) {
        int a_i = a*i;
        if (a_i > n) {
            break;
        }
        for (int j = 0; j <= n/b; j++) {
            int b_j = b*j;
            if (a_i + b_j > n) {
                break;
            }
            for (int k = 0; k <= n/c; k++) {
                int c_k = c*k;
                if (a_i + b_j + c_k > n) {
                    break;
                }
                if (a_i + b_j + c_k == n) {
                    m = std::max(m, i + j + k);
                }
            }
        }
    }
    return m;
}


int main() {
    int n, a, b, c;
    std::cin >> n >> a >> b >> c;

    int m = test(n, a, b, c);

    std::cout << m << std::endl;
}
