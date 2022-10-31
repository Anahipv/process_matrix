from tercera_version import process_matrix

def test_process_matrix():

    assert process_matrix([]) == []
    assert process_matrix([[]]) == [[]]
    assert process_matrix([[],[],[]]) == [[],[],[]]
    assert process_matrix([[1,2,3]]) == [[1.5,2,2.5]]
    assert process_matrix([[1], [2], [3]]) == [[1.5], [2], [2.5]]
    assert process_matrix([[2,2],
                        [3,3], 
                        [4,4],
                        [5,5]]) == [[2.33, 2.33],[3,3],[4,4],[4.67,4.67]]
    assert process_matrix([[2,4,4,2],
                        [1,2,3,4],
                        [3,5,7,8]]) == [[2.33, 3, 3.25, 3.33], [2, 3, 4, 4.25], [3, 4.25, 5.75, 6.33]]