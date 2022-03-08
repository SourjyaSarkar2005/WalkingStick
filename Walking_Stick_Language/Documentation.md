### The Walking Stick language

This programming language has been made to teach programming concepts to the not so lucky people, ie., those who are physically handicapped.

This is a Documentation on how to use the language. The goal at hand is to be as simple as possible. 

## **Where to read/write/run code?**

*This section needs to be updated. Right now, we are working on the compiler. The compiler will be python based.*

## **Variables:**

syntax: ` variable = 34 `

Usage: can be used to assign a value to a variable. The value can be numerical, string, or value of another variable.

## **Functions:**

Since this a language aimed at teaching programming concepts, it is going to have the most vital functions only, like an equivalent of print, input, numeric conversions, mathematical operations, etc. 

# **say function:**

syntax: `say "text to speak. it can be variable as well" argument`

Usage: This function is to be used to speak or print a certain string, either contained in a variable or in quotation. Then a suitable argument is to be used to perform other functions. 

**Arguments:**
1. `times` argument: to repeat a certain string for a number of times.

	syntax: ` say "hello world!" 5 times `

2. `+` argument: to combine certain strings or variables to say together.

	*example*: ` a = "world" `

		     ` say "hello" + a 2 times `

	Other usage: can be used to perform and speak or print 	mathematical operation. Like, `say 5 + 9`
	*NOTE*: It is different from ` say "5" + "9" `


# **Mathematical operators**

The valid mathematical operators are `+`, `-`, `/`, `*`. These are to be used with number and strings (not all operators however are valid with string).

*Examples:*
	`a + b`
	`"hello" * 2` | Output = `hellohello`
	`"hello" + 2` | Output = `hello2`
	`10 + 5` | Output = `15`


# **`number` function**

This function converts a string to number.

syntax: `variable = number "string to change. Can be a variable."`

NOTE: String must be numeric. Else it will produce error. There is no distinction between float and integer in this language for simplicity.


# **`know` function**

This function takes user input.

syntax: `variable = know "string to be said to the user"`

This will take the user input and store the input in the variable `variable`.


*To take numeric input,*
`variable = know number "string to be said to the user" `


## **LOOPS**

# **`while` loop:**

This will forever execute a command until the condition is fulfilled.

syntax:

```
	while |condition| 
		1 say "hello"
		2 say "bye"
	endwhile
```

Although indentation is used in this case and is encouraged as well, this is not **compulsory**. The above code is equivalent to - 

` while |condition| 1 say "hello" 2 say "bye" endwhile`

However, the instructions needs to be ordered by using numbers.


# **`for` loop:**

This loop will iterate over something, or a range of numbers.

syntax:

```
	for |condition|
		1 name = know "what is your name?"
		2 say "hello " + name
	endfor
```

Again, indentation is not necessary.

*An example to iterate for a certain number of times:*

```
	for 5 times 1 name = know "what is your name" 2 say "hello" + name endfor
```

The `times` argument can be used to iterate a loop
