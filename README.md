# chsize

----

chsize = chinese character size

get the real size of a character use in shell(with monospace font)

for example 

```
'a'  use 1
'啊' use 2
```


## usage

```
In [1]: from chsize import chlen

In [2]: chlen('hello world!')
Out[2]: 12

In [3]: chlen('你好世界！')
Out[3]: 10
```


## why make it

recently I need to auto generate rst layout doc for Sphinx, but when generate table 

```
# Ipython Python 3.4.3

In [1]: u' {:{}} |'.format( a', 2)
Out[1]: ' a  |'

In [2]: u' {:{}} |'.format('我', 2)
Out[2]: ' 我  |'

```

because python only take care of count of word, not if it is half width or full width.



## how it work

inspired from `http://stackoverflow.com/questions/10959227/how-to-distinguish-whether-a-word-is-half-width-or-full-width`

[detail](test.sh)

3400—4DBF

now only support for some commonly used word in work

1. half-width and full width [FF00—FFEF](http://unicode-table.com/cn/blocks/halfwidth-and-fullwidth-forms/) 
2. chinese/japanese/korean character [4E00—9FFF](http://unicode-table.com/cn/blocks/cjk-unified-ideographs/)

