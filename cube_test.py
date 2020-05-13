""" 测试三阶魔方的各种复原方法的正确性

    the statistics of this file:
    lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
    000000001845    ----------------------m    00000000000001    0000000000000000    ~~~~~~~~~~~~~
"""

import unittest

import numpy as np

import recover_rubik_cube


class CubeTestCase(unittest.TestCase):
    def test_one_face_clockwise_90(self):
        """ 测试某个面顺时针旋转90°
        """
        self.skipTest('跳过test_one_face_clockwise_90')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['white', 'green'],
                  ['white'],
                  ['white', 'blue']],
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'white', 'red'],
                  ['green', 'red'],
                  ['green', 'yellow', 'red']],
                 [['green', 'white'],
                  ['green'],
                  ['green', 'yellow']],
                 [['green', 'white', 'orange'],
                  ['green', 'orange'],
                  ['green', 'yellow', 'orange']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.one_face_clockwise_90(self.standard_color_cube, 4)
        # print(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_one_face_anticlockwise_90(self):
        """ 测试某个面逆时针旋转90°
        """
        self.skipTest('跳过test_one_face_anticlockwise_90')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['white', 'green'],
                  ['white'],
                  ['white', 'blue']],
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'yellow', 'red'],
                  ['blue', 'red'],
                  ['blue', 'white', 'red']],
                 [['blue', 'yellow'],
                  ['blue'],
                  ['blue', 'white']],
                 [['blue', 'yellow', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'white', 'orange']]]
            ]
        )
        recover_rubik_cube.one_face_anticlockwise_90(self.standard_color_cube, 5)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_y_right_hand_positive_90(self):
        """ 测试沿着Y轴右手定理旋转90°
        """
        self.skipTest('跳过test_y_right_hand_positive_90')
        test_cube = np.array(
            [
                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'green', 'white'],
                  ['red', 'white'],
                  ['red', 'blue', 'white']],
                 [['red', 'green'],
                  ['red'],
                  ['red', 'blue']],
                 [['red', 'green', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'blue', 'yellow']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['white', 'blue', 'red'],
                  ['white', 'red'],
                  ['white', 'green', 'red']],
                 [['white', 'blue'],
                  ['white'],
                  ['white', 'green']],
                 [['white', 'blue', 'orange'],
                  ['white', 'orange'],
                  ['white', 'green', 'orange']]],

                [[['green', 'white', 'red'],
                  ['green', 'red'],
                  ['green', 'yellow', 'red']],
                 [['green', 'white'],
                  ['green'],
                  ['green', 'yellow']],
                 [['green', 'white', 'orange'],
                  ['green', 'orange'],
                  ['green', 'yellow', 'orange']]],

                [[['blue', 'yellow', 'red'],
                  ['blue', 'red'],
                  ['blue', 'white', 'red']],
                 [['blue', 'yellow'],
                  ['blue'],
                  ['blue', 'white']],
                 [['blue', 'yellow', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'white', 'orange']]]
            ]
        )
        recover_rubik_cube.y_right_hand_positive_90(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_y_right_hand_negative_90(self):
        """ 测试沿着Y轴右手定理旋转-90°
        """
        self.skipTest('跳过test_y_right_hand_negative_90')
        test_cube = np.array(
            [
                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'green', 'white'],
                  ['red', 'white'],
                  ['red', 'blue', 'white']],
                 [['red', 'green'],
                  ['red'],
                  ['red', 'blue']],
                 [['red', 'green', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'blue', 'yellow']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['white', 'blue', 'red'],
                  ['white', 'red'],
                  ['white', 'green', 'red']],
                 [['white', 'blue'],
                  ['white'],
                  ['white', 'green']],
                 [['white', 'blue', 'orange'],
                  ['white', 'orange'],
                  ['white', 'green', 'orange']]],

                [[['green', 'white', 'red'],
                  ['green', 'red'],
                  ['green', 'yellow', 'red']],
                 [['green', 'white'],
                  ['green'],
                  ['green', 'yellow']],
                 [['green', 'white', 'orange'],
                  ['green', 'orange'],
                  ['green', 'yellow', 'orange']]],

                [[['blue', 'yellow', 'red'],
                  ['blue', 'red'],
                  ['blue', 'white', 'red']],
                 [['blue', 'yellow'],
                  ['blue'],
                  ['blue', 'white']],
                 [['blue', 'yellow', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'white', 'orange']]]
            ]
        )
        recover_rubik_cube.y_right_hand_negative_90(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_x_right_hand_positive_90(self):
        """ 测试沿着X轴右手定理旋转90°
        """
        self.skipTest('跳过test_x_right_hand_positive_90')
        test_cube = np.array(
            [
                [[['green', 'yellow', 'orange'],
                  ['green', 'orange'],
                  ['green', 'white', 'orange']],
                 [['green', 'yellow'],
                  ['green'],
                  ['green', 'white']],
                 [['green', 'yellow', 'red'],
                  ['green', 'red'],
                  ['green', 'white', 'red']]],

                [[['blue', 'yellow', 'red'],
                  ['blue', 'red'],
                  ['blue', 'white', 'red']],
                 [['blue', 'yellow'],
                  ['blue'],
                  ['blue', 'white']],
                 [['blue', 'yellow', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'white', 'orange']]],

                [[['orange', 'yellow', 'blue'],
                  ['orange', 'blue'],
                  ['orange', 'white', 'blue']],
                 [['orange', 'yellow'],
                  ['orange'],
                  ['orange', 'white']],
                 [['orange', 'yellow', 'green'],
                  ['orange', 'green'],
                  ['orange', 'white', 'green']]],

                [[['red', 'white', 'blue'],
                  ['red', 'blue'],
                  ['red', 'yellow', 'blue']],
                 [['red', 'white'],
                  ['red'],
                  ['red', 'yellow']],
                 [['red', 'white', 'green'],
                  ['red', 'green'],
                  ['red', 'yellow', 'green']]],

                [[['yellow', 'red', 'blue'],
                  ['yellow', 'blue'],
                  ['yellow', 'orange', 'blue']],
                 [['yellow', 'red'],
                  ['yellow'],
                  ['yellow', 'orange']],
                 [['yellow', 'red', 'green'],
                  ['yellow', 'green'],
                  ['yellow', 'orange', 'green']]],

                [[['white', 'orange', 'blue'],
                  ['white', 'blue'],
                  ['white', 'red', 'blue']],
                 [['white', 'orange'],
                  ['white'],
                  ['white', 'red']],
                 [['white', 'orange', 'green'],
                  ['white', 'green'],
                  ['white', 'red', 'green']]]
            ]
        )
        recover_rubik_cube.x_right_hand_positive_90(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_x_right_hand_negative_90(self):
        """ 测试沿着X轴右手定理旋转-90°
        """
        self.skipTest('跳过test_x_right_hand_negative_90')
        test_cube = np.array(
            [
                [[['green', 'yellow', 'orange'],
                  ['green', 'orange'],
                  ['green', 'white', 'orange']],
                 [['green', 'yellow'],
                  ['green'],
                  ['green', 'white']],
                 [['green', 'yellow', 'red'],
                  ['green', 'red'],
                  ['green', 'white', 'red']]],

                [[['blue', 'yellow', 'red'],
                  ['blue', 'red'],
                  ['blue', 'white', 'red']],
                 [['blue', 'yellow'],
                  ['blue'],
                  ['blue', 'white']],
                 [['blue', 'yellow', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'white', 'orange']]],

                [[['orange', 'yellow', 'blue'],
                  ['orange', 'blue'],
                  ['orange', 'white', 'blue']],
                 [['orange', 'yellow'],
                  ['orange'],
                  ['orange', 'white']],
                 [['orange', 'yellow', 'green'],
                  ['orange', 'green'],
                  ['orange', 'white', 'green']]],

                [[['red', 'white', 'blue'],
                  ['red', 'blue'],
                  ['red', 'yellow', 'blue']],
                 [['red', 'white'],
                  ['red'],
                  ['red', 'yellow']],
                 [['red', 'white', 'green'],
                  ['red', 'green'],
                  ['red', 'yellow', 'green']]],

                [[['yellow', 'red', 'blue'],
                  ['yellow', 'blue'],
                  ['yellow', 'orange', 'blue']],
                 [['yellow', 'red'],
                  ['yellow'],
                  ['yellow', 'orange']],
                 [['yellow', 'red', 'green'],
                  ['yellow', 'green'],
                  ['yellow', 'orange', 'green']]],

                [[['white', 'orange', 'blue'],
                  ['white', 'blue'],
                  ['white', 'red', 'blue']],
                 [['white', 'orange'],
                  ['white'],
                  ['white', 'red']],
                 [['white', 'orange', 'green'],
                  ['white', 'green'],
                  ['white', 'red', 'green']]]
            ]
        )
        recover_rubik_cube.x_right_hand_negative_90(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_z_right_hand_positive_90(self):
        """ 测试沿着Z轴右手定理旋转90°
        """
        self.skipTest('跳过test_z_right_hand_positive_90')
        test_cube = np.array(
            [
                [[['white', 'red', 'green'],
                  ['white', 'green'],
                  ['white', 'orange', 'green']],
                 [['white', 'red'],
                  ['white'],
                  ['white', 'orange']],
                 [['white', 'red', 'blue'],
                  ['white', 'blue'],
                  ['white', 'orange', 'blue']]],

                [[['yellow', 'red', 'blue'],
                  ['yellow', 'blue'],
                  ['yellow', 'orange', 'blue']],
                 [['yellow', 'red'],
                  ['yellow'],
                  ['yellow', 'orange']],
                 [['yellow', 'red', 'green'],
                  ['yellow', 'green'],
                  ['yellow', 'orange', 'green']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]]
            ]
        )
        recover_rubik_cube.z_right_hand_positive_90(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_z_right_hand_negative_90(self):
        """ 测试沿着Z轴右手定理旋转-90°
        """
        self.skipTest('跳过test_z_right_hand_negative_90')
        test_cube = np.array(
            [
                [[['white', 'red', 'green'],
                  ['white', 'green'],
                  ['white', 'orange', 'green']],
                 [['white', 'red'],
                  ['white'],
                  ['white', 'orange']],
                 [['white', 'red', 'blue'],
                  ['white', 'blue'],
                  ['white', 'orange', 'blue']]],

                [[['yellow', 'red', 'blue'],
                  ['yellow', 'blue'],
                  ['yellow', 'orange', 'blue']],
                 [['yellow', 'red'],
                  ['yellow'],
                  ['yellow', 'orange']],
                 [['yellow', 'red', 'green'],
                  ['yellow', 'green'],
                  ['yellow', 'orange', 'green']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]]
            ]
        )
        recover_rubik_cube.z_right_hand_negative_90(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_f_clockwise(self):
        """ 测试沿着F顺时针旋转90°
        """
        self.skipTest('跳过test_f_clockwise')
        test_cube = np.array(
            [
                [[['blue', 'white', 'orange'],  # c
                  ['blue', 'orange'],  # c
                  ['blue', 'yellow', 'orange']],  # c
                 [['white', 'green'],
                  ['white'],  # D
                  ['white', 'blue']],
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['green', 'white', 'orange'],  # c
                  ['green', 'orange'],  # c
                  ['green', 'yellow', 'orange']]],  # c

                [[['orange', 'white', 'green'],
                  ['orange', 'green'],
                  ['orange', 'yellow', 'green']],
                 [['orange', 'white'],
                  ['orange'],  # F, clockwise
                  ['orange', 'yellow']],
                 [['orange', 'white', 'blue'],
                  ['orange', 'blue'],
                  ['orange', 'yellow', 'blue']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],  # B
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['white', 'orange', 'green']],  # c
                 [['green', 'red'],
                  ['green'],  # L
                  ['white', 'orange']],  # c
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['white', 'orange', 'blue']]],  # c

                [[['yellow', 'orange', 'green'],  # c
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['yellow', 'orange'],  # c
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['yellow', 'orange', 'blue'],  # c
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.f_clockwise(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_f_anticlockwise(self):
        """ 测试沿着F逆时针旋转90°
        """
        self.skipTest('跳过test_f_anticlockwise')
        test_cube = np.array(
            [
                [[['blue', 'white', 'orange'],  # c
                  ['blue', 'orange'],  # c
                  ['blue', 'yellow', 'orange']],  # c
                 [['white', 'green'],
                  ['white'],  # D
                  ['white', 'blue']],
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['green', 'white', 'orange'],  # c
                  ['green', 'orange'],  # c
                  ['green', 'yellow', 'orange']]],  # c

                [[['orange', 'white', 'green'],
                  ['orange', 'green'],
                  ['orange', 'yellow', 'green']],
                 [['orange', 'white'],
                  ['orange'],  # F, clockwise
                  ['orange', 'yellow']],
                 [['orange', 'white', 'blue'],
                  ['orange', 'blue'],
                  ['orange', 'yellow', 'blue']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],  # B
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['white', 'orange', 'green']],  # c
                 [['green', 'red'],
                  ['green'],  # L
                  ['white', 'orange']],  # c
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['white', 'orange', 'blue']]],  # c

                [[['yellow', 'orange', 'green'],  # c
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['yellow', 'orange'],  # c
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['yellow', 'orange', 'blue'],  # c
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.f_anticlockwise(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_b_clockwise(self):
        """ 测试沿着B顺时针旋转90°
        """
        self.skipTest('跳过test_b_clockwise')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['white', 'green'],
                  ['white'],  # D
                  ['white', 'blue']],
                 [['green', 'yellow', 'red'],  # c
                  ['green', 'red'],  # c
                  ['green', 'white', 'red']]],  # c

                [[['blue', 'yellow', 'red'],  # c
                  ['blue', 'red'],  # c
                  ['blue', 'white', 'red']],  # c
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'white', 'blue'],
                  ['red', 'blue'],
                  ['red', 'yellow', 'blue']],
                 [['red', 'white'],
                  ['red'],  # B, clockwise
                  ['red', 'yellow']],
                 [['red', 'white', 'green'],
                  ['red', 'green'],
                  ['red', 'yellow', 'green']]],

                [[['yellow', 'red', 'blue'],  # c
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['yellow', 'red'],  # c
                  ['green'],  # L
                  ['green', 'orange']],
                 [['yellow', 'red', 'green'],  # c
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['white', 'red', 'blue']],  # c
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['white', 'red']],  # c
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['white', 'red', 'green']]]  # c
            ]
        )
        recover_rubik_cube.b_clockwise(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_b_anticlockwise(self):
        """ 测试沿着B逆时针旋转90°
        """
        self.skipTest('跳过test_b_anticlockwise')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['white', 'green'],
                  ['white'],  # D
                  ['white', 'blue']],
                 [['green', 'yellow', 'red'],  # c
                  ['green', 'red'],  # c
                  ['green', 'white', 'red']]],  # c

                [[['blue', 'yellow', 'red'],  # c
                  ['blue', 'red'],  # c
                  ['blue', 'white', 'red']],  # c
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'white', 'blue'],
                  ['red', 'blue'],
                  ['red', 'yellow', 'blue']],
                 [['red', 'white'],
                  ['red'],  # B, clockwise
                  ['red', 'yellow']],
                 [['red', 'white', 'green'],
                  ['red', 'green'],
                  ['red', 'yellow', 'green']]],

                [[['yellow', 'red', 'blue'],  # c
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['yellow', 'red'],  # c
                  ['green'],  # L
                  ['green', 'orange']],
                 [['yellow', 'red', 'green'],  # c
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['white', 'red', 'blue']],  # c
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['white', 'red']],  # c
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['white', 'red', 'green']]]  # c
            ]
        )
        recover_rubik_cube.b_anticlockwise(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_d_clockwise(self):
        """ 测试沿着D顺时针旋转90°
        """
        self.skipTest('跳过test_d_clockwise')
        test_cube = np.array(
            [
                [[['white', 'red', 'green'],
                  ['white', 'green'],
                  ['white', 'orange', 'green']],
                 [['white', 'red'],
                  ['white'],  # D, clockwise
                  ['white', 'orange']],
                 [['white', 'red', 'blue'],
                  ['white', 'blue'],
                  ['white', 'orange', 'blue']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['green', 'red', 'white'],  # c
                  ['green', 'white'],  # c
                  ['green', 'orange', 'white']]],  # c

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],  # B
                  ['red', 'green']],
                 [['blue', 'orange', 'white'],  # c
                  ['blue', 'white'],  # c
                  ['blue', 'red', 'white']]],  # c

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],  # L
                  ['green', 'orange']],
                 [['red', 'blue', 'white'],  # c
                  ['red', 'white'],  # c
                  ['red', 'green', 'white']]],  # c

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['orange', 'green', 'white'],  # c
                  ['orange', 'white'],  # c
                  ['orange', 'blue', 'white']]]  # c
            ]
        )
        recover_rubik_cube.d_clockwise(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_d_anticlockwise(self):
        """ 测试沿着D逆时针旋转90°
        """
        self.skipTest('跳过test_d_anticlockwise')
        test_cube = np.array(
            [
                [[['white', 'red', 'green'],
                  ['white', 'green'],
                  ['white', 'orange', 'green']],
                 [['white', 'red'],
                  ['white'],  # D, clockwise
                  ['white', 'orange']],
                 [['white', 'red', 'blue'],
                  ['white', 'blue'],
                  ['white', 'orange', 'blue']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['green', 'red', 'white'],  # c
                  ['green', 'white'],  # c
                  ['green', 'orange', 'white']]],  # c

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],  # B
                  ['red', 'green']],
                 [['blue', 'orange', 'white'],  # c
                  ['blue', 'white'],  # c
                  ['blue', 'red', 'white']]],  # c

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],  # L
                  ['green', 'orange']],
                 [['red', 'blue', 'white'],  # c
                  ['red', 'white'],  # c
                  ['red', 'green', 'white']]],  # c

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['orange', 'green', 'white'],  # c
                  ['orange', 'white'],  # c
                  ['orange', 'blue', 'white']]]  # c
            ]
        )
        recover_rubik_cube.d_anticlockwise(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_u_clockwise(self):
        """ 测试沿着U顺时针旋转90°
        """
        self.skipTest('跳过test_u_clockwise')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['white', 'green'],
                  ['white'],  # D
                  ['white', 'blue']],
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['yellow', 'orange', 'green'],
                  ['yellow', 'green'],
                  ['yellow', 'red', 'green']],
                 [['yellow', 'orange'],
                  ['yellow'],  # U, clockwise
                  ['yellow', 'red']],
                 [['yellow', 'orange', 'blue'],
                  ['yellow', 'blue'],
                  ['yellow', 'red', 'blue']]],

                [[['blue', 'orange', 'yellow'],  # c
                  ['blue', 'yellow'],  # c
                  ['blue', 'red', 'yellow']],  # c
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['green', 'red', 'yellow'],  # c
                  ['green', 'yellow'],  # c
                  ['green', 'orange', 'yellow']],  # c
                 [['red', 'blue'],
                  ['red'],  # B
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['orange', 'green', 'yellow'],  # c
                  ['orange', 'yellow'],  # c
                  ['orange', 'blue', 'yellow']],  # c
                 [['green', 'red'],
                  ['green'],  # L
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['red', 'blue', 'yellow'],  # c
                  ['red', 'yellow'],  # c
                  ['red', 'green', 'yellow']],  # c
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.u_clockwise(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_u_anticlockwise(self):
        """ 测试沿着U逆时针旋转90°
        """
        self.skipTest('跳过test_u_anticlockwise')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['white', 'green'],
                  ['white'],  # D
                  ['white', 'blue']],
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['yellow', 'orange', 'green'],
                  ['yellow', 'green'],
                  ['yellow', 'red', 'green']],
                 [['yellow', 'orange'],
                  ['yellow'],  # U, clockwise
                  ['yellow', 'red']],
                 [['yellow', 'orange', 'blue'],
                  ['yellow', 'blue'],
                  ['yellow', 'red', 'blue']]],

                [[['blue', 'orange', 'yellow'],  # c
                  ['blue', 'yellow'],  # c
                  ['blue', 'red', 'yellow']],  # c
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['green', 'red', 'yellow'],  # c
                  ['green', 'yellow'],  # c
                  ['green', 'orange', 'yellow']],  # c
                 [['red', 'blue'],
                  ['red'],  # B
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['orange', 'green', 'yellow'],  # c
                  ['orange', 'yellow'],  # c
                  ['orange', 'blue', 'yellow']],  # c
                 [['green', 'red'],
                  ['green'],  # L
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['red', 'blue', 'yellow'],  # c
                  ['red', 'yellow'],  # c
                  ['red', 'green', 'yellow']],  # c
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.u_anticlockwise(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_l_clockwise(self):
        """ 测试沿着L顺时针旋转90°
        """
        self.skipTest('跳过test_l_clockwise')
        test_cube = np.array(
            [
                [[['orange', 'green', 'yellow'],  # c
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['orange', 'green'],  # c
                  ['white'],  # D
                  ['white', 'blue']],
                 [['orange', 'green', 'white'],  # c
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['red', 'green', 'white'],  # c
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['red', 'green'],  # c
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['red', 'green', 'yellow'],  # c
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['yellow', 'green', 'red'],  # c
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['yellow', 'green'],  # c
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['yellow', 'green', 'orange'],  # c
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['white', 'green', 'red']],  # c
                 [['red', 'blue'],
                  ['red'],  # B
                  ['white', 'green']],  # c
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['white', 'green', 'orange']]],  # c

                [[['green', 'white', 'red'],
                  ['green', 'red'],
                  ['green', 'yellow', 'red']],
                 [['green', 'white'],
                  ['green'],  # L, clockwise
                  ['green', 'yellow']],
                 [['green', 'white', 'orange'],
                  ['green', 'orange'],
                  ['green', 'yellow', 'orange']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.l_clockwise(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_l_anticlockwise(self):
        """ 测试沿着L逆时针旋转90°
        """
        self.skipTest('跳过test_l_anticlockwise')
        test_cube = np.array(
            [
                [[['orange', 'green', 'yellow'],  # c
                  ['white', 'orange'],
                  ['white', 'blue', 'orange']],
                 [['orange', 'green'],  # c
                  ['white'],  # D
                  ['white', 'blue']],
                 [['orange', 'green', 'white'],  # c
                  ['white', 'red'],
                  ['white', 'blue', 'red']]],

                [[['red', 'green', 'white'],  # c
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['red', 'green'],  # c
                  ['yellow'],  # U
                  ['yellow', 'blue']],
                 [['red', 'green', 'yellow'],  # c
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['yellow', 'green', 'red'],  # c
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['yellow', 'green'],  # c
                  ['orange'],  # F
                  ['orange', 'blue']],
                 [['yellow', 'green', 'orange'],  # c
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['white', 'green', 'red']],  # c
                 [['red', 'blue'],
                  ['red'],  # B
                  ['white', 'green']],  # c
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['white', 'green', 'orange']]],  # c

                [[['green', 'white', 'red'],
                  ['green', 'red'],
                  ['green', 'yellow', 'red']],
                 [['green', 'white'],
                  ['green'],  # L, clockwise
                  ['green', 'yellow']],
                 [['green', 'white', 'orange'],
                  ['green', 'orange'],
                  ['green', 'yellow', 'orange']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],  # R
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ]
        )
        recover_rubik_cube.l_anticlockwise(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_r_clockwise(self):
        """ 测试沿着R顺时针旋转90°
        """
        self.skipTest('跳过test_r_clockwise')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['red', 'blue', 'white']],  # c
                 [['white', 'green'],
                  ['white'],  # D
                  ['red', 'blue']],  # c
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['red', 'blue', 'yellow']]],  # c

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['orange', 'blue', 'yellow']],  # c
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['orange', 'blue']],  # c
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['orange', 'blue', 'white']]],  # c

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['white', 'blue', 'orange']],  # c
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['white', 'blue']],  # c
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['white', 'blue', 'red']]],  # c

                [[['yellow', 'blue', 'orange'],  # c
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['yellow', 'blue'],  # c
                  ['red'],  # B
                  ['red', 'green']],
                 [['yellow', 'blue', 'red'],  # c
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],  # L
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'white', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'yellow', 'orange']],
                 [['blue', 'white'],
                  ['blue'],  # R, clockwise
                  ['blue', 'yellow']],
                 [['blue', 'white', 'red'],
                  ['blue', 'red'],
                  ['blue', 'yellow', 'red']]]
            ]
        )
        recover_rubik_cube.r_clockwise(self.standard_color_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_r_anticlockwise(self):
        """ 测试沿着R逆时针旋转90°
        """
        self.skipTest('跳过test_r_anticlockwise')
        test_cube = np.array(
            [
                [[['white', 'green', 'orange'],
                  ['white', 'orange'],
                  ['red', 'blue', 'white']],  # c
                 [['white', 'green'],
                  ['white'],  # D
                  ['red', 'blue']],  # c
                 [['white', 'green', 'red'],
                  ['white', 'red'],
                  ['red', 'blue', 'yellow']]],  # c

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['orange', 'blue', 'yellow']],  # c
                 [['yellow', 'green'],
                  ['yellow'],  # U
                  ['orange', 'blue']],  # c
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['orange', 'blue', 'white']]],  # c

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['white', 'blue', 'orange']],  # c
                 [['orange', 'green'],
                  ['orange'],  # F
                  ['white', 'blue']],  # c
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['white', 'blue', 'red']]],  # c

                [[['yellow', 'blue', 'orange'],  # c
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['yellow', 'blue'],  # c
                  ['red'],  # B
                  ['red', 'green']],
                 [['yellow', 'blue', 'red'],  # c
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],  # L
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'white', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'yellow', 'orange']],
                 [['blue', 'white'],
                  ['blue'],  # R, clockwise
                  ['blue', 'yellow']],
                 [['blue', 'white', 'red'],
                  ['blue', 'red'],
                  ['blue', 'yellow', 'red']]]
            ]
        )
        recover_rubik_cube.r_anticlockwise(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_recover_center(self):
        """ 测试复原魔方的6个中心
        """
        self.skipTest('跳过test_recover_center')
        test_cube = np.array(
            [
                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'green', 'white'],
                  ['red', 'white'],
                  ['red', 'blue', 'white']],
                 [['red', 'green'],
                  ['red'],
                  ['red', 'blue']],
                 [['red', 'green', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'blue', 'yellow']]],

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['white', 'blue', 'red'],
                  ['white', 'red'],
                  ['white', 'green', 'red']],
                 [['white', 'blue'],
                  ['white'],
                  ['white', 'green']],
                 [['white', 'blue', 'orange'],
                  ['white', 'orange'],
                  ['white', 'green', 'orange']]],

                [[['green', 'white', 'red'],
                  ['green', 'red'],
                  ['green', 'yellow', 'red']],
                 [['green', 'white'],
                  ['green'],
                  ['green', 'yellow']],
                 [['green', 'white', 'orange'],
                  ['green', 'orange'],
                  ['green', 'yellow', 'orange']]],

                [[['blue', 'yellow', 'red'],
                  ['blue', 'red'],
                  ['blue', 'white', 'red']],
                 [['blue', 'yellow'],
                  ['blue'],
                  ['blue', 'white']],
                 [['blue', 'yellow', 'orange'],
                  ['blue', 'orange'],
                  ['blue', 'white', 'orange']]]
            ]
        )
        recover_rubik_cube.recover_center(test_cube)
        outcome_ar = test_cube == self.standard_color_cube
        # print(outcome_ar)
        self.assertTrue(outcome_ar.all())

    def test_recover_down_cross(self):
        """ 测试复原底层十字架

        :return: None
        """
        self.skipTest('跳过test_recover_down_cross')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        # print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0][1][0], ['white', 'green'])
        self.assertEqual(self.standard_color_cube[0][2][1], ['white', 'red'])
        self.assertEqual(self.standard_color_cube[0][1][2], ['white', 'blue'])
        self.assertEqual(self.standard_color_cube[0][0][1], ['white', 'orange'])

    def test_recover_down_corner(self):
        """ 测试复原底层四个角块

        :return: None
        """
        self.skipTest('跳过test_recover_down_corner')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        recover_rubik_cube.recover_down_corner(self.standard_color_cube)
        # print(recover_rubik_cube.total_operate_list)
        # print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0][0][0], ['white', 'green', 'orange'])
        self.assertEqual(self.standard_color_cube[0][2][0], ['white', 'green', 'red'])
        self.assertEqual(self.standard_color_cube[0][2][2], ['white', 'blue', 'red'])
        self.assertEqual(self.standard_color_cube[0][0][2], ['white', 'blue', 'orange'])

    def test_recover_second_floor(self):
        """ 测试复原第二层四个角块

        :return: None
        """
        self.skipTest('跳过test_recover_second_floor')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        recover_rubik_cube.recover_down_corner(self.standard_color_cube)
        recover_rubik_cube.recover_second_floor(self.standard_color_cube)
        # print(recover_rubik_cube.total_operate_list)
        # print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0].tolist(),
                         [[['white', 'green', 'orange'],
                           ['white', 'orange'],
                           ['white', 'blue', 'orange']],
                          [['white', 'green'],
                           ['white'],
                           ['white', 'blue']],
                          [['white', 'green', 'red'],
                           ['white', 'red'],
                           ['white', 'blue', 'red']]])
        self.assertEqual(self.standard_color_cube[2][1][0], ['orange', 'green'])
        self.assertEqual(self.standard_color_cube[2][1][2], ['orange', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][0], ['red', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][2], ['red', 'green'])

    def test_recover_up_cross(self):
        """ 测试复原顶层十字

        :return: None
        """
        self.skipTest('跳过test_recover_up_cross')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        recover_rubik_cube.recover_down_corner(self.standard_color_cube)
        recover_rubik_cube.recover_second_floor(self.standard_color_cube)
        recover_rubik_cube.recover_up_cross(self.standard_color_cube)
        # print(recover_rubik_cube.total_operate_list)
        # print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0].tolist(),
                         [[['white', 'green', 'orange'],
                           ['white', 'orange'],
                           ['white', 'blue', 'orange']],
                          [['white', 'green'],
                           ['white'],
                           ['white', 'blue']],
                          [['white', 'green', 'red'],
                           ['white', 'red'],
                           ['white', 'blue', 'red']]])
        self.assertEqual(self.standard_color_cube[2][1][0], ['orange', 'green'])
        self.assertEqual(self.standard_color_cube[2][1][2], ['orange', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][0], ['red', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][2], ['red', 'green'])
        self.assertEqual(self.standard_color_cube[1][0][1][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][1][0], 'yellow')

    def test_recover_up_to_one_color(self):
        """ 测试复原顶层为一色

        :return: None
        """
        self.skipTest('跳过test_recover_up_to_one_color')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        recover_rubik_cube.recover_down_corner(self.standard_color_cube)
        recover_rubik_cube.recover_second_floor(self.standard_color_cube)
        recover_rubik_cube.recover_up_cross(self.standard_color_cube)
        recover_rubik_cube.recover_up_to_one_color(self.standard_color_cube)
        # print(recover_rubik_cube.total_operate_list)
        # print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0].tolist(),
                         [[['white', 'green', 'orange'],
                           ['white', 'orange'],
                           ['white', 'blue', 'orange']],
                          [['white', 'green'],
                           ['white'],
                           ['white', 'blue']],
                          [['white', 'green', 'red'],
                           ['white', 'red'],
                           ['white', 'blue', 'red']]])

        self.assertEqual(self.standard_color_cube[2][1][0], ['orange', 'green'])
        self.assertEqual(self.standard_color_cube[2][1][2], ['orange', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][0], ['red', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][2], ['red', 'green'])

        self.assertEqual(self.standard_color_cube[1][0][1][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][1][0], 'yellow')

        self.assertEqual(self.standard_color_cube[1][0][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][0][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][2][0], 'yellow')

    def test_recover_up_corner(self):
        """ 测试复原顶层四个角

        :return: None
        """
        self.skipTest('跳过test_recover_up_corner')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        recover_rubik_cube.recover_down_corner(self.standard_color_cube)
        recover_rubik_cube.recover_second_floor(self.standard_color_cube)
        recover_rubik_cube.recover_up_cross(self.standard_color_cube)
        recover_rubik_cube.recover_up_to_one_color(self.standard_color_cube)
        recover_rubik_cube.recover_up_corner(self.standard_color_cube)
        # print(recover_rubik_cube.total_operate_list)
        # print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0].tolist(),
                         [[['white', 'green', 'orange'],
                           ['white', 'orange'],
                           ['white', 'blue', 'orange']],
                          [['white', 'green'],
                           ['white'],
                           ['white', 'blue']],
                          [['white', 'green', 'red'],
                           ['white', 'red'],
                           ['white', 'blue', 'red']]])

        self.assertEqual(self.standard_color_cube[2][1][0], ['orange', 'green'])
        self.assertEqual(self.standard_color_cube[2][1][2], ['orange', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][0], ['red', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][2], ['red', 'green'])

        self.assertEqual(self.standard_color_cube[1][0][1][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][1][0], 'yellow')

        self.assertEqual(self.standard_color_cube[1][0][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][0][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][2][0], 'yellow')

        self.assertEqual(self.standard_color_cube[1][0][0], ['yellow', 'green', 'red'])
        self.assertEqual(self.standard_color_cube[1][0][2], ['yellow', 'blue', 'red'])
        self.assertEqual(self.standard_color_cube[1][2][0], ['yellow', 'green', 'orange'])
        self.assertEqual(self.standard_color_cube[1][2][2], ['yellow', 'blue', 'orange'])

    def test_recover_up_init(self):
        """ 测试复原顶层四个棱

        :return: None
        """
        # self.skipTest('跳过test_recover_up_init')
        distort_oder_test = recover_rubik_cube.generate_random_order(20)
        # print(distort_oder_test)
        recover_rubik_cube.distort_cube(self.standard_color_cube, distort_oder_test)
        recover_rubik_cube.recover_center(self.standard_color_cube)
        recover_rubik_cube.recover_down_cross(self.standard_color_cube)
        recover_rubik_cube.recover_down_corner(self.standard_color_cube)
        recover_rubik_cube.recover_second_floor(self.standard_color_cube)
        recover_rubik_cube.recover_up_cross(self.standard_color_cube)
        recover_rubik_cube.recover_up_to_one_color(self.standard_color_cube)
        recover_rubik_cube.recover_up_corner(self.standard_color_cube)
        recover_rubik_cube.recover_to_init(self.standard_color_cube)
        print(recover_rubik_cube.total_operate_list)
        print(self.standard_color_cube)
        self.assertEqual(self.standard_color_cube[0].tolist(),
                         [[['white', 'green', 'orange'],
                           ['white', 'orange'],
                           ['white', 'blue', 'orange']],
                          [['white', 'green'],
                           ['white'],
                           ['white', 'blue']],
                          [['white', 'green', 'red'],
                           ['white', 'red'],
                           ['white', 'blue', 'red']]])

        self.assertEqual(self.standard_color_cube[2][1][0], ['orange', 'green'])
        self.assertEqual(self.standard_color_cube[2][1][2], ['orange', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][0], ['red', 'blue'])
        self.assertEqual(self.standard_color_cube[3][1][2], ['red', 'green'])

        self.assertEqual(self.standard_color_cube[1][0][1][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][1][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][1][0], 'yellow')

        self.assertEqual(self.standard_color_cube[1][0][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][0][2][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][0][0], 'yellow')
        self.assertEqual(self.standard_color_cube[1][2][2][0], 'yellow')

        self.assertEqual(self.standard_color_cube[1][0][0], ['yellow', 'green', 'red'])
        self.assertEqual(self.standard_color_cube[1][0][2], ['yellow', 'blue', 'red'])
        self.assertEqual(self.standard_color_cube[1][2][0], ['yellow', 'green', 'orange'])
        self.assertEqual(self.standard_color_cube[1][2][2], ['yellow', 'blue', 'orange'])

        self.assertEqual(self.standard_color_cube.tolist(), recover_rubik_cube.standard_colors.tolist())

    def setUp(self) -> None:
        # print('in')
        self.standard_color_cube = np.array(
            [
                [[['white', 'green', 'orange'],  # 前、左、上
                  ['white', 'orange'],             # 前、上
                  ['white', 'blue', 'orange']],  # 前、右、上
                 [['white', 'green'],              # 前、左
                  ['white'],                           # D
                  ['white', 'blue']],              # 前、右
                 [['white', 'green', 'red'],     # 前、左、下
                  ['white', 'red'],                # 前、下
                  ['white', 'blue', 'red']]],    # 前、右、下

                [[['yellow', 'green', 'red'],
                  ['yellow', 'red'],
                  ['yellow', 'blue', 'red']],
                 [['yellow', 'green'],
                  ['yellow'],                          # U
                  ['yellow', 'blue']],
                 [['yellow', 'green', 'orange'],
                  ['yellow', 'orange'],
                  ['yellow', 'blue', 'orange']]],

                [[['orange', 'green', 'yellow'],
                  ['orange', 'yellow'],
                  ['orange', 'blue', 'yellow']],
                 [['orange', 'green'],
                  ['orange'],                          # F
                  ['orange', 'blue']],
                 [['orange', 'green', 'white'],
                  ['orange', 'white'],
                  ['orange', 'blue', 'white']]],

                [[['red', 'blue', 'yellow'],
                  ['red', 'yellow'],
                  ['red', 'green', 'yellow']],
                 [['red', 'blue'],
                  ['red'],                             # B
                  ['red', 'green']],
                 [['red', 'blue', 'white'],
                  ['red', 'white'],
                  ['red', 'green', 'white']]],

                [[['green', 'red', 'yellow'],
                  ['green', 'yellow'],
                  ['green', 'orange', 'yellow']],
                 [['green', 'red'],
                  ['green'],                           # L
                  ['green', 'orange']],
                 [['green', 'red', 'white'],
                  ['green', 'white'],
                  ['green', 'orange', 'white']]],

                [[['blue', 'orange', 'yellow'],
                  ['blue', 'yellow'],
                  ['blue', 'red', 'yellow']],
                 [['blue', 'orange'],
                  ['blue'],                            # R
                  ['blue', 'red']],
                 [['blue', 'orange', 'white'],
                  ['blue', 'white'],
                  ['blue', 'red', 'white']]]
            ])

    def tearDown(self) -> None:
        # print('out')
        pass


if __name__ == '__main__':
    unittest.main()


