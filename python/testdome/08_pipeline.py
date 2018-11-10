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
"""


# class Pipeline:
#     @staticmethod
#     def pipeline(*funcs):
#
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
            # Step 2
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
