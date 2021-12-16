## Quesiton 3

    Data communication and cloud computing largely depend on cryptography regardless of the type. Cryptography keeps senders and receivers to be assured that chances are high for non-targeted receivers in understanding the contents shared.

    In this context we are required to work on an encryption algorithm that will organize that text in a matrix guided by the key value such that data can be re-written in columns to produce encrypted data.

    For example,

**Text**: Plain text</br>
**Key**: 2

## Table
![image](image_50.jpeg)

    The key specifies the number of rows while the text length specifies the number of columns. The encrypting function will take two values text and the key, in the end it will return encrypted text. The decryption algorithm will equally have two arguments encrypted text and the key, it will return correct text

**Encrypted message:** Pantxli et (write a row after a row)

### Tasks to be complete

    Write algorithms that will implement the encryption and decryption in this context (You may choose to use the pseudo codes or natural English statements, it is up to your choice).
    Clarify the correctness of the algorithms by providing the actual implementation in a programming language (of your choice). Present the match between inputs and outputs.
    Highlight factors that make the algorithm simple and clear.
    What is the running time of the algorithm?
    Change the key to be 3 instead of 2, which algorithms among the two (the algorithm that has the key of 2 and the algorithm that has the key of 3) will tend to run slow (and which one will tend to run fast).