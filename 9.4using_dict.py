Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: G:/python/code/9.1 using_list.py =================
i have 4 items to buy
These items are:
apple
mango
carrot
banana

I also have to buy rice
Traceback (most recent call last):
  File "G:/python/code/9.1 using_list.py", line 14, in <module>
    shoplist.attend('rice')
AttributeError: 'list' object has no attribute 'attend'
>>> 
================= RESTART: G:/python/code/9.1 using_list.py =================
i have 4 items to buy
These items are:
apple
mango
carrot
banana

I also have to buy rice
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
the first item i will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
>>> 
================= RESTART: G:/python/code/9.1 using_list.py =================
i have 4 items to buy
These items are:

apple
mango
carrot
banana

I also have to buy rice

My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
the first item i will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
>>> 
================= RESTART: G:/python/code/9.1 using_list.py =================
i have 4 items to buy
These items are:

apple
mango
carrot
banana

I also have to buy rice

My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
the first item i will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
>>> 
================= RESTART: G:/python/code/9.1 using_list.py =================
i have 4 items to buy
These items are:
apple
mango
carrot
banana

I also have to buy rice

My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
the first item i will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
>>> 
================= RESTART: G:/python/code/9.1 using_list.py =================
i have 4 items to buy
These items are:
apple
mango
carrot
banana

I also have to buy rice

My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
the first item i will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
================= RESTART: G:/python/code/9.2using_tuple.py =================
Number of animals in the zoo is  6
Number of animals in the new zoo is 3
All animals in new zoo are ('monkey', 'dolphin', ('wolf', 'cat', 'tiger', 'lion', 'elephant', 'penguin'))
Animals brought from old zoo are ('wolf', 'cat', 'tiger', 'lion', 'elephant', 'penguin')
Last animal brought from old zoo is penguin
>>> 
================= RESTART: G:/python/code/9.3print_tuple.py =================
%s is %d years old%(name,age)
Why is Phil playing with that python?
>>> 
================= RESTART: G:/python/code/9.3print_tuple.py =================
Phil is 22 years old
Why is Phil playing with that python?
>>> 
======================= RESTART: G:/python/code/9.4.py =======================
Swaroop's address is swaroopch@byteofpython.info

There are 4 contacts in the address-book

Contact Swaroop at swaroopch@byteofpython.info
Contact Larry at larry@wall.org
Contact Matsumoto at matz@ruby-lang.org
Contact Guido at guido@python.org
/nGuido's address is guido@python.org
>>> 
