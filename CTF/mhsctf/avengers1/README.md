# Avengers Assemble 1 Write-Up

## Challenge Description

```
The club I've been trying to get into has tightened up their security a lot! Can you get the password for me again? Note: the file uses the .asm extension which is not necessarily entirely accurate.
```

* * *

## File

> [Avengers Assemble 1](./avengers1.asm)

* * *

## First Meet with python assembly

This challenges need to find the '**key**' in given assembly file. Before open it, I though it was intel syntax assembly.

But as you can see in Sub title that was python disassembly and looks like interesting.

```
  1           0 LOAD_CONST               0 (<code object main at 0x564456b6b9c0, file "example.py", line 1>)
              2 LOAD_CONST               1 ('main')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (main)

 15           8 LOAD_NAME                0 (main)
             10 CALL_FUNCTION            0
             12 POP_TOP
             14 LOAD_CONST               2 (None)
             16 RETURN_VALUE
```

Above code is part of disassembly result. They have **a lot of different** syntax even though structure(example, code progress) is similar to intel syntax.

If i knew about disassembly code of python i would interpret only related with **Key Generation** function, but i didn't know anything so try to step-by-step.

* * *

## Python Disassembly with dis module

I found the module to change disassembly code from python code the called 'dis'. You can download module by pip if you haven't yet.

I'm refer to the python dis module [document](https://docs.python.org/3/library/dis.html) and not difficult if you learned assembly already.

This is example:

```
def foo:
    # How to Work?

dis.dis(foo) # Show disassembly result foo function
```

* * *

## HandRay

I can't find decompiler so i did decompile with my hand & eye. Follow code is result my decompile. Not a perfect but working is same.

```python
def main():
    inp = input("What's the password")
    pwd = ''

    for i in range(len(inp)):
        pwd += chr(ord(inp[i]) + int(i % 7))

    comp = [102, 109, 99, 106, 127, 53, 116, 95, 122, 113, 120, 118, 100, 55, 51, 103, 57, 128]
    incor = False

    for i in range(len(pwd)):
        if pwd != chr(comp[i]):
            print("Incorrect Password")
            incor = True
            break

    if incor:
        pass
    else:
        print("Welcome!!")
```

Encoding process is too much simple `inp[i] + i % 7 == comp[i]` If know `comp list`, `inp[i] == comp[i] - i % 7`.

It's my decoding code.

```python
def decode():
    pwd = ''
    comp = [102, 109, 99, 106, 127, 53, 116, 95, 122, 113, 120, 118, 100, 55, 51, 103, 57, 128]

    for i in range(len(comp)):
        pwd += chr(comp[i] - int(i % 7))
    return print(pwd)
```

* * *

## flag

> `flag{0n_your_13f7}`
