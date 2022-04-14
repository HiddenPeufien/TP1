def secondMin(numbers):

    # initialisation
    m1 = m2 = float('inf')

    # algorithm
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x +1
            

    # return        
    if m2 == float('inf') or m2 == m1:
        m2 = None
    return m2
