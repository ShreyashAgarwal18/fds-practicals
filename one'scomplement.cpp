#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

void insert(Node*& head, int value) {
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = nullptr;
    newNode->prev = nullptr;

    if (head == nullptr) {
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    }
}

void printList(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data;
        temp = temp->next;
    }
    cout << endl;
}

void onesComplement(Node* head) {
    Node* temp = head;
    while (temp != nullptr) {
        temp->data = (temp->data == 0) ? 1 : 0;
        temp = temp->next;
    }
}

void twosComplement(Node* head) {
    onesComplement(head);

    Node* temp = head;
    Node* last = nullptr;

    while (temp->next != nullptr) {
        temp = temp->next;
    }
    last = temp;

    int carry = 1;
    while (last != nullptr) {
        int sum = last->data + carry;
        last->data = sum % 2;
        carry = sum / 2;
        last = last->prev;
    }
}

int main() {
    Node* head = nullptr;

    // Input binary number
    string binary;
    cout << "Enter binary number: ";
    cin >> binary;

    for (char ch : binary) {
        insert(head, ch - '0');
    }

    cout << "Original: ";
    printList(head);

    onesComplement(head);
    cout << "1's Complement: ";
    printList(head);

    twosComplement(head);
    cout << "2's Complement: ";
    printList(head);

    return 0;
}