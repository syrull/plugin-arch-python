# Solution 2

The benefits of this solution are that we have a control over the decorator and we can pass some custom `*args, **kwargs` to the decorated functions.

## To Register an action

- New python file in `actions/` folder
- Create function with an appropriate name (ex. `action_onclick`)
- Decorate the function with `register_action` decorator
- Export the function in the `__all__` method in `actions/__init__.py` file

After that the function will be avaliable at the `register` in the `main.py` file.


```console
$ python main.py
[<function action_example1 at 0x000001CC3F88D310>, <function action_example2 at 0x000001CC3F88D3A0>]
```

## Benchmarks

```powershell
Measure-Command { python .\main.py }

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 22
Ticks             : 227803
TotalDays         : 2.6366087962963E-07
TotalHours        : 6.32786111111111E-06
TotalMinutes      : 0.000379671666666667
TotalSeconds      : 0.0227803
TotalMilliseconds : 22.7803
```