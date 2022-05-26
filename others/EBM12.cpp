
//Листинг программы (2)
#include <iostream>
#include <string>
using namespace std;
class Confuse {
public:
    string k;
    Confuse(string k) {
        for (int i = 0; i < k.size(); ++i) {
            if (k[i] >= 'A' && k[i] <= 'Z')
                this->k += k[i];
            else if (k[i] >= 'a' && k[i] <= 'z')
                this->k += k[i] + 'A' - 'a';
        }
    }
    string encryption(string t) {
        string output;
        for (int i = 0, j = 0; i < t.length(); ++i) {
            char c = t[i];
            if (c >= 'a' && c <= 'z')
                c += 'A' - 'a';
            else if (c < 'A' || c > 'Z')
                continue;
            output += (c + k[j] - 2 * 'A') % 26 + 'A'; //added 'A' to bring it in range of ASCII alphabet [ 65-90 | A-Z ]
            j = (j + 1) % k.length();
        }
        return output;
    }
    string decryption(string t) {
        string output;
        for (int i = 0, j = 0; i < t.length(); ++i) {
            char c = t[i];
            if (c >= 'a' && c <= 'z')
                c += 'A' - 'a';
            else if (c < 'A' || c > 'Z')
                continue;
            output += (c - k[j] + 26) % 26 + 'A';//added 'A' to bring it in range of ASCII alphabet [ 65-90 | A-Z ]
            j = (j + 1) % k.length();
        }
        return output;
    }
};
int main() {
    string key;
    string ori;
    cout << "Enter your key word: ";
    cin >> key ;
    Confuse v(key);
    cout << "Enter string to encrypt: " << endl; cin >> ori;
    string encrypt = v.encryption(ori);
    string decrypt = v.decryption(encrypt);
    cout << "Original Message: " << ori << endl<<endl;
    cout << "Encrypted Message: " << encrypt << endl<<endl;
    cout << "Decrypted Message: " << decrypt << endl << endl;
    return 0;
}





