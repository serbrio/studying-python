###############################################
# Simple function factory example (from Lutz) #
###############################################

"""The outer function generates and returns a nested function
without calling it.
'Maker' creates 'action', but does not run it.
The nested function 'remembers' the value of the variable n in maker,
even though maker has returned and exited by the time we call action.
Like: object with generated 'action' has 'n' as an attachment.
So when the generated object (with the generated 'action') is called,
it takes an argument (x) and has the 'n' at its disposal for further actions.
"""


def maker(n):
    def action(x):
        return x * n
    return action


# >>> f = maker(2)   # Pass 2 to argument 'n'
# >>> f
# >>> <function maker.<locals>.action at ......>
# >>> f(3)           # Pass 3 to 'x'; 'n' is remembered as 2 -> 2*3 -> 6
# >>> 6
