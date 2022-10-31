
from segunda_version import process_matrix, transform_matrix

def test_transform_matrix():
    assert transform_matrix([[2],[2],[2]]) == [[None,None,None],[None,2,None],[None,2,None],[None,2,None],[None,None,None]]
    assert transform_matrix([[2,3,4],[2,3,4],[2,3,4],[2,3,4]]) == [[None,None,None,None,None],[None,2,3,4,None],[None,2,3,4,None],[None,2,3,4,None],[None,2,3,4,None],[None,None,None,None,None]]


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