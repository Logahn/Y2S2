// logan@logan:~/VS Code Projects/Python/others$ g++ EBM8.cpp
// logan@logan:~/VS Code Projects/Python/others$ ./a.out
#include <iostream>
using namespace std;

int log(int x)
{
    x += 1;
    if (x == 2)
    {
        x = 0;
    }
    return x;
}

int main()
{
    int x1 = 0, x2 = 0, x3 = 0;
    cout << "X1 | X2 | X3 |  Y" << endl;
    for (int i = 0; i < 8; i++)
    {
        if (i != 0)
        {
            x3 += 1;
            {
                if (x3 == 2)
                {
                    x3 = 0;
                    x2 += 1;
                    if (x2 == 2)
                    {
                        x2 = 0;
                        x1 = 1;
                    }
                }
            }
        }
        int y = log(x2) + log(x1) * log(x3);
        if (y == 2)
        {
            y = 1;
        }
        cout << x1 << "  | " << x2 << "  |  " << x3 << " |  " << y << endl;
    }
}
