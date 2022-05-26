#include "pch.h"
#include "locale.h"
#include <iostream>
 
using namespace std;
 
class Pair
{
public:
    virtual void input() = 0;
    virtual void output() = 0;
    virtual void add(Pair*, Pair*)=0;
    virtual void sub(Pair*, Pair*)=0;
    virtual void mul(Pair*, Pair*)=0;
    virtual ~Pair() {};
};
 
class Money : public Pair
{
private:
    long int rub;
    unsigned char cop;
 
    void checkOver()
    {
        int sign = (rub < 0) ? -1 : 1;
        rub += cop / 100 * sign;
        cop %= 100;
    }
 
public:
    Money() : rub(0), cop(0) {};
 
    long int GetRub() { return rub; }
    unsigned char GetCop() { return cop; }
 
    virtual void input()
    {
        cout << "Введите сумму денег\n";
        cout << "Рубли: "; cin >> rub;
        cout << "Копейки: "; cin >> cop;
        this->checkOver();
    }
    virtual void output()
    {
        cout << "Cумма денег: " << rub << "," << cop;
    }
    virtual void add(Pair *s, Pair *t)
    {
        Money* sum2 = dynamic_cast<Money*>(s);
        Money* tmp = dynamic_cast<Money*>(t);
        tmp->rub = rub + sum2->rub;
        tmp->cop = cop + sum2->cop;
        tmp->checkOver();
    }
    
    virtual void sub(Pair *s, Pair *t)
    {
        Money* sum2 = dynamic_cast<Money*>(s);
        Money* tmp = dynamic_cast<Money*>(t);
        tmp->rub = rub - sum2->rub;
        tmp->cop = cop - sum2->cop;
        tmp->checkOver();
    }
 
    virtual void mul(Pair *a, Pair *t)
    {
        Money* arg = dynamic_cast<Money*>(a);
        Money* tmp = dynamic_cast<Money*>(t);
        float fullcop1, fullcop2, fullcop3;
        fullcop1 = (float)(rub * 100 + cop);
        fullcop2 = (float)(arg->rub * 100 + arg->cop);
        fullcop3 = (float)fullcop1*fullcop2;
        tmp->rub = (int)fullcop2;
        tmp->cop = (int)((fullcop2 - (int)fullcop2) * 100);
    }
 
  
};
 
class Fraction : public Pair
{
private:
    long num; //Целая часть
    unsigned short den; //Дробная часть
 
    int OrderFrac()
    {
        int i = 0, pden = den;
        {
            pden /= 10;
            i++;
        } while (den != 0);
        return i;
    }
 
    void MakeSameOrder(Fraction *frac2)
    {
        int ord1 = this->OrderFrac(),
            ord2 = frac2->OrderFrac();
        if (ord1 > ord2)
        for (int i = 1; i <= ord1 - ord2; i++)
            den *= 10;
        else
        for (int i = 1; i <= ord2 - ord1; i++)
            den *= 10;
    }
public:
    Fraction() : num(0), den(0) {};
 
    long GetNum() { return num; }
    unsigned short GetDen() { return den; }
 
    virtual void input()
    {
        cout << "Введите дробь\n";
        cout << "Целая часть: "; cin >> num;
        do
        {
            cout << "\nДробная часть: ";
            cin >> den;
            if (den < 0)
                cout << "Дробная часть должна быть неотрицательной! Повторите ввод.";
        } while (den < 0);
    }
 
    virtual void output()
    {
        cout << "Ваша дробь: " << num << "/" << den;
    }
 
    virtual void add(Pair *f, Pair *t)
    {
        Fraction* frac2 = dynamic_cast<Fraction*>(f);
        Fraction* tmp = dynamic_cast<Fraction*>(t);
        tmp->num = num + frac2->num;
        this->MakeSameOrder(frac2);
        tmp->den = den + frac2->den;
        int ordnew = tmp->OrderFrac();
        int ord = this->OrderFrac();
        if (ordnew > ord)
        {
            tmp->num++;
            int k = 10;
            for (int i = 1; i <= ordnew; i++)
                k *= 10;
            tmp->den %= k;
        }
 
    }
 
    virtual void sub(Pair *f, Pair *t)
    {
        Fraction* frac2 = dynamic_cast<Fraction*>(f);
        Fraction* tmp = dynamic_cast<Fraction*>(t);
        tmp->num = num - frac2->num;
        this->MakeSameOrder(frac2);
        if (frac2->den > den)
        {
            tmp->num--;
            int k = 1;
            int ord = frac2->OrderFrac();
            for (int i = 1; i <= ord; i++)
                k *= 10;
            tmp->den = k - abs(den - frac2->den);
        }
        else
            tmp->den = den - frac2->den;
    }
 
    virtual void mul(Pair *f, Pair *t)
    {
        Fraction* frac2 = dynamic_cast<Fraction*>(f);
        Fraction* tmp = dynamic_cast<Fraction*>(t);
        this->MakeSameOrder(frac2);
        int ordfrac = this->OrderFrac();
        int k = 1;
        for (int i = 1; i <= ordfrac; i++)
            k *= 10;
        int nm1 = num*k + den,
            nm2 = frac2->num*k + frac2->den;
        tmp->num = (nm1*nm2) / (k*k);
        tmp->den = (nm1*nm2) % (k*k);
    }
 
 
};
 
int _tmain(int argc, _TCHAR* argv[])
{
    setlocale(LC_ALL,"Russian");
    Pair* pr1, *pr2, *pr3;
    int i,j;
    cout << "С чем вы хотите работать?\n";
    cout << "1 - Money " << endl;
    cout << "2 - Fraction " << endl;
    cin >> i;
    if (i == 1) {
        pr1 = new Money();
        pr2 = new Money();
        pr3 = new Money();
        pr1->input();
    }
    else {
        pr1 = new Fraction();
        pr2 = new Fraction();
        pr3 = new Fraction();
        pr1->input();
    }
    cout << " 1 - Сложение;" << endl;
    cout << " 2 - Вычитание;" << endl;
    cout << " 3 - Умножение" << endl;
    cin >> j;
    switch (j)
    {
    case 1:pr2->input();
        cout << "Сложение: ";
        pr1->add(pr2, pr3);
        pr3->output();
        break;
    case 2:pr2->input(); 
        cout << "Вычитание: ";
        pr1->sub(pr2, pr3);
        pr3->output();
        break;
    case 3:pr2->input(); 
        cout << "Умножение: ";
        pr1->mul(pr2, pr3);
        pr3->output();
        break;
    }
delete pr1;
delete pr2;
delete pr3;
system("pause");
}