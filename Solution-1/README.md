# Solution 1

Loading the `__subclasses__` of the `BaseAction` class and creating a 'pluggable' classes. The actions can be specified in the `configuration.py` file in the `ACTIONS` const. This method is inspired by django's `INSTALLED_APPS` method. 

The `call` method is a placeholder for the "actions".

## To Register an action

- New python file in `actions/` folder
- Create a class with an appropriate name (ex. `ClickAction`)
- Extend the class with `BaseAction`
- Add an entry to `ACTIONS` const located in `configuration.py` file with the approriate path to the module

After that the function will be avaliable at the `register` in the `main.py` file.

```console
$ python main.py
[<class 'actions.action_example1.Example1Action'>, <class 'actions.action_example2.Example2Action'>]
```

## Benchmarks

```powershell
Measure-Command { python .\main.py }

Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 24
Ticks             : 240745
TotalDays         : 2.78640046296296E-07
TotalHours        : 6.68736111111111E-06
TotalMinutes      : 0.000401241666666667
TotalSeconds      : 0.0240745
TotalMilliseconds : 24.0745
```