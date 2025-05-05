//
// Created by Andrew Pham on 4/21/25.
//

#include "StringQueue.h"
#include <string>
#include <iostream>
#include <stdexcept>

StringQueue::StringQueue() {
    m_data = new std::string[8];
}

StringQueue::~StringQueue() {
    delete[] m_data;
}

StringQueue::StringQueue(const StringQueue& other) {
    m_data = new std::string[other.m_dataSize];
    m_dataSize = other.m_dataSize;
    m_count = other.m_count;
    m_front = other.m_front;
    m_rear = other.m_rear;
    for (size_t i = 0; i < m_count; ++i) {
        m_data[i] = other.m_data[i];
    }
}

StringQueue::StringQueue(StringQueue&& other) {
    m_data = other.m_data;
    m_dataSize = other.m_dataSize;
    m_count = other.m_count;
    m_front = other.m_front;
    m_rear = other.m_rear;
    other.m_data = nullptr;
    other.m_dataSize = 0;
    other.m_count = 0;
    other.m_front = 0;
    other.m_rear = 0;
}

StringQueue& StringQueue::operator=(const StringQueue& rhs) {
    if (this == &rhs) {
        return *this;
    }
    m_dataSize = rhs.m_dataSize;
    m_count = rhs.m_count;
    m_front = rhs.m_front;
    m_rear = rhs.m_rear;
    delete[] m_data;
    m_data = new std::string[rhs.m_dataSize];
    for (size_t i = 0; i < m_count; ++i) {
        m_data[i] = rhs.m_data[i];
    }
    return *this;
}

StringQueue& StringQueue::operator=(StringQueue&& rhs) {
    if (this == &rhs) {
        return *this;
    }
    delete[] m_data;
    m_data = rhs.m_data;
    m_dataSize = rhs.m_dataSize;
    m_count = rhs.m_count;
    m_front = rhs.m_front;
    m_rear = rhs.m_rear;
    rhs.m_data = nullptr;
    rhs.m_dataSize = 0;
    rhs.m_count = 0;
    rhs.m_front = 0;
    rhs.m_rear = 0;

    return *this;
}

size_t StringQueue::size() const {
    return m_count;
}

size_t StringQueue::capacity() const {
    return m_dataSize - m_count;
}

void StringQueue::clear() {
    m_count = 0;
    m_front = 0;
    m_rear = 0;
}

void StringQueue::enqueue(std::string value) {
    if (capacity() == 0) {
        std::string *newData = new std::string[m_dataSize * 2];
        for (size_t i = 0; i < m_count; ++i) {
            newData[i] = std::move(m_data[(m_front + i) % m_dataSize]);
        }
        m_dataSize *= 2;
        delete[] m_data;
        m_data = newData;
        m_front = 0;
        m_rear = m_count;
    }
    m_data[m_rear] = std::move(value);
    if (m_rear + 1 == m_dataSize) {
        m_rear = 0;
    }
    else {
        ++m_rear;
    }
    ++m_count;
}

std::string StringQueue::dequeue() { //fix this because what if you try to dequeue when queue is empty
    if (m_count == 0) {
        throw std::runtime_error("Can't dequeue from empty queue!");
    }
    std::string temp = std::move(m_data[m_front]);
    m_front = (m_front + 1) % m_dataSize;
    --m_count;
    return temp;
}

std::ostream& operator<<(std::ostream &lhs, const StringQueue &rhs) { //same for this, what happens when you try to print when queue is empty
    if (rhs.m_count == 0) {
        lhs << "Queue is empty";
    }
    for (size_t i = 0; i < rhs.m_count; ++i) {
        lhs << rhs.m_data[(rhs.m_front + i) % rhs.m_dataSize];
        if (i + 1 < rhs.m_count){
            lhs << ',';
        }
    }
    return lhs;
}