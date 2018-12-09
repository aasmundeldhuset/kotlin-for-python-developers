_This material was written by [Aasmund Eldhuset](https://eldhuset.net/); it is owned by [Khan Academy](https://www.khanacademy.org/) and is licensed for use under [CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). Please note that this is not a part of Khan Academy's official product offering._

---


Let's get straight to the point - type this into a file with the extension `.kt`:

```kotlin
fun main(args: Array<String>) {
    println("Hello World!")
}
```

Only imports and declarations can exist at the top level of a Kotlin file. Therefore, "running" an individual file only makes sense if it contains an _entry point_, which must be a function called `main` with one argument called `args` of the type "array of strings". `args` will contain the command-line arguments that the program is invoked with, similarly to `sys.argv` in Python; it can be omitted if your program does not need to accept command-line arguments and you are using Kotlin 1.3:

```kotlin
fun main() {
    println("Hello World!")
}
```

The function body is delimited by curly braces - indentation is generally not significant in Kotlin, but you should of course indent your code properly for the benefit of human readers.

Comments are initiated with `//` and last until the end of the line. Block comments start with `/*` and end with `*/`.

Like in Python, statements may be terminated by a semicolon, but it's discouraged. There is no line continuation character; instead, a line is automatically joined with one or more of the subsequent lines if that's the only way to make the code parse correctly. In practice, that means that a statement continues on the next line if we're inside an open parenthesis (like in Python), or if the line ends with a "dangling operator" (unlike in Python) or the following line doesn't parse unless it's joined to the previous one (also unlike in Python). Note that this is pretty much [the opposite of JavaScript](https://stackoverflow.com/questions/2846283/what-are-the-rules-for-javascripts-automatic-semicolon-insertion-asi#2846298), which generally will keep joining lines as long as the resulting code still parses. Thus, the following is two expressions in Kotlin and in Python (because `+` can be unary, so the second line parses on its own), but one in JavaScript:

```kotlin
1 + 2
+ 3
```

This is one expression in both Kotlin (because the first line doesn't parse on its own) and JavaScript, and doesn't parse in Python:

```kotlin
1 + 2 +
3
```

So is the following. The difference between `+` and `.` is that `+` can be a unary operator, but `.` can't, so the only way to get the second line to parse is to join it with the preceding line:

```kotlin
x.foo()
 .bar()
```

This is one expression in all three languages:

```kotlin
(1 + 2
 + 3)
```

Don't split lines if the resulting two lines are also grammatically valid on their own (even if it results in a compilation error that is not directly related to the grammar of Kotlin). The following does not actually return the result of `foo()` - it returns a special value called `Unit`, which we'll cover later, and `foo()` is never called.

```kotlin
return    // Empty return statement
    foo() // Separate, unreachable statement
```


