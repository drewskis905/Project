#include <iostream>
#include <string>
#include "StringQueue.h"
int main() {
    StringQueue q;
    StringQueue q1;
    StringQueue q2;
    StringQueue og;
    bool t5 = true;
    std::cout << "For test case 1: " << std::endl;
    for (int i = 0; i < 8; ++i) {
        q.enqueue(std::to_string(i));
    }
    std::cout << "Filled: " << q << std::endl;
    const std::string front = q.dequeue();
    std::cout << "Dequeued: " << front << std::endl;
    q.enqueue("8");
    std::cout << "After dequeuing and enqueuing: " << q << std::endl;

    std::cout << "\nFor test case 2: " << std::endl;
    for (int i = 0; i < 8; ++i) {
        q1.enqueue(std::to_string(i));
    }
    std::cout << "Filled: " << q1 << std::endl;
    for (int i = 0; i < 2; ++i) {
        std::cout << "Dequeued: " << q1.dequeue() << std::endl;
    }
    std::cout << "After dequeuing: " << q1 << std::endl;
    for (int i = 8; i <= 11; ++i) {
        q1.enqueue(std::to_string(i));
    }
    std::cout << "After resizing: " << q1 << std::endl;

    std::cout << "\nFor test case 3: " << std::endl;
    for (int i = 0; i < 8; ++i) {
        q2.enqueue(std::to_string(i));
    }
    std::cout << "Filled: " << q2 << std::endl;
    for (int i = 0; i < 8; ++i) {
        q2.dequeue();
    }
    std::cout << "After dequeue everything: " << q2 << std::endl;
    q2.enqueue("1");
    q2.enqueue("2");
    std::cout << "Queue after enqueuing: " << q2 << std::endl;

    std::cout << "\nFor test case 4: " << std::endl;
    for (int i = 0; i < 8; ++i) {
        og.enqueue(std::to_string(i));
    }
    std::cout << "Filled: " << og << std::endl;
    {
        StringQueue c = og;
        std::cout << "This is copy of the original: " << c << std::endl;
    }
    std::cout << "Original after copy went out of scope: " << og << std::endl;

    std::cout << "\nFor test case 5: " << std::endl;
    std::cout << "Existing queue: " << q1 << std::endl;
    if (t5) {
        StringQueue temp;
        temp.enqueue("41");
        temp.enqueue("23");
        temp.enqueue("99");
        std::cout << "Temporary before move: " << temp << std::endl;
        q2 = std::move(temp);
    }
    std::cout << "After move: " << q2 << std::endl;
    return 0;
}
