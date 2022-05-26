// logan@logan:~/VS Code Projects/Python/others$ g++ EBM11.cpp
// logan@logan:~/VS Code Projects/Python/others$ ./a.out

#include <iostream>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <string>
#define _USE_MATH_DEFINES
using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	srand(time(0));
	int Einf = 3000000, Rk = 4096, Vk = 9600, Mk = 17, Nosh = 6;
	cout << "Объем передаваемой информации = " << Einf << endl;
	cout << "Длина одного кадра = " << Rk << endl;
	cout << "Пропускная способность канала связи = " << Vk << endl;
	cout << "Количество каналов в многоканальной линии связи = " << Mk << endl;
	cout << "Число кадров в окне, принятых с ошибкой =" << Nosh << endl;
	float T1, T2;
	float Lk, Lzu, Ezu, Nk, Nok;
	cout << "Введите длину окна (количество кадров в окне) = ";
	cin >> Lk;
	Nok = ceil(Einf * pow (2,20)/ (double) Lk * Rk);
	cout << "Количество окон в передаваемом объёме информации = " << Nok << endl;
	T1 = (double) Nok * (Lk + Nosh) * Rk / Vk;
	cout << "Время передачи информации = " << T1;
	Lzu = Lk - 3;
	cout << "\nКоличество кадров данного окна, временно сохраняемых в буферном ЗУ = " << Lzu << endl;
	Ezu = Lzu * Rk * Mk;
	cout << "Необходимый объем буферного ЗУ = " << Ezu << endl;
	Nk = Lk - 2;
	cout << "Возвращение на Nк кадров = " << Nk << endl;
	T2 = (double) Nok * (Lk + Nk) * Rk / Vk;
	cout << "Время на передачу информации = " << T2 << endl;
	return 0;
}



// #include <iostream>
// #include <cmath>
// #include <ctime>
// #include <iomanip>
// #include <string>
// #define _USE_MATH_DEFINES
// using namespace std;

// int main()
// {
// 	setlocale(LC_ALL, "Russian");
// 	srand(time(0));
// 	int Einf = 5000000, Rk = 4096, Vk = 9600, Mk = 35, Nosh = 5;
// 	cout << "Объем передаваемой информации = " << Einf << endl;
// 	cout << "Длина одного кадра = " << Rk << endl;
// 	cout << "Пропускная способность канала связи = " << Vk << endl;
// 	cout << "Количество каналов в многоканальной линии связи = " << Mk << endl;
// 	cout << "Число кадров в окне, принятых с ошибкой =" << Nosh << endl;
// 	float T1, T2;
// 	float Lk, Lzu, Ezu, Nk, Nok;
// 	cout << "Введите длину окна (количество кадров в окне) = ";
// 	cin >> Lk;
// 	Nok = ceil(Einf * pow (2,20)/ (double) Lk * Rk);
// 	cout << "Количество окон в передаваемом объёме информации = " << Nok << endl;
// 	T1 = (double) Nok * (Lk + Nosh) * Rk / Vk;
// 	cout << "Время передачи информации = " << T1;
// 	Lzu = Lk - 3;
// 	cout << "Количество кадров данного окна, временно сохраняемых в буферном ЗУ = " << Lzu << endl;
// 	Ezu = Lzu * Rk * Mk;
// 	cout << "Необходимый объем буферного ЗУ = " << Ezu << endl;
// 	Nk = Lk - 2;
// 	cout << "Возвращение на Nк кадров = " << Nk << endl;
// 	T2 = (double) Nok * (Lk + Nk) * Rk / Vk;
// 	cout << "Время на передачу информации = " << T2 << endl;
// 	return 0;
// }