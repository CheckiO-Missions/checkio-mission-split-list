"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4,5,6]],
            "answer": [[1,2,3], [4,5,6]],
        },
        {
            "input": [[1,2,3]],
            "answer": [[1,2], [3,]],
        },
        {
            "input": [[1,2,3,4,5]],
            "answer": [[1,2,3], [4,5]],
        },
        {
            "input": [[1,]],
            "answer": [[1,], []],
        },
        {
            "input": [[]],
            "answer": [[], []],
        }
    ],
    "Extra": [
        {
            "input": [[1,1,1,1,1]],
            "answer": [[1,1,1], [1,1]],
        },
        {
            "input": [[6,7,8,9]],
            "answer": [[6,7], [8,9]],
        }
    ]
}
