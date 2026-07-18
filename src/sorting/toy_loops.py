def forward_loop_with_left_backtrack(array):
    ''' Outer loop skips the first position and moves forward by 1 while 
        inner loop moves backward by one over the subarray [0, i]. 

        Used for insertion sort.
    '''

    # skip first position and iterate to end
    for i in range(1, len(array)):
        # backtrack from i-th to start
        for j in range(i-1, 0, -1):
            print(f'outer: {i}, inner: {j}, values: ({array[i]}, {array[j]})')


def forward_loop_with_right_backtrack(array):
    ''' Outer loop moves forward by 1 while inner loop moves backward by one
        over the subarray [i+1, len(array)] meaning that the i-th position is
        excluded from the outer loop. 

        Used for bubble sort, and selection sort.
    '''

    # iterate from start to right but skip last position
    for i in range(len(array)-1):
        # backtrack from end to i-th position
        for j in range(len(array)-1, i, -1):
            #print(array[j])
            print(f'outer: {i}, inner: {j}, values: ({array[i]}, {array[j]})')


def visualize_shell_sort(array):
    ''' A Selection sort over a 'gap' step, rather than consecutive, space
        between positions. The gap decrements by a factor of 2 each iteration. 
    '''
    decrement_factor: int = 3
    gap: int = len(array) // decrement_factor     # floor division

    while gap > 0:
        print(f'Current Gap: {gap}')
        # skip first subarray so there is a previous position for compare
        for i in range(gap, len(array)):
            j = i
            while j >= 0:
                prev = j - gap
                curr = j

                # guards left out of bounds prev index
                if prev < 0:
                    break

                print(f'comparing indicies: {prev}, {curr}')
                j -= gap

        gap //= decrement_factor


if __name__ == "__main__":
    forward = [1, 2, 3, 4, 5, 6, 7, 8]
    backward = [8, 7, 6, 5, 4, 3, 2, 1]
    array = forward

    '''
    print('forward loop with left backtrack')
    print(f'array used: {array}')
    forward_loop_with_left_backtrack(array)
    print('-'*10)

    print('forward loop with right backtrack')
    print(f'array used: {array}')
    forward_loop_with_right_backtrack(array)
    print('-'*10)
    '''

    print('shell sort selector')
    print(f'array used: {array}')
    visualize_shell_sort(array)
    print('-'*10)

