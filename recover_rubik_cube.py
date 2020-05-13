""" 复原三阶魔方

    本代码要做到以下几点
    1.提供魔方的每个转法，例如经典的R、U等等
    2.提供魔方的打乱方法
    3.提供魔方的复原方法

    实施：
    1.首先给出魔方的状态存储方式，我给出的是六面存储状态，每面都按照相同的次序排列
    e.g.
    standard_colors = np.array(
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
    2.按照经典复原方法复原魔方：
        ①复原底层十字
        ②复原底层四个角块
        ③复原第二层四个边角块
        ④复原顶层十字
        ⑤复原顶层为同色
        ⑥复原顶层四个顶角块
        ⑦复原顶层四个边角块
    3.描述打乱魔方步骤和复原步骤

    the statistics of this file:
    lines(count)    understand_level(h/m/l)    classes(count)    functions(count)    fields(count)
    000000002521    ----------------------h    00000000000000    0000000000000031    ~~~~~~~~~~~12
"""

import time
import random
import pprint

import numpy as np

__author__ = '与C同行'
standard_colors = np.array(
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
# 魔方沿着轴转动之后状态
# region
standard_y_colors = np.array(
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
    ])
standard_x_colors = np.array(
    [
        [ [['green', 'yellow', 'orange'],
           ['green', 'orange'],
           ['green', 'white', 'orange']],
          [['green', 'yellow'],
           ['green'],
           ['green', 'white']],
          [['green', 'yellow', 'red'],
           ['green', 'red'],
           ['green', 'white', 'red']]],

        [ [['blue', 'yellow', 'red'],
           ['blue', 'red'],
           ['blue', 'white', 'red']],
          [['blue', 'yellow'],
           ['blue'],
           ['blue', 'white']],
          [['blue', 'yellow', 'orange'],
           ['blue', 'orange'],
           ['blue', 'white', 'orange']]],

        [ [['orange', 'yellow', 'blue'],
           ['orange', 'blue'],
           ['orange', 'white', 'blue']],
          [['orange', 'yellow'],
           ['orange'],
           ['orange', 'white']],
          [['orange', 'yellow', 'green'],
           ['orange', 'green'],
           ['orange', 'white', 'green']]],

        [ [['red', 'white', 'blue'],
           ['red', 'blue'],
           ['red', 'yellow', 'blue']],
          [['red', 'white'],
           ['red'],
           ['red', 'yellow']],
          [['red', 'white', 'green'],
           ['red', 'green'],
           ['red', 'yellow', 'green']]],

        [ [['yellow', 'red', 'blue'],
           ['yellow', 'blue'],
           ['yellow', 'orange', 'blue']],
          [['yellow', 'red'],
           ['yellow'],
           ['yellow', 'orange']],
          [['yellow', 'red', 'green'],
           ['yellow', 'green'],
           ['yellow', 'orange', 'green']]],

        [ [['white', 'orange', 'blue'],
           ['white', 'blue'],
           ['white', 'red', 'blue']],
          [['white', 'orange'],
           ['white'],
           ['white', 'red']],
          [['white', 'orange', 'green'],
           ['white', 'green'],
           ['white', 'red', 'green']]]
    ])
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
# endregion
# 魔方12种转动方法之后对应的魔方状态
# region
f_clockwise_colors = np.array(
    [
     [[['blue', 'white', 'orange'],      # c
       ['blue', 'orange'],               # c
       ['blue', 'yellow', 'orange']],    # c
      [['white', 'green'],
       ['white'],                           # D
       ['white', 'blue']],
      [['white', 'green', 'red'],
       ['white', 'red'],
       ['white', 'blue', 'red']]],

     [[['yellow', 'green', 'red'],
       ['yellow', 'red'],
       ['yellow', 'blue', 'red']],
      [['yellow', 'green'],
       ['yellow'],                          # U
       ['yellow', 'blue']],
      [['green', 'white', 'orange'],     # c
       ['green', 'orange'],              # c
       ['green', 'yellow', 'orange']]],  # c

     [[['orange', 'white', 'green'],
       ['orange', 'green'],
       ['orange', 'yellow', 'green']],
      [['orange', 'white'],
       ['orange'],                          # F, clockwise
       ['orange', 'yellow']],
      [['orange', 'white', 'blue'],
       ['orange', 'blue'],
       ['orange', 'yellow', 'blue']]],

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
       ['white', 'orange', 'green']],    # c
      [['green', 'red'],
       ['green'],                           # L
       ['white', 'orange']],             # c
      [['green', 'red', 'white'],
       ['green', 'white'],
       ['white', 'orange', 'blue']]],    # c

     [[['yellow', 'orange', 'green'],    # c
       ['blue', 'yellow'],
       ['blue', 'red', 'yellow']],
      [['yellow', 'orange'],             # c
       ['blue'],                            # R
       ['blue', 'red']],
      [['yellow', 'orange', 'blue'],     # c
       ['blue', 'white'],
       ['blue', 'red', 'white']]]
    ])
b_clockwise_colors = np.array(
    [
     [[['white', 'green', 'orange'],
       ['white', 'orange'],
       ['white', 'blue', 'orange']],
      [['white', 'green'],
       ['white'],                           # D
       ['white', 'blue']],
      [['green', 'yellow', 'red'],     # c
       ['green', 'red'],               # c
       ['green', 'white', 'red']]],    # c

     [[['blue', 'yellow', 'red'],      # c
       ['blue', 'red'],                # c
       ['blue', 'white', 'red']],      # c
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

     [[['red', 'white', 'blue'],
       ['red', 'blue'],
       ['red', 'yellow', 'blue']],
      [['red', 'white'],
       ['red'],                             # B, clockwise
       ['red', 'yellow']],
      [['red', 'white', 'green'],
       ['red', 'green'],
       ['red', 'yellow', 'green']]],

     [[['yellow', 'red', 'blue'],      # c
       ['green', 'yellow'],
       ['green', 'orange', 'yellow']],
      [['yellow', 'red'],              # c
       ['green'],                           # L
       ['green', 'orange']],
      [['yellow', 'red', 'green'],     # c
       ['green', 'white'],
       ['green', 'orange', 'white']]],

     [[['blue', 'orange', 'yellow'],
       ['blue', 'yellow'],
       ['white', 'red', 'blue']],      # c
      [['blue', 'orange'],
       ['blue'],                            # R
       ['white', 'red']],              # c
      [['blue', 'orange', 'white'],
       ['blue', 'white'],
       ['white', 'red', 'green']]]     # c
    ])
d_clockwise_colors = np.array(
    [
     [[['white', 'red', 'green'],
       ['white', 'green'],
       ['white', 'orange', 'green']],
      [['white', 'red'],
       ['white'],                           # D, clockwise
       ['white', 'orange']],
      [['white', 'red', 'blue'],
       ['white', 'blue'],
       ['white', 'orange', 'blue']]],

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
      [['green', 'red', 'white'],        # c
       ['green', 'white'],               # c
       ['green', 'orange', 'white']]],   # c

     [[['red', 'blue', 'yellow'],
       ['red', 'yellow'],
       ['red', 'green', 'yellow']],
      [['red', 'blue'],
       ['red'],                             # B
       ['red', 'green']],
      [['blue', 'orange', 'white'],      # c
       ['blue', 'white'],                # c
       ['blue', 'red', 'white']]],       # c

     [[['green', 'red', 'yellow'],
       ['green', 'yellow'],
       ['green', 'orange', 'yellow']],
      [['green', 'red'],
       ['green'],                           # L
       ['green', 'orange']],
      [['red', 'blue', 'white'],         # c
       ['red', 'white'],                 # c
       ['red', 'green', 'white']]],      # c

     [[['blue', 'orange', 'yellow'],
       ['blue', 'yellow'],
       ['blue', 'red', 'yellow']],
      [['blue', 'orange'],
       ['blue'],                            # R
       ['blue', 'red']],
      [['orange', 'green', 'white'],     # c
       ['orange', 'white'],              # c
       ['orange', 'blue', 'white']]]     # c
    ])
u_clockwise_colors = np.array(
    [
     [[['white', 'green', 'orange'],
       ['white', 'orange'],
       ['white', 'blue', 'orange']],
      [['white', 'green'],
       ['white'],                           # D
       ['white', 'blue']],
      [['white', 'green', 'red'],
       ['white', 'red'],
       ['white', 'blue', 'red']]],

     [[['yellow', 'orange', 'green'],
       ['yellow', 'green'],
       ['yellow', 'red', 'green']],
      [['yellow', 'orange'],
       ['yellow'],                          # U, clockwise
       ['yellow', 'red']],
      [['yellow', 'orange', 'blue'],
       ['yellow', 'blue'],
       ['yellow', 'red', 'blue']]],

     [[['blue', 'orange', 'yellow'],    # c
       ['blue', 'yellow'],              # c
       ['blue', 'red', 'yellow']],      # c
      [['orange', 'green'],
       ['orange'],                          # F
       ['orange', 'blue']],
      [['orange', 'green', 'white'],
       ['orange', 'white'],
       ['orange', 'blue', 'white']]],

     [[['green', 'red', 'yellow'],      # c
       ['green', 'yellow'],             # c
       ['green', 'orange', 'yellow']],  # c
      [['red', 'blue'],
       ['red'],                             # B
       ['red', 'green']],
      [['red', 'blue', 'white'],
       ['red', 'white'],
       ['red', 'green', 'white']]],

     [[['orange', 'green', 'yellow'],   # c
       ['orange', 'yellow'],            # c
       ['orange', 'blue', 'yellow']],   # c
      [['green', 'red'],
       ['green'],                           # L
       ['green', 'orange']],
      [['green', 'red', 'white'],
       ['green', 'white'],
       ['green', 'orange', 'white']]],

     [[['red', 'blue', 'yellow'],       # c
       ['red', 'yellow'],               # c
       ['red', 'green', 'yellow']],     # c
      [['blue', 'orange'],
       ['blue'],                            # R
       ['blue', 'red']],
      [['blue', 'orange', 'white'],
       ['blue', 'white'],
       ['blue', 'red', 'white']]]
    ])
