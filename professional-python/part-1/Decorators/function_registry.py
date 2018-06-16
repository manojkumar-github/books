registry = []
def register(decorated):
    registry.append(decorated)
    return decorated

@register
def foo():
    return 3

@register
def bar():
    return 5

answers = []
for func in registry:
    answers.append(func())

# functions are executed in order and the results are appended as it is
print answers