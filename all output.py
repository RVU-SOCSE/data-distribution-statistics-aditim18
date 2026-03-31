Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/array.py
Original Array: [1 2 3 4 5 6]

Reshaped Array:
 [[1 2 3]
 [4 5 6]]

First element: 1
Element at [0][1]: 2

Sum of elements: 21

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/operation array.py
Matrix A:
 [[1 2]
 [3 4]]

Matrix B:
 [[5 6]
 [7 8]]

Addition:
 [[ 6  8]
 [10 12]]

Multiplication:
 [[19 22]
 [43 50]]

Transpose of A:
 [[1 3]
 [2 4]]

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/data file.py
DataFrame from Dictionary:
     Name  Marks
0  Aditi     85
1  Rohan     90
2  Meera     78

DataFrame from CSV:
     Name  Marks   Age
0  Aditi   85.0  20.0
1  Rohan    NaN  21.0
2  Meera   78.0   NaN
3  Aditi   85.0  20.0

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/data.py
Missing Values:
     Name  Marks    Age
0  False  False  False
1  False   True  False
2  False  False   True
3  False  False  False

Cleaned Data:
     Name      Marks        Age
0  Aditi  85.000000  20.000000
1  Rohan  82.666667  21.000000
2  Meera  78.000000  20.333333

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/data1.py
Mean:
 Marks    82.666667
Age      20.333333
dtype: float64

Median:
 Marks    85.0
Age      20.0
dtype: float64

Mode:
     Name  Marks   Age
0  Aditi   85.0  20.0

Min:
 Marks    78.0
Age      20.0
dtype: float64

Max:
 Marks    85.0
Age      21.0
dtype: float64

Variance:
 Marks    16.333333
Age       0.333333
dtype: float64

Standard Deviation:
 Marks    4.041452
Age      0.577350
dtype: float64
>>> 
= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/data2.py
Describe:
            Marks        Age
count   3.000000   3.000000
mean   82.666667  20.333333
std     4.041452   0.577350
min    78.000000  20.000000
25%    81.500000  20.000000
50%    85.000000  20.000000
75%    85.000000  20.500000
max    85.000000  21.000000
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/all prog/data2.py", line 6, in <module>
    print("\nQuantiles:\n", df.quantile([0.25, 0.5, 0.75]))
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\frame.py", line 16165, in quantile
    res = data._mgr.quantile(qs=q, interpolation=interpolation)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\internals\managers.py", line 1720, in quantile
    blk.quantile(qs=qs, interpolation=interpolation) for blk in self.blocks
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\internals\blocks.py", line 1495, in quantile
    result = quantile_compat(self.values, np.asarray(qs._values), interpolation)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\array_algos\quantile.py", line 41, in quantile_compat
    return values._quantile(qs, interpolation)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\arrays\_mixins.py", line 512, in _quantile
    res_values = quantile_with_mask(arr, mask, fill_value, qs, interpolation)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\array_algos\quantile.py", line 84, in quantile_with_mask
    res_values = quantile_with_mask(values, mask, fill_value, qs, interpolation)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\array_algos\quantile.py", line 97, in quantile_with_mask
    result = _nanquantile(
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\core\array_algos\quantile.py", line 218, in _nanquantile
    return np.quantile(
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\numpy\lib\_function_base_impl.py", line 4496, in quantile
    return _quantile_unchecked(
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\numpy\lib\_function_base_impl.py", line 4510, in _quantile_unchecked
    return _ureduce(a,
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\numpy\lib\_function_base_impl.py", line 3880, in _ureduce
    r = func(a, **kwargs)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\numpy\lib\_function_base_impl.py", line 4669, in _quantile_ureduce_func
    result = _quantile(arr,
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\numpy\lib\_function_base_impl.py", line 4807, in _quantile
    result = _lerp(previous,
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\numpy\lib\_function_base_impl.py", line 4596, in _lerp
    diff_b_a = b - a
TypeError: unsupported operand type(s) for -: 'str' and 'str'
