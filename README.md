# Kotlin for Python developers

_By [Aasmund Eldhuset](https://eldhuset.net/), Software Engineer at [Khan Academy](https://www.khanacademy.org/). Published on November 29, 2018._  
_This document is not a part of Khan Academy's official product offering, but rather an [internal resource](http://engineering.khanacademy.org/posts/kotlin-for-python-developers.htm) that we're providing "as&nbsp;is" for the benefit of the programming community. If you find any errors, please submit an [issue](https://github.com/Khan/kotlin-for-python-developers/issues) or a [pull request](https://github.com/Khan/kotlin-for-python-developers/pulls)._

---

Kotlin is a compiled, statically typed language, which might provide some initial hurdles for people who are used to the interpreted, dynamically typed Python. This document aims to explain a substantial portion of Kotlin's syntax and concepts in terms of how they compare to corresponding concepts in Python.

Kotlin can be compiled for several different platforms. In this document, we assume that the target platform is the Java virtual machine, which grants some extra capabilities - in particular, your code will be compiled to Java bytecode and will therefore be interoperable with the large ecosystem of Java libraries.

Even if you don't know Python, this document should hopefully be a useful introduction to Kotlin, in particular if you are used to other dynamically typed languages. However, if you're coming from a Java background, you're probably better off diving directly into the excellent [official docs](https://kotlinlang.org/docs/reference/) (from which this doc has drawn a lot of inspiration). To some extent, you can try to write Java code and look stuff up whenever what you're trying to do doesn't work - and some IDEs can even automatically convert Java code to Kotlin.


## Contents

* [Hello World](#hello-world)
* [Compiling and running](#compiling-and-running)
* [Declaring variables](#declaring-variables)
    * [Read-only variables](#read-only-variables)
    * [Constants](#constants)
    * [Specifying the type explicitly](#specifying-the-type-explicitly)
    * [Scopes and naming](#scopes-and-naming)
* [Primitive data types and their limitations](#primitive-data-types-and-their-limitations)
    * [Integer types](#integer-types)
    * [Floating-point and other types](#floating-point-and-other-types)
* [Strings](#strings)
* [Conditionals](#conditionals)
    * [`if`/`else`](#ifelse)
    * [Comparisons](#comparisons)
    * [`when`](#when)
* [Collections](#collections)
* [Loops](#loops)
    * [`for`](#for)
    * [`while`](#while)
    * [`continue` and `break`](#continue-and-break)
* [Functions](#functions)
    * [Declaration](#declaration)
    * [Calling](#calling)
    * [Returning](#returning)
    * [Overloading](#overloading)
    * [Varargs and optional/named parameters](#varargs-and-optionalnamed-parameters)
* [Classes](#classes)
    * [Declaration and instantiation](#declaration-and-instantiation)
    * [Inherited built-in functions](#inherited-built-in-functions)
    * [Properties](#properties)
    * [Constructors and initializer blocks](#constructors-and-initializer-blocks)
    * [Setters and getters](#setters-and-getters)
    * [Member functions](#member-functions)
    * [Lateinit](#lateinit)
    * [Infix functions](#infix-functions)
    * [Operators](#operators)
    * [Enum classes](#enum-classes)
    * [Data classes](#data-classes)
* [Exceptions](#exceptions)
    * [Throwing and catching](#throwing-and-catching)
    * [Nothing](#nothing)
* [Null safety](#null-safety)
    * [Working with nulls](#working-with-nulls)
    * [Safe call operator](#safe-call-operator)
    * [Elvis operator](#elvis-operator)
    * [Not-null assertion operator](#not-null-assertion-operator)
* [Functional programming](#functional-programming)
    * [Function types](#function-types)
    * [Function literals: lambda expressions and anonymous functions](#function-literals-lambda-expressions-and-anonymous-functions)
    * [Comprehensions](#comprehensions)
    * [Receivers](#receivers)
    * [Inline functions](#inline-functions)
    * [Nice utility functions](#nice-utility-functions)
        * [`run()`, `let()`, and `with()`](#run-let-and-with)
        * [`apply()` and `also()`](#apply-and-also)
        * [`takeIf()` and `takeUnless()`](#takeif-and-takeunless)
* [Packages and imports](#packages-and-imports)
    * [Packages](#packages)
    * [Imports](#imports)
* [Visibility modifiers](#visibility-modifiers)
* [Inheritance](#inheritance)
    * [Subclassing](#subclassing)
    * [Overriding](#overriding)
    * [Interfaces](#interfaces)
    * [Abstract classes](#abstract-classes)
    * [Polymorphism](#polymorphism)
    * [Casting and type testing](#casting-and-type-testing)
    * [Delegation](#delegation)
    * [Delegated properties](#delegated-properties)
    * [Sealed classes](#sealed-classes)
* [Objects and companion objects](#objects-and-companion-objects)
    * [Object declarations](#object-declarations)
    * [Companion objects](#companion-objects)
    * [Object expressions](#object-expressions)
* [Generics](#generics)
    * [Generic type parameters](#generic-type-parameters)
    * [Constraints](#constraints)
    * [Variance](#variance)
        * [Introduction](#introduction)
        * [Declaration-site covariance and contravariance](#declaration-site-covariance-and-contravariance)
        * [Variance directions](#variance-directions)
        * [Type projections (use-site covariance and contravariance)](#type-projections-use-site-covariance-and-contravariance)
    * [Reified type parameters](#reified-type-parameters)
* [Extension functions/properties](#extension-functionsproperties)
* [Member references and reflection](#member-references-and-reflection)
    * [Property references](#property-references)
    * [Function references](#function-references)
    * [Obtaining member references from a class reference](#obtaining-member-references-from-a-class-reference)
    * [Java-style reflection](#java-style-reflection)
* [Annotations](#annotations)
* [File I/O](#file-io)
* [Scoped resource usage](#scoped-resource-usage)
* [Documentation](#documentation)


## Hello World

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


## Compiling and running

The author strongly recommends that you use an IDE with Kotlin support, as the static typing allows an IDE to do reliable navigation and code completion. I recommend [IntelliJ IDEA](https://www.jetbrains.com/idea/), which is built by the same company that created Kotlin. The Community Edition is free; see [instructions for getting started](https://kotlinlang.org/docs/tutorials/getting-started.html) (it comes bundled with Kotlin, and you can run your program from the IDE).

If you insist on using a plain editor and the command line, see [these instructions instead](https://kotlinlang.org/docs/tutorials/command-line.html). In short, you need to _compile_ your Kotlin code before running it. Assuming that your Kotlin file is called `program.kt`:

```bash
kotlinc program.kt -include-runtime -d program.jar
```

By default, Kotlin compiles down to Java (so you have the entire Java Standard Library available to you, and interacting with Java libraries is a breeze), so you now have a Java Archive (`program.jar`) which includes the Java libraries that are necessary to support the Kotlin features (thanks to `-include-runtime`), and you can run it using an out-of-the-box Java runtime:

```bash
java -jar program.jar
```


## Declaring variables

Every variable must be _declared_. Any attempt to use a variable that hasn't been declared yet is a syntax error; thus, you are protected from accidentally assigning to a misspelled variable. The declaration also decides what kind of data you are allowed to store in the variable.

Local variables are typically declared and initialized at the same time, in which case the type of the variable is _inferred_ to be the type of the expression you initialize it with:

```kotlin
var number = 42
var message = "Hello"
```

We now have a local variable `number` whose value is 42 and whose type is `Int` (because that's the type of the literal `42`), and another local variable `message` whose value is `"Hello"` and whose type is `String`. Subsequent usages of the variable must use only the name, not `var`:

```kotlin
number = 10
number += 7
println(number)
println(message + " there")
```

However, you cannot change the type of a variable: `number` can only ever refer to `Int` values, and `message` can only ever refer to `String` values, so both `number = "Test"` and `message = 3` are illegal and will produce syntax errors.


### Read-only variables

Frequently, you'll find that during the lifetime of your variable, it only ever needs to refer to one object. Then, you can declare it with `val` (for "value") instead:

```kotlin
val message = "Hello"
val number = 42
```

The terminology is that `var` declares a _mutable_ variable, and that `val` declares a _read-only_ or _assign-once_ variable - so both kinds are called _variables_.

Note that a read-only variable is not a constant per se: it can be initialized with the value of a variable (so its value doesn't need to be known at compile-time), and if it is declared inside a construct that is repeatedly invoked (such as a function or a loop), it can take on a different value on each invocation. Also, while the read-only variable may not be reassigned while it is in scope, it can still refer to an object which is in itself mutable (such as a list).


### Constants

If you have a value that is truly constant, and the value is a string or a primitive type (see below) that is known at compile-time, you can declare an actual constant instead. You can only do this at the top level of a file or inside an [object declaration](#object-declarations) (but not inside a class declaration):

```kotlin
const val x = 2
```


### Specifying the type explicitly

If you really want to, you can both initialize and specify the type on the same line. This is mostly useful if you're dealing with a class hierarchy (more on that later) and you want the variable type to be a base type of the value's class:

```kotlin
val characters: CharSequence = "abc"
```

In this doc, we'll sometimes specify the type unnecessarily, in order to highlight what type is produced by an expression. (Also, a good IDE will be able to show you the resulting type.)

For completeness: it is also possible (but discouraged) to split the declaration and the initial assignment, and even to initialize in multiple places based on some condition. You can only read the variable at a point where the compiler can prove that every possible execution path will have initialized it. If you're creating a read-only variable in this way, you must also ensure that every possible execution path assigns to it _exactly_ once.

```kotlin
val x: String
x = 3
```


### Scopes and naming

A variable only exists inside the _scope_ (curly-brace-enclosed block of code; more on that later) in which it has been declared - so a variable that's declared inside a loop only exists in that loop; you can't check its final value after the loop. Variables can be redeclared inside nested scopes - so if there's a parameter `x` to a function and you create a loop and declare an `x` inside that loop, the `x` inside the loop is a different variable than the parameter `x`.

Variable names should use `lowerCamelCase` instead of `snake_case`.

In general, identifiers may consist of letters, digits, and underscores, and may not begin with a digit. However, if you are writing code that e.g. autogenerates JSON based on identifiers and you want the JSON key to be a string that does not conform to these rules or that collides with a keyword, you can enclose it in backticks: `` `I can't believe this is not an error!` `` is a valid identifier.


## Primitive data types and their limitations

The _primitive data types_ are the most fundamental types in Kotlin; all other types are built up of these types and arrays thereof. Their representation is very efficient (both in terms of memory and CPU time), as they map to small byte groups that are directly manipulatable by the CPU.


### Integer types

Integer types in Kotlin have a _limited size_, as opposed to the arbitrarily large integers in Python. The limit depends on the type, which decides how many bits the number occupies in memory:

Type | Bits | Min value | Max value
-----|------|-----------|----------
`Long` | 64 | -9223372036854775808 | 9223372036854775807
`Int` | 32 | -2147483648 | 2147483647
`Short` | 16 | -32768 | 32767
`Byte` | 8 | -128 | 127

Bytes are -128 through 127 due to Kotlin inheriting a bad design decision from Java. In order to get a traditional byte value between 0 and 255, keep the value as-is if it is positive, and add 256 if it is negative (so -128 is really 128, and -1 is really 255). See the section on [extension functions](#extension-functionsproperties) for a neat workaround for this.

An integer literal has the type `Int` if its value fits in an `Int`, or `Long` otherwise. `Long` literals should be suffixed by `L` for clarity, which will also let you make a `Long` with a "small" value. There are no literal suffixes for `Short` or `Byte`, so such values need an explicit type declaration or the use of an explicit conversion function.

```kotlin
val anInt = 3
val anotherInt = 2147483647
val aLong = 2147483648
val aBetterLong = 2147483649L
val aSmallLong = 3L
val aShort: Short = 32767
val anotherShort = 1024.toShort()
val aByte: Byte = 65
val anotherByte = -32.toByte()
```

Beware that dividing an integer by an integer produces an integer (like in Python 2, but unlike Python 3). If you want a floating-point result, at least one of the operands needs to be a floating-point number (and recall that like in most languages, floating-point operations are generally imprecise):

```kotlin
println(7 / 3)            // Prints 2
println(7 / 3.0)          // Prints 2.3333333333333335
val x = 3
println(7 / x)            // Prints 2
println(7 / x.toDouble()) // Prints 2.3333333333333335
```

Whenever you use an arithmetic operator on two integers of the same type (or when you use a unary operator like negation), _there is no automatic "upgrading" if the result doesn't fit in the type of the operands!_ Try this:

```kotlin
val mostPositive = 2147483647
val mostNegative = -2147483648
println(mostPositive + 1)
println(-mostNegative)
```

Both of these print `-2147483648`, because only the lower 32 bits of the "real" result are stored.

When you use an arithmetic operator on two integers of different types, the result is "upgraded" to the widest type. Note that the result might still overflow.

In short: _think carefully through your declarations of integers, and be absolutely certain that the value will never ever need to be larger than the limits of the type!_ If you need an integer of unlimited size, use the non-primitive type `BigInteger`.


### Floating-point and other types

Type | Bits | Notes
-----|------|------
`Double` | 64 | 16-17 significant digits (same as `float` in Python)
`Float` | 32 | 6-7 significant digits
`Char` | 16 | UTF-16 code unit (see the section on [strings](#strings) - in most cases, this is one Unicode character, but it might be just one half of a Unicode character)
`Boolean` | 8 | `true` or `false`

Floating-point numbers act similarly to in Python, but they come in two types, depending on how many digits you need. If you need larger precision, or to work with monetary amounts (or other situations where you must have exact results), use the non-primitive type `BigDecimal`.


## Strings

Unicode correctness can be onerous in Python 2, since the "default" string type `str` is really just a byte array, while `unicode` is actually a sequence of _code units_ (see below) - and whether the code units are 16 or 32 bits wide depends on how your Python distribution was built. In Kotlin, there's no such confusion: `String`, which is what you get when you make a string literal (which you can only do with double quotes), is an immutable sequence of UTF-16 code units. `ByteArray` is a fixed-size (but otherwise mutable) byte array (and `String` can specifically _not_ be used as a byte array).

A UTF-16 _code unit_ is a 16-byte unsigned integral value that represents either one Unicode _code point_ (character code) or must be combined with another code unit to form a code unit. If this makes no sense, I strongly recommend [Joel Spolsky's excellent essay on Unicode and its encodings](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/). For most Western scripts, including English, all code points fit inside one code unit, so it's tempting to think of a code unit as a character - but that will lead astray once your code encounters non-Western scripts. A single UTF-16 code unit can be represented with single quotes, and has the type `Char`:

```kotlin
val c = 'x' // Char
val message = "Hello" // String
val m = message[0] // Char
```

Thus, single quotes can not be used to form string literals.

Given a string `s`, you can get a `ByteArray` with the UTF-8 encoding of the string by calling `s.toByteArray()`, or you can specify another encoding, e.g. `s.toByteArray(Charsets.US_ASCII)` - just like `encode()` in Python. Given a byte array `b` that contains a UTF-8-encoded string, you can get a `String` by calling `String(b)`; if you've got a different encoding, use e.g. `String(b, Charsets.US_ASCII)`, just like `decode()` in Python. You can also call e.g. `b.toString(Charsets.US_ASCII)`, but do _not_ call `b.toString()` without parameters (this will just print an internal reference to the byte array).

You can do string interpolation with `$`, and use curly braces for expressions:

```kotlin
val name = "Anne"
val yearOfBirth = 1985
val yearNow = 2018
val message = "$name is ${yearNow - yearOfBirth} years old"
```

If you want a literal `$`, you need to escape it: `\$`. Escaping generally works the same way as in Python, with a similar set of standard escape sequences.



## Conditionals


### `if`/`else`

`if`/`else` works the same way as in Python, but it's `else if` instead of `elif`, the conditions are enclosed in parentheses, and the bodies are enclosed in curly braces:

```kotlin
val age = 42
if (age < 10) {
    println("You're too young to watch this movie")
} else if (age < 13) {
    println("You can watch this movie with a parent")
} else {
    println("You can watch this movie")
}
```

The curly braces around a body can be omitted if the body is a oneliner. This is discouraged unless the body goes on the same line as the condition, because it makes it easy to make this mistake, especially when one is used to Python:

```kotlin
if (age < 10)
    println("You're too young to watch this movie")
    println("You should go home") // Mistake - this is not a part of the if body!
```

Without the curly braces, only the first line is a part of the body. Indentation in Kotlin matters only for human readers, so the second print is outside the if and will always be executed.

An if/else statement is also an expression, meaning that a ternary conditional (which looks like `result = true_body if condition else false_body` in Python) looks like this in Kotlin:

```kotlin
val result = if (condition) trueBody else falseBody
```

When using if/else as an expression, the `else` part is mandatory (but there can also be `else if` parts). If the body that ends up being evaluated contains more than one line, it's the result of the last line that becomes the result of the `if`/`else`.


### Comparisons

Structural equality comparisons are done with `==` and `!=`, like in Python, but it's up to each class to define what that means, by [overriding](#overriding) [`equals()`](#inherited-built-in-functions) (which will be called on the left operand with the right operand as the parameter) and `hashCode()`. Most built-in collection types implement deep equality checks for these operators and functions. Reference comparisons - checking if two variables refer to the same object (the same as `is` in Python) - are done with `===` and `!==`.

Boolean expressions are formed with `&&` for logical AND, `||` for logical OR, and `!` for logical NOT. As in Python, `&&` and `||` are short-circuiting: they only evaluate the right-hand side if it's necessary to determine the outcome. Beware that the keywords `and` and `or` also exist, but they only perform _bitwise_ operations on integral values, and they do not short-circuit.

There are no automatic conversions to boolean and thus no concept of truthy and falsy: checks for zero, empty, or null must be done explicitly with `==` or `!=`. Most collection types have an `isEmpty()` and an `isNotEmpty()` function.


### `when`

We're not going to cover the [`when` expression](https://kotlinlang.org/docs/reference/control-flow.html#when-expression) in depth here since it doesn't have a close equivalent in Python, but check it out - it's pretty nifty, as it lets you compare one expression against many kinds of expressions in a very compact way (but it's not a full functional-programming-style pattern matcher). For example:

```kotlin
val x = 42
when (x) {
    0 -> println("zero")
    in 1..9 -> println("single digit")
    else -> println("multiple digits")
}
```


## Collections

Arrays in Kotlin have a constant length, so one normally uses lists, which are similar to the ones in Python. What's called a _dict_ in Python is called a _map_ in Kotlin (not to be confused with the function `map()`). `List`, `Map`, and `Set` are all _interfaces_ which are implemented by many different classes. In most situations, a standard array-backed list or hash-based map or set will do, and you can easily make those like this:

```kotlin
val strings = listOf("Anne", "Karen", "Peter") // List<String>
val map = mapOf("a" to 1, "b" to 2, "c" to 3)  // Map<String, Int>
val set = setOf("a", "b", "c")                 // Set<String>
```

(Note that `to` is an [infix function](#infix-functions) that creates a `Pair` containing a key and a value, from which the map is constructed.) The resulting collections are immutable - you can neither change their size nor replace their elements - however, the elements themselves may still be mutable objects. For mutable collections, do this:

```kotlin
val strings = mutableListOf("Anne", "Karen", "Peter")
val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)
val set = mutableSetOf("a", "b", "c")
```

You can get the size/length of a collection `c` with `c.size` (except for string objects, where you for legacy Java reasons must use `s.length` instead).

Unfortunately, if you want an empty collection, you need to either declare the resulting collection type explicitly, or supply the element type(s) to the function that constructs the collection:

```kotlin
val noInts: List<Int> = listOf()
val noStrings = listOf<String>()
val emptyMap = mapOf<String, Int>()
```

The types inside the angle brackets are called _generic type parameters_, which we will cover later. In short, it's a useful technique to make a class that is tied to another class (such as a container class, which is tied to its element class) applicable to many different classes.

If you really really need a mixed-type collection, you can use the element type `Any` - but you'll need typecasting to get the elements back to their proper type again, so if what you want is a multiple-value return from a function, please use the per-element-typed `Pair` or `Triple` instead. If you need four or more elements, consider making a [data class](#data-classes) for the return type instead (which you should ideally do for two or three elements as well, especially if it's a public function, since it gives you proper names for the elements) - it's very easy and usually a oneliner.


## Loops


### `for`

Kotlin's loops are similar to Python's. `for` iterates over anything that is _iterable_ (anything that has an `iterator()` function that provides an `Iterator` object), or anything that is itself an iterator:

```kotlin
val names = listOf("Anne", "Peter", "Jeff")
for (name in names) {
    println(name)
}
```

Note that a `for` loop always implicitly declares a new read-only variable (in this example, `name`) - if the outer scope already contains a variable with the same name, it will be shadowed by the unrelated loop variable. For the same reason, the final value of the loop variable is not accessible after the loop.

You can also create a range with the `..` operator - but beware that unlike Python's `range()`, it _includes_ its endpoint:

```kotlin
for (x in 0..10) println(x) // Prints 0 through 10 (inclusive)
```

If you want to exclude the last value, use `until`:

```kotlin
for (x in 0 until 10) println(x) // Prints 0 through 9
```

You can control the increment with `step`:

```kotlin
for (x in 0 until 10 step 2) println(x) // Prints 0, 2, 4, 6, 8
```

The step value must be positive. If you need to count downwards, use the inclusive `downTo`:

```kotlin
for (x in 10 downTo 0 step 2) println(x) // Prints 10, 8, 6, 4, 2, 0
```

Any of the expressions to the right of `in` in the loops above can also be used outside of loops in order to generate _ranges_ (one type of iterables - this is similar to `xrange()` in Python 2 and `range()` in Python 3), which can be iterated over later or turned into lists:

```kotlin
val numbers = (0..9).toList()
```

If you need to know the index of the current element when you're iterating through something, you can use `withIndex()`, which corresponds to `enumerate()`. It produces a sequence of objects that have got two properties (the index and the value) and two specially-named accessor functions called `component1()` and `component2()`; Kotlin lets you destructure such an object into a declaration:

```kotlin
for ((index, value) in names.withIndex()) {
    println("$index: $value")
}
```


### `while`

The `while` loop is similar to Python (but keep in mind that the condition must be an actual boolean expression, as there's no concept of truthy or falsy values).

```kotlin
var x = 0
while (x < 10) {
    println(x)
    x++ // Same as x += 1
}
```

The loop variable(s), if any, must be declared outside of the `while` loop, and are therefore available for inspection afterwards, at which point they will contain the value(s) that made the loop condition false.


### `continue` and `break`

A plain `continue` or `break` works the same way as in Python: `continue` skips to the next iteration of the innermost containing loop, and `break` stops the loop. However, you can also _label_ your loops and reference the label in the `continue` or `break` statement in order to indicate which loop you want to affect. A label is an identifier followed by `@,` e.g. `outer@` (possibly followed by a space). For example, to generate primes:

```kotlin
outer@ for (n in 2..100) {
    for (d in 2 until n) {
        if (n % d == 0) continue@outer
    }
    println("$n is prime")
}
```

Note that there must be no space between `continue`/`break` and `@`.


## Functions


### Declaration

Functions are declared with the `fun` keyword. For the parameters, you must declare not only their names, but also their types, and you must declare the type of the value the function is intending to return. The body of the function is usually a _block_, which is enclosed in curly braces:

```kotlin
fun happyBirthday(name: String, age: Int): String {
    return "Happy ${age}th birthday, $name!"
}
```

Here, `name` must be a string, `age` must be an integer, and the function must return a string. However, you can also make a oneliner function, where the body simply is the expression whose result is to be returned. In that case, the return type is inferred, and an equals sign is used to indicate that it's a oneliner:

```kotlin
fun square(number: Int) = number * number
```

(Note that there is no `**` operator; non-square exponentiation should be done via `Math.pow()`.)

Function names should use `lowerCamelCase` instead of `snake_case`.


### Calling

Functions are called the same way as in Python:

```kotlin
val greeting = happyBirthday("Anne", 32)
```

If you don't care about the return value, you don't need to assign it to anything.


### Returning

As opposed to Python, omitting `return` at the end of a function does not implicitly return null; if you want to return null, you must do so with `return null`. If a function never needs to return anything, the function should have the return type `Unit` (or not declare a return type at all, in which case the return type defaults to `Unit`). In such a function, you may either have no `return` statement at all, or say just `return`. `Unit` is both a singleton object (which `None` in Python also happens to be) and the type of that object, and it represents "this function never returns any information" (rather than "this function sometimes returns information, but this time, it didn't", which is more or less the semantics of returning null).


### Overloading

In Python, function names must be unique within a module or a class. In Kotlin, we can _overload_ functions: there can be multiple declarations of functions that have the same name. Overloaded functions must be distinguishable from each other through their parameter lists. (The types of the parameter list, together with the return type, is known as a function's _signature_, but the return type cannot be used to disambiguate overloaded functions.) For example, we can have both of these functions in the same file:

```kotlin
fun square(number: Int) = number * number
fun square(number: Double) = number * number
```

At the call sites, which function to use is determined from the type of the arguments:

```kotlin
square(4)    // Calls the first function; result is 16 (Int)
square(3.14) // Calls the second function; result is 9.8596 (Double)
```

While this example happened to use the same expression, that is not necessary - overloaded functions can do completely different things if need be (although your code can get confusing if you make functions that have very different behavior be overloads of each other).


### Varargs and optional/named parameters

A function can take an arbitrary number of arguments, similarly to `*args` in Python, but they must all be of the same type. Unlike Python, you may declare other positional parameters after the variadic one, but there can be at most one variadic parameter. If its type is `X`, the type of the argument will be `XArray` if `X` is a primitive type and `Array<X>` if not.

```kotlin
fun countAndPrintArgs(vararg numbers: Int) {
    println(numbers.size)
    for (number in numbers) println(number)
}
```

There are no `**kwargs` in Kotlin, but you can define optional parameters with default values, and you may choose to name some or all of the parameters when you call the function (whether they've got default values or not). A parameter with a default value must still specify its type explicitly. Like in Python, the named arguments can be reordered at will at the call site:

```kotlin
fun foo(decimal: Double, integer: Int, text: String = "Hello") { ... }

foo(3.14, text = "Bye", integer = 42)
foo(integer = 12, decimal = 3.4)
```


In Python, the expression for a default value is evaluated once, at function definition time. That leads to this classic trap, where the developer hopes to get a new, empty list every time the function is called without a value for `numbers`, but instead, the same list is being used every time:

```python
def tricky(x, numbers=[]):  # Bug: every call will see the same list!
    numbers.append(x)
    print numbers
```

In Kotlin, the expression for a default value is evaluated every time the function is invoked. Therefore, you will avoid the above trap as long as you use an expression that produces a new list every time it is evaluated:

```kotlin
fun tricky(x: Int, numbers: MutableList<Int> = mutableListOf()) {
    numbers.add(x)
    println(numbers)
}
```

For this reason, you should probably not use a function with side effects as a default value initializer, as the side effects will happen on every call. If you just reference a variable instead of calling a function, the same variable will be read every time the function is invoked: `numbers: MutableList<Int> = myMutableList`. If the variable is immutable, each call will see the same value (but if the value itself is mutable, it might change between calls), and if the variable is mutable, each call will see the current value of the variable. Needless to say, these situations easily lead to confusion, so a default value initializer should be either a constant or a function call that always produces a new object with the same value.

You can call a variadic function with one array (but not a list or any other iterable) that contains all the variadic arguments, by _spreading_ it with the `*` operator (same syntax as Python):

```kotlin
val numbers = listOf(1, 2, 3)
countAndPrintArgs(*numbers.toIntArray())
```

Kotlin has inherited Java's fidgety array system, so primitive types have got their own array types and conversion functions, while any other type uses the generic `Array` type, to which you can convert with `.toTypedArray()`.

However, you can't spread a map into a function call and expect the values in the map to be passed to the parameters named by the keys - the names of the parameters must be known at compile time. If you need runtime-defined parameter names, your function must either take a map or take `vararg kwargs: Pair<String, X>` (where `X` is the "lowest common denominator" of the parameter types, in the worst case `Any?` - be prepared to have to typecast the parameter values, and note that you'll lose type safety). You can call such a function like this: `foo("bar" to 42, "test" to "hello")`, since `to` is an [infix function](#infix-functions) that creates a `Pair`.


## Classes

Kotlin's object model is substantially different from Python's. Most importantly, classes are _not_ dynamically modifiable at runtime! (There are some limited exceptions to this, but you generally shouldn't do it. However, it _is_ possible to dynamically _inspect_ classes and objects at runtime with a feature called _reflection_ - this can be useful, but should be judiciously used.) All properties (attributes) and functions that might ever be needed on a class must be declared either directly in the class body or as [_extension functions_](#extension-functionsproperties), so you should think carefully through your class design.


### Declaration and instantiation

Classes are declared with the `class` keyword. A basic class without any properties or functions of its own looks like this:

```kotlin
class Empty
```

You can then create an instance of this class in a way that looks similar to Python, as if the class were a function (but this is just syntactic sugar - unlike Python, classes in Kotlin aren't really functions):

```kotlin
val object = Empty()
```

Class names should use `UpperCamelCase`, just like in Python.


### Inherited built-in functions

Every class that doesn't explicitly declare a parent class inherits from `Any`, which is the root of the class hierarchy (similar to `object` in Python) - more on [inheritance](#inheritance) later. Via `Any`, every class automatically has the following functions:

* `toString()` returns a string representation of the object, similar to `__str__()` in Python (the default implementation is rather uninteresting, as it only returns the class name and something akin to the object's id)
* `equals(x)` checks if this object is equal to some other object `x` of any class (by default, this just checks if this object is the _same_ object as `x` - just like `is` in Python - but it can be overridden by subclasses to do custom comparisons of property values)
* `hashCode()` returns an integer that can be used by hash tables and for shortcutting complex equality comparisons (objects that are equal according to `equals()` must have the same hash code, so if two objects' hash codes are different, the objects cannot be equal)


### Properties

Empty classes aren't very interesting, so let's make a class with some _properties_:

```kotlin
class Person {
    var name = "Anne"
    var age = 32
}
```

Note that the type of a property must be explicitly specified. As opposed to Python, declaring a property directly inside the class does not create a class-level property, but an instance-level one: every instance of `Person` will have _its own_ `name` and `age`. Their values will start out in every instance as `"Anne"` and `32`, respectively, but the value in each instance can be modified independently of the others:

```kotlin
val a = Person()
val b = Person()
println("${a.age} ${b.age}") // Prints "32 32"
a.age = 42
println("${a.age} ${b.age}") // Prints "42 32"
```

To be fair, you'd get the same output in Python, but the mechanism would be different: both instances would start out without any attributes of their own (`age` and `name` would be attributes on the class), and the first printing would access the class attribute; only the assignment would cause an `age` attribute to appear on `a`. In Kotlin, there are no class properties in this example, and each instance starts out with both properties. If you need a class-level property, see the section on [companion objects](#companion-objects).

Because the set of properties of an object is constrained to be exactly the set of properties that are declared at compile-time in the object's class, it's not possible to add new properties to an object or to a class at runtime, so e.g. `a.nationality = "Norwegian"` won't compile.

Property names should use `lowerCamelCase` instead of `snake_case`.


### Constructors and initializer blocks

Properties that don't have a sensible default should be taken as constructor parameters. Like with Python's `__init__()`, Kotlin constructors and initializer blocks run automatically whenever an instance of an object is created (note that there's nothing that corresponds to `__new__()`).  A Kotlin class may have one _primary constructor_, whose parameters are supplied after the class name. The primary constructor parameters are available when you initialize properties in the class body, and also in the optional _initializer block_, which can contain complex initialization logic (a property can be declared without an initial value, in which case it must be initialized in `init`). Also, you'll frequently want to use `val` instead of `var` in order to make your properties immutable after construction.

```kotlin
class Person(firstName: String, lastName: String, yearOfBirth: Int) {
    val fullName = "$firstName $lastName"
    var age: Int
    
    init {
        age = 2018 - yearOfBirth
    }
}
```

If all you want to do with a constructor parameter value is to assign it to a property with the same name, you can declare the property in the primary constructor parameter list (the oneliner below is sufficient for both declaring the properties, declaring the constructor parameters, and initializing the properties with the parameters):

```kotlin
class Person(val name: String, var age: Int)
```

If you need multiple ways to initialize a class, you can create _secondary constructors_, each of which looks like a function whose name is `constructor`. Every secondary constructor must invoke another (primary or secondary) constructor by using the `this` keyword as if it were a function (so that every instance construction eventually calls the primary constructor).

```kotlin
class Person(val name: String, var age: Int) {
    constructor(name: String) : this(name, 0)
    constructor(yearOfBirth: Int, name: String)
        : this(name, 2018 - yearOfBirth)
}
```

(A secondary constructor can also have a body in curly braces if needs to do more than what the primary constructor does.) The constructors are distinguished from each other through the types of their parameters, like in ordinary function overloading. That's the reason we had to flip the parameter order in the last secondary constructor - otherwise, it would have been indistinguishable from the primary constructor (parameter names are not a part of a function's signature and don't have any effect on overload resolution). In the most recent example, we can now create a `Person` in three different ways:

```kotlin
val a = Person("Jaime", 35)
val b = Person("Jack") // age = 0
val c = Person(1995, "Lynne") // age = 23
```

Note that if a class has got a primary constructor, it is no longer possible to create an instance of it without supplying any parameters (unless one of the secondary constructors is parameterless).


### Setters and getters

A property is really a _backing field_ (kind of a hidden variable inside the object) and two accessor functions: one that gets the value of the variable and one that sets the value. You can override one or both of the accessors (an accessor that is not overridden automatically gets the default behavior of just returning or setting the backing field directly). Inside an accessor, you can reference the backing field with `field`. The setter accessor must take a parameter `value`, which is the value that is being assigned to the property. A getter body could either be a one-line expression preceded by `=` or a more complex body enclosed in curly braces, while a setter body typically includes an assignment and must therefore be enclosed in curly braces.  If you want to validate that the age is nonnegative:

```kotlin
class Person(age: Int) {
    var age = 0
        set(value) {
            if (value < 0) throw IllegalArgumentException(
                    "Age cannot be negative")
            field = value
        }

    init {
        this.age = age
    }
}
```

Annoyingly, the setter logic is not invoked by the initialization, which instead sets the backing field directly - that's why we have to use an initializer block in this example in order to verify that newly-created persons also don't get a negative age. Note the use of `this.age` in the initializer block in order to distinguish between the identically-named property and constructor parameter.

If for some reason you want to store a different value in the backing field than the value that is being assigned to the property, you're free to do that, but then you will probably want a getter to give the calling code back what they expect: if you say `field = value * 2` in the setter and `this.age = age * 2` in the initializer block, you should also have `get() = field / 2`.

You can also create properties that don't actually have a backing field, but just reference another property:

```kotlin
val isNewborn
    get() = age == 0
```

Note that even though this is a read-only property due to declaring it with `val` (in which case you may not provide a setter), its value can still change since it reads from a mutable property - you just can't assign to the property. Also, note that the property type is inferred from the return value of the getter.

The indentation in front of the accessors is due to convention; like elsewhere in Kotlin, it has no syntactic significance. The compiler can tell which accessors belong to which properties because the only legal place for an accessor is immediately after the property declaration (and there can be at most one getter and one setter) - so you can't split the property declaration and the accessor declarations. However, the order of the accessors doesn't matter.


### Member functions

A function declared inside a class is called a _member function_ of that class. Like in Python, every invocation of a member function must be performed on an instance of the class, and the instance will be available during the execution of the function - but unlike Python, the function signature doesn't declare that: there is no explicit `self` parameter. Instead, every member function can use the keyword `this` to reference the current instance, without declaring it. Unlike Python, as long as there is no name conflict with an identically-named parameter or local variable, `this` can be omitted. If we do this inside a `Person` class with a `name` property:

```kotlin
fun present() {
    println("Hello, I'm $name!")
}
```

We can then do this:

```kotlin
val p = Person("Claire")
p.present() // Prints "Hello, I'm Claire!"
```

You could have said `${this.name}`, but that's redundant and generally discouraged. Oneliner functions can be declared with an `=`:

```kotlin
fun greet(other: Person) = println("Hello, ${other.name}, I'm $name!")
```

Apart from the automatic passing of the instance into `this`, member functions generally act like ordinary functions.

Because the set of member functions of an object is constrained to be exactly the set of member functions that are declared at compile-time in the object's class and base classes, it's not possible to add new member functions to an object or to a class at runtime, so e.g. `p.leave = fun() { println("Bye!") }` or anything of the sort won't compile.

Member function names should use `lowerCamelCase` instead of `snake_case`.


### Lateinit

Kotlin requires that every member property is initialized during instance construction. Sometimes, a class is intended to be used in such a way that the constructor doesn't have enough information to initialize all properties (such as when making a builder class or when using property-based dependency injection). In order to not have to make those properties nullable, you can use a _late-initialized property_:

```kotlin
lateinit var name: String
```

Kotlin will allow you to declare this property without initializing it, and you can set the property value at some point after construction (either directly or via a function). It is the responsibility of the class itself as well as its users to take care not to read the property before it has been set, and Kotlin allows you to write code that reads `name` as if it were an ordinary, non-nullable property. However, the compiler is unable to enforce correct usage, so if the property is read before it has been set, an `UninitializedPropertyAccessException` will be thrown at runtime.

Inside the class that declares a lateinit property, you can check if it has been initialized:

```kotlin
if (::name.isInitialized) println(name)
```

`lateinit` can only be used with `var`, not with `val`, and the type must be non-primitive and non-nullable.


### Infix functions

You can designate a one-parameter member function or [extension function](#extension-functionsproperties) for use as an infix operator, which can be useful if you're designing a DSL. The left operand will become `this`, and the right operand will become the parameter. If you do this inside a `Person` class that has got a `name` property:

```kotlin
infix fun marry(spouse: Person) {
    println("$name and ${spouse.name} are getting married!")
}
```

We can now do this (but it's still possible to call the function the normal way):

```kotlin
val lisa = Person("Lisa")
val anne = Person("Anne")
lisa marry anne // Prints "Lisa and Anne are getting married!"
```

All infix functions have the same [precedence](https://kotlinlang.org/docs/reference/grammar.html#precedence) (which is shared with all the built-in infix functions, such as the bitwise functions `and`, `or`, `inv`, etc.): lower than the arithmetic operators and the `..` range operator, but higher than the Elvis operator `?:`, comparisons, logic operators, and assignments.


### Operators

Most of the operators that are recognized by Kotlin's syntax have predefined textual names and are available for implementation in your classes, just like you can do with Python's double-underscore operator names. For example, the binary `+` operator is called `plus`. Similarly to the infix example, if you do this inside a `Person` class that has got a `name` property:

```kotlin
operator fun plus(spouse: Person) {
    println("$name and ${spouse.name} are getting married!")
}
```

With `lisa` and `anne` from the infix example, you can now do:

```kotlin
lisa + anne // Prints "Lisa and Anne are getting married!"
```

A particularly interesting operator is the function-call parenthesis pair, whose function name is `invoke` - if you implement this, you'll be able to call instances of your class as if they were functions. You can even overload it in order to provide different function signatures.

`operator` can also be used for certain other predefined functions in order to create fancy effects, such as [delegated properties](#delegated-properties).

Since the available operators are hardcoded into the formal Kotlin syntax, you can not invent new operators, and overriding an operator does not affect its [precedence](https://kotlinlang.org/docs/reference/grammar.html#precedence).


### Enum classes

Whenever you want a variable that can only take on a limited number of values where the only feature of each value is that it's distinct from all the other values, you can create an _enum class_:

```kotlin
enum class ContentKind {
    TOPIC,
    ARTICLE,
    EXERCISE,
    VIDEO,
}
```

There are exactly four instances of this class, named `ContentKind.TOPIC`, and so on. Instances of this class can be compared to each other with `==` and `!=`, and you can get all the allowable values with `ContentKind.values()`. You can also tack on more information to each instance if you need:

```kotlin
enum class ContentKind(val kind: String) {
    TOPIC("Topic"),
    ARTICLE("Article"),
    EXERCISE("Exercise"),
    VIDEO("Video"),
    ;

    override fun toString(): String {
        return kind
    }
}
```

Null safety is enforced as usual, so a variable of type `ContentKind` can not be null, unlike in Java.


### Data classes

Frequently - especially if you want a complex return type from a function or a complex key for a map - you'll want a quick and dirty class which only contains some properties, but is still comparable for equality and is usable as a map key. If you create a _data class_, you'll get automatic implementations of the following functions: `toString()` (which will produce a string containing all the property names and values), `equals()` (which will do a per-property `equals()`), `hashCode()` (which will hash the individual properties and combine the hashes), and the functions that are required to enable Kotlin to destructure an instance of the class into a declaration (`component1()`, `component2()`, etc.):

```kotlin
data class ContentDescriptor(val kind: ContentKind, val id: String) {
    override fun toString(): String {
        return kind.toString() + ":" + id
    }
}
```


## Exceptions


### Throwing and catching

Exceptions pretty much work like they do in Python. You _throw_ (raise) one with `throw`:

```kotlin
throw IllegalArgumentException("Value must be positive")
```

You _catch_ it with `try`/`catch` (which corresponds to `try`/`except` in Python):

```kotlin
fun divideOrZero(numerator: Int, denominator: Int): Int {
    try {
        return numerator / denominator
    } catch (e: ArithmeticException) {
        return 0
    }
}
```

The `catch` blocks are tried in order until an exception type is found that matches the thrown exception (it doesn't need to be an exact match; the thrown exception's class can be a subclass of the declared one), and at most one `catch` block will be executed. If no match is found, the exception bubbles out of the `try`/`catch`.

The `finally` block (if any) is executed at the end, no matter what the outcome is: either after the try block completes successfully, or after a catch block is executed (even if another exception is thrown by the catch block), or if no matching catch is found.

Unlike Python, `try`/`catch` is an expression: the last expression of the `try` block (if it succeeds) or the chosen `catch` block becomes the result value (`finally` doesn't affect the result), so we can refactor the function body above to:

```kotlin
return try {
    numerator / denominator
} catch (e: ArithmeticException) {
    0
}
```

The base exception class is `Throwable` (but it is more common to extend its subclass `Exception`), and there are a ton of built-in exception classes. If you don't find one that match your needs, you can create your own by inheriting from an existing exception class.

Note that exceptions are somewhat discouraged in Kotlin except when interacting with Java code. Instead of throwing exceptions in your own code, consider using special return types like [Option](https://arrow-kt.io/docs/datatypes/option/) or [Either](https://arrow-kt.io/docs/datatypes/either/) from the [Arrow library](https://arrow-kt.io/).


### Nothing

`throw` is also an expression, and its return type is the special class `Nothing`, which does not have any instances. The compiler knows that an expression whose type is `Nothing` will never return normally, and will therefore generally accept its use even where a different type would normally be required, such as after the [Elvis operator](#elvis-operator). If you make a function that always throws, or that starts an infinite loop, you could declare its return type to be `Nothing` in order to make the compiler aware of this. One fun example of this is the built-in function `TODO`, which you can call in any expression (possibly supplying a string argument), and it raises a `NotImplementedError`.

The nullable version `Nothing?` will be used by the compiler when something is initialized with null and there is no other type information. In `val x = null`, the type of `x` will be `Nothing?`. This type does not have the "never returns normally" semantics; instead, the compiler knows that the value will always be null.


## Null safety


### Working with nulls

A variable that doesn't refer to anything refers to `null` (or you can say that the variable "is null"). As opposed to `None` in Python, `null` is not an object - it's just a keyword that is used to make a variable refer to nothing or to check if it does (that check must be performed with `==` or `!=`). Because nulls are a frequent source of programming errors, Kotlin encourages avoiding them as much as possible - a variable cannot actually be null unless it's been declared to allow for null, which you do by suffixing the type name with `?`. For example:

```kotlin
fun test(a: String, b: String?) {
}
```

The compiler will allow this function to be called as e.g. `test("a", "b")` or `test("a", null)`, but not as `test(null, "b")` or `test(null, null)`. Calling `test(a, b)` is only allowed if the compiler can prove that `a` cannot possibly be null. Inside of `test`, the compiler will not allow you to do anything with `b` that would result in an exception if `b` should happen to be null - so you can do `a.length`, but not `b.length`. However, once you're inside a conditional where you have checked that `b` is not null, you can do it:

```kotlin
if (b != null) {
    println(b.length)
}
```

Or:

```kotlin
if (b == null) {
    // Can't use members of b in here
} else {
    println(b.length)
}
```

Making frequent null checks is annoying, so if you have to allow for the possibility of nulls, there are several very useful operators in Kotlin to ease working with values that might be null, as described below.


### Safe call operator

`x?.y` evaluates `x`, and if it is not null, it evaluates `x.y` (without reevaluating `x`), whose result becomes the result of the expression - otherwise, you get null. This also works for functions, and it can be chained - for example, `x?.y()?.z?.w()` will return null if any of `x`, `x.y()`, or `x.y().z` produce null; otherwise, it will return the result of `x.y().z.w()`.


### Elvis operator

`x ?: y` evaluates `x`, which becomes the result of the expression unless it's null, in which case you'll get `y` instead (which ought to be of a non-nullable type).  This is also known as the "Elvis operator". You can even use it to perform an early return in case of null:

```kotlin
val z = x ?: return y
```

This will assign `x` to `z` if `x` is non-null, but if it is null, the entire function that contains this expression will stop and return `y` (this works because `return` is also an expression, and if it is evaluated, it evaluates its argument and then makes the containing function return the result).


### Not-null assertion operator

Sometimes, you're in a situation where you have a value `x` that you know is not null, but the compiler doesn't realize it. This can legitimately happen when you're interacting with Java code, but if it happens because your code's logic is more complicated than the compiler's ability to reason about it, you should probably restructure your code. If you can't convince the compiler, you can resort to saying `x!!` to form an expression that produces the value of `x`, but whose type is non-nullable:

```kotlin
val x: String? = javaFunctionThatYouKnowReturnsNonNull()
val y: String = x!!
```

It can of course be done as a single expression: `val x = javaFunctionThatYouKnowReturnsNonNull()!!`.

`!!` will will raise a `NullPointerException` if the value actually is null. So you could also use it if you really need to call a particular function and would rather have an exception if there's no object to call it on (`maybeNull!!.importantFunction()`), although a better solution (because an NPE isn't very informational) is this:

```kotlin
val y: String = x ?: throw SpecificException("Useful message")
y.importantFunction()
```

The above could also be a oneliner - and note that the compiler knows that because the `throw` will prevent `y` from coming into existence if `x` is null, `y` must be non-null if we reach the line below. Contrast this with `x?.importantFunction()`, which is a no-op if `x` is null.


## Functional programming


### Function types

Like in Python, functions in Kotlin are first-class values - they can be assigned to variables and passed around as parameters. The type a function is a _function type_, which is indicated with a parenthesized parameter type list and an arrow to the return type. Consider this function:

```kotlin
fun safeDivide(numerator: Int, denominator: Int) =
    if (denominator == 0.0) 0.0 else numerator.toDouble() / denominator
```

It takes two `Int` parameters and returns a `Double`, so its type is `(Int, Int) -> Double`. We can reference the function itself by prefixing its name with `::`, and we can assign it to a variable (whose type would normally be inferred, but we show the type signature for demonstration):

```kotlin
val f: (Int, Int) -> Double = ::safeDivide
```

When you have a variable or parameter of function type (sometimes called a _function reference_), you can call it as if it were an ordinary function, and that will cause the referenced function to be called:

```kotlin
val quotient = f(3.14, 0.0)
```

It is possible for a class to implement a function type as if it were an interface. It must then supply an operator function called `invoke` with the given signature, and instances of that class may then be assigned to a variable of that function type:

```kotlin
class Divider : (Int, Int) -> Double {
    override fun invoke(numerator: Int, denominator: Int): Double = ...
}
```


### Function literals: lambda expressions and anonymous functions

Like in Python, you can write _lambda expressions_: unnamed function declarations with a very compact syntax, which evaluate to callable function objects. In Kotlin, lambdas can contain multiple statements, which make them useful for [more complex tasks](#receivers) than the single-expression lambdas of Python. The last statement must be an expression, whose result will become the return value of the lambda (unless `Unit` is the return type of the variable/parameter that the lambda expression is assigned to, in which case the lambda has no return value). A lambda expression is enclosed in curly braces, and begins by listing its parameter names and possibly their types (unless the types can be inferred from context):

```kotlin
val safeDivide = { numerator: Int, denominator: Int ->
    if (denominator == 0.0) 0.0 else numerator.toDouble() / denominator
}
```

The type of `safeDivide` is `(Int, Int) -> Double`. Note that unlike function type declarations, the parameter list of a lambda expression must not be enclosed in parentheses.

Note that the other uses of curly braces in Kotlin, such as in function and class definitions and after `if`/`else`/`for`/`while` statements, are not lambda expressions (so it is _not_ the case that `if` is a function that conditionally executes a lambda function).

The return type of a lambda expression is inferred from the type of the last expression inside it (or from the function type of the variable/parameter that the lambda expression is assigned to). If a lambda expression is passed as a function parameter (which is the ordinary use) or assigned to a variable with a declared type, Kotlin can infer the parameter types too, and you only need to specify their names:

```kotlin
val safeDivide: (Int, Int) -> Double = { numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

Or:

```kotlin
fun callAndPrint(function: (Int, Int) -> Double) {
    println(function(2, 0))
}

callAndPrint({ numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
})
```

A parameterless lambda does not need the arrow. A one-parameter lambda can choose to omit the parameter name and the arrow, in which case the parameter will be called `it`:

```kotlin
val square: (Double) -> Double = { it * it }
```

If the type of the last parameter to a function is a function type and you want to supply a lambda expression, you can place the lambda expression _outside_ of the parameter parentheses. If the lambda expression is the only parameter, you can omit the parentheses entirely. This is very useful for [constructing DSLs](#receivers).

```kotlin
fun callWithPi(function: (Double) -> Double) {
    println(function(3.14))
}

callWithPi { it * it }
```

If you want to be more explicit about the fact that you're creating a function, you can make an _anonymous function_, which is still an expression rather than a declaration:

```kotlin
callWithPi(fun(x: Double): Double { return x * x })
```

Or:

```kotlin
callWithPi(fun(x: Double) = x * x)
```

Lambda expressions and anonymous functions are collectively called _function literals_.


### Comprehensions

Kotlin can get quite close to the compactness of Python's `list`/`dict`/`set` comprehensions. Assuming that `people` is a collection of `Person` objects with a `name` property:

```kotlin
val shortGreetings = people
    .filter { it.name.length < 10 }
    .map { "Hello, ${it.name}!" }
```

corresponds to

```python
short_greetings = [
    f"Hello, {p.name}"  # In Python 2, this would be: "Hello, %s!" % p.name
    for p in people
    if len(p.name) < 10
]
```

In some ways, this is easier to read because the operations are specified in the order they are applied to the values. The result will be an immutable `List<T>`, where `T` is whichever type is produced by the transformations you use (in this case, `String`). If you need a mutable list, call `toMutableList()` at the end. If you want a set, call `toSet()` or `toMutableSet()` at the end. If you want to transform a collection into a map, call `associateBy()`, which takes two lambdas that specify how to extract the key and the value from each element: `people.associateBy({it.ssn}, {it.name})` (you can omit the second lambda if you want the entire element to be the value, and you can call `toMutableMap()` at the end if you want the result to be mutable).

These transformations can also be applied to `Sequence<T>`, which is similar to Python's generators and allows for lazy evaluation. If you have a huge list and you want to process it lazily, you can call `asSequence()` on it.

There's a vast collection of functional programming-style operations available in the [`kotlin.collections` package](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/index.html).


### Receivers

The signature of a member function or an [extension function](#extension-functionsproperties) begins with a _receiver_: the type upon which the function can be invoked. For example, the signature of `toString()` is `Any.() -> String` - it can be called on any non-null object (the receiver), it takes no parameters, and it returns a `String`. It is possible to write a lambda function with such a signature - this is called a _function literal with receiver_, and is extremely useful for building DSLs.

A function literal with receiver is perhaps easiest to think of as an extension function in the form of a lambda expression. The declaration looks like an ordinary lambda expression; what makes it take a receiver is the context - it must be passed to a function that takes a function with receiver as a parameter, or assigned to a variable/property whose type is a function type with receiver. The only way to use a function with receiver is to invoke it on an instance of the receiver class, as if it were a member function or extension function. For example:

```kotlin
class Car(val horsepowers: Int)

val boast: Car.() -> String = { "I'm a car with $horsepowers HP!"}

val car = Car(120)
println(car.boast())
```

Inside a lambda expression with receiver, you can use `this` to refer to the receiver object (in this case, `car`). As usual, you can omit `this` if there are no naming conflicts, which is why we can simply say `$horsepowers` instead of `${this.horsepowers}`. So beware that in Kotlin, `this` can have different meanings depending on the context: if used inside (possibly nested) lambda expressions with receivers, it refers to the receiver object of the innermost enclosing lambda expression with receiver. If you need to "break out" of the function literal and get the "original" `this` (the instance the member function you're inside is executing on), mention the containing class name after `this@` - so if you're inside a function literal with receiver inside a member function of Car, use `this@Car`.

As with other function literals, if the function takes one parameter (other than the receiver object that it is invoked on), the single parameter is implicitly called `it`, unless you declare another name. If it takes more than one parameter, you must declare their names.

Here's a small DSL example for constructing tree structures:

```kotlin
class TreeNode(val name: String) {
    val children = mutableListOf<TreeNode>()

    fun node(name: String, initialize: (TreeNode.() -> Unit)? = null) {
        val child = TreeNode(name)
        children.add(child)
        if (initialize != null) {
            child.initialize()
        }
    }
}

fun tree(name: String, initialize: (TreeNode.() -> Unit)? = null): TreeNode {
    val root = TreeNode(name)
    if (initialize != null) {
        root.initialize()
    }
    return root
}

val t = tree("root") {
    node("math") {
        node("algebra")
        node("trigonometry")
    }
    node("science") {
        node("physics")
    }
}
```

The block after `tree("root")` is the first function literal with receiver, which will be passed to `tree()` as the `initialize` parameter. According to the parameter list of `tree()`, the receiver is of type `TreeNode`, and therefore, `tree()` can call `initialize()` on `root`. `root` then becomes `this` inside the scope of that lambda expression, so when we call `node("math")`, it implicitly says `this.node("math")`, where `this` refers to the same `TreeNode` as `root`. The next block is passed to `TreeNode.node()`, and is invoked on the first child of the `root` node, namely `math`, and inside it, `this` will refer to `math`.

If we had wanted to express the same thing in Python, it would have looked like this, and we would be hamstrung by the fact that lambda functions can only contain one expression, so we need explicit function definitions for everything but the oneliners:

```python
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def node(self, name, initialize=None):
        child = TreeNode(name)
        self.children.append(child)
        if initialize:
            initialize(child)

def tree(name, initialize=None):
    root = TreeNode(name)
    if initialize:
        initialize(root)
    return root

def init_root(root):
    root.node("math", init_math)
    root.node("science",
              lambda science: science.node("physics"))

def init_math(math):
    math.node("algebra")
    math.node("trigonometry")

t = tree("root", init_root)
```

The official docs also have a very cool example with a [ DSL for constructing HTML documents](https://kotlinlang.org/docs/reference/type-safe-builders.html).


### Inline functions

There's a little bit of runtime overhead associated with lambda functions: they are really objects, so they must be instantiated, and (like other functions) calling them takes a little bit of time too. If we use the `inline` keyword on a function, we tell the compiler to _inline_ both the function and its lambda parameters (if any) - that is, the compiler will copy the code of the function (and its lambda parameters) into _every_ callsite, thus eliminating the overhead of both the lambda instantiation and the calling of the function and the lambdas. This will happen unconditionally, unlike in C and C++, where `inline` is more of a hint to the compiler. This will cause the size of the compiled code to grow, but it may be worth it for certain small but frequently-called functions.

```kotlin
inline fun time(action: () -> Unit): Long {
    val start = Instant.now().toEpochMilli()
    action()
    return Instant.now().toEpochMilli() - start
}
```

Now, if you do:

```kotlin
val t = time { println("Lots of code") }
println(t)
```

The compiler will generate something like this (except that `start` won't collide with any other identifiers with the same name):

```kotlin
val start = Instant.now().toEpochMilli()
println("Lots of code")
val t = Instant.now().toEpochMilli() - start
println(t)
```

In an inline function definition, you can use `noinline` in front of any function-typed parameter to prevent the lambda that will be passed to it from also being inlined.


### Nice utility functions


#### `run()`, `let()`, and `with()`

`?.` is nice if you want to call a function on something that might be null. But what if you want to call a function that takes a non-null parameter, but the value you want to pass for that parameter might be null? Try `run()`, which is an extension function on `Any?` that takes a lambda with receiver as a parameter and invokes it on the value that it's called on, and use `?.` to call `run()` only if the object is non-null:

```kotlin
val result = maybeNull?.run { functionThatCanNotHandleNull(this) }
```

If `maybeNull` is null, the function won't be called, and `result` will be null; otherwise, it will be the return value of `functionThatCanNotHandleNull(this)`, where `this` refers to  `maybeNull`. You can chain `run()` calls with `?.` - each one will be called on the previous result if it's not null:

```kotlin
val result = maybeNull
    ?.run { firstFunction(this) }
    ?.run { secondFunction(this) }
```

The first `this` refers to `maybeNull`, the second one refers to the result of `firstFunction()`, and `result` will be the result of `secondFunction()` (or null if `maybeNull` or any of the intermediate results were null).

A syntactic variation of `run()` is `let()`, which takes an ordinary function type instead of a function type with receiver, so the expression that might be null will be referred to as `it` instead of `this`.

Both `run()` and `let()` are also useful if you've got an expression that you need to use multiple times, but you don't care to come up with a variable name for it and make a null check:

```kotlin
val result = someExpression?.let {
   firstFunction(it)
   it.memberFunction() + it.memberProperty
}
```

Yet another version is `with()`, which you can also use to avoid coming up with a variable name for an expression, but only if you know that its result will be non-null:

```kotlin
val result = with(someExpression) {
   firstFunction(this)
   memberFunction() + memberProperty
}
```

In the last line, there's an implicit `this.` in front of both `memberFunction()` and `memberProperty` (if these exist on the type of `someExpression`). The return value is that of the last expression.


#### `apply()` and `also()`

If you don't care about the return value from the function, but you want to make one or more calls involving something that might be null and then keep on using that value, try `apply()`, which returns the value it's called on. This is particularly useful if you want to work with many members of the object in question:

```kotlin
maybeNull?.apply {
    firstFunction(this)
    secondFunction(this)
    memberPropertyA = memberPropertyB + memberFunctionA()
}?.memberFunctionB()
```

Inside the `apply` block, `this` refers to `maybeNull`. There's an implicit `this` in front of `memberPropertyA`, `memberPropertyB`, and `memberFunctionA` (unless these don't exist on `maybeNull`, in which case they'll be looked for in the containing scopes). Afterwards, `memberFunctionB()` is also invoked on `maybeNull`.

If you find the `this` syntax to be confusing, you can use `also` instead, which takes ordinary lambdas:

```kotlin
maybeNull?.also {
    firstFunction(it)
    secondFunction(it)
    it.memberPropertyA = it.memberPropertyB + it.memberFunctionA()
}?.memberFunctionB()
```


#### `takeIf()` and `takeUnless()`

If you want to use a value only if it satisfies a certain condition, try `takeIf()`, which returns the value it's called on if it satisfies the given predicate, and null otherwise. There's also `takeUnless()`, which inverts the logic. You can follow this with a `?.` to perform an operation on the value only if it satisfies the predicate. Below, we compute the square of some expression, but only if the expression value is at least 42:

```kotlin
val result = someExpression.takeIf { it >= 42 } ?.let { it * it }
```


## Packages and imports


### Packages

Every Kotlin file should belong to a _package_. This is somewhat similar to modules in Python, but files need to explicitly declare which package they belong to, and a package implicitly comes into existence whenever any file declares itself to belong to that package (as opposed to explicitly defining a module with `__init__.py` and having all the files in that directory implicitly belong to the module). The package declaration must go on the top of the file:

```kotlin
package content.exercises
```

If a file doesn't declare a package, it belongs to the nameless _default package_. This should be avoided, as it will make it hard to reference the symbols from that file in case of naming conflicts (you can't explicitly import the empty package).

Package names customarily correspond to the directory structure - note that the source file name should _not_ be a part of the package name (so if you follow this, file-level symbol names must be unique within an entire directory, not just within a file). However, this correspondence is not required, so if you're going to do interop with Java code and all your package names must start with the same prefix, e.g. `org.khanacademy`, you might be relieved to learn that you don't need to put all your code inside `org/khanacademy` (which is what Java would have forced you to do) - instead, you could start out with a directory called e.g. `content`, and the files inside it could declare that they belong to the package `org.khanacademy.content`. However, if you have a mixed project with both Kotlin and Java code, the convention is to use the Java-style package directories for Kotlin code too.

While the dots suggest that packages are nested inside each other, that's not actually the case from a language standpoint. While it's a good idea to organize your code such that the "subpackages" of `content`, such as  `content.exercises` and `content.articles`, both contain content-related code, these three packages are unrelated from a language standpoint. However, if you use _modules_ (as defined by your build system), it is typically the case that all "subpackages" go in the same module, in which case symbols with [`internal` visibility](#visibility-modifiers) are visible throughout the subpackages.

Package names customarily contain only lowercase letters (no underscores) and the separating dots.


### Imports

In order to use something from a package, it is sufficient to use the package name to fully qualify the name of the symbol at the place where you use the symbol:

```kotlin
val exercise = content.exercises.Exercise()
```

This quickly gets unwieldy, so you will typically _import_ the symbols you need. You can import a specific symbol:

```kotlin
import content.exercises.Exercise
```

Or an entire package, which will bring in all the symbols from that package:

```kotlin
import content.exercises.*
```

With either version of the import, you can now simply do:

```kotlin
val exercise = Exercise()
```

If there is a naming conflict, you should usually import just one of the symbols and fully qualify the usages of the other. If both are heavily used, you can rename the symbol at import time:

```kotlin
import content.exercises.Exercise as Ex
```

In Kotlin, importing is a compile-time concept - importing something does not actually cause any code to run (unlike Python, where all top-level statements in a file are executed at import time). Therefore, circular imports are allowed, but they might suggest a design problem in your code. However, during execution, a class will be loaded the first time it (or any of its properties or functions) is referenced, and class loading causes [companion objects](#companion-objects) to be initialized - this can lead to runtime exceptions if you have circular dependencies.

Every file implicitly imports its own package and a number of built-in Kotlin and Java packages.


## Visibility modifiers

Kotlin allows you to enforce symbol visibility (which Python only does via underscore conventions) via _visibility modifiers_, which can be placed on symbol declarations. If you don't supply a visibility modifier, you get the default visibility level, which is _public_.

The meaning of a visibility modifier depends on whether it's applied to a top-level declaration or to a declaration inside a class. For top-level declarations:

* `public` (or omitted): this symbol is visible throughout the entire codebase
* `internal`: this symbol is only visible inside files that belong to the same _module_ (a source code grouping which is defined by your IDE or build tool) as the file where this symbol is declared
* `private`: this symbol is only visible inside the file where this symbol is declared

For example, `private` could be used to define a property or helper function that is needed by several functions in one file, or a complex type returned by one of your private functions, without leaking them to the rest of the codebase:

```kotlin
private class ReturnType(val a: Int, val b: Double, val c: String)

private fun secretHelper(x: Int) = x * x

private const val secretValue = 3.14
```

For a symbol that is declared inside a class:

* `public` (or omitted): this symbol is visible to any code that can see the containing class
* `internal`: this symbol is only visible to code that exists inside a file that belongs to the same module as the file where this symbol is declared, and that can also see the containing class
* `protected`: this symbol is only visible inside the containing class and all of its subclasses, no matter where they are declared (so if your class is public and [open](#subclassing), anyone can subclass it and thus get to see and use the protected members). If you have used Java: this does _not_ also grant access from the rest of the package.
* `private`: this symbol is only visible inside the containing class

A constructor can also have a visibility modifier. If you want to place one on the primary constructor (which you might want to do if you have a number of secondary constructors which all invoke a complicated primary constructor that you don't want to expose), you need to include the `constructor` keyword: `class Person private constructor(val name: String)`.

Visibility modifiers can't be placed on local variables, since their visibility is always limited to the containing block.

The type of a property, and the types that are used for the parameters and the return type of a function, must be "at least as visible" as the property/function itself. For example, a public function can't take a private type as a parameter.

The visibility level only affects the _lexical visibility_ of the _symbol_ - i.e., where the compiler allows you to type out the symbol. It does not affect where _instances_ are used: for example, a public top-level function may well return an instance of a private class, as long as the return type doesn't mention the private class name but is instead a public base class of the private class (possibly `Any`) or a public interface that the private class implements. When you [subclass](#subclassing) a class, its private members are also inherited by the subclass, but are not directly accessible there - however, if you call an inherited public function that happens to access a private member, that's fine.


## Inheritance


### Subclassing

Kotlin supports single-parent class inheritance - so each class (except the root class `Any`) has got exactly one parent class, called a _superclass_. Kotlin wants you to think through your class design to make sure that it's actually safe to _subclass_ it, so classes are _closed_ by default and can't be inherited from unless you explicitly declare the class to be _open_ or _abstract_. You can then subclass from that class by declaring a new class which mentions its parent class after a colon:

```kotlin
open class MotorVehicle
class Car : MotorVehicle()
```

Classes that don't declare a superclass implicitly inherit from `Any`. The subclass must invoke one of the constructors of the base class, passing either parameters from its own constructor or constant values:

```kotlin
open class MotorVehicle(val maxSpeed: Double, val horsepowers: Int)
class Car(
    val seatCount: Int,
    maxSpeed: Double
) : MotorVehicle(maxSpeed, 100)
```

The subclass _inherits_ all members that exist in its superclass - both those that are directly defined in the superclass and the ones that the superclass itself has inherited. In this example, `Car` contains the following members:

* `seatCount`, which is `Car`'s own property
* `maxSpeed` and `horsepowers`, which are inherited from `MotorVehicle`
* `toString()`, `equals()`, and `hashCode()`, which are inherited from `Any`

Note that the terms "subclass" and "superclass" can span multiple levels of inheritance - `Car` is a subclass of `Any`, and `Any` is the superclass of everything. If we want to restrict ourselves to one level of inheritance, we will say "direct subclass" or "direct superclass".

Note that we do not use `val` in front of `maxSpeed` in `Car` - doing so would have introduced a distinct property in `Car` that would have _shadowed_ the one inherited from `MotorVehicle`. As written, it's just a constructor parameter that we pass on to the superconstructor.

`private` members (and `internal` members from superclasses in other modules) are also inherited, but are not directly accessible: if the superclass contains a private property `foo` that is referenced by a public function `bar()`, instances of the subclass will contain a `foo`; they can't use it directly, but they are allowed to call `bar()`.

When an instance of a subclass is constructed, the superclass "part" is constructed first (via the superclass constructor). This means that during execution of the constructor of an open class, it could be that the object being constructed is an instance of a subclass, in which case the subclass-specific properties have not been initialized yet. For that reason, calling an open function from a constructor is risky: it might be overridden in the subclass, and if it is accessing subclass-specific properties, those won't be initialized yet.


### Overriding

If a member function or property is declared as `open`, subclasses may _override_ it by providing a new implementation. Let's say that `MotorVehicle` declares this function:

```kotlin
open fun drive() =
    "$horsepowers HP motor vehicle driving at $maxSpeed MPH"
```

If `Car` does nothing, it will inherit this function as-is, and it will return a message with the car's horsepowers and max speed. If we want a car-specific message, `Car` can override the function by redeclaring it with the `override` keyword:

```kotlin
override fun drive() =
   "$seatCount-seat car driving at $maxSpeed MPH"
```

The signature of the overriding function must exactly match the overridden one, except that the return type in the overriding function may be a subtype of the return type of the overridden function.

If what the overriding function wants to do is an extension of what the overridden function did, you can call the overridden function via `super` (either before, after, or between other code):

```kotlin
override fun drive() =
    super.drive() + " with $seatCount seats"
```


### Interfaces

The single-parent rule often becomes too limiting, as you'll often find commonalities between classes in different branches of a class hierarchy. These commonalities can be expressed in _interfaces_.

An interface is essentially a contract that a class may choose to sign; if it does, the class is obliged to provide implementations of the properties and functions of the interface. However, an interface may (but typically doesn't) provide a default implementation of some or all of its properties and functions. If a property or function has a default implementation, the class may choose to override it, but it doesn't have to. Here's an interface without any default implementations:

```kotlin
interface Driveable {
    val maxSpeed: Double
    fun drive(): String
}
```

We can choose to let `MotorVehicle` implement that interface, since it's got the required members - but now we need to mark those members with `override`, and we can remove `open` since an overridden function is implicitly open:

```kotlin
open class MotorVehicle(
    override val maxSpeed: Double,
    val wheelCount: Int
) : Driveable {
    override fun drive() = "Wroom!"
}
```

If we were to introduce another class `Bicycle`, which should be neither a subclass nor a superclass of `MotorVehicle`, we could still make it implement `Driveable`, as long as we declare `maxSpeed` and `drive` in `Bicycle`.

Subclasses of a class that implements an interface (in this case, `Car`) are also considered to be implementing the interface.

A symbol that is declared inside an interface normally should be public. The only other legal visibility modifier is `private`, which can only be used if the function body is supplied - that function may then be called by each class that implements the interface, but not by anyone else.

As for why you would want to create an interface, other than as a reminder to have your classes implement certain members, see the section on [polymorphism](#polymorphism).


### Abstract classes

Some superclasses are very useful as a grouping mechanism for related classes and for providing shared functions, but are so general that they're not useful on their own. `MotorVehicle` seems to fit this description. Such a class should be declared _abstract_, which will prevent the class from being instantiated directly:

```kotlin
abstract class MotorVehicle(val maxSpeed: Double, val wheelCount: Int)
```

Now, you can no longer say `val mv = MotorVehicle(100, 4)`.

Abstract classes are implicitly open, since they are useless if they don't have any concrete subclasses.

When an abstract class implements one or more interfaces, it is not required to provide definitions of the members of its interfaces (but it can if it wants to). It must still _declare_ such members, using `abstract override` and not providing any body for the function or property:

```kotlin
abstract override val foo: String
abstract override fun bar(): Int
```

Being abstract is the only way to "escape" from having to implement the members of your interfaces, by offloading the work onto your subclasses - if a subclass wants to be concrete, it must implement all the "missing" members.


### Polymorphism

Polymorphism is the ability to treat objects with similar traits in a common way. In Python, this is achieved via _ducktyping_: if `x` refers to some object, you can call `x.quack()` as long as the object happens to have the function `quack()` - nothing else needs to be known (or rather, assumed) about the object. That's very flexible, but also risky: if `x` is a parameter, every caller of your function must be aware that the object they pass to it must have `quack()`, and if someone gets it wrong, the program blows up at runtime.

In Kotlin, polymorphism is achieved via the class hierarchy, in such a way that it is impossible to run into a situation where a property or function is missing. The basic rule is that a variable/property/parameter whose declared type is `A` may refer to an instance of a class `B` if and only if `B` is a subtype of `A`. This means that either, `A` must be a class and `B` must be a subclass of `A`, or that `A` must be an interface and `B` must be a class that implements that interface or be a subclass of a class that does. With our classes and interfaces from the previous sections, we can define these functions:

```kotlin
fun boast(mv: MotorVehicle) =
    "My ${mv.wheelCount} wheel vehicle can drive at ${mv.maxSpeed} MPH!"

fun ride(d: Driveable) =
    "I'm riding my ${d.drive()}"
```

and call them like this:

```kotlin
val car = Car(4, 120)
boast(car)
ride(car)
```

We're allowed to pass a `Car` to `boast()` because `Car` is a subclass of `MotorVehicle`. We're allowed to pass a `Car` to `ride()` because `Car` implements `Driveable` (thanks to being a subclass `MotorVehicle`). Inside `boast()`, we're only allowed to access the members of the declared parameter type `MotorVehicle`, even if we're in a situation where we know that it's really a `Car` (because there could be other callers that pass a non-`Car`). Inside `ride()`, we're only allowed to access the members of the declared parameter type `Driveable`. This ensures that every member lookup is safe - the compiler only allows you to pass objects that are guaranteed to have the necessary members. The downside is that you will sometimes be forced to declare "unnecessary" interfaces or wrapper classes in order to make a function accept instances of different classes.

With collections and functions, polymorphism becomes more complicated - see the section on [generics](#generics).


[//]: TODO (Overload resolution rules)


### Casting and type testing

When you take an interface or an open class as a parameter, you generally don't know the real type of the parameter at runtime, since it could be an instance of a subclass or of any class that implements the interface. It is possible to check what the exact type is, but like in Python, you should generally avoid it and instead design your class hierarchy such that you can do what you need by proper overriding of functions or properties.

If there's no nice way around it, and you need to take special actions based on what type something is or to access functions/properties that only exist on some classes, you can use `is` to check if the real type of an object is a particular class or a subclass thereof (or an implementor of an interface). When this is used as the condition in an `if`, the compiler will let you perform type-specific operations on the object inside the `if` body:

```kotlin
fun foo(x: Any) {
    if (x is Person) {
        println("${x.name}") // This wouldn't compile outside the if
    }
}
```

If you want to check for _not_ being an instance of a type, use `!is`. Note that `null` is never an instance of any non-nullable type, but it is always an "instance" of any nullable type (even though it technically isn't an instance, but an absence of any instance).

The compiler will not let you perform checks that can't possibly succeed because the declared type of the variable is a class that is on an unrelated branch of the class hierarchy from the class you're checking against - if the declared type of `x` is `MotorVehicle`, you can't check if `x` is a `Person`. If the right-hand side of `is` is an interface, Kotlin will allow the type of the left-hand side to be any interface or open class, because it could be that some subclass thereof implements the interface.

If your code is too clever for the compiler, and you know without the help of `is` that `x` is an instance of `Person` but the compiler doesn't, you can _cast_ your value with `as`:

```kotlin
val p = x as Person
```

This will raise a `ClassCastException` if the object is not actually an instance of `Person` or any of its subclasses. If you're not sure what `x` is, but you're happy to get null if it's not a `Person`, you can use `as?`, which will return null if the cast fails. Note that the resulting type is `Person?`:

```kotlin
val p = x as? Person
```

You can also use `as` to cast to a nullable type. The difference between this and the previous `as?` cast is that this one will fail if `x` is a non-null instance of another type than `Person`:

```kotlin
val p = x as Person?
```


### Delegation

If you find that an interface that you want a class to implement is already implemented by one of the properties of the class, you can _delegate_ the implementation of that interface to that property with `by`:

```kotlin
interface PowerSource {
    val horsepowers: Int
}

class Engine(override val horsepowers: Int) : PowerSource

open class MotorVehicle(val engine: Engine): PowerSource by engine
```

This will automatically implement all the interface members of `PowerSource` in `MotorVehicle` by invoking the same member on `engine`. This only works for properties that are declared in the constructor.


### Delegated properties

Let's say that you're writing a simple ORM. Your database library represents a row as instances of a class `Entity`, with functions like `getString("name")` and `getLong("age")` for getting typed values from the given columns. We could create a typed wrapper class like this:

```kotlin
abstract class DbModel(val entity: Entity)

class Person(val entity: Entity) : DbModel(entity) {
    val name = entity.getString("name")
    val age = entity.getLong("age")
}
```

That was easy, but maybe we'd want to do lazy-loading so that we won't spend time on extracting the fields that won't be used (especially if some of them contain a lot of data in a format that it is time-consuming to parse), and maybe we'd like support for default values. While we could implement that logic in a `get()` block, it would need to be duplicated in every property. Alternatively, we could implement the logic in a separate `StringProperty` class (note that this simple example is not thread-safe):

```kotlin
class StringProperty(
    private val model: DbModel,
    private val fieldName: String,
    private val defaultValue: String? = null
) {
    private var _value: String? = defaultValue
    private var loaded = false
    val value: String?
        get() {
            // Warning: This is not thread-safe!
            if (loaded) return _value
            if (model.entity.contains(fieldName)) {
                _value = model.entity.getString(fieldName)
            }
            loaded = true
            return _value
        }
}

// In Person
val name = StringProperty(this, "name", "Unknown Name")
```

Unfortunately, using this would require us to type `p.name.value` every time we wanted to use the property. We could do the following, but that's also not great since it introduces an extra property:

```kotlin
// In Person
private val _name = StringProperty(this, "name", "Unknown Name")
val name get() = _name.value
```

The solution is a _delegated property_, which allows you to specify the behavior of getting and setting a property (somewhat similar to implementing `__getattribute__()` and `__setattribute__()` in Python, but for one property at a time).

```kotlin
class DelegatedStringProperty(
    private val fieldName: String,
    private val defaultValue: String? = null
) {
    private var _value: String? = null
    private var loaded = false
    operator fun getValue(thisRef: DbModel, property: KProperty<*>): String? {
        if (loaded) return _value
        if (thisRef.entity.contains(fieldName)) {
            _value = thisRef.entity.getString(fieldName)
        }
        loaded = true
        return _value
    }
}
```

The delegated property can be used like this to declare a property in `Person` - note the use of `by` instead of `=`:

```kotlin
val name by DelegatedStringProperty(this, "name", "Unknown Name")
```

Now, whenever anyone reads `p.name`, `getValue()` will be invoked with `p` as `thisRef` and metadata about the `name` property as `property`. Since `thisRef` is a `DbModel`, this delegated property can only be used inside `DbModel` and its subclasses.

A nice built-in delegated property is `lazy`, which is a properly threadsafe implementation of the lazy loading pattern. The supplied lambda expression will only be evaluated once, the first time the property is accessed.

```kotlin
val name: String? by lazy {
    if (thisRef.entity.contains(fieldName)) {
        thisRef.entity.getString(fieldName)
    } else null
}
```


### Sealed classes

If you want to restrict the set of subclasses of a base class, you can declare the base class to be `sealed` (which also makes it abstract), in which case you can only declare subclasses in the same file. The compiler then knows the complete set of possible subclasses, which will let you do exhaustive `when` expression for all the possible subtypes without the need for an `else` clause (and if you add another subclass in the future and forget to update the `when`, the compiler will let you know).


## Objects and companion objects


### Object declarations

If you need a _singleton_ - a class that only has got one instance - you can declare the class in the usual way, but use the `object` keyword instead of `class`:

```kotlin
object CarFactory {
    val cars = mutableListOf<Car>()
    
    fun makeCar(horsepowers: Int): Car {
        val car = Car(horsepowers)
        cars.add(car)
        return car
    }
}
```

There will only ever be one instance of this class, and the instance (which is created the first time it is accessed, in a thread-safe manner) has got the same name as the class:

```kotlin
val car = CarFactory.makeCar(150)
println(CarFactory.cars.size)
```


### Companion objects

If you need a function or a property to be tied to a class rather than to instances of it (similar to `@staticmethod` in Python), you can declare it inside a _companion object_:

```kotlin
class Car(val horsepowers: Int) {
    companion object Factory {
        val cars = mutableListOf<Car>()

        fun makeCar(horsepowers: Int): Car {
            val car = Car(horsepowers)
            cars.add(car)
            return car
        }
    }
}
```

The companion object is a singleton, and its members can be accessed directly via the name of the containing class (although you can also insert the name of the companion object if you want to be explicit about accessing the companion object):

```kotlin
val car = Car.makeCar(150)
println(Car.Factory.cars.size)
```

In spite of this syntactical convenience, the companion object is a proper object on its own, and can have its own supertypes - and you can assign it to a variable and pass it around. If you're integrating with Java code and need a true `static` member, you can [annotate](#annotations) a member inside a companion object with `@JvmStatic`.

A companion object is initialized when the class is loaded (typically the first time it's referenced by other code that is being executed), in a thread-safe manner. You can omit the name, in which case the name defaults to `Companion`. A class can only have one companion object, and companion objects can not be nested.

Companion objects and their members can only be accessed via the containing class name, not via instances of the containing class. Kotlin does not support class-level functions that also can be overridden in subclasses (like `@classmethod` in Python). If you try to redeclare a companion object in a subclass, you'll just shadow the one from the base class. If you need an overridable "class-level" function, make it an ordinary open function in which you do not access any instance members - you can override it in subclasses, and when you call it via an object instance, the override in the object's class will be called. It is possible, but inconvenient, to call functions via a class reference in Kotlin, so we won't cover that here.


### Object expressions

Java only got support for function types and lambda expressions a few years ago. Previously, Java worked around this by using an interface to define a function signature and allowing an inline, anonymous definition of a class that implements the interface. This is also available in Kotlin, partly for compatibility with Java libraries and partly because it can be handy for specifying event handlers (in particular if there is more than one event type that must be listened for by the same listener object). Consider an interface or a (possibly abstract) class, as well a function that takes an instance of it:

```kotlin
interface Vehicle {
    fun drive(): String
}

fun start(vehicle: Vehicle) = println(vehicle.drive())
```

By using an _object expression_, you can now define an anonymous, unnamed class and at the same time create one instance of it, called an _anonymous object_:

```kotlin
start(object : Vehicle {
    override fun drive() = "Driving really fast"
})
```

If the supertype has a constructor, it must be invoked with parentheses after the supertype name. You can specify multiple supertypes if need be (but as usual, at most one superclass).

Since an anonymous class has no name, it can't be used as a return type - if you do return an anonymous object, the function's return type must be `Any`.

In spite of the `object` keyword being used, a new instance of the anonymous class will be created whenever the object expression is evaluated.

The body of an object expression may access, and possibly modify, the local variables of the containing scope.


## Generics


### Generic type parameters

One might think that static typing would make it very impractical to make collection classes or any other class that needs to contain members whose types vary with each usage. Generics to the rescue: they allow you to specify a "placeholder" type in a class or function that must be filled in whenever the class or function is used. For example, a node in a linked list needs to contain data of some type that is not known when we write the class, so we introduce a _generic type parameter_ `T` (they are conventionally given single-letter names):

```kotlin
class TreeNode<T>(val value: T?, val next: TreeNode<T>? = null)
```

Whenever you create an instance of this class, you must specify an actual type in place of `T`, unless the compiler can infer it from the constructor parameters: `TreeNode("foo")` or `TreeNode<String>(null)`. Every use of this instance will act as if it were an instance of a class that looks like this:

```kotlin
class TreeNode<String>(val value: String?, val next: TreeNode<String>? = null)
```

Member properties and member functions inside a generic class may for the most part use the class' generic type parameters as if they were ordinary types, without having to redeclare them. It is also possible to make functions that take more generic parameters than the class does, and to make generic functions inside nongeneric classes, and to make generic top-level functions (which is what we'll do in the next example). Note the different placement of the generic type parameter in generic function declarations:

```kotlin
fun <T> makeLinkedList(vararg elements: T): TreeNode<T>? {
    var node: TreeNode<T>? = null
    for (element in elements.reversed()) {
        node = TreeNode(element, node)
    }
    return node
}
```


### Constraints

You can restrict the types that can be used for a generic type parameter, by specifying that it must be an instance of a specific type or of a subclass thereof. If you've got a class or interface called `Vehicle`, you can do:

```kotlin
class TreeNode<T : Vehicle>
```

Now, you may not create a `TreeNode` of a type that is not a subclass/implementor of `Vehicle`. Inside the class, whenever you've got a value of type `T`, you may access all the public members of `Vehicle` on it.

If you want to impose additional constraints, you must use a separate `where` clause, in which case the type parameter must be a subclass of the given class (if you specify a class, and you can specify at most one) _and_ implement all the given interfaces. You may then access all the public members of all the given types whenever you've got a value of type `T`:

```kotlin
class TreeNode<T> where T : Vehicle, T : HasWheels
```


### Variance


#### Introduction

Pop quiz: if `Apple` is a subtype of `Fruit`, and `Bowl` is a generic container class, is `Bowl<Apple>` a subtype of `Bowl<Fruit>`? The answer is - perhaps surprisingly - _no_. The reason is that if it were a subtype, we would be able to break the type system like this:

```kotlin
fun add(bowl: Bowl<Fruit>, fruit: Fruit) = bowl.add(fruit)

val bowl = Bowl<Apple>()
add(bowl, Pear()) // Doesn't actually compile!
val apple = bowl.get() // Boom!
```

If the second-to-last line compiled, it would allow us to put a pear into what is ostensibly a bowl of only apples, and your code would explode when it tried to extract the "apple" from the bowl. However, it's frequently useful to be able to let the type hierarchy of a generic type parameter "flow" to the generic class. As we saw above, though, some care must be taken - the solution is to restrict the direction in which you can move data in and out of the generic object.


#### Declaration-site covariance and contravariance

If you have an instance of `Generic<Subtype>`, and you want to refer to it as a `Generic<Supertype>`, you can safely _get_ instances of the generic type parameter from it - these will truly be instances of `Subtype` (because they come from an instance of `Generic<Subtype>`), but they will appear to you as instances of `Supertype` (because you've told the compiler that you have a `Generic<Supertype>`). This is safe; it is called _covariance_, and Kotlin lets you do _declaration-site covariance_ by putting `out` in front of the generic type parameter. If you do, you may only use that type parameter as a return type, not as a parameter type. Here is the simplest useful covariant interface:

```kotlin
interface Producer<out T> {
    fun get(): T
}
```

It is safe to treat a `Producer<Apple>` as if it were a `Producer<Fruit>` - the only thing it will ever produce is `Apple` instances, but that's okay, because an `Apple` is a `Fruit`.

Conversely, if you have an instance of `Generic<Supertype>`, and you want to refer to it as a `Generic<Subtype>` (which you can't do with nongeneric classes), you can safely _give_ instances of the generic type parameter to it - the compiler will require those instances to be of the type `Subtype`, which will be acceptable to the real instance because it can handle any `Supertype`. This is called _contravariance_, and Kotlin lets you do _declaration-site contravariance_ by putting `in` in front of the generic type parameter. If you do, you may only use that type parameter as a parameter type, not as a return type. Here is the simplest useful contravariant interface:

```kotlin
interface Consumer<in T> {
    fun add(item: T)
}
```

It is safe to treat a `Consumer<Fruit>` as a `Consumer<Apple>` - you are then restricted to only adding `Apple` instances to it, but that's okay, because it is capable of receiving any `Fruit`.

With these two interfaces, we can make a more versatile fruit bowl. The bowl itself needs to both produce and consume its generic type, so it can neither be covariant nor contravariant, but it can implement our covariant and contravariant interfaces:

```kotlin
class Bowl<T> : Producer<T>, Consumer<T> {
    private val items = mutableListOf<T>()
    override fun get(): T = items.removeAt(items.size - 1)
    override fun add(item: T) { items.add(item) }
}
```

Now, you can treat a bowl of `T` as a producer of any superclass of `T`, and as a consumer of any subclass of `T`:

```kotlin
val p: Producer<Fruit> = Bowl<Apple>()
val c: Consumer<Apple> = Bowl<Fruit>()
```


#### Variance directions

If the parameters or return types of the members of a variant type are themselves variant, it gets a bit complicated. Function types in parameters and return types make it even more challenging. If you're wondering whether it's safe to use a variant type parameter `T` in a particular position, ask yourself:

* If `T` is covariant: is it okay that the user of my class thinks that `T` in this position is a `Supertype`, while in reality, it's a `Subtype`?
* If `T` is contravariant: is it okay that the user of my class thinks that `T` in this position is a `Subtype`, while in reality, it's a `Supertype`?

These considerations lead to the following rules. A covariant type parameter `T` (which the user of an object might think is `Fruit`, while the object in reality is tied to `Apple`) may be used as:

*   `val v: T`

    A read-only property type (the user is expecting a `Fruit`, and gets an `Apple`)

*   `val p: Producer<T>`

    The covariant type parameter of a read-only property type (the user is expecting a producer of `Fruit`, and gets a producer of `Apple`)

*   `fun f(): T`

    A return type (as we've already seen)

*   `fun f(): Producer<T>`

    The covariant type parameter of a return type (the user is expecting that the returned value will produce a `Fruit`, so it's okay if it really produces an `Apple`)

*   `fun f(consumer: Consumer<T>)`

    The contravariant type parameter of a parameter type (the user is passing a consumer that can handle any `Fruit`, and it will be given an `Apple`)

*   `fun f(function: (T) -> Unit)`

    The parameter type of a function-typed parameter (the user is passing a function that can handle any `Fruit`, and it will be given an `Apple`)

*   `fun f(function: (Producer<T>) -> Unit)`

    The covariant type parameter of the parameter type of a function-typed parameter (the user is passing a function that can handle any `Fruit` producer, and it will be given an `Apple` producer)

*   `fun f(function: () -> Consumer<T>)`

    The contravariant type parameter of the return type of a function-typed parameter (the user is passing a function that will return a consumer of any `Fruit`, and the returned consumer will be given `Apple` instances)

*   `fun f(): () -> T`

    The return type of a function-typed return type (the user expects the returned function to return `Fruit`, so it's okay if it really returns `Apple`)

*   `fun f(): () -> Producer<T>`

    The covariant type parameter of the return type of a function-typed return type (the user expects the returned function to return something that produces `Fruit`, so it's okay if it really produces `Apple`)

*   `fun f(): (Consumer<T>) -> Unit`

    The contravariant type parameter of a parameter of a function-typed return type (the user will call the returned function with something that can consume any `Fruit`, so it's okay to return a function that expects to receive something that can handle `Apple`)

A contravariant type parameter may be used in the converse situations. It is left as an exercise to the reader to figure out the justifications for why these member signatures are legal:

* `val c: Consumer<T>`
* `fun f(item: T)`
* `fun f(): Consumer<T>`
* `fun f(producer: Producer<T>)`
* `fun f(function: () -> T)`
* `fun f(function: () -> Producer<T>)`
* `fun f(function: (Consumer<T>) -> Unit)`
* `fun f(): (T) -> Unit`
* `fun f(): (Producer<T>) -> Unit`
* `fun f(): () -> Consumer<T>`


#### Type projections (use-site covariance and contravariance)

If you're using a generic class whose type parameters haven't been declared in a variant way (either because its authors didn't think of it, or because the type parameters can't have either variance kind because they are used both as parameter types and return types), you can still use it in a variant way thanks to _type projection_. The term "projection" refers to the fact that when you do this, you might restrict yourself to using only some of its members - so you're in a sense only seeing a partial, or "projected" version of the class. Let's look again at our `Bowl` class, but without the variant interfaces this time:

```kotlin
class Bowl<T> {
    private val items = mutableListOf<T>()
    fun get(): T = items.removeAt(items.size - 1)
    fun add(item: T) { items.add(item) }
}
```

Because `T` is used as a parameter type, it can't be covariant, and because it's used as a return type, it can't be contravariant. But if we only want to use the `get()` function, we can project it covariantly with `out`:

```kotlin
fun <T> moveCovariantly(from: Bowl<out T>, to: Bowl<T>) {
    to.add(from.get())
}
```

Here, we're saying that the type parameter of `from` must be a subtype of the type parameter of `to`. This function will accept e.g. a `Bowl<Apple>` as `from` and `Bowl<Fruit>` as `to`. The price we're paying for using the `out` projection is that we can't call `add()` on `from()`, since we don't know its true type parameter and we would therefore risk adding incompatible fruits to it.

We could do a similar thing with contravariant projection by using `in`:

```kotlin
fun <T> moveContravariantly(from: Bowl<T>, to: Bowl<in T>) {
    to.add(from.get())
}
```

Now, the type parameter of `to` must be a supertype of that of `from`. This time, we're losing the ability to call `get()` on `to`.

The same type parameter can be used in both covariant and contravariant projections (because it's the generic classes that are being projected, not the type parameter):

```kotlin
fun <T> moveContravariantly(from: Bowl<out T>, to: Bowl<in T>) {
    to.add(from.get())
}
```

While doing so was not useful in this particular example, one could get interesting effects by adding an unprojected parameter type `via: Bowl<T>`, in which case the generic type parameter of `via` would be forced to be "in-between" those of `from` and `to`.

If you don't have any idea (or don't care) what the generic type might be, you can use a _star-projection_:

```kotlin
fun printSize(items: List<*>) = println(items.size)
```

When using a generic type where you have star-projected one or more of its type parameters, you can:

* Use any members that don't mention the star-projected type parameter(s) at all
* Use any members that return the star-projected type parameter(s), but the return type will appear to be `Any?` (unless the type parameter is constrained, in which case you'll get the type mentioned in the constraint)
* Not use any members that take a star-projected type as a parameter


### Reified type parameters

Sadly, Kotlin has inherited Java's limitation on generics: they are strictly a compile-time concept - the generic type information is _erased_ at runtime. Therefore, you can not say `T()` to construct a new instance of a generic type; you can not at runtime check if an object is an instance of a generic type parameter; and if you try to cast between generic types, the compiler can't guarantee the correctness of it.

Luckily, Kotlin has got _reified type parameters_, which alleviates some of these problems. By writing `reified` in front of a generic type parameter, it does become available at runtime, and you'll get to write `T::class` to get the [class metadata](#obtaining-member-references-from-a-class-reference). You can only do this in inline functions (because an inline function will be compiled into its callsite, where the type information _is_ available at runtime), but it still goes a long way. For example, you can make an inline wrapper function for a big function that has got a less elegant signature.

In the example below, we assume that there is a `DbModel` base class, and that every subclass has got a parameterless primary constructor. In the inline function, `T` is reified, so we can get the class metadata. We pass this to the function that does the real work of talking to the database.

```kotlin
inline fun <reified T : DbModel> loadFromDb(id: String): T =
    loadFromDb(T::class, id)

fun <T : DbModel> loadFromDb(cls: KClass<T>, id: String): T {
    val entity = cls.primaryConstructor!!.call()
    val tableName = cls.simpleName
    // DB magic goes here - load from table `tableName`,
    // and use the data to populate `entity`
    // (possibly via `memberProperties`)
    return entity
}
```

Now, you can say `loadFromDb<Exercise>("x01234567")` to load an object from the `Exercise` database table.


## Extension functions/properties

Since you can't modify built-in or third-party classes, you can't directly add functions or properties to them. If you can achieve what you want by only using the public members of a class, you can of course just write a function that takes an instance of the class as a parameter - but sometimes, you'd really like to be able to say `x.foo(y)` instead of `foo(x, y)`,  especially if you want to make a chain of such calls or property lookups: `x.foo(y).bar().baz` instead of `getBaz(bar(foo(x, y)))`. 

There is a nice piece of syntactic sugar that lets you do this: _extension functions_ and _extension properties_. They look like regular member functions/properties, but they are defined outside of any class - yet they reference the class name and can use `this`. However, they can only use visible members of the class (typically just the public ones). Behind the scenes, they get compiled down to regular functions that take the target instance as a parameter.

For example, if you work a lot with bytes, you might want to easily get an unsigned byte in the range 0 through 255 instead of the default -128 through 127 (the result will have to be in the form of a `Short`/`Int`/`Long`, though). `Byte` is a built-in class that you can't modify, but you can define this extension function:

```kotlin
fun Byte.toUnsigned(): Int {
    return if (this < 0) this + 256 else this.toInt()
}
```

Now, you can do:

```kotlin
val x: Byte = -1
println(x.toUnsigned()) // Prints 255
```

If you'd rather do `x.unsigned`, you can define an extension property:

```kotlin
val Byte.unsigned: Int
    get() = if (this < 0) this + 256 else this.toInt()
```

Keep in mind that this is just syntactic sugar - you're not actually modifying the class or its instances. Therefore, you have to import an extension function/property wherever you want to use it (since it isn't carried along with the instances of the class). For the same reason, you can not override extension members - you can reimplement them for subtypes, but the resolution happens at compile-time based on the static type of the expression you're invoking it on. So if you declare an extension function for `Vehicle`, and one with the same name and signature for its subclass `Car`, and you do the following, it's the extension function on `Vehicle` that will be called, even though `v` is really a `Car`:

```kotlin
fun foo(v: Vehicle) = v.extension()
val x = foo(Car())
```

There are a lot of built-in extension functions/properties in Kotlin - for example, `map()`, `filter()`, and the rest of the framework for processing collections in a functional manner is built using extension functions.


## Member references and reflection


### Property references

Consider this class: 

```kotlin
class Person(val name: String, var age: Int) {
    fun present() = "I'm $name, and I'm $age years old"
    fun greet(other: String) = "Hi, $other, I'm $name"
}
```

You can get reference to its `name` property like this:

```kotlin
val prop = Person::name
```

The result is an object which represents a reference to the property (the "Platonic ideal" property, not a property on a particular instance). There's a type hierarchy for property objects: the base interface is `KProperty`, which lets you get metadata about the property, such as its name and type. If you want to use the property object to read or modify the property's value in an object, you need to use a subinterface that specifies what kind of property it is. Immutable properties typically are `KProperty1<R, V>`, and mutable properties typically are `KMutableProperty1<R, V>`. Both of these are generic interfaces, with `R` being the receiver type (the type on which the property is declared, in this case `Person`) and `V` being the type of the property's value.

Given an `R` instance, `KProperty1<R, V>` will let you read the value that the property has in that instance by calling `get()`, and `KMutableProperty1<R, V>` will also let you change the property value in the instance by calling `set()`. Using this, we can start writing functions that manipulate properties without knowing in advance which property (or which class) they are going to deal with:

```kotlin
fun <T> printProperty(instance: T, prop: KProperty1<T, *>) {
    println("${prop.name} = ${prop.get(instance)}")
}

fun <T> incrementProperty(
    instance: T, prop: KMutableProperty1<T, Int>
) {
    val value = prop.get(instance)
    prop.set(instance, value + 1)
}

val person = Person("Lisa", 23)
printProperty(person, Person::name)
incrementProperty(person, Person::age)
```

You can also get a reference to a top-level property by just prefixing the property name with `::` (e.g. `::foo`), and its type will be `KProperty0<V>` or `KMutableProperty0<V>`.


### Function references

Functions act similarly to properties, but can be referenced as two different kinds of types.

If you want to look at the metadata of a function (e.g. its name), use `KFunction<V>` or one of its subinterfaces, where `V` is the function's return type. Here's a basic example:

```kotlin
val person = Person("Lisa", 32)
val g: KFunction<String> = Person::greet
println(g.name)
println(g.call(person, "Anne"))
```

Invoking `call()` on a function object will call the function. If it is a member function, the first parameter must be the _receiver_ (the object on which the function is to be invoked, in this case `person`), and the remaining parameters must be the ordinary function parameters (in this case `"Anne"`).

Since the parameter types are not encoded as generic type parameters in `KFunction<V>`, you won't get compile-time type validation of the parameters you pass. In order to encode the parameter types, use one of the subinterfaces `KFunction1<A, V>`, `KFunction2<A, B, V>`, `KFunction3<A, B, C, V>`, and so on, depending on how many parameters the function has got. Keep in mind that if you are referencing a member function, the first generic type parameter is the receiver type. For example, `KFunction3<A, B, C, V>` may reference either an ordinary function that takes `A`, `B`, and `C` as parameters and returns `V`, or it may reference a member function on `A` that takes `B` and `C` as parameters and returns `V`. When you use any of these types, you can call the function through its reference as if the reference were a function, e.g. `function(a, b)`, and this call will be type-safe.

You can also reference a member property directly on an object, in which case you get a member function reference that is already bound to its receiver, so that you don't need the receiver type in the signature. Here's an example of both approaches:

```kotlin
fun <A, V> callAndPrintOneParam(function: KFunction1<A, V>, a: A): V {
    val result = function(a)
    println("${function.name}($a) = $result")
    return result
}

fun <A, B, V> callAndPrintTwoParam(function: KFunction2<A, B, V>, a: A, b: B): V {
    val result = function(a, b)
    println("${function.name}($a, $b) = $result")
    return result
}

val p = Person("Lisa", 32)
callAndPrintOneParam(p::greet, "Alice")
callAndPrintTwoParam(Person::greet, person, "Lisa")
```

If you only want to call the function and don't care about the metadata, use a function type, e.g. `(A, B) -> V` for an ordinary function reference or a bound member function reference, or `A.(B, C) -> V` for an unbound member function reference on `A`. Note that `KFunction<V>` and its subinterfaces are only available for declared functions (obtained either by explicitly referencing it in the code, or through reflection, as shown later) - only function types are available for function literals (lambda expressions or anonymous functions).

You can get a reference to an top-level function by prefixing the function name with `::` (e.g. `::foo`).


### Obtaining member references from a class reference

While it is possible in Kotlin to dynamically create new classes at runtime or to add members to a class, it's tricky and slow, and generally discouraged. However, it is easy to dynamically inspect an object to see e.g. what properties and functions it contains and which annotations exist on them. This is called _reflection_, and it's not very performant, so avoid it unless you really need it.

Kotlin has got its own reflection library (`kotlin-reflect.jar` must be included in your build). When targeting the JVM, you can also use the Java reflection facilities. Note that the Kotlin reflection isn't quite feature-complete yet - in particular, you can't use it to inspect built-in classes like `String`.

Warning: using reflection is usually the wrong way to solve problems in Kotlin! In particular, if you have several classes that all have some common properties/functions and you want to write a function that can take an instance of any of those classes and use those properties, the correct approach is to define an interface with the common properties/functions and make all the relevant classes implement it; the function can then take that interface as a parameter. If you don't control those classes, you can use the [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern) and write wrapper classes that implement the interface - this is very easy thanks to Kotlin's [delegation feature](#delegation). You can also get a lot of leverage out of using generics in clever ways.

Appending `::class` to a class name will give you a `KClass<C>` metadata object for that class. The generic type parameter `C` is the class itself, so you can use `KClass<*>` if you're writing a function that can work with metadata for any class, or you can make a generic function with a type parameter `T` and parameter type `KClass<T>`. From this, you can obtain references to the members of the class. The most interesting properties on `KClass` are probably `primaryConstructor`, `constructors`, `memberProperties`, `declaredMemberProperties`, `memberFunctions`, and `declaredMemberFunctions`. The difference between e.g. `memberProperties` and `declaredMemberProperties` is that the former includes inherited properties, while the latter only includes the properties that have been declared in the class' own body.

In this example, using `Person` and `callAndPrintTwoParam()` from the previous section, we locate a member function reference by name and call it:

```kotlin
val f = Person::class.memberFunctions.single { it.name == "greet" } as KFunction2<Person, String, String>
callAndPrintTwoParam(f, person, "Lisa")
```

The signature of `greet()` is `KFunction2<Person, String, String>` because it's a function on `Person` that takes a `String` and returns a `String`.

Constructor references are effectively factory functions for creating new instances of a class, which might come in handy:

```kotlin
val ctor = Person::class.primaryConstructor!! as (String, Int) -> Person
val newPerson = ctor("Karen", 45)
```


### Java-style reflection

If you're targeting the JVM platform, you can also use Java's reflection system directly. In this example, we grab a function reference from an object's class by specifying the function's name as a string (if the function takes parameters, you also need to specify their types), and then we call it. Note that we didn't mention `String` anywhere - this technique works without knowing what the object's class is, but it will raise an exception if the object's class doesn't have the requested function. However, Java-style function references do not have type information, so you won't get verification of the parameter types, and you must cast the return value:

```kotlin
val s = "Hello world"
val length = s.javaClass.getMethod("length")
val x = length.invoke(s) as Int
```

If you don't have an instance of the class, you can get the class metadata with `String::class.java` (but you can't invoke any of its members until you have an instance).

If you need to look up the class dynamically as well, you can use `Class.forName()` and supply the fully-qualified name of the class.


## Annotations

While Kotlin annotations look like Python decorators, they are far less flexible: they can generally only be used for metadata. They are pure data-containing classes, and do not contain any executable code. Some built-in annotations have an effect on the compilation process (such as `@JvmStatic`), but custom annotations are only useful for providing metadata that can be inspected at runtime by the reflection system. We won't delve deeply into annotations here, but here is an example. The annotations on the annotation declaration itself specify what constructs the annotation may be applied to and whether it is available for runtime inspection.

```kotlin
enum class TestSizes { SMALL, MEDIUM, LARGE }

@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
annotation class TestSize(val size: TestSizes)

@TestSize(TestSizes.SMALL)
class Tests { ... }

fun getTestSize(cls: KClass<*>): TestSizes? =
    cls.findAnnotation<TestSize>()?.size

println(getTestSize(Tests::class))
```


## File I/O

Kotlin has inherited Java's fidgety (but very flexible) way of doing I/O, but with some simplifying extra features. We won't get into all of it here, so for starters, this is how to iterate through all the lines of a file (you'll need `import java.io.File`):

```kotlin
File("data.txt").forEachLine { println(it) }
```

The default [encoding](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) is UTF-8, but you can specify it if you need something else:

```kotlin
File("data.txt").forEachLine(Charsets.UTF_16) { println(it) }
```

Note that the trailing newline of each line is stripped. You can also call `readLines()` on a file object to get a list of all the lines, or `useLines()` to supply a function that will be called on every line. If you simply want the entire file contents as one string or byte array, call `readText()` or `readBytes()`, respectively.

Note that while `File()` does create a "file object", it doesn't actually open the file - the file object is just a reference to the file path; opening the file is a separate action. The preceding functions open and close the file automatically, whereas other functions separately open and close the file. For example, if you're parsing binary data and you don't want to read the entire file at once, you must create an _input stream_ (for binary data) or an _input stream reader_ (for strings) - the example below will read 16 bytes:

```kotlin
val stream = File("data.txt").inputStream()
val bytes = ByteArray(16)
stream.read(bytes)
stream.close()
println(bytes)
```

It's important to close a stream when you're done with it; otherwise, your program will leak a file handle. See the next section for how do do this nicely.

If you've got one string that you want to write to a file, overwriting the existing contents if the file already exists, do this (again, UTF-8 is the default encoding):

```kotlin
File("data.txt").writeText("Hello world!")
```

If you want to write strings gradually, you need to create an `OutputStreamWriter` by calling `writer()` on the file object. You can write binary data to a file by calling `outputStream()` on a file object and use the resulting `OutputStream` to write bytes.

If you need a fancier way of reading or writing file data, you have access to  the full Java suite of I/O classes - in particular, `Scanner`, which can parse numbers and other data types from files or other streams, and `BufferedReader` (which is good for efficient reading of large amounts of data), which you can obtain by calling `bufferedReader()` on a file or stream. See any Java tutorial for how to use these.


## Scoped resource usage

Kotlin does not have Python's _resource managers_ or Java's _try-with-resources_, but thanks to extension functions, there's `use`:

```kotlin
File("/home/aasmund/test.txt").inputStream().use {
     val bytes = it.readBytes()
     println(bytes.size)
}
```

`use` can be invoked on anything that implements the `Closeable` interface, and when the `use` block ends (whether normally or due to an exception), `close()` will be called on the object upon which you invoked `use`. If an exception is raised within the block or by `close()`, it will bubble out of `use`. If both the block and `close()` raise, it's the exception from the block that will bubble out.

Thus, you can create something resource manager-like by creating a class that implements `Closeable`, does its setup work in `init`, and does its cleanup work in `close()`.

In case you're wondering about how `use`, which is a function, can just be followed by a block like that, see the section on [DSL support](#receivers).


## Documentation

Kotlin's documentation syntax is called _KDoc_. A KDoc block is placed above the construct it describes, and begins with `/**` and ends with `*/` (possibly on one line; if not, each intermediate lines should start with an aligned asterisk). The first block of text is the summary; then, you can use _block tags_ to provide information about specific parts of the construct. Some block tags are `@param` for function parameters and generic type parameters, and `@return` for the return value. You can link to identifiers inside brackets. All the text outside of links and block tag names is in Markdown format.

```kotlin
/**
 * Squares a number.
 *
 * @param number Any [Double] number whose absolute value is
 * less than or equal to the square root of [Double.MAX_VALUE].
 * @return A nonnegative number: the result of multiplying [number] with itself.
 */
fun square(number: Double) = number * number
```

Package-level documentation can be provided in a separate Markdown file.

Unlike docstrings, KDoc blocks are not available to the program at runtime.

You can generate separate documentation files in HTML format from KDoc by using a tool called [Dokka](https://github.com/Kotlin/dokka/blob/master/README.md).

---

_This material was written by [Aasmund Eldhuset](https://eldhuset.net/); it is owned by [Khan Academy](https://www.khanacademy.org/) and licensed for use under [CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)._
