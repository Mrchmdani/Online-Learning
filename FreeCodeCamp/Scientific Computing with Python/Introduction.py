x = 1
print(x)
x = x + 1
print(x)

x = 2           #assignment statement
x = x + 1       #asignment with expression
print(x)        #print statement

# Interactive cs script
    # Interactive = type directly to python one line at a time and it responds
    # script = enter a sequence of statements (line) into a file using a text editor and tell Python to execute the statement in the file

#Conditional Steps
x = 5
if x < 10 :
    print('smaller')
if x > 20 :
    print('bigger')
print('Finish')

#Repeated Steps
n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff')

#Sequential Code
name = input('Enter file:')
handle = open(name, 'r')

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

#Variables
    #A variable is a named place in the memory where a programmer can store data and later retrieve it

x = 12.2
y = 14
x = 100     #rewrite the first 'x' variable

#python variable name rules
    #must start with a letter or underscore
    #must consist of letters, numbers, and underscore
    #case censitive

#Numeric Expression
    # + addition
    # - subtraction
    # * multiplication
    # / division
    # ** power
    # % remainder / modular operator -> bilangan yang tidak habis setelah dibagi misal: 23/5 -> 5*4 = 20 -> 23-20 = 3 -> 3 adalah sisanya/remainder/modular

#Operator Precedence Rules
    # Parenthese
    # Exponentiation (power)
    # Multiplication, division, and remainder
    #addition and subtraction
    # left to right

#User Input
name = input('Who are you? ')
print('Welcome', name)

#Comparison Operators
# < Less than
# <= Less than or Equal to
# == Equal to
# >= Greater than or Equal to
# > Greater than
# != Not equal

x = 5
if x == 5 :
    print('Equal 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than 5 or Equals 5')    
if x < 6 :
    print('Less than 4')
if x <= 5 :
    print('Less than or Equal 5')
if x != 6 :
    print('Not Equal 6')

#One-Way Decisions
x = 5
print('Before 5')
if x == 5 :
    print ('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x -- 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

#Nested Decisions
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
        print('Less than 100')
print('All done')

#Two-way Decisions with Else
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
Print 'All done'

#Multi-way
if x < 2 :
    print('Small')
elif x < 10 :
    print*'Medium'
else :
    print('Large')
print('All done')

#Indent is matter, wrong index makes error

#IndetationError: unexpected indent
x = 5
    if x < 10 :         #there is spaces before "IF", that cause error
print('smaller')
print('Finish')

#IndetationError: unindent does not match any outer indentation level
x = 5
if x < 10 :
print('smaller')        #this code has the same number of spaces with before
print('Finish')

# Unindent does not match any outer indentation level. 
    # This line of code has fewer spaces at the start than the one before, but equally it does not match any other block it could be part of.
    # Python cannot decide where it goes.

#Try and except condition
astr = 'Bob'
try :
    print('Hallo')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print('Nice work')
else:
    print('Not a number')

#Stored (and reused) Steps
def thing():
    print('Hello')
    print('Fun')
thing()         #Hello Fun
print('Zip')    #Zip
thing()         #Hello Fun

x = 5
print('Hello')
def print_lyric() :
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyric()
x = x + 2
print(x)