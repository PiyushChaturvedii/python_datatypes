Binary Search:
1. Findout the middle element in the sorted list.
2. Compare "key" with the middle element.
3. if "key" matches with middle element, print message "key is found". STOP
4. else if key is greater than the middle element, the "key" is searched in right sublist. start with the step 1.

    fourmula to find mid:
            mid = low/high/2

main rule of binary search:
key == list1[mid]   fail
key  > list1[mid]   fail
key < list1[mid]   fail

no element is found
