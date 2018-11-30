"""
8. Pipeline

As part of a data processing pipeline, complete the implementation of the pipeline method:

* The method should accept a variable number of functions,
 and it should return a new function that accepts one
 parameter arg.

* The returned function should call the first function in the
 pipeline with the parameter arg, and call the second
 function with the result of the first function.

* The returned function should continue calling each function
 in the pipeline in order, following the same pattern, and
 return the value from the last function.

For example, Pipeline.pipeline(lambda x: x * 3, lambda x: x + 1,
lambda x: x / 2) then calling the returned function with 3 should
return 5.0.


Time : 66 min
Tests: 2 pass / 1 fail
  Example case: Correct answer
  Various functions: File "pipeline.py", line 11, in helper: TypeError
  Various data types: Correct answer


* Subject - Closure, Decorator(core concept)
* Learning
    1. passing func to *args (tuple)

"""


# class Pipeline:
#     @staticmethod
#     def pipeline(*funcs):
#         funcs_list = list(funcs)
#
#         def helper(arg):
#             # Step 1
#             # print('hi')
#             # return funcs[0](arg)
#
#             # Step 2
#             result = funcs_list[0](arg)
#             if len(funcs_list) > 1:
#                 funcs_list[0:1] = []
#                 return helper(result)
#             else:
#                 return result
#         return helper

class Pipeline:
    @staticmethod
    def pipeline(*funcs):
        i = 0

        def helper(arg):
            nonlocal i
            result = funcs[i](arg)
            i += 1
            if i < len(funcs):
                return helper(result)
            else:
                return result
        return helper


fun = Pipeline.pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
# fun = Pipeline.pipeline(lambda x: x * 3)
print(fun(3))  # should print 5.0

"""
181111 Review

Time : 29 min
Tests: 3 pass / 0 fail
  Example case: Correct answer 
  Various functions: Correct answer 
  Various data types: Correct answer 
"""


# class Pipeline:
#     @staticmethod
#     def pipeline(*funcs):
#         def helper(arg, *func_list):
#             if not func_list:
#                 arg = funcs[0](arg)
#                 func_list = funcs
#             else:
#                 func_list = func_list[0]
#                 arg = func_list[0](arg)
#
#             if len(func_list) == 1:
#                 return arg
#             return helper(arg, func_list[1:])
#         return helper
#
#
# fun = Pipeline.pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
# print(fun(3))  # should print 5.0
#

"""
181129 Review

Time : 60 min
Tests: 3 pass / 0 fail
  Example case: Correct answer 
  Various functions: Correct answer 
  Various data types: Correct answer 
"""


# 1) Various functions: "pipeline.py", line 11, in helper: IndexError

class Pipeline:
    @staticmethod
    def pipeline(*funcs):
        def helper(arg, *funcs2):

            if not funcs2:
                ret = funcs[0](arg)

                # This made an exception(error) above
                return helper(ret, funcs[1:])

                # hot_fix
                # funcs2 = funcs

            else:
                funcs2 = funcs2[0]
                ret = funcs2[0](arg)

            if len(funcs2) == 1:
                return ret

            return helper(ret, funcs2[1:])

        return helper


# 2) UnboundLocalError: local variable 'funcs' referenced before assignment
# class Pipeline:
#     @staticmethod
#     def pipeline(*funcs):
#
#         def helper(arg, *args):
#
#             ret = funcs[0](arg)
#             funcs = funcs[1:]
#
#             return helper(ret)
#         return helper


# 3) Tests: 3 pass / 0 fail
class Pipeline:
    @staticmethod
    def pipeline(*funcs):
        def helper(arg, *args):

            if not args:
                funcs2 = funcs
            else:
                funcs2 = args[0]

            ret = funcs2[0](arg)

            if len(funcs2) == 1:
                return ret

            return helper(ret, funcs2[1:])
        return helper


fun = Pipeline.pipeline(lambda x: x / 2)
print(fun(3))  # should print 5.0
