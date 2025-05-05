//
// Created by Andrew Pham on 4/21/25.
//

#ifndef STRINGQUEUE_H
#define STRINGQUEUE_H
#include <string>


class StringQueue {
    std::string* m_data;
    size_t m_dataSize = 8;
    size_t m_count = 0;
    size_t m_front = 0;
    size_t m_rear = 0;
public:
    StringQueue(); //finished
    ~StringQueue(); //finished
    StringQueue(const StringQueue& other); //finished
    StringQueue(StringQueue&& other); //finished

    StringQueue& operator=(const StringQueue& rhs);
    StringQueue& operator=(StringQueue&& rhs);


    size_t size() const;
    size_t capacity() const;
    void clear();
    void enqueue(std::string value);
    std::string dequeue();
    friend std::ostream& operator<<(std::ostream& lhs, const StringQueue& rhs);



};



#endif //STRINGQUEUE_H
