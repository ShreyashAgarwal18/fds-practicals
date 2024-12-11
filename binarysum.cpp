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

Node* addBinary(Node* head1, Node* head2) {
    Node* result = nullptr;
    Node* tail1 = head1;
    Node* tail2 = head2;

    while (tail1 && tail1->next) tail1 = tail1->next;
    while (tail2 && tail2->next) tail2 = tail2->next;

    int carry = 0;
    while (tail1 != nullptr || tail2 != nullptr || carry != 0) {
        int sum = carry;
        if (tail1 != nullptr) {
            sum += tail1->data;
            tail1 = tail1->prev;
        }
        if (tail2 != nullptr) {
            sum += tail2->data;
            tail2 = tail2->prev;
        }
        Node* newNode = new Node();
        newNode->data = sum % 2;
        newNode->next = result;
        if (result != nullptr) result->prev = newNode;
        result = newNode;
        carry = sum / 2;
    }
    return result;
}

int main() {
    Node* binary1 = nullptr;
    Node* binary2 = nullptr;

    string bin1, bin2;
    cout << "Enter first binary number: ";
    cin >> bin1;
    for (char ch : bin1) {
        insert(binary1, ch - '0');
    }

    cout << "Enter second binary number: ";
    cin >> bin2;
    for (char ch : bin2) {
        insert(binary2, ch - '0');
    }

    cout << "First Binary: ";
    printList(binary1);

    cout << "Second Binary: ";
    printList(binary2);

    Node* result = addBinary(binary1, binary2);

    cout << "Sum: ";
    printList(result);

    return 0;
}