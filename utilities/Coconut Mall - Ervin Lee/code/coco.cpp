#include <iostream>
#include <string>
#include <fstream>
using namespace std;


void ascii_art() {
    const char *ascii_art = R"(                                                                                                                           
        _|_|_|    _|_|      _|_|_|    _|_|    _|      _|  _|    _|  _|_|_|_|_|      _|      _|    _|_|    _|        _|        _|  
      _|        _|    _|  _|        _|    _|  _|_|    _|  _|    _|      _|          _|_|  _|_|  _|    _|  _|        _|        _|  
      _|        _|    _|  _|        _|    _|  _|  _|  _|  _|    _|      _|          _|  _|  _|  _|_|_|_|  _|        _|        _|  
      _|        _|    _|  _|        _|    _|  _|    _|_|  _|    _|      _|          _|      _|  _|    _|  _|        _|            
        _|_|_|    _|_|      _|_|_|    _|_|    _|      _|    _|_|        _|          _|      _|  _|    _|  _|_|_|_|  _|_|_|_|  _|  
    )";
    cout << ascii_art << endl;
}

void display_message() {
    cout << "Welcome to COCONUT MALL!" << endl;
    cout << "Where anything is possible..." << endl;
    cout << "Stand a chance to win the Golden Coconut!" << endl;
}

void print_flag() {
    ifstream file ("flag.txt");
    string str;
    while (getline(file, str)) {
        cout << str << endl;
    }
}

void display_options() {
    cout << "What would you like to buy?" << endl;
    cout << "1. Golden Coconut Shop" << endl;
    cout << "2. Regular Coconuts" << endl;
    cout << "3. Coconut Milk" << endl;
    cout << "4. Quit" << endl;
}

int golden_coconut(int wallet) {
    cout << "Welcome to the Golden Coconut Shop!" << endl;
    cout << "Here you can buy the Golden Coconut!" << endl;
    cout << "The Golden Coconut is a special coconut that can be used to buy anything in the mall!" << endl;
    cout << "It costs $100000.00" << endl;
    cout << "Your Wallet Balance: " << wallet << endl;
    cout << "Would you like to buy it?" << endl;
    cout << "1. Yes" << endl;
    cout << "2. No" << endl;
    int price = 100000;
    int choice;
    while (choice != 1 || choice != 2) {
        cin >> choice;
        if (choice == 1) {
            if (wallet >= price) {
                cout << "You have bought the Golden Coconut!" << endl;
                cout << "You can now buy anything in the mall!" << endl;
                print_flag();
                wallet -= price;
                return wallet;
            } else {
                cout << "You do not have enough money!" << endl;
                return wallet;
            }
        } else if (choice == 2) {
            cout << "You have chosen not to buy the Golden Coconut!" << endl;
            return wallet;
            break;
        } else {
            cout << "Invalid choice!" << endl;
            cout << "Your Wallet Balance: " << wallet << endl;
            cout << "Would you like to buy it?" << endl;
            cout << "1. Yes" << endl;
            cout << "2. No" << endl;
        }
    }
}

unsigned int regular_coconuts(unsigned int wallet) {
    cout << "Welcome to the Regular Coconut Shop!" << endl;
    cout << "Here you can buy Regular Coconuts!" << endl;
    cout << "Regular Coconuts are coconuts that can be used to buy anything in the mall!" << endl;
    cout << "It costs $100.00" << endl;
    cout << "Would you like to buy it?" << endl;
    cout << "Your Wallet Balance: " << wallet << endl;
    cout << "1. Yes" << endl;
    cout << "2. No" << endl;
    unsigned int price = 100.0;
    unsigned int quantity;
    int choice;
    while (choice != 1 && choice != 2) {
        cin >> choice;
        if (choice == 1) {
            cout << "How many Regular Coconuts would you like to buy?" << endl;
            cin >> quantity;
            price *= quantity;
            wallet -= price;
            return wallet;
        } else if (choice == 2) {
            cout << "You have chosen not to buy the Regular Coconuts!" << endl;
            return wallet;
        } else {
            cout << "Invalid choice!" << endl;
        }
    }
}

int main() {
    int money = 100;
    ascii_art();
    display_message();
    display_options();
    int choice;
    cin >> choice;
    while (choice != 4) {
        if (choice == 1) {
            money = golden_coconut(money);
            cout << "You have $" << money << " left!" << endl;
            display_options();
            cin >> choice;
        } else if (choice == 2) {
            money = regular_coconuts(money);
            cout << "You have $" << money << " left!" << endl;
            display_options();
            cin >> choice;
        } else if (choice == 3) {
            cout << "WE ARE OPENING SOON! STAY TUNED!" << endl;
            display_options();
            cin >> choice;
        } else {
            cout << "Invalid choice!" << endl;
            display_options();
            cin >> choice;
        }
    }
    return 0;
}