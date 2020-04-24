# File Recursion


I used recursion and concatenated each new file found to the path , then append this path to the list and return it

***Time** Complexity:*
O(n*m)  because we loop over sub-directories `m` and the number of files in each directory `n`

***Space** Complexity:*
O(n*m) as the worst case we will have n files to hold and m sub-directories to search
