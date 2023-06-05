#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

int main()
{
    ofstream file("c:\\учеба\\ППОИС\\semestr4\\playground.txt");
    srand(time(NULL));;
    if (!file.is_open()) // вызов метода is_open()
        cout << "Все ПЛОХО! Файл закрыт!\n\n" << endl;
    string str = "";
    for (int i = 0; i < 45; i++) {
        for (int j = 0; j < 45; j++) {
            int animal = rand() % 5;
            switch (animal) {
            case 1:
                str += "P,";
            case 2:
                str += "H,";
            case 3:
                str += "G,";
            case 4:
                str += " ,";
            }
        }
        file << str << endl;
        str = "";
    }
    file.close();
}
