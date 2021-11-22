print ("Hello world")
>>> print("Hello world")
Hello world
>>> pwd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pwd' is not defined
>>> cd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cd' is not defined
>>> ls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ls' is not defined
>>> type (3)
<class 'int'>
>>> type (a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> type (abc)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> type ("abc")
<class 'str'>
>>> ballots = 1,341
>>> ballot (1, 341)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ballot' is not defined
>>> ballots
(1, 341)
>>> type (ballots)
<class 'tuple'>
>>> type ('Hello world')
<class 'str'>
>>> type (      hello   world   )
  File "<stdin>", line 1
    type (      hello   world   )
                      ^
SyntaxError: invalid syntax
>>> type ("")
<class 'str'>
>>> type (True)
<class 'bool'>
>>> type (False)
<class 'bool'>
>>> type ('True')
<class 'str'>
>>> help ("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>> 5+2*#
  File "<stdin>", line 1
    5+2*#
        ^
SyntaxError: invalid syntax
>>> 5+2*3
11
>>> 8//5-3
-2
>>> 8+22*2-4
48
>>> 16-3/2+7-1
20.5
>>> 3**3 % 5
2
>>> 5+9*3/2-4
14.5
>>> 3**(3 % 5)
27
>>> (5+2) * 3
21
>>> (8//5)-3
-2
>>> 5 + (9*3/2-4)
14.5
>>> 5+(9*3/(2-4))
-8.5
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> my_list = []
>>> my_list = list ()
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties (0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> counties[0]
'Arapahoe'
>>> print(counties[0])
Arapahoe
>>> print(counties[-2])
Denver
>>> counties[-1]
'Jefferson'
>>> counties[0]
'Arapahoe'
>>> len(counties[0])
8
>>> len(counties)
3
>>> counties[0:2]
['Arapahoe', 'Denver']
>>> counties[1:2]
['Denver']
>>> counties[1:3]
['Denver', 'Jefferson']
>>> counties[0:1]
['Arapahoe']
>>> counties [:3]
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[1:}
  File "<stdin>", line 1
    counties[1:}
               ^
SyntaxError: invalid syntax
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties.append ('El Paso')
>>> counties[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> counties[3]
'El Paso'
>>> counties[0:]
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.append(2,'El Paso')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> counties.insert(2,'El Paso')
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.remove('El Paso')
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.remove('El Paso')
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties.append ('El Paso')
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop(-4)
'Arapahoe'
>>> counties.insert(1,'Arapahoe')
>>> counties
['Denver', 'Arapahoe', 'Jefferson', 'El Paso']
>>> counties.pop(1)
'Arapahoe'
>>> counties.insert(0, 'Arapahoe')
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop(3)
'El Paso'
>>> counties[2]='El Paso'
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties[1]='El Paso'
>>> counties.pop(0)
'Arapahoe'
>>> counties[1]='Jefferson'
>>> counties
['El Paso', 'Jefferson']
>>> counties[2]='Denver'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> counties.append('Denver')
>>> counties
['El Paso', 'Jefferson', 'Denver']
>>> counties.append('Arapahoe')
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Arapahoe']
>>> my_tuple = ()
>>> my_tuple =tuple()
>>> counties_tuple
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'counties_tuple' is not defined
>>> counties_tuple = ("Arapahoe","Denver","Jefferson")
>>> len(counties_tuple)
3
>>> counties_tuple[1]
'Denver'
>>> counties_tupl2[):]
  File "<stdin>", line 1
    counties_tupl2[):]
                   ^
SyntaxError: invalid syntax
>>> counties_tuple[0:]
('Arapahoe', 'Denver', 'Jefferson')
>>> counties_tuple[-2]
'Denver'
>>> counties_tuple:-2]
  File "<stdin>", line 1
    counties_tuple:-2]
                     ^
SyntaxError: invalid syntax
>>> counties_tuple[:-2]
('Arapahoe',)
>>> counties_tuple[:2]
('Arapahoe', 'Denver')
>>> counties_tuple[-1]
'Jefferson'
>>> counties_tuple[1:2]
('Denver',)
>>> counties_tuple[:-2]
('Arapahoe',)
>>> counties_tuple[:-1]
('Arapahoe', 'Denver')
>>> my_dictionary = {}
>>> my_dictionary = dict()
>>> dict
<class 'dict'>
>>> int
<class 'int'>
>>> s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> counties_dict = {}
>>> counties_dict["Arapahoe"]=422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict["Denver"]=463353
>>> counties_dict["Jeffersion"]=432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jeffersion': 432438}
>>> len(counties_dict)
3
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jeffersion', 432438)])
>>> counties_dict.items([1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: items() takes no arguments (1 given)
>>> counties_dict.item([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'item'
>>> count_dict()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count_dict' is not defined
>>> counties_dict()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jeffersion'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get(Denver)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Denver' is not defined
>>> counties_dict.get("Denver")
463353
>>> counties_dict['Arapahoe']
422829
>>> voting_date = []
>>> voting_date.append({"county":"Arapahoe","registered_voters":422829})
>>> voting_date.append({"county":"Denver","registered_voters":463353})
>>> voting_data.append({"county":"Jefferson","registered_voters":432438})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'voting_data' is not defined
>>> voting_date.append({"county":"Jefferson","registered_voters":432438})
>>> voting_date
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> len(voting_date)
3
>>> voting_date[1]
{'county': 'Denver', 'registered_voters': 463353}
>>> voting_date.append({"county":"El Paso","registered_voters":461149})
>>> voting_date.pop("Arapahoe")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> voting_date.remove("Arapahoe")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> voting_date.remove({"county:"Arapahoe","registered_voteres":422829})
  File "<stdin>", line 1
    voting_date.remove({"county:"Arapahoe","registered_voteres":422829})
                                        ^
SyntaxError: invalid syntax
>>> voting_date
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Paso', 'registered_voters': 461149}]
>>> voting_date.remove[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> voting_date.remove(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> voting_date.remove
