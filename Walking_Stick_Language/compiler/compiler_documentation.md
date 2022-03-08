### Compiler for the Walking Stick Language (WSL)


## **ver 0.1 (alpha)**

# **ver 0.1 (alpha) targets**

- Input file, by taking the `filename`. Perform integrity check (as of now, check extension).
- Iterate over the file. Separate everything in spaces into a python list. Call it program_list.
- Create a class `program`. Its purpose is to - 
	- Iterate over the `program_list`, understand the program, and translate it to its python equivalent.
		- Separate the logical command lines (like, `say "hello"`), and translate it to its python equivalent (`print("hello")`)
		- Add those "command lines" to a string, call it the `execstring` (make sure to give proper indentation and newlines)
	- Execute the python equivalent.
		- use `exec` function to execute the `execstring`

	> **NOTE:** `program_list`, `filename`, `execstring` should be the properties of the class `program`.