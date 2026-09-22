#include<iostream>
#include<string>

using namespace std;

class Movie{
private:
    string title;
    int year;
public:
    void setInfo(string t,int y){
        title=t;
        year=y;
    }
    void display(){
        cout << "Title: " << title << " | Year: " << year << endl;
    }
};
int main(){
    Movie move1;
    //move1.title = "Inception";
    move1.setInfo("Inception",2010);
    move1.display();
    return 0;
}