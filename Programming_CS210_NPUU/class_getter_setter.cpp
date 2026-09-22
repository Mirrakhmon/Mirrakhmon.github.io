#include<iostream>
#include<string>

using namespace std;

class Car{
public : 
    string brand;
    int speed;

    void showInfo(){
        cout << "Brand: " << brand << "  Speed: " << speed << " km/h" << endl;
    }

};

int main(){
    Car car1;
    car1.brand="Tesla M 3";
    car1.speed=210;

    Car car2;
    car2.brand="Chevrolet";
    car2.speed=200;

    car1.showInfo();
    car2.showInfo();

    return 0;
}