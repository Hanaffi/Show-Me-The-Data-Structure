# Huffman Coding


I primarily used Dictionaries to store data as it allows for an _O_(1) runtime.
The Priority Queue, along with Node having a frequency parameter, allowed me to keep track of the frequencies of each letter. This helped in creating the Tree when having the pop the least frequent letter.


***Time** Complexity:*
O(nlogn) since I constantly run through the initial data when determining frequencies, building the priority queue, building the tree, creating the compressed data, and decompressing the data

***Space** Complexity:*
_O_(_n_) from storing the binary codes, priority queue, frequencies.
The rest of the data stored is _O_(1).

