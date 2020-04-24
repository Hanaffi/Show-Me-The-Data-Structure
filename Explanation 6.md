# Union and Intersection

Union add all elements in list1 and list2 to a set which won't allow duplicate and then return a LinkedList of these elements

For Intersection we loop over every element of list1 and check if there is element equal to it in list2 , if True , add it to temporary set/list
then append all elements of this list to a linkedlist

***Time** Complexity:*
For Union , O(n)  because we iterate only one time for each list
For Intersection , O(n^2) 
***Space** Complexity:*
O(n) for both ,  because we use one list to store the union values and intersection values

