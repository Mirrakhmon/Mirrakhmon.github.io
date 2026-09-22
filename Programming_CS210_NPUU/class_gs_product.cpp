#include <iostream>
#include <string>
using namespace std;

class Product {
private:
    string name;
    double price;
    int quantity;

public:
    void setName(string n) { name = n; }
    string getName() { return name; }

    void setPrice(double p) {
        if (p < 0) {
            cout << "Invalid price!" << endl;
            return;
        }
        price = p;
    }
    double getPrice() { return price; }

    void setQuantity(int q) {
        if (q < 0) {
            cout << "Invalid quantity!" << endl;
            return;
        }
        quantity = q;
    }
    int getQuantity() { return quantity; }
};

int main() {
    Product p;
    p.setName("Notebook");
    p.setPrice(25000);
    p.setQuantity(10);

    p.setPrice(-500);   // rejected, old price stays

    cout << "Name: " << p.getName()
         << " | Price: " << p.getPrice()
         << " | Qty: " << p.getQuantity() << endl;
    return 0;
}