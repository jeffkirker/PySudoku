import unittest

from simpleSolver import *


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],  
    [5, 2, 0, 0, 0, 0, 0, 0, 0],  
    [0, 8, 7, 0, 0, 0, 0, 3, 1],  
    [0, 0, 3, 0, 1, 0, 0, 8, 0],  
    [9, 0, 0, 8, 6, 3, 0, 0, 5],  
    [0, 5, 0, 0, 9, 0, 6, 0, 0],  
    [1, 3, 0, 0, 0, 0, 2, 5, 0],  
    [0, 0, 0, 0, 0, 0, 0, 7, 4],  
    [0, 0, 5, 2, 0, 6, 3, 0, 0]]

board_soln = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6 ,9 ,2 ,3 ,5 ,1 ,8 ,7 ,4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9]]

class TestCheckRow(unittest.TestCase):
    def test_in_row(self):
        """
        Test to confirm value is in row
        """
        value = 5
        row = 0
        result = check_in_row(board, row, value)
        self.assertEqual(result, True)

    def test_not_in_row(self):
        """
        Test to confirm value is not in row
        """
        value = 2
        row = 0
        result = check_in_row(board, row, value)
        self.assertEqual(result, False)

class TestCheckCol(unittest.TestCase):
    def test_in_col(self):
        value = 5
        col = 0
        result = check_in_col(board,col,value)
        self.assertEqual(result, True)
    def test_not_in_col(self):
        value = 2
        col = 4
        result = check_in_col(board, col, value)
        self.assertEqual(result, False)


class TestCheckSubgrid(unittest.TestCase):
    def test_one_true(self):
        row = 1 
        col = 1
        num = 3
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_one_false(self):
        row = 1
        col = 1
        num = 4
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_two_true(self):
        row = 2 
        col = 3
        num = 5
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_two_false(self):
        row = 2
        col = 3
        num = 6
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_three_true(self):
        row = 2 
        col = 7
        num = 4
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_three_false(self):
        row = 2
        col = 7
        num = 9
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_four_true(self):
        row = 3 
        col = 1
        num = 9
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_four_false(self):
        row = 3
        col = 1
        num = 2
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_five_true(self):
        row = 4 
        col = 5
        num = 8
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_five_false(self):
        row = 4
        col = 5
        num = 7
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_six_true(self):
        row = 5 
        col = 8
        num = 5
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_six_false(self):
        row = 5
        col = 8
        num = 3
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_seven_true(self):
        row = 6 
        col = 2
        num = 1
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_seven_false(self):
        row = 6
        col = 2
        num = 2
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_eight_true(self):
        row = 7 
        col = 4
        num = 2
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_eight_false(self):
        row = 7
        col = 4
        num = 4
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
    def test_nine_true(self):
        row = 8 
        col = 8
        num = 4
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, True)
    def test_nine_false(self):
        row = 8
        col = 8
        num = 6
        result = check_in_subgrid(board, row, col, num)
        self.assertEqual(result, False)
        
class TestEmptyExists(unittest.TestCase):
    def test_empty_cell(self):
        row = 0
        col = 0
        result = empty_exists(board)
        self.assertEqual(result, True)

    def test_no_empty(self):
        row = 0
        col = 0
        result = empty_exists(board_soln)
        self.assertEqual(result, False)

class TestSolver(unittest.TestCase):
    def test_solver(self):
        result = solve_sudoku(board)
        self.assertEqual(result, board)

if __name__ == '__main__':
    unittest.main()       