l_clockwise_colors = np.array(
    [
     [[['orange', 'green', 'yellow'],  # c
       ['white', 'orange'],
       ['white', 'blue', 'orange']],
      [['orange', 'green'],            # c
       ['white'],                           # D
       ['white', 'blue']],
      [['orange', 'green', 'white'],   # c
       ['white', 'red'],
       ['white', 'blue', 'red']]],

     [[['red', 'green', 'white'],      # c
       ['yellow', 'red'],
       ['yellow', 'blue', 'red']],
      [['red', 'green'],               # c
       ['yellow'],                          # U
       ['yellow', 'blue']],
      [['red', 'green', 'yellow'],     # c
       ['yellow', 'orange'],
       ['yellow', 'blue', 'orange']]],

     [[['yellow', 'green', 'red'],     # c
       ['orange', 'yellow'],
       ['orange', 'blue', 'yellow']],
      [['yellow', 'green'],            # c
       ['orange'],                          # F
       ['orange', 'blue']],
      [['yellow', 'green', 'orange'],  # c
       ['orange', 'white'],
       ['orange', 'blue', 'white']]],

     [[['red', 'blue', 'yellow'],
       ['red', 'yellow'],
       ['white', 'green', 'red']],     # c
      [['red', 'blue'],
       ['red'],                             # B
       ['white', 'green']],            # c
      [['red', 'blue', 'white'],
       ['red', 'white'],
       ['white', 'green', 'orange']]],  # c

     [[['green', 'white', 'red'],
       ['green', 'red'],
       ['green', 'yellow', 'red']],
      [['green', 'white'],
       ['green'],                           # L, clockwise
       ['green', 'yellow']],
      [['green', 'white', 'orange'],
       ['green', 'orange'],
       ['green', 'yellow', 'orange']]],

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
r_clockwise_colors = np.array(
    [
     [[['white', 'green', 'orange'],
       ['white', 'orange'],
       ['red', 'blue', 'white']],       # c
      [['white', 'green'],
       ['white'],                           # D
       ['red', 'blue']],                # c
      [['white', 'green', 'red'],
       ['white', 'red'],
       ['red', 'blue', 'yellow']]],     # c

     [[['yellow', 'green', 'red'],
       ['yellow', 'red'],
       ['orange', 'blue', 'yellow']],   # c
      [['yellow', 'green'],
       ['yellow'],                          # U
       ['orange', 'blue']],             # c
      [['yellow', 'green', 'orange'],
       ['yellow', 'orange'],
       ['orange', 'blue', 'white']]],   # c

     [[['orange', 'green', 'yellow'],
       ['orange', 'yellow'],
       ['white', 'blue', 'orange']],    # c
      [['orange', 'green'],
       ['orange'],                          # F
       ['white', 'blue']],              # c
      [['orange', 'green', 'white'],
       ['orange', 'white'],
       ['white', 'blue', 'red']]],      # c

     [[['yellow', 'blue', 'orange'],    # c
       ['red', 'yellow'],
       ['red', 'green', 'yellow']],
      [['yellow', 'blue'],              # c
       ['red'],                             # B
       ['red', 'green']],
      [['yellow', 'blue', 'red'],       # c
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

     [[['blue', 'white', 'orange'],
       ['blue', 'orange'],
       ['blue', 'yellow', 'orange']],
      [['blue', 'white'],
       ['blue'],                            # R, clockwise
       ['blue', 'yellow']],
      [['blue', 'white', 'red'],
       ['blue', 'red'],
       ['blue', 'yellow', 'red']]]
    ])


# endregion
# 魔方一面转动90°方法
# region
def one_face_clockwise_90(in_cube, which_face):
    """ 将一面顺时针旋转90°

    :param in_cube: 给的魔方状态
    :param which_face: 旋转那一面
    :return: None
    """
    temp_face_arr = in_cube[which_face]
    var1 = temp_face_arr[2][0][2]
    var2 = temp_face_arr[2][0][1]
    var3 = temp_face_arr[1][0][1]
    var4 = temp_face_arr[0][0][2]
    var5 = temp_face_arr[0][0][1]
    var6 = temp_face_arr[2][1][1]
    var7 = temp_face_arr[0][1][1]
    var8 = temp_face_arr[2][2][2]
    var9 = temp_face_arr[2][2][1]
    var10 = temp_face_arr[1][2][1]
    var11 = temp_face_arr[0][2][2]
    var12 = temp_face_arr[0][2][1]

    # 补
    var13 = temp_face_arr[2][0][0]
    var14 = temp_face_arr[1][0][0]
    var15 = temp_face_arr[0][0][0]
    var16 = temp_face_arr[2][1][0]
    var17 = temp_face_arr[0][1][0]
    var18 = temp_face_arr[2][2][0]
    var19 = temp_face_arr[1][2][0]
    var20 = temp_face_arr[0][2][0]

    in_cube[which_face][0][0][1] = var1
    in_cube[which_face][0][0][2] = var2
    in_cube[which_face][0][1][1] = var3
    in_cube[which_face][0][2][1] = var4
    in_cube[which_face][0][2][2] = var5

    in_cube[which_face][1][0][1] = var6
    in_cube[which_face][1][2][1] = var7

    in_cube[which_face][2][0][1] = var8
    in_cube[which_face][2][0][2] = var9
    in_cube[which_face][2][1][1] = var10
    in_cube[which_face][2][2][1] = var11
    in_cube[which_face][2][2][2] = var12

    # 补
    in_cube[which_face][0][0][0] = var13
    in_cube[which_face][0][1][0] = var14
    in_cube[which_face][0][2][0] = var15
    in_cube[which_face][1][0][0] = var16
    in_cube[which_face][1][2][0] = var17
    in_cube[which_face][2][0][0] = var18
    in_cube[which_face][2][1][0] = var19
    in_cube[which_face][2][2][0] = var20


def one_face_anticlockwise_90(in_cube, which_face):
    """ 将一面逆时针旋转90°

    :param in_cube: 给的魔方状态
    :param which_face: 旋转的面
    :return: None
    """
    temp_face_arr = in_cube[which_face]
    var1 = temp_face_arr[0][0][1]
    var2 = temp_face_arr[0][0][2]
    var3 = temp_face_arr[0][1][1]
    var4 = temp_face_arr[0][2][1]
    var5 = temp_face_arr[0][2][2]

    var6 = temp_face_arr[1][0][1]
    var7 = temp_face_arr[1][2][1]

    var8 = temp_face_arr[2][0][1]
    var9 = temp_face_arr[2][0][2]
    var10 = temp_face_arr[2][1][1]
    var11 = temp_face_arr[2][2][1]
    var12 = temp_face_arr[2][2][2]

    # 补
    var13 = temp_face_arr[0][2][0]
    var14 = temp_face_arr[1][2][0]
    var15 = temp_face_arr[2][2][0]
    var16 = temp_face_arr[0][1][0]
    var17 = temp_face_arr[2][1][0]
    var18 = temp_face_arr[0][0][0]
    var19 = temp_face_arr[1][0][0]
    var20 = temp_face_arr[2][0][0]

    in_cube[which_face][2][0][2] = var1
    in_cube[which_face][2][0][1] = var2
    in_cube[which_face][1][0][1] = var3
    in_cube[which_face][0][0][2] = var4
    in_cube[which_face][0][0][1] = var5

    in_cube[which_face][2][1][1] = var6
    in_cube[which_face][0][1][1] = var7

    in_cube[which_face][2][2][2] = var8
    in_cube[which_face][2][2][1] = var9
    in_cube[which_face][1][2][1] = var10
    in_cube[which_face][0][2][2] = var11
    in_cube[which_face][0][2][1] = var12

    # 补
    in_cube[which_face][0][0][0] = var13
    in_cube[which_face][0][1][0] = var14
    in_cube[which_face][0][2][0] = var15
    in_cube[which_face][1][0][0] = var16
    in_cube[which_face][1][2][0] = var17
    in_cube[which_face][2][0][0] = var18
    in_cube[which_face][2][1][0] = var19
    in_cube[which_face][2][2][0] = var20


# endregion
# 魔方沿着轴转动方法
# region
def y_right_hand_positive_90(needed_cube):
    """ 根据三轴绕Y轴右手定理旋转90°

    :param needed_cube: 给的魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0] = temp_ar[2]
    needed_cube[1] = temp_ar[3]
    one_face_clockwise_90(needed_cube, 1)
    one_face_clockwise_90(needed_cube, 1)
    needed_cube[2] = temp_ar[1]
    needed_cube[3] = temp_ar[0]
    one_face_clockwise_90(needed_cube, 3)
    one_face_clockwise_90(needed_cube, 3)
    needed_cube[4] = temp_ar[4]
    one_face_clockwise_90(needed_cube, 4)
    needed_cube[5] = temp_ar[5]
    one_face_anticlockwise_90(needed_cube, 5)


def y_right_hand_negative_90(needed_cube):
    """ 根据三轴绕Y轴右手定理旋转-90°

    :param needed_cube: 给的魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0] = temp_ar[3]
    one_face_clockwise_90(needed_cube, 0)
    one_face_clockwise_90(needed_cube, 0)
    needed_cube[1] = temp_ar[2]

    needed_cube[2] = temp_ar[0]
    needed_cube[3] = temp_ar[1]
    one_face_clockwise_90(needed_cube, 3)
    one_face_clockwise_90(needed_cube, 3)
    needed_cube[4] = temp_ar[4]
    one_face_anticlockwise_90(needed_cube, 4)
    needed_cube[5] = temp_ar[5]
    one_face_clockwise_90(needed_cube, 5)


def x_right_hand_positive_90(needed_cube):
    """ 根据三轴绕X轴右手定理旋转90°

    :param needed_cube: 给的魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0] = temp_ar[4]
    one_face_anticlockwise_90(needed_cube, 0)
    needed_cube[1] = temp_ar[5]
    one_face_anticlockwise_90(needed_cube, 1)
    needed_cube[2] = temp_ar[2]
    one_face_anticlockwise_90(needed_cube, 2)
    needed_cube[3] = temp_ar[3]
    one_face_clockwise_90(needed_cube, 3)
    needed_cube[4] = temp_ar[1]
    one_face_anticlockwise_90(needed_cube, 4)
    needed_cube[5] = temp_ar[0]
    one_face_anticlockwise_90(needed_cube, 5)


def x_right_hand_negative_90(needed_cube):
    """ 根据三轴绕X轴右手定理旋转-90°

    :param needed_cube: 给的魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0] = temp_ar[5]
    one_face_clockwise_90(needed_cube, 0)
    needed_cube[1] = temp_ar[4]
    one_face_clockwise_90(needed_cube, 1)
    needed_cube[2] = temp_ar[2]
    one_face_clockwise_90(needed_cube, 2)
    needed_cube[3] = temp_ar[3]
    one_face_anticlockwise_90(needed_cube, 3)
    needed_cube[4] = temp_ar[0]
    one_face_clockwise_90(needed_cube, 4)
    needed_cube[5] = temp_ar[1]
    one_face_clockwise_90(needed_cube, 5)


def z_right_hand_positive_90(needed_cube):
    """ 根据三轴绕Z轴右手定理旋转90°

    :param needed_cube: 给的魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0] = temp_ar[0]
    one_face_clockwise_90(needed_cube, 0)
    needed_cube[1] = temp_ar[1]
    one_face_anticlockwise_90(needed_cube, 1)
    needed_cube[2] = temp_ar[4]
    needed_cube[3] = temp_ar[5]
    needed_cube[4] = temp_ar[3]
    needed_cube[5] = temp_ar[2]


def z_right_hand_negative_90(needed_cube):
    """ 根据三轴绕Z轴右手定理旋转-90°

    :param needed_cube: 给的魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0] = temp_ar[0]
    one_face_anticlockwise_90(needed_cube, 0)
    needed_cube[1] = temp_ar[1]
    one_face_clockwise_90(needed_cube, 1)
    needed_cube[2] = temp_ar[5]
    needed_cube[3] = temp_ar[4]
    needed_cube[4] = temp_ar[2]
    needed_cube[5] = temp_ar[3]


# endregion
# 12种转动魔方方法
# region
def f_clockwise(needed_cube):
    """ F

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0][0][0][0] = temp_ar[5][2][0][0]
    needed_cube[0][0][0][1] = temp_ar[5][2][0][2]
    needed_cube[0][0][0][2] = temp_ar[5][2][0][1]
    needed_cube[0][0][1][0] = temp_ar[5][1][0][0]
    needed_cube[0][0][1][1] = temp_ar[5][1][0][1]
    needed_cube[0][0][2][0] = temp_ar[5][0][0][0]
    needed_cube[0][0][2][1] = temp_ar[5][0][0][2]
    needed_cube[0][0][2][2] = temp_ar[5][0][0][1]

    needed_cube[1][2][0][0] = temp_ar[4][2][2][0]
    needed_cube[1][2][0][1] = temp_ar[4][2][2][2]
    needed_cube[1][2][0][2] = temp_ar[4][2][2][1]
    needed_cube[1][2][1][0] = temp_ar[4][1][2][0]
    needed_cube[1][2][1][1] = temp_ar[4][1][2][1]
    needed_cube[1][2][2][0] = temp_ar[4][0][2][0]
    needed_cube[1][2][2][1] = temp_ar[4][0][2][2]
    needed_cube[1][2][2][2] = temp_ar[4][0][2][1]

    one_face_clockwise_90(needed_cube, 2)

    needed_cube[4][0][2][0] = temp_ar[0][0][0][0]
    needed_cube[4][0][2][1] = temp_ar[0][0][0][2]
    needed_cube[4][0][2][2] = temp_ar[0][0][0][1]
    needed_cube[4][1][2][0] = temp_ar[0][0][1][0]
    needed_cube[4][1][2][1] = temp_ar[0][0][1][1]
    needed_cube[4][2][2][0] = temp_ar[0][0][2][0]
    needed_cube[4][2][2][1] = temp_ar[0][0][2][2]
    needed_cube[4][2][2][2] = temp_ar[0][0][2][1]

    needed_cube[5][0][0][0] = temp_ar[1][2][0][0]
    needed_cube[5][0][0][1] = temp_ar[1][2][0][2]
    needed_cube[5][0][0][2] = temp_ar[1][2][0][1]
    needed_cube[5][1][0][0] = temp_ar[1][2][1][0]
    needed_cube[5][1][0][1] = temp_ar[1][2][1][1]
    needed_cube[5][2][0][0] = temp_ar[1][2][2][0]
    needed_cube[5][2][0][1] = temp_ar[1][2][2][2]
    needed_cube[5][2][0][2] = temp_ar[1][2][2][1]


def f_anticlockwise(needed_cube):
    """ F'

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[5][2][0][0] = temp_ar[0][0][0][0]
    needed_cube[5][2][0][2] = temp_ar[0][0][0][1]
    needed_cube[5][2][0][1] = temp_ar[0][0][0][2]
    needed_cube[5][1][0][0] = temp_ar[0][0][1][0]
    needed_cube[5][1][0][1] = temp_ar[0][0][1][1]
    needed_cube[5][0][0][0] = temp_ar[0][0][2][0]
    needed_cube[5][0][0][2] = temp_ar[0][0][2][1]
    needed_cube[5][0][0][1] = temp_ar[0][0][2][2]

    needed_cube[4][2][2][0] = temp_ar[1][2][0][0]
    needed_cube[4][2][2][2] = temp_ar[1][2][0][1]
    needed_cube[4][2][2][1] = temp_ar[1][2][0][2]
    needed_cube[4][1][2][0] = temp_ar[1][2][1][0]
    needed_cube[4][1][2][1] = temp_ar[1][2][1][1]
    needed_cube[4][0][2][0] = temp_ar[1][2][2][0]
    needed_cube[4][0][2][2] = temp_ar[1][2][2][1]
    needed_cube[4][0][2][1] = temp_ar[1][2][2][2]

    one_face_anticlockwise_90(needed_cube, 2)

    needed_cube[0][0][0][0] = temp_ar[4][0][2][0]
    needed_cube[0][0][0][2] = temp_ar[4][0][2][1]
    needed_cube[0][0][0][1] = temp_ar[4][0][2][2]
    needed_cube[0][0][1][0] = temp_ar[4][1][2][0]
    needed_cube[0][0][1][1] = temp_ar[4][1][2][1]
    needed_cube[0][0][2][0] = temp_ar[4][2][2][0]
    needed_cube[0][0][2][2] = temp_ar[4][2][2][1]
    needed_cube[0][0][2][1] = temp_ar[4][2][2][2]

    needed_cube[1][2][0][0] = temp_ar[5][0][0][0]
    needed_cube[1][2][0][2] = temp_ar[5][0][0][1]
    needed_cube[1][2][0][1] = temp_ar[5][0][0][2]
    needed_cube[1][2][1][0] = temp_ar[5][1][0][0]
    needed_cube[1][2][1][1] = temp_ar[5][1][0][1]
    needed_cube[1][2][2][0] = temp_ar[5][2][0][0]
    needed_cube[1][2][2][2] = temp_ar[5][2][0][1]
    needed_cube[1][2][2][1] = temp_ar[5][2][0][2]


def b_clockwise(needed_cube):
    """ B

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0][2][0][0] = temp_ar[4][0][0][0]
    needed_cube[0][2][0][1] = temp_ar[4][0][0][2]
    needed_cube[0][2][0][2] = temp_ar[4][0][0][1]
    needed_cube[0][2][1][0] = temp_ar[4][1][0][0]
    needed_cube[0][2][1][1] = temp_ar[4][1][0][1]
    needed_cube[0][2][2][0] = temp_ar[4][2][0][0]
    needed_cube[0][2][2][1] = temp_ar[4][2][0][2]
    needed_cube[0][2][2][2] = temp_ar[4][2][0][1]

    needed_cube[1][0][0][0] = temp_ar[5][0][2][0]
    needed_cube[1][0][0][1] = temp_ar[5][0][2][2]
    needed_cube[1][0][0][2] = temp_ar[5][0][2][1]
    needed_cube[1][0][1][0] = temp_ar[5][1][2][0]
    needed_cube[1][0][1][1] = temp_ar[5][1][2][1]
    needed_cube[1][0][2][0] = temp_ar[5][2][2][0]
    needed_cube[1][0][2][1] = temp_ar[5][2][2][2]
    needed_cube[1][0][2][2] = temp_ar[5][2][2][1]

    needed_cube[4][0][0][0] = temp_ar[1][0][2][0]
    needed_cube[4][0][0][1] = temp_ar[1][0][2][2]
    needed_cube[4][0][0][2] = temp_ar[1][0][2][1]
    needed_cube[4][1][0][0] = temp_ar[1][0][1][0]
    needed_cube[4][1][0][1] = temp_ar[1][0][1][1]
    needed_cube[4][2][0][0] = temp_ar[1][0][0][0]
    needed_cube[4][2][0][1] = temp_ar[1][0][0][2]
    needed_cube[4][2][0][2] = temp_ar[1][0][0][1]

    needed_cube[5][0][2][0] = temp_ar[0][2][2][0]
    needed_cube[5][0][2][1] = temp_ar[0][2][2][2]
    needed_cube[5][0][2][2] = temp_ar[0][2][2][1]
    needed_cube[5][1][2][0] = temp_ar[0][2][1][0]
    needed_cube[5][1][2][1] = temp_ar[0][2][1][1]
    needed_cube[5][2][2][0] = temp_ar[0][2][0][0]
    needed_cube[5][2][2][1] = temp_ar[0][2][0][2]
    needed_cube[5][2][2][2] = temp_ar[0][2][0][1]

    one_face_clockwise_90(needed_cube, 3)


def b_anticlockwise(needed_cube):
    """ B'

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[4][0][0][0] = temp_ar[0][2][0][0]
    needed_cube[4][0][0][2] = temp_ar[0][2][0][1]
    needed_cube[4][0][0][1] = temp_ar[0][2][0][2]
    needed_cube[4][1][0][0] = temp_ar[0][2][1][0]
    needed_cube[4][1][0][1] = temp_ar[0][2][1][1]
    needed_cube[4][2][0][0] = temp_ar[0][2][2][0]
    needed_cube[4][2][0][2] = temp_ar[0][2][2][1]
    needed_cube[4][2][0][1] = temp_ar[0][2][2][2]

    needed_cube[5][0][2][0] = temp_ar[1][0][0][0]
    needed_cube[5][0][2][2] = temp_ar[1][0][0][1]
    needed_cube[5][0][2][1] = temp_ar[1][0][0][2]
    needed_cube[5][1][2][0] = temp_ar[1][0][1][0]
    needed_cube[5][1][2][1] = temp_ar[1][0][1][1]
    needed_cube[5][2][2][0] = temp_ar[1][0][2][0]
    needed_cube[5][2][2][2] = temp_ar[1][0][2][1]
    needed_cube[5][2][2][1] = temp_ar[1][0][2][2]

    needed_cube[1][0][2][0] = temp_ar[4][0][0][0]
    needed_cube[1][0][2][2] = temp_ar[4][0][0][1]
    needed_cube[1][0][2][1] = temp_ar[4][0][0][2]
    needed_cube[1][0][1][0] = temp_ar[4][1][0][0]
    needed_cube[1][0][1][1] = temp_ar[4][1][0][1]
    needed_cube[1][0][0][0] = temp_ar[4][2][0][0]
    needed_cube[1][0][0][2] = temp_ar[4][2][0][1]
    needed_cube[1][0][0][1] = temp_ar[4][2][0][2]

    needed_cube[0][2][2][0] = temp_ar[5][0][2][0]
    needed_cube[0][2][2][2] = temp_ar[5][0][2][1]
    needed_cube[0][2][2][1] = temp_ar[5][0][2][2]
    needed_cube[0][2][1][0] = temp_ar[5][1][2][0]
    needed_cube[0][2][1][1] = temp_ar[5][1][2][1]
    needed_cube[0][2][0][0] = temp_ar[5][2][2][0]
    needed_cube[0][2][0][2] = temp_ar[5][2][2][1]
    needed_cube[0][2][0][1] = temp_ar[5][2][2][2]

    one_face_anticlockwise_90(needed_cube, 3)


def d_clockwise(needed_cube):
    """ D

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[2][2][0][0] = temp_ar[4][2][0][0]
    needed_cube[2][2][0][1] = temp_ar[4][2][0][1]
    needed_cube[2][2][0][2] = temp_ar[4][2][0][2]
    needed_cube[2][2][1][0] = temp_ar[4][2][1][0]
    needed_cube[2][2][1][1] = temp_ar[4][2][1][1]
    needed_cube[2][2][2][0] = temp_ar[4][2][2][0]
    needed_cube[2][2][2][1] = temp_ar[4][2][2][1]
    needed_cube[2][2][2][2] = temp_ar[4][2][2][2]

    needed_cube[3][2][0][0] = temp_ar[5][2][0][0]
    needed_cube[3][2][0][1] = temp_ar[5][2][0][1]
    needed_cube[3][2][0][2] = temp_ar[5][2][0][2]
    needed_cube[3][2][1][0] = temp_ar[5][2][1][0]
    needed_cube[3][2][1][1] = temp_ar[5][2][1][1]
    needed_cube[3][2][2][0] = temp_ar[5][2][2][0]
    needed_cube[3][2][2][1] = temp_ar[5][2][2][1]
    needed_cube[3][2][2][2] = temp_ar[5][2][2][2]

    needed_cube[4][2][0][0] = temp_ar[3][2][0][0]
    needed_cube[4][2][0][1] = temp_ar[3][2][0][1]
    needed_cube[4][2][0][2] = temp_ar[3][2][0][2]
    needed_cube[4][2][1][0] = temp_ar[3][2][1][0]
    needed_cube[4][2][1][1] = temp_ar[3][2][1][1]
    needed_cube[4][2][2][0] = temp_ar[3][2][2][0]
    needed_cube[4][2][2][1] = temp_ar[3][2][2][1]
    needed_cube[4][2][2][2] = temp_ar[3][2][2][2]

    needed_cube[5][2][0][0] = temp_ar[2][2][0][0]
    needed_cube[5][2][0][1] = temp_ar[2][2][0][1]
    needed_cube[5][2][0][2] = temp_ar[2][2][0][2]
    needed_cube[5][2][1][0] = temp_ar[2][2][1][0]
    needed_cube[5][2][1][1] = temp_ar[2][2][1][1]
    needed_cube[5][2][2][0] = temp_ar[2][2][2][0]
    needed_cube[5][2][2][1] = temp_ar[2][2][2][1]
    needed_cube[5][2][2][2] = temp_ar[2][2][2][2]

    one_face_clockwise_90(needed_cube, 0)


def d_anticlockwise(needed_cube):
    """ D'

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[4][2][0][0] = temp_ar[2][2][0][0]
    needed_cube[4][2][0][1] = temp_ar[2][2][0][1]
    needed_cube[4][2][0][2] = temp_ar[2][2][0][2]
    needed_cube[4][2][1][0] = temp_ar[2][2][1][0]
    needed_cube[4][2][1][1] = temp_ar[2][2][1][1]
    needed_cube[4][2][2][0] = temp_ar[2][2][2][0]
    needed_cube[4][2][2][1] = temp_ar[2][2][2][1]
    needed_cube[4][2][2][2] = temp_ar[2][2][2][2]

    needed_cube[5][2][0][0] = temp_ar[3][2][0][0]
    needed_cube[5][2][0][1] = temp_ar[3][2][0][1]
    needed_cube[5][2][0][2] = temp_ar[3][2][0][2]
    needed_cube[5][2][1][0] = temp_ar[3][2][1][0]
    needed_cube[5][2][1][1] = temp_ar[3][2][1][1]
    needed_cube[5][2][2][0] = temp_ar[3][2][2][0]
    needed_cube[5][2][2][1] = temp_ar[3][2][2][1]
    needed_cube[5][2][2][2] = temp_ar[3][2][2][2]

    needed_cube[3][2][0][0] = temp_ar[4][2][0][0]
    needed_cube[3][2][0][1] = temp_ar[4][2][0][1]
    needed_cube[3][2][0][2] = temp_ar[4][2][0][2]
    needed_cube[3][2][1][0] = temp_ar[4][2][1][0]
    needed_cube[3][2][1][1] = temp_ar[4][2][1][1]
    needed_cube[3][2][2][0] = temp_ar[4][2][2][0]
    needed_cube[3][2][2][1] = temp_ar[4][2][2][1]
    needed_cube[3][2][2][2] = temp_ar[4][2][2][2]

    needed_cube[2][2][0][0] = temp_ar[5][2][0][0]
    needed_cube[2][2][0][1] = temp_ar[5][2][0][1]
    needed_cube[2][2][0][2] = temp_ar[5][2][0][2]
    needed_cube[2][2][1][0] = temp_ar[5][2][1][0]
    needed_cube[2][2][1][1] = temp_ar[5][2][1][1]
    needed_cube[2][2][2][0] = temp_ar[5][2][2][0]
    needed_cube[2][2][2][1] = temp_ar[5][2][2][1]
    needed_cube[2][2][2][2] = temp_ar[5][2][2][2]

    one_face_anticlockwise_90(needed_cube, 0)


def u_clockwise(needed_cube):
    """ U

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[2][0][0][0] = temp_ar[5][0][0][0]
    needed_cube[2][0][0][1] = temp_ar[5][0][0][1]
    needed_cube[2][0][0][2] = temp_ar[5][0][0][2]
    needed_cube[2][0][1][0] = temp_ar[5][0][1][0]
    needed_cube[2][0][1][1] = temp_ar[5][0][1][1]
    needed_cube[2][0][2][0] = temp_ar[5][0][2][0]
    needed_cube[2][0][2][1] = temp_ar[5][0][2][1]
    needed_cube[2][0][2][2] = temp_ar[5][0][2][2]

    needed_cube[3][0][0][0] = temp_ar[4][0][0][0]
    needed_cube[3][0][0][1] = temp_ar[4][0][0][1]
    needed_cube[3][0][0][2] = temp_ar[4][0][0][2]
    needed_cube[3][0][1][0] = temp_ar[4][0][1][0]
    needed_cube[3][0][1][1] = temp_ar[4][0][1][1]
    needed_cube[3][0][2][0] = temp_ar[4][0][2][0]
    needed_cube[3][0][2][1] = temp_ar[4][0][2][1]
    needed_cube[3][0][2][2] = temp_ar[4][0][2][2]

    needed_cube[4][0][0][0] = temp_ar[2][0][0][0]
    needed_cube[4][0][0][1] = temp_ar[2][0][0][1]
    needed_cube[4][0][0][2] = temp_ar[2][0][0][2]
    needed_cube[4][0][1][0] = temp_ar[2][0][1][0]
    needed_cube[4][0][1][1] = temp_ar[2][0][1][1]
    needed_cube[4][0][2][0] = temp_ar[2][0][2][0]
    needed_cube[4][0][2][1] = temp_ar[2][0][2][1]
    needed_cube[4][0][2][2] = temp_ar[2][0][2][2]

    needed_cube[5][0][0][0] = temp_ar[3][0][0][0]
    needed_cube[5][0][0][1] = temp_ar[3][0][0][1]
    needed_cube[5][0][0][2] = temp_ar[3][0][0][2]
    needed_cube[5][0][1][0] = temp_ar[3][0][1][0]
    needed_cube[5][0][1][1] = temp_ar[3][0][1][1]
    needed_cube[5][0][2][0] = temp_ar[3][0][2][0]
    needed_cube[5][0][2][1] = temp_ar[3][0][2][1]
    needed_cube[5][0][2][2] = temp_ar[3][0][2][2]

    one_face_clockwise_90(needed_cube, 1)


def u_anticlockwise(needed_cube):
    """ U'

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[5][0][0][0] = temp_ar[2][0][0][0]
    needed_cube[5][0][0][1] = temp_ar[2][0][0][1]
    needed_cube[5][0][0][2] = temp_ar[2][0][0][2]
    needed_cube[5][0][1][0] = temp_ar[2][0][1][0]
    needed_cube[5][0][1][1] = temp_ar[2][0][1][1]
    needed_cube[5][0][2][0] = temp_ar[2][0][2][0]
    needed_cube[5][0][2][1] = temp_ar[2][0][2][1]
    needed_cube[5][0][2][2] = temp_ar[2][0][2][2]

    needed_cube[4][0][0][0] = temp_ar[3][0][0][0]
    needed_cube[4][0][0][1] = temp_ar[3][0][0][1]
    needed_cube[4][0][0][2] = temp_ar[3][0][0][2]
    needed_cube[4][0][1][0] = temp_ar[3][0][1][0]
    needed_cube[4][0][1][1] = temp_ar[3][0][1][1]
    needed_cube[4][0][2][0] = temp_ar[3][0][2][0]
    needed_cube[4][0][2][1] = temp_ar[3][0][2][1]
    needed_cube[4][0][2][2] = temp_ar[3][0][2][2]

    needed_cube[2][0][0][0] = temp_ar[4][0][0][0]
    needed_cube[2][0][0][1] = temp_ar[4][0][0][1]
    needed_cube[2][0][0][2] = temp_ar[4][0][0][2]
    needed_cube[2][0][1][0] = temp_ar[4][0][1][0]
    needed_cube[2][0][1][1] = temp_ar[4][0][1][1]
    needed_cube[2][0][2][0] = temp_ar[4][0][2][0]
    needed_cube[2][0][2][1] = temp_ar[4][0][2][1]
    needed_cube[2][0][2][2] = temp_ar[4][0][2][2]

    needed_cube[3][0][0][0] = temp_ar[5][0][0][0]
    needed_cube[3][0][0][1] = temp_ar[5][0][0][1]
    needed_cube[3][0][0][2] = temp_ar[5][0][0][2]
    needed_cube[3][0][1][0] = temp_ar[5][0][1][0]
    needed_cube[3][0][1][1] = temp_ar[5][0][1][1]
    needed_cube[3][0][2][0] = temp_ar[5][0][2][0]
    needed_cube[3][0][2][1] = temp_ar[5][0][2][1]
    needed_cube[3][0][2][2] = temp_ar[5][0][2][2]

    one_face_anticlockwise_90(needed_cube, 1)


def l_clockwise(needed_cube):
    """ L

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0][0][0][0] = temp_ar[2][0][0][0]
    needed_cube[0][0][0][1] = temp_ar[2][0][0][1]
    needed_cube[0][0][0][2] = temp_ar[2][0][0][2]
    needed_cube[0][1][0][0] = temp_ar[2][1][0][0]
    needed_cube[0][1][0][1] = temp_ar[2][1][0][1]
    needed_cube[0][2][0][0] = temp_ar[2][2][0][0]
    needed_cube[0][2][0][1] = temp_ar[2][2][0][1]
    needed_cube[0][2][0][2] = temp_ar[2][2][0][2]

    needed_cube[1][0][0][0] = temp_ar[3][2][2][0]
    needed_cube[1][0][0][1] = temp_ar[3][2][2][1]
    needed_cube[1][0][0][2] = temp_ar[3][2][2][2]
    needed_cube[1][1][0][0] = temp_ar[3][1][2][0]
    needed_cube[1][1][0][1] = temp_ar[3][1][2][1]
    needed_cube[1][2][0][0] = temp_ar[3][0][2][0]
    needed_cube[1][2][0][1] = temp_ar[3][0][2][1]
    needed_cube[1][2][0][2] = temp_ar[3][0][2][2]

    needed_cube[2][0][0][0] = temp_ar[1][0][0][0]
    needed_cube[2][0][0][1] = temp_ar[1][0][0][1]
    needed_cube[2][0][0][2] = temp_ar[1][0][0][2]
    needed_cube[2][1][0][0] = temp_ar[1][1][0][0]
    needed_cube[2][1][0][1] = temp_ar[1][1][0][1]
    needed_cube[2][2][0][0] = temp_ar[1][2][0][0]
    needed_cube[2][2][0][1] = temp_ar[1][2][0][1]
    needed_cube[2][2][0][2] = temp_ar[1][2][0][2]

    needed_cube[3][0][2][0] = temp_ar[0][2][0][0]
    needed_cube[3][0][2][1] = temp_ar[0][2][0][1]
    needed_cube[3][0][2][2] = temp_ar[0][2][0][2]
    needed_cube[3][1][2][0] = temp_ar[0][1][0][0]
    needed_cube[3][1][2][1] = temp_ar[0][1][0][1]
    needed_cube[3][2][2][0] = temp_ar[0][0][0][0]
    needed_cube[3][2][2][1] = temp_ar[0][0][0][1]
    needed_cube[3][2][2][2] = temp_ar[0][0][0][2]

    one_face_clockwise_90(needed_cube, 4)


def l_anticlockwise(needed_cube):
    """ L'

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[2][0][0][0] = temp_ar[0][0][0][0]
    needed_cube[2][0][0][1] = temp_ar[0][0][0][1]
    needed_cube[2][0][0][2] = temp_ar[0][0][0][2]
    needed_cube[2][1][0][0] = temp_ar[0][1][0][0]
    needed_cube[2][1][0][1] = temp_ar[0][1][0][1]
    needed_cube[2][2][0][0] = temp_ar[0][2][0][0]
    needed_cube[2][2][0][1] = temp_ar[0][2][0][1]
    needed_cube[2][2][0][2] = temp_ar[0][2][0][2]

    needed_cube[3][2][2][0] = temp_ar[1][0][0][0]
    needed_cube[3][2][2][1] = temp_ar[1][0][0][1]
    needed_cube[3][2][2][2] = temp_ar[1][0][0][2]
    needed_cube[3][1][2][0] = temp_ar[1][1][0][0]
    needed_cube[3][1][2][1] = temp_ar[1][1][0][1]
    needed_cube[3][0][2][0] = temp_ar[1][2][0][0]
    needed_cube[3][0][2][1] = temp_ar[1][2][0][1]
    needed_cube[3][0][2][2] = temp_ar[1][2][0][2]

    needed_cube[1][0][0][0] = temp_ar[2][0][0][0]
    needed_cube[1][0][0][1] = temp_ar[2][0][0][1]
    needed_cube[1][0][0][2] = temp_ar[2][0][0][2]
    needed_cube[1][1][0][0] = temp_ar[2][1][0][0]
    needed_cube[1][1][0][1] = temp_ar[2][1][0][1]
    needed_cube[1][2][0][0] = temp_ar[2][2][0][0]
    needed_cube[1][2][0][1] = temp_ar[2][2][0][1]
    needed_cube[1][2][0][2] = temp_ar[2][2][0][2]

    needed_cube[0][2][0][0] = temp_ar[3][0][2][0]
    needed_cube[0][2][0][1] = temp_ar[3][0][2][1]
    needed_cube[0][2][0][2] = temp_ar[3][0][2][2]
    needed_cube[0][1][0][0] = temp_ar[3][1][2][0]
    needed_cube[0][1][0][1] = temp_ar[3][1][2][1]
    needed_cube[0][0][0][0] = temp_ar[3][2][2][0]
    needed_cube[0][0][0][1] = temp_ar[3][2][2][1]
    needed_cube[0][0][0][2] = temp_ar[3][2][2][2]

    one_face_anticlockwise_90(needed_cube, 4)


def r_clockwise(needed_cube):
    """ R

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[0][0][2][0] = temp_ar[3][2][0][0]
    needed_cube[0][0][2][1] = temp_ar[3][2][0][1]
    needed_cube[0][0][2][2] = temp_ar[3][2][0][2]
    needed_cube[0][1][2][0] = temp_ar[3][1][0][0]
    needed_cube[0][1][2][1] = temp_ar[3][1][0][1]
    needed_cube[0][2][2][0] = temp_ar[3][0][0][0]
    needed_cube[0][2][2][1] = temp_ar[3][0][0][1]
    needed_cube[0][2][2][2] = temp_ar[3][0][0][2]

    needed_cube[1][0][2][0] = temp_ar[2][0][2][0]
    needed_cube[1][0][2][1] = temp_ar[2][0][2][1]
    needed_cube[1][0][2][2] = temp_ar[2][0][2][2]
    needed_cube[1][1][2][0] = temp_ar[2][1][2][0]
    needed_cube[1][1][2][1] = temp_ar[2][1][2][1]
    needed_cube[1][2][2][0] = temp_ar[2][2][2][0]
    needed_cube[1][2][2][1] = temp_ar[2][2][2][1]
    needed_cube[1][2][2][2] = temp_ar[2][2][2][2]

    needed_cube[2][0][2][0] = temp_ar[0][0][2][0]
    needed_cube[2][0][2][1] = temp_ar[0][0][2][1]
    needed_cube[2][0][2][2] = temp_ar[0][0][2][2]
    needed_cube[2][1][2][0] = temp_ar[0][1][2][0]
    needed_cube[2][1][2][1] = temp_ar[0][1][2][1]
    needed_cube[2][2][2][0] = temp_ar[0][2][2][0]
    needed_cube[2][2][2][1] = temp_ar[0][2][2][1]
    needed_cube[2][2][2][2] = temp_ar[0][2][2][2]

    needed_cube[3][0][0][0] = temp_ar[1][2][2][0]
    needed_cube[3][0][0][1] = temp_ar[1][2][2][1]
    needed_cube[3][0][0][2] = temp_ar[1][2][2][2]
    needed_cube[3][1][0][0] = temp_ar[1][1][2][0]
    needed_cube[3][1][0][1] = temp_ar[1][1][2][1]
    needed_cube[3][2][0][0] = temp_ar[1][0][2][0]
    needed_cube[3][2][0][1] = temp_ar[1][0][2][1]
    needed_cube[3][2][0][2] = temp_ar[1][0][2][2]

    one_face_clockwise_90(needed_cube, 5)


def r_anticlockwise(needed_cube):
    """ R'

    :param needed_cube: 被给魔方状态
    :return: None
    """
    temp_ar = needed_cube.__deepcopy__(None)
    needed_cube[3][2][0][0] = temp_ar[0][0][2][0]
    needed_cube[3][2][0][1] = temp_ar[0][0][2][1]
    needed_cube[3][2][0][2] = temp_ar[0][0][2][2]
    needed_cube[3][1][0][0] = temp_ar[0][1][2][0]
    needed_cube[3][1][0][1] = temp_ar[0][1][2][1]
    needed_cube[3][0][0][0] = temp_ar[0][2][2][0]
    needed_cube[3][0][0][1] = temp_ar[0][2][2][1]
    needed_cube[3][0][0][2] = temp_ar[0][2][2][2]

    needed_cube[2][0][2][0] = temp_ar[1][0][2][0]
    needed_cube[2][0][2][1] = temp_ar[1][0][2][1]
    needed_cube[2][0][2][2] = temp_ar[1][0][2][2]
    needed_cube[2][1][2][0] = temp_ar[1][1][2][0]
    needed_cube[2][1][2][1] = temp_ar[1][1][2][1]
    needed_cube[2][2][2][0] = temp_ar[1][2][2][0]
    needed_cube[2][2][2][1] = temp_ar[1][2][2][1]
    needed_cube[2][2][2][2] = temp_ar[1][2][2][2]

    needed_cube[0][0][2][0] = temp_ar[2][0][2][0]
    needed_cube[0][0][2][1] = temp_ar[2][0][2][1]
    needed_cube[0][0][2][2] = temp_ar[2][0][2][2]
    needed_cube[0][1][2][0] = temp_ar[2][1][2][0]
    needed_cube[0][1][2][1] = temp_ar[2][1][2][1]
    needed_cube[0][2][2][0] = temp_ar[2][2][2][0]
    needed_cube[0][2][2][1] = temp_ar[2][2][2][1]
    needed_cube[0][2][2][2] = temp_ar[2][2][2][2]

    needed_cube[1][2][2][0] = temp_ar[3][0][0][0]
    needed_cube[1][2][2][1] = temp_ar[3][0][0][1]
    needed_cube[1][2][2][2] = temp_ar[3][0][0][2]
    needed_cube[1][1][2][0] = temp_ar[3][1][0][0]
    needed_cube[1][1][2][1] = temp_ar[3][1][0][1]
    needed_cube[1][0][2][0] = temp_ar[3][2][0][0]
    needed_cube[1][0][2][1] = temp_ar[3][2][0][1]
    needed_cube[1][0][2][2] = temp_ar[3][2][0][2]

    one_face_anticlockwise_90(needed_cube, 5)
# endregion
# 映射魔方转动操作操作
# region


operate_map = {"X": x_right_hand_positive_90,
               "X'": x_right_hand_negative_90,
               "Y": y_right_hand_positive_90,
               "Y'": y_right_hand_negative_90,
               "Z": z_right_hand_positive_90,
               "Z'": z_right_hand_negative_90,
               "D": d_clockwise,
               "D'": d_anticlockwise,
               "U": u_clockwise,
               "U'": u_anticlockwise,
               "F": f_clockwise,
               "F'": f_anticlockwise,
               "B": b_clockwise,
               "B'": b_anticlockwise,
               "L": l_clockwise,
               "L'": l_anticlockwise,
               "R": r_clockwise,
               "R'": r_anticlockwise,
               }
# 总操作步骤
total_operate_list = []


def complete_operate(needed_cube, operate_list):
    global total_operate_list
    for item in operate_list:
        total_operate_list.append(item)
        operate_map[item](needed_cube)


# endregion
# 打乱魔方方法
# region
def distort_cube(needed_cube, distort_order):
    if not distort_order:
        return
    for item in distort_order:
        operate_map[item](needed_cube)


def generate_random_order(k):
    global operate_map
    random_distort_order = []
    transition_list = list(operate_map.keys())
    for i in range(k):
        random_distort_order.append(random.choice(transition_list))
    return random_distort_order


# endregion
# 复原魔方方法
# region
def recover_center(needed_cube):
    """ 复原魔方的中心
        先复原白色中心,再复原橙色中心

    :param needed_cube: 魔方状态
    :return: None
    """
    def recover_orange(inner_cube):
        if inner_cube[3][1][1][0] == 'orange':
            complete_operate(inner_cube, ["Z", "Z"])
        if inner_cube[4][1][1][0] == 'orange':
            complete_operate(inner_cube, ["Z"])
        if inner_cube[5][1][1][0] == 'orange':
            complete_operate(inner_cube, ["Z'"])

    if needed_cube[0][1][1][0] == 'white':
        recover_orange(needed_cube)

    if needed_cube[1][1][1][0] == 'white':
        complete_operate(needed_cube, ["Y", "Y"])
        recover_orange(needed_cube)

    if needed_cube[2][1][1][0] == 'white':
        complete_operate(needed_cube, ["Y"])
        recover_orange(needed_cube)

    if needed_cube[3][1][1][0] == 'white':
        complete_operate(needed_cube, ["Y'"])
        recover_orange(needed_cube)

    if needed_cube[4][1][1][0] == 'white':
        complete_operate(needed_cube, ["X"])
        recover_orange(needed_cube)

    if needed_cube[5][1][1][0] == 'white':
        complete_operate(needed_cube, ["X'"])
        recover_orange(needed_cube)


def recover_down_cross(needed_cube):
    complete_operate(needed_cube, ["Y'"])
    # 1.复原白绿
    # region
    white_green = ['white', 'green']
    green_white = ['green', 'white']
    if needed_cube[2][1][0] == white_green:
        pass
    if needed_cube[2][1][0] == green_white:
        complete_operate(needed_cube, ["L'", "U'", "F'"])

    if needed_cube[2][0][1] == white_green:
        complete_operate(needed_cube, ["F'"])
    if needed_cube[2][0][1] == green_white:
        complete_operate(needed_cube, ["F'", "L'", "U'", "F'"])

    if needed_cube[2][1][2] == white_green:
        complete_operate(needed_cube, ["F'", "F'"])
    if needed_cube[2][1][2] == green_white:
        complete_operate(needed_cube, ["F'", "F'", "L'", "U'", "F'"])

    if needed_cube[2][2][1] == white_green:
        complete_operate(needed_cube, ["F"])
    if needed_cube[2][2][1] == green_white:
        complete_operate(needed_cube, ["F", "L'", "U'", "F'"])

    if needed_cube[4][0][1] == white_green:
        complete_operate(needed_cube, ["U'", "F'"])
    if needed_cube[4][0][1] == green_white:
        complete_operate(needed_cube, ["L"])

    if needed_cube[4][2][1] == white_green:
        complete_operate(needed_cube, ["D", "F"])
    if needed_cube[4][2][1] == green_white:
        complete_operate(needed_cube, ["L'"])

    if needed_cube[5][0][1] == white_green:
        complete_operate(needed_cube, ["U", "F'"])
    if needed_cube[5][0][1] == green_white:
        complete_operate(needed_cube, ["R'", "F", "F"])

    if needed_cube[5][2][1] == white_green:
        complete_operate(needed_cube, ["D'", "F"])
    if needed_cube[5][2][1] == green_white:
        complete_operate(needed_cube, ["R", "F", "F"])

    if needed_cube[4][1][0] == white_green:
        complete_operate(needed_cube, ["L", "U'", "F'"])
    if needed_cube[4][1][0] == green_white:
        complete_operate(needed_cube, ["L", "L"])

    if needed_cube[1][0][1] == white_green:
        complete_operate(needed_cube, ["U'", "L"])
    if needed_cube[1][0][1] == green_white:
        complete_operate(needed_cube, ["B", "L", "L"])

    if needed_cube[5][1][2] == white_green:
        complete_operate(needed_cube, ["R'", "U", "F'"])
    if needed_cube[5][1][2] == green_white:
        complete_operate(needed_cube, ["B", "B", "L", "L"])

    if needed_cube[3][2][1] == white_green:
        complete_operate(needed_cube, ["B'", "L", "L"])
    if needed_cube[3][2][1] == green_white:
        complete_operate(needed_cube, ["D", "L'"])
    # endregion
    # 2.复原白红
    # region
    white_red = ['white', 'red']
    red_white = ['red', 'white']
    if needed_cube[2][2][1] == white_red:
        pass
    if needed_cube[2][2][1] == red_white:
        complete_operate(needed_cube, ["D", "R'", "B'", "D", "D"])

    if needed_cube[2][0][1] == white_red:
        complete_operate(needed_cube, ["U'", "R'", "R'", "D'"])
    if needed_cube[2][0][1] == red_white:
        complete_operate(needed_cube, ["U", "U", "B'", "R", "D'"])

    if needed_cube[2][1][2] == white_red:
        complete_operate(needed_cube, ["R'", "R'", "B'", "D", "D"])
    if needed_cube[2][1][2] == red_white:
        complete_operate(needed_cube, ["R'", "D'"])

    if needed_cube[4][0][1] == white_red:
        complete_operate(needed_cube, ["U'", "U'", "R'", "R'", "D'"])
    if needed_cube[4][0][1] == red_white:
        complete_operate(needed_cube, ["U", "B'", "R", "D'"])

    if needed_cube[4][2][1] == white_red:
        complete_operate(needed_cube, ["D"])
    if needed_cube[4][2][1] == red_white:
        complete_operate(needed_cube, ["D'", "B", "R", "D'"])

    if needed_cube[5][0][1] == white_red:
        complete_operate(needed_cube, ["R'", "R'", "D'"])
    if needed_cube[5][0][1] == red_white:
        complete_operate(needed_cube, ["R", "B'", "D", "D"])

    if needed_cube[5][2][1] == white_red:
        complete_operate(needed_cube, ["D'"])
    if needed_cube[5][2][1] == red_white:
        complete_operate(needed_cube, ["R'", "B'", "D", "D"])

    if needed_cube[4][1][0] == white_red:
        complete_operate(needed_cube, ["L'", "D", "L"])
    if needed_cube[4][1][0] == red_white:
        complete_operate(needed_cube, ["B", "D", "D"])

    if needed_cube[1][0][1] == white_red:
        complete_operate(needed_cube, ["B'", "R", "D'"])
    if needed_cube[1][0][1] == red_white:
        complete_operate(needed_cube, ["B", "B", "D", "D"])

    if needed_cube[5][1][2] == white_red:
        complete_operate(needed_cube, ["R", "D'"])
    if needed_cube[5][1][2] == red_white:
        complete_operate(needed_cube, ["B'", "D", "D"])

    if needed_cube[3][2][1] == white_red:
        complete_operate(needed_cube, ["D", "D"])
    if needed_cube[3][2][1] == red_white:
        complete_operate(needed_cube, ["B", "R", "D'"])
    # endregion
    # 3.复原白蓝
    # region
    white_blue = ['white', 'blue']
    blue_white = ['blue', 'white']
    if needed_cube[2][1][2] == white_blue:
        pass
    if needed_cube[2][1][2] == blue_white:
        complete_operate(needed_cube, ["F'", "U'", "F", "R'"])

    if needed_cube[2][0][1] == white_blue:
        complete_operate(needed_cube, ["F", "R", "F'", "R'"])
    if needed_cube[2][0][1] == blue_white:
        complete_operate(needed_cube, ["U'", "R'"])

    if needed_cube[4][0][1] == white_blue:
        complete_operate(needed_cube, ["U'", "F", "R", "F'", "R'"])
    if needed_cube[4][0][1] == blue_white:
        complete_operate(needed_cube, ["U", "U", "R'"])

    if needed_cube[4][2][1] == white_blue:
        complete_operate(needed_cube, ["F", "D'", "F'", "B", "R", "R"])
    if needed_cube[4][2][1] == blue_white:
        complete_operate(needed_cube, ["F", "D", "D", "F'", "R"])

    if needed_cube[5][0][1] == white_blue:
        complete_operate(needed_cube, ["R", "B", "U", "R'"])
    if needed_cube[5][0][1] == blue_white:
        complete_operate(needed_cube, ["R'"])

    if needed_cube[5][2][1] == white_blue:
        complete_operate(needed_cube, ["F", "R", "F'", "U'", "R'"])
    if needed_cube[5][2][1] == blue_white:
        complete_operate(needed_cube, ["R"])

    if needed_cube[4][1][0] == white_blue:
        complete_operate(needed_cube, ["B'", "U", "R'"])
    if needed_cube[4][1][0] == blue_white:
        complete_operate(needed_cube, ["B", "B", "R", "R"])

    if needed_cube[1][0][1] == white_blue:
        complete_operate(needed_cube, ["U", "R'"])
    if needed_cube[1][0][1] == blue_white:
        complete_operate(needed_cube, ["B'", "R", "R"])

    if needed_cube[5][1][2] == white_blue:
        complete_operate(needed_cube, ["B", "U", "R'"])
    if needed_cube[5][1][2] == blue_white:
        complete_operate(needed_cube, ["R", "R"])

    if needed_cube[3][2][1] == white_blue:
        complete_operate(needed_cube, ["B", "R", "R"])
    if needed_cube[3][2][1] == blue_white:
        complete_operate(needed_cube, ["D'", "R", "D"])
    # endregion
    # 4.复原白橙
    # region
    white_orange = ['white', 'orange']
    orange_white = ['orange', 'white']
    if needed_cube[2][0][1] == white_orange:
        pass
    if needed_cube[2][0][1] == orange_white:
        complete_operate(needed_cube, ["F", "R", "F'", "U"])

    if needed_cube[4][0][1] == white_orange:
        complete_operate(needed_cube, ["U'"])
    if needed_cube[4][0][1] == orange_white:
        complete_operate(needed_cube, ["L'", "B'", "L", "U", "U"])

    if needed_cube[4][2][1] == white_orange:
        complete_operate(needed_cube, ["F'", "L", "L", "F", "U'"])
    if needed_cube[4][2][1] == orange_white:
        complete_operate(needed_cube, ["F'", "L", "B'", "F", "U", "U"])

    if needed_cube[5][0][1] == white_orange:
        complete_operate(needed_cube, ["U"])
    if needed_cube[5][0][1] == orange_white:
        complete_operate(needed_cube, ["R", "B", "R'", "U", "U"])

    if needed_cube[5][2][1] == white_orange:
        complete_operate(needed_cube, ["F", "R'", "R'", "F'", "U"])
    if needed_cube[5][2][1] == orange_white:
        complete_operate(needed_cube, ["F", "R'", "B", "F'", "U", "U"])

    if needed_cube[4][1][0] == white_orange:
        complete_operate(needed_cube, ["L", "U'", "L'"])
    if needed_cube[4][1][0] == orange_white:
        complete_operate(needed_cube, ["B'", "U", "U"])

    if needed_cube[1][0][1] == white_orange:
        complete_operate(needed_cube, ["B", "L", "U'", "L'"])
    if needed_cube[1][0][1] == orange_white:
        complete_operate(needed_cube, ["U", "U"])

    if needed_cube[5][1][2] == white_orange:
        complete_operate(needed_cube, ["R'", "U", "R"])
    if needed_cube[5][1][2] == orange_white:
        complete_operate(needed_cube, ["B", "U", "U"])

    if needed_cube[3][2][1] == white_orange:
        complete_operate(needed_cube, ["B", "B", "U", "U"])
    if needed_cube[3][2][1] == orange_white:
        complete_operate(needed_cube, ["B", "R'", "U", "R"])
    # endregion
    complete_operate(needed_cube, "Y")


def recover_down_corner(needed_cube):
    """ 复原底部四个角块

    :param needed_cube: 魔方状态
    :return: None
    """
    def recover_wgo(inner_cube):
        """ 复原white-green-orange

        :param inner_cube: 魔方状态
        :return: None
        """
        white_green_orange = ['white', 'green', 'orange']
        orange_white_green = ['orange', 'white', 'green']
        green_orange_white = ['green', 'orange', 'white']
        if inner_cube[0][0][0] == white_green_orange:
            return
        if inner_cube[0][0][0] == orange_white_green:
            complete_operate(inner_cube, ["L'", "U'", "L", "U", "U", "F", "U'", "F'"])
            return
        if inner_cube[0][0][0] == green_orange_white:
            complete_operate(inner_cube, ["F", "U", "F'", "U", "U", "L'", "U", "L"])
            return

        if inner_cube[2][2][2] == white_green_orange:
            complete_operate(inner_cube, ["F'", "U'", "F", "F", "U", "U", "F'"])
            return
        if inner_cube[2][2][2] == orange_white_green:
            complete_operate(inner_cube, ["R", "U", "R'", "U'", "L'", "U", "L"])
            return
        if inner_cube[2][2][2] == green_orange_white:
            complete_operate(inner_cube, ["R", "U", "R'", "U", "F", "U'", "F'"])
            return

        if inner_cube[0][2][2] == white_green_orange:
            complete_operate(inner_cube, ["B", "U", "B'", "U", "U", "F", "U'", "F'"])
            return
        if inner_cube[0][2][2] == orange_white_green:
            complete_operate(inner_cube, ["R'", "U'", "R", "F", "U'", "F'"])
            return
        if inner_cube[0][2][2] == green_orange_white:
            complete_operate(inner_cube, ["B", "U", "B'", "L'", "U", "L"])
            return

        if inner_cube[3][2][2] == white_green_orange:
            complete_operate(inner_cube, ["B'", "U'", "B", "U", "F", "U'", "F'"])
            return
        if inner_cube[3][2][2] == orange_white_green:
            complete_operate(inner_cube, ["L", "U", "L'", "L'", "U", "U", "L"])
            return
        if inner_cube[3][2][2] == green_orange_white:
            complete_operate(inner_cube, ["B'", "U'", "B", "U'", "L'", "U", "L"])
            return

        if inner_cube[2][0][0] == white_green_orange:
            complete_operate(inner_cube, ["U'", "L'", "U", "L"])
            return
        if inner_cube[2][0][0] == orange_white_green:
            complete_operate(inner_cube, ["U", "F", "U'", "F'"])
            return
        if inner_cube[2][0][0] == green_orange_white:
            complete_operate(inner_cube, ["F", "U'", "F'", "L'", "U", "U", "L"])
            return

        if inner_cube[1][2][2] == white_green_orange:
            complete_operate(inner_cube, ["R", "U'", "R'", "U'", "U'", "L'", "U", "L"])
            return
        if inner_cube[1][2][2] == orange_white_green:
            complete_operate(inner_cube, ["L'", "U", "L"])
            return
        if inner_cube[1][2][2] == green_orange_white:
            complete_operate(inner_cube, ["U", "U", "F", "U'", "F'"])
            return

        if inner_cube[3][0][0] == white_green_orange:
            complete_operate(inner_cube, ["L'", "U", "U", "L"])
            return
        if inner_cube[3][0][0] == orange_white_green:
            complete_operate(inner_cube, ["U'", "F", "U'", "F'"])
            return
        if inner_cube[3][0][0] == green_orange_white:
            complete_operate(inner_cube, ["R'", "U", "R", "U", "F", "U'", "F'"])
            return

        if inner_cube[4][0][0] == white_green_orange:
            complete_operate(inner_cube, ["U", "U", "L'", "U", "L"])
            return
        if inner_cube[4][0][0] == orange_white_green:
            complete_operate(inner_cube, ["F", "U'", "F'"])
            return
        if inner_cube[4][0][0] == green_orange_white:
            complete_operate(inner_cube, ["L", "U'", "L'", "L'", "U", "L"])
            return

    def recover_wbo(inner_cube):
        """ 复原white-blue-orange

        :param inner_cube: 魔方状态
        :return: None
        """
        white_blue_orange = ['white', 'blue', 'orange']
        orange_white_blue = ['orange', 'white', 'blue']
        blue_orange_white = ['blue', 'orange', 'white']
        if inner_cube[0][0][2] == white_blue_orange:
            return
        if inner_cube[0][0][2] == orange_white_blue:
            complete_operate(inner_cube, ["R", "U", "R'", "U'", "U'", "F'", "U", "F"])
            return
        if inner_cube[0][0][2] == blue_orange_white:
            complete_operate(inner_cube, ["F'", "U'", "F", "U", "U", "R", "U'", "R'"])
            return

        if inner_cube[3][2][0] == white_blue_orange:
            complete_operate(inner_cube, ["B", "U", "B'", "U'", "F'", "U", "F"])
            return
        if inner_cube[3][2][0] == orange_white_blue:
            complete_operate(inner_cube, ["R'", "U", "U", "R", "R", "U'", "R'"])
            return
        if inner_cube[3][2][0] == blue_orange_white:
            complete_operate(inner_cube, ["R'", "U'", "R", "F'", "U", "U", "F"])
            return

        if inner_cube[0][2][0] == white_blue_orange:
            complete_operate(inner_cube, ["L", "U", "L'", "U", "U", "R", "U'", "R'"])
            return
        if inner_cube[0][2][0] == orange_white_blue:
            complete_operate(inner_cube, ["L", "U", "L'", "F'", "U", "F"])
            return
        if inner_cube[0][2][0] == blue_orange_white:
            complete_operate(inner_cube, ["B'", "U'", "B", "R", "U'", "R'"])
            return

        if inner_cube[1][2][0] == white_blue_orange:
            complete_operate(inner_cube, ["U'", "R", "U'", "R'", "F'", "U'", "U'", "F"])
            return
        if inner_cube[1][2][0] == orange_white_blue:
            complete_operate(inner_cube, ["R", "U'", "R'"])
            return
        if inner_cube[1][2][0] == blue_orange_white:
            complete_operate(inner_cube, ["U'", "U'", "F'", "U", "F"])
            return

        if inner_cube[2][0][2] == white_blue_orange:
            complete_operate(inner_cube, ["U", "R", "U'", "R'"])
            return
        if inner_cube[2][0][2] == orange_white_blue:
            complete_operate(inner_cube, ["U'", "F'", "U", "F"])
            return
        if inner_cube[2][0][2] == blue_orange_white:
            complete_operate(inner_cube, ["R", "U'", "R'", "F'", "U", "U", "F"])
            return

        if inner_cube[5][0][2] == white_blue_orange:
            complete_operate(inner_cube, ["U'", "U'", "R", "U'", "R'"])
            return
        if inner_cube[5][0][2] == orange_white_blue:
            complete_operate(inner_cube, ["F'", "U", "F"])
            return
        if inner_cube[5][0][2] == blue_orange_white:
            complete_operate(inner_cube, ["B", "U'", "B'", "U'", "U'", "F'", "U", "F"])
            return

        if inner_cube[3][0][2] == white_blue_orange:
            complete_operate(inner_cube, ["R", "U'", "U'", "R'"])
            return
        if inner_cube[3][0][2] == orange_white_blue:
            complete_operate(inner_cube, ["F'", "U", "U", "F"])
            return
        if inner_cube[3][0][2] == blue_orange_white:
            complete_operate(inner_cube, ["L", "U'", "L'", "U'", "F'", "U", "F"])
            return

    def recover_wbr(inner_cube):
        """ 复原white-blue-red

        :param inner_cube: 魔方状态
        :return: None
        """
        white_blue_red = ['white', 'blue', 'red']
        red_white_blue = ['red', 'white', 'blue']
        blue_red_white = ['blue', 'red', 'white']
        if inner_cube[0][0][0] == white_blue_red:
            return
        if inner_cube[0][0][0] == red_white_blue:
            complete_operate(inner_cube, ["L'", "U'", "L", "U'", "F", "U", "U", "F'"])
            return
        if inner_cube[0][0][0] == blue_red_white:
            complete_operate(inner_cube, ["F", "U", "F'", "U'", "U'", "L'", "U", "L"])
            return

        if inner_cube[2][2][2] == white_blue_red:
            complete_operate(inner_cube, ["F'", "U'", "F", "F", "U", "U", "F'"])
            return
        if inner_cube[2][2][2] == red_white_blue:
            complete_operate(inner_cube, ["R", "U", "R'", "U'", "L'", "U", "L"])
            return
        if inner_cube[2][2][2] == blue_red_white:
            complete_operate(inner_cube, ["F'", "U'", "F", "L'", "U", "U", "L"])
            return

        if inner_cube[2][0][0] == white_blue_red:
            complete_operate(inner_cube, ["U'", "L'", "U", "L"])
            return
        if inner_cube[2][0][0] == red_white_blue:
            complete_operate(inner_cube, ["U", "F", "U'", "F'"])
            return
        if inner_cube[2][0][0] == blue_red_white:
            complete_operate(inner_cube, ["F", "U'", "F'", "L'", "U", "U", "L"])
            return

        if inner_cube[1][2][2] == white_blue_red:
            complete_operate(inner_cube, ["F'", "U", "F", "F", "U'", "F'"])
            return
        if inner_cube[1][2][2] == red_white_blue:
            complete_operate(inner_cube, ["L'", "U", "L"])
            return
        if inner_cube[1][2][2] == blue_red_white:
            complete_operate(inner_cube, ["U", "U", "F", "U'", "F'"])
            return

        if inner_cube[3][0][0] == white_blue_red:
            complete_operate(inner_cube, ["L'", "U", "U", "L"])
            return
        if inner_cube[3][0][0] == red_white_blue:
            complete_operate(inner_cube, ["F", "U", "U", "F'"])
            return
        if inner_cube[3][0][0] == blue_red_white:
            complete_operate(inner_cube, ["U", "F'", "U", "F", "F", "U'", "F'"])
            return

        if inner_cube[4][0][0] == white_blue_red:
            complete_operate(inner_cube, ["U", "L'", "U", "U", "L"])
            return
        if inner_cube[4][0][0] == red_white_blue:
            complete_operate(inner_cube, ["F", "U'", "F'"])
            return
        if inner_cube[4][0][0] == blue_red_white:
            complete_operate(inner_cube, ["U'", "F", "U'", "F'", "L'", "U", "U", "L"])
            return

    def recover_wgr(inner_cube):
        """ 复原white-green-red

        :param inner_cube: 魔方状态
        :return: None
        """
        white_green_red = ['white', 'green', 'red']
        red_white_green = ['red', 'white', 'green']
        green_red_white = ['green', 'red', 'white']
        if inner_cube[0][0][2] == white_green_red:
            return
        if inner_cube[0][0][2] == red_white_green:
            complete_operate(inner_cube, ["R", "U", "R'", "U'", "U'", "F'", "U", "F"])
            return
        if inner_cube[0][0][2] == green_red_white:
            complete_operate(inner_cube, ["F'", "U'", "F", "U", "U", "R", "U'", "R'"])
            return

        if inner_cube[1][2][0] == white_green_red:
            complete_operate(inner_cube, ["U'", "R", "U'", "R'", "F'", "U'", "U'", "F"])
            return
        if inner_cube[1][2][0] == red_white_green:
            complete_operate(inner_cube, ["R", "U'", "R'"])
            return
        if inner_cube[1][2][0] == green_red_white:
            complete_operate(inner_cube, ["U", "F'", "U'", "U'", "F"])
            return

        if inner_cube[2][0][2] == white_green_red:
            complete_operate(inner_cube, ["U", "R", "U'", "R'"])
            return
        if inner_cube[2][0][2] == red_white_green:
            complete_operate(inner_cube, ["R", "U", "R'"])
            return
        if inner_cube[2][0][2] == green_red_white:
            complete_operate(inner_cube, ["R", "U'", "R'", "F'", "U", "U", "F"])
            return

        if inner_cube[1][0][2] == white_green_red:
            complete_operate(inner_cube, ["U", "F'", "U", "F", "R", "U'", "U'", "R'"])
            return
        if inner_cube[1][0][2] == red_white_green:
            complete_operate(inner_cube, ["U", "U", "R", "U'", "R'"])
            return
        if inner_cube[1][0][2] == green_red_white:
            complete_operate(inner_cube, ["F'", "U", "F"])
            return

        if inner_cube[3][0][2] == white_green_red:
            complete_operate(inner_cube, ["R", "U", "U", "R'"])
            return
        if inner_cube[3][0][2] == red_white_green:
            complete_operate(inner_cube, ["F'", "U'", "U'", "F"])
            return
        if inner_cube[3][0][2] == green_red_white:
            complete_operate(inner_cube, ["U", "U", "R", "U'", "R'", "F'", "U", "U", "F"])
            return

    recover_wgo(needed_cube)
    recover_wbo(needed_cube)
    complete_operate(needed_cube, ["Z", "Z"])
    recover_wbr(needed_cube)
    recover_wgr(needed_cube)
    complete_operate(needed_cube, ["Z'", "Z'"])


def recover_second_floor(needed_cube):
    """ 复原第二层魔方

    :param needed_cube: 魔方状态
    :return: None
    """
    def recover_one_center_corner(inner_cube, positive_color, anti_color):
        """ 复原第二层通用方法

        :param inner_cube: 魔方状态
        :param positive_color: 给的魔方块正向颜色
        :param anti_color: 给的魔方块逆向颜色
        :return: None
        """
        if inner_cube[2][0][1] == positive_color:
            complete_operate(inner_cube, ["U", "R", "U'", "R'", "U'", "F'", "U", "F"])
            return
        if inner_cube[4][0][1] == positive_color:
            complete_operate(inner_cube, ["R", "U'", "R'", "U'", "F'", "U", "F"])
            return
        if inner_cube[3][0][1] == positive_color:
            complete_operate(inner_cube, ["U'", "R", "U'", "R'", "U'", "F'", "U", "F"])
            return
        if inner_cube[5][0][1] == positive_color:
            complete_operate(inner_cube, ["U'", "U'", "R", "U'", "R'", "U'", "F'", "U", "F"])
            return
        if inner_cube[2][1][2] == positive_color:
            return
        if inner_cube[2][1][0] == positive_color:
            complete_operate(inner_cube, ["F", "U'", "F'", "U'", "L'", "U", "L", "U",
                                          "U", "R", "U'", "R'", "U'", "F'", "U", "F"])
            return
        if inner_cube[4][1][0] == positive_color:
            complete_operate(inner_cube, ["L", "U'", "L'", "U'", "B'", "U", "B",
                                          "U", "R", "U'", "R'", "U'", "F'", "U", "F"])
            return
        if inner_cube[5][1][2] == positive_color:
            complete_operate(inner_cube, ["R'", "U", "R", "U", "B", "U'", "B'",
                                          "U", "R", "U'", "R'", "U'", "F'", "U", "F"])
            return

        if inner_cube[2][0][1] == anti_color:#
            complete_operate(inner_cube, ["U'", "U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[4][0][1] == anti_color:#
            complete_operate(inner_cube, ["U", "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[3][0][1] == anti_color:#
            complete_operate(inner_cube, [ "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[5][0][1] == anti_color:#
            complete_operate(inner_cube, ["U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[2][1][2] == anti_color:#
            complete_operate(inner_cube, ["F'", "U", "F", "U", "R", "U'", "R'",
                                          "U", "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[2][1][0] == anti_color:#
            complete_operate(inner_cube, ["F", "U'", "F'", "U'", "L'", "U", "L",
                                          "U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[4][1][0] == anti_color:#
            complete_operate(inner_cube, ["L", "U'", "L'", "U'", "B'", "U", "B",
                                          "U'", "U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            return
        if inner_cube[5][1][2] == anti_color:#
            complete_operate(inner_cube, ["R'", "U", "R", "U", "B", "U'", "B'",
                                          "U'", "U'", "F'", "U", "F", "U", "R", "U'", "R'"])
            return

    # 复原橙蓝
    recover_one_center_corner(needed_cube, ['orange', 'blue'], ['blue', 'orange'])
    complete_operate(needed_cube, ["Z"])
    # 复原绿橙
    recover_one_center_corner(needed_cube, ['green', 'orange'], ['orange', 'green'])
    complete_operate(needed_cube, ["Z"])
    # 复原红绿
    recover_one_center_corner(needed_cube, ['red', 'green'], ['green', 'red'])
    complete_operate(needed_cube, ["Z"])
    # 复原蓝红
    recover_one_center_corner(needed_cube, ['blue', 'red'], ['red', 'blue'])
    complete_operate(needed_cube, ["Z"])


def recover_up_cross(needed_cube):
    """ 复原顶层十字

    :param needed_cube: 魔方状态
    :return: None
    """
    if ((needed_cube[1][0][1][0] == 'yellow') &
            (needed_cube[1][1][0][0] == 'yellow') &
            (needed_cube[1][1][2][0] == 'yellow') &
            (needed_cube[1][2][1][0] == 'yellow')):
        pass

    if ((needed_cube[1][0][1][0] != 'yellow') &
            (needed_cube[1][1][0][0] != 'yellow') &
            (needed_cube[1][1][2][0] != 'yellow') &
            (needed_cube[1][2][1][0] != 'yellow')):
        complete_operate(needed_cube, ["F", "R", "U", "R'", "U'", "F'", "U", "U",
                                       "F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"])

    if ((needed_cube[1][0][1][0] == 'yellow') &
            (needed_cube[1][1][0][0] == 'yellow') &
            (needed_cube[1][1][2][0] != 'yellow') &
            (needed_cube[1][2][1][0] != 'yellow')):
        complete_operate(needed_cube, ["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"])

    if ((needed_cube[1][0][1][0] != 'yellow') &
            (needed_cube[1][1][0][0] == 'yellow') &
            (needed_cube[1][1][2][0] != 'yellow') &
            (needed_cube[1][2][1][0] == 'yellow')):
        complete_operate(needed_cube, ["U",
                                       "F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"])

    if ((needed_cube[1][0][1][0] != 'yellow') &
            (needed_cube[1][1][0][0] != 'yellow') &
            (needed_cube[1][1][2][0] == 'yellow') &
            (needed_cube[1][2][1][0] == 'yellow')):
        complete_operate(needed_cube, ["U", "U",
                                       "F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"])

    if ((needed_cube[1][0][1][0] == 'yellow') &
            (needed_cube[1][1][0][0] != 'yellow') &
            (needed_cube[1][1][2][0] == 'yellow') &
            (needed_cube[1][2][1][0] != 'yellow')):
        complete_operate(needed_cube, ["U'",
                                       "F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"])

    if ((needed_cube[1][0][1][0] != 'yellow') &
            (needed_cube[1][1][0][0] == 'yellow') &
            (needed_cube[1][1][2][0] == 'yellow') &
            (needed_cube[1][2][1][0] != 'yellow')):
        complete_operate(needed_cube, ["F", "R", "U", "R'", "U'", "F'"])

    if ((needed_cube[1][0][1][0] == 'yellow') &
            (needed_cube[1][1][0][0] != 'yellow') &
            (needed_cube[1][1][2][0] != 'yellow') &
            (needed_cube[1][2][1][0] == 'yellow')):
        complete_operate(needed_cube, ["U",
                                       "F", "R", "U", "R'", "U'", "F'"])


def recover_up_to_one_color(needed_cube):
    """ 复原顶面为一色

    :param needed_cube: 魔方状态
    :return: None
    """
    def recover_one_to_full(inner_cube):
        if ((inner_cube[1][0][2][0] == 'yellow') and
                (inner_cube[3][0][2][0] == 'yellow') and
                (inner_cube[4][0][2][0] == 'yellow') and
                (inner_cube[2][0][2][0] == 'yellow')):
            complete_operate(inner_cube, ["L", "U", "L'", "U", "L", "U", "U", "L'"])
            return
        if ((inner_cube[1][0][2][0] == 'yellow') and
                (inner_cube[4][0][0][0] == 'yellow') and
                (inner_cube[2][0][0][0] == 'yellow') and
                (inner_cube[5][0][0][0] == 'yellow')):
            complete_operate(inner_cube, ["F'", "U'", "F", "U'", "F'", "U'", "U'", "F"])
            return

    def recover_multi_condition(inner_cube):
        # +---
        if ((inner_cube[1][0][2][0] == 'yellow') and
                (inner_cube[1][0][0][0] != 'yellow') and
                (inner_cube[1][2][0][0] != 'yellow') and
                (inner_cube[1][2][2][0] != 'yellow')):
            recover_one_to_full(inner_cube)
            return
        # ++--
        if ((inner_cube[5][0][0][0] == 'yellow') and
                (inner_cube[5][0][2][0] == 'yellow') and
                (inner_cube[1][0][0][0] == 'yellow') and
                (inner_cube[1][2][0][0] == 'yellow')):
            complete_operate(inner_cube, ["F'", "U'", "F", "U'", "F'", "U'", "U'", "F",
                                          "U"])
            recover_one_to_full(inner_cube)
            return
        if ((inner_cube[3][0][0][0] == 'yellow') and
                (inner_cube[2][0][2][0] == 'yellow') and
                (inner_cube[1][0][0][0] == 'yellow') and
                (inner_cube[1][2][0][0] == 'yellow')):
            complete_operate(inner_cube, ["L", "U", "L'", "U", "L", "U", "U", "L'",
                                          "U"])
            recover_one_to_full(inner_cube)
            return
        # +-+-
        if ((inner_cube[5][0][2][0] == 'yellow') and
                (inner_cube[1][0][0][0] == 'yellow') and
                (inner_cube[2][0][0][0] == 'yellow') and
                (inner_cube[1][2][2][0] == 'yellow')):
            complete_operate(inner_cube, ["F'", "U'", "F", "U'", "F'", "U'", "U'", "F"])
            recover_one_to_full(inner_cube)
            return
        if ((inner_cube[3][0][0][0] == 'yellow') and
                (inner_cube[1][0][0][0] == 'yellow') and
                (inner_cube[4][0][2][0] == 'yellow') and
                (inner_cube[1][2][2][0] == 'yellow')):
            complete_operate(inner_cube, ["L", "U", "L'", "U", "L", "U", "U", "L'"])
            recover_one_to_full(inner_cube)
            return
        # ----
        if ((inner_cube[2][0][2][0] == 'yellow') and
                (inner_cube[2][0][0][0] == 'yellow') and
                (inner_cube[3][0][0][0] == 'yellow') and
                (inner_cube[3][0][2][0] == 'yellow')):
            complete_operate(inner_cube, ["F'", "U'", "F", "U'", "F'", "U'", "U'", "F"])
            recover_one_to_full(inner_cube)
            return
        if ((inner_cube[2][0][2][0] == 'yellow') and
                (inner_cube[2][0][0][0] == 'yellow') and
                (inner_cube[4][0][0][0] == 'yellow') and
                (inner_cube[5][0][2][0] == 'yellow')):
            complete_operate(inner_cube, ["L", "U", "L'", "U", "L", "U", "U", "L'",
                                          "U"])
            recover_one_to_full(inner_cube)
            return

    for i in range(4):
        recover_multi_condition(needed_cube)
        if ((needed_cube[1][0][0][0] == 'yellow') and
                (needed_cube[1][0][2][0] == 'yellow') and
                (needed_cube[1][2][0][0] == 'yellow') and
                (needed_cube[1][2][2][0] == 'yellow')):
            break
        complete_operate(needed_cube, ["U"])


def recover_up_corner(needed_cube):
    """ 复原顶层四个角块

    :param needed_cube: 魔方状态
    :return: None
    """
    for i in range(4):
        if((needed_cube[2][0][0][0] == needed_cube[2][0][2][0]) and
                (needed_cube[4][0][0][0] != needed_cube[4][0][2][0]) and
                (needed_cube[3][0][0][0] != needed_cube[3][0][2][0]) and
                (needed_cube[5][0][0][0] != needed_cube[5][0][2][0])):
            complete_operate(needed_cube, ["R", "B'", "R", "F", "F", "R'", "B", "R",
                                           "F", "F", "R", "R"])
            break

        if ((needed_cube[2][0][0][0] == needed_cube[2][0][2][0]) and
                (needed_cube[4][0][0][0] == needed_cube[4][0][2][0]) and
                (needed_cube[3][0][0][0] == needed_cube[3][0][2][0]) and
                (needed_cube[5][0][0][0] == needed_cube[5][0][2][0])):
            break

        if ((needed_cube[2][0][0][0] != needed_cube[2][0][2][0]) and
                (needed_cube[4][0][0][0] != needed_cube[4][0][2][0]) and
                (needed_cube[3][0][0][0] != needed_cube[3][0][2][0]) and
                (needed_cube[5][0][0][0] != needed_cube[5][0][2][0])):
            complete_operate(needed_cube, ["R", "B'", "R", "F", "F", "R'", "B", "R",
                                           "F", "F", "R", "R"])

        complete_operate(needed_cube, ["U"])

    for i in range(4):
        if needed_cube[2][0][0][0] == 'orange':
            break
        complete_operate(needed_cube, ["U"])


def recover_to_init(needed_cube):
    """ 复原顶层四个棱

    :param needed_cube: 魔方状态
    :return: None
    """
    z_count = 0
    for i in range(4):
        if ((needed_cube[3][0][1][0] == needed_cube[3][1][1][0]) and
                (needed_cube[4][0][1][0] == needed_cube[4][1][1][0]) and
                (needed_cube[2][0][1][0] == needed_cube[2][1][1][0]) and
                (needed_cube[5][0][1][0] == needed_cube[5][1][1][0])):
            break

        if ((needed_cube[3][0][1][0] == needed_cube[3][1][1][0]) and
                (needed_cube[4][0][1][0] == needed_cube[5][1][1][0]) and
                (needed_cube[2][0][1][0] == needed_cube[4][1][1][0]) and
                (needed_cube[5][0][1][0] == needed_cube[2][1][1][0])):
            complete_operate(needed_cube, ["L'", "U", "L'", "U'", "L'", "U'", "L'", "U",
                                           "L", "U", "L'", "L'"])
            break

        if ((needed_cube[3][0][1][0] == needed_cube[3][1][1][0]) and
                (needed_cube[4][0][1][0] == needed_cube[2][1][1][0]) and
                (needed_cube[2][0][1][0] == needed_cube[5][1][1][0]) and
                (needed_cube[5][0][1][0] == needed_cube[4][1][1][0])):
            complete_operate(needed_cube, ["R", "U'", "R", "U", "R", "U", "R", "U'",
                                           "R'", "U'", "R", "R"])
            break

        if ((needed_cube[3][0][1][0] == needed_cube[4][1][1][0]) and
                (needed_cube[4][0][1][0] == needed_cube[3][1][1][0]) and
                (needed_cube[2][0][1][0] == needed_cube[5][1][1][0]) and
                (needed_cube[5][0][1][0] == needed_cube[2][1][1][0])):
            complete_operate(needed_cube, ["R", "U'", "R", "U", "R", "U", "R", "U'",
                                           "R'", "U'", "R", "R",
                                           "U'",
                                           "R", "U'", "R", "U", "R", "U", "R", "U'",
                                           "R'", "U'", "R", "R",
                                           "U"])
            break
            
        if ((needed_cube[3][0][1][0] == needed_cube[2][1][1][0]) and
                (needed_cube[4][0][1][0] == needed_cube[5][1][1][0]) and
                (needed_cube[2][0][1][0] == needed_cube[3][1][1][0]) and
                (needed_cube[5][0][1][0] == needed_cube[4][1][1][0])):
            complete_operate(needed_cube, ["R", "U'", "R", "U", "R", "U", "R", "U'",
                                           "R'", "U'", "R", "R",
                                           "U",
                                           "R", "U'", "R", "U", "R", "U", "R", "U'",
                                           "R'", "U'", "R", "R",
                                           "U'"])
            break

        complete_operate(needed_cube, ["Z"])
        z_count += 1

    if z_count == 1:
        complete_operate(needed_cube, ["Z'"])
    if z_count == 2:
        complete_operate(needed_cube, ["Z'", "Z'"])
    if z_count == 3:
        complete_operate(needed_cube, ["Z"])


# endregion
if __name__ == '__main__':
    print(f'当前时间:{time.ctime()}')
    input_content = input('随机打乱魔方(Y/y|N/n,默认随机):')
    is_random_distort = input_content.upper() if input_content != '' else 'Y'
    if is_random_distort == 'N':
        input_distort_steps = input("输入打乱步骤,提示U,F',X,B,用英文逗号隔开:")
        if input_distort_steps == '':
            distort_steps = []
        else:
            distort_steps = input_distort_steps.split(',')
    elif is_random_distort == 'Y':
        distort_number = input('输入打乱次数:')
        distort_steps = generate_random_order(int(distort_number))
    else:
        raise Exception('输入的文字有问题')
    print("魔方初始状态:")
    pprint.pprint(standard_colors.tolist(), width=40)
    distort_cube(standard_colors, distort_steps)
    print('魔方打乱之后状态:')
    pprint.pprint(standard_colors.tolist(), width=40)
    print('开始复原魔方')
    time_start = time.time()
    recover_center(standard_colors)
    recover_down_cross(standard_colors)
    recover_down_corner(standard_colors)
    recover_second_floor(standard_colors)
    recover_up_cross(standard_colors)
    recover_up_to_one_color(standard_colors)
    recover_up_corner(standard_colors)
    recover_to_init(standard_colors)
    time_end = time.time()
    print(f'魔方复原耗时:{time_end-time_start}s')
    print('魔方复原成功')
    print('魔方复原之后状态')
    pprint.pprint(standard_colors.tolist(), width=40)
    print('魔方打乱步骤:')
    print(distort_steps)
    print('魔方复原步骤:')
    print(total_operate_list)

