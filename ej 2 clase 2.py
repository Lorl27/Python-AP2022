Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 3/7
0.42857142857142855
>>> 3*5
15
>>> 8**3
512
>>> 8*3
24
>>> 8*8
64
>>> 8*8*3
192
>>> 8*8*3*3
576
>>> "Hola" + "Mundo"
'HolaMundo'
>>> cerrar
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    cerrar
NameError: name 'cerrar' is not defined
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> simbols
No Python documentation found for 'simbols'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> (symbols)
No Python documentation found for '(symbols)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> "symbols"

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> "keywords"

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and""                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> "topics"

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> "**"
The power operator
******************

The power operator binds more tightly than unary operators on its
left; it binds less tightly than unary operators on its right.  The
syntax is:

   power ::= (await_expr | primary) ["**" u_expr]

Thus, in an unparenthesized sequence of power and unary operators, the
operators are evaluated from right to left (this does not constrain
the evaluation order for the operands): "-1**2" results in "-1".

The power operator has the same semantics as the built-in "pow()"
function, when called with two arguments: it yields its left argument
raised to the power of its right argument.  The numeric arguments are
first converted to a common type, and the result is of that type.

For int operands, the result has the same type as the operands unless
the second argument is negative; in that case, all arguments are
converted to float and a float result is delivered. For example,
"10**2" returns "100", but "10**-2" returns "0.01".

Raising "0.0" to a negative power results in a "ZeroDivisionError".
Raising a negative number to a fractional power results in a "complex"
number. (In earlier versions it raised a "ValueError".)

Related help topics: EXPRESSIONS, OPERATORS

help> 