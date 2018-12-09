_This material was written by [Aasmund Eldhuset](https://eldhuset.net/); it is owned by [Khan Academy](https://www.khanacademy.org/) and is licensed for use under [CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). Please note that this is not a part of Khan Academy's official product offering._

---


## Declaration

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


## Calling

Functions are called the same way as in Python:

```kotlin
val greeting = happyBirthday("Anne", 32)
```

If you don't care about the return value, you don't need to assign it to anything.


## Returning

As opposed to Python, omitting `return` at the end of a function does not implicitly return null; if you want to return null, you must do so with `return null`. If a function never needs to return anything, the function should have the return type `Unit` (or not declare a return type at all, in which case the return type defaults to `Unit`). In such a function, you may either have no `return` statement at all, or say just `return`. `Unit` is both a singleton object (which `None` in Python also happens to be) and the type of that object, and it represents "this function never returns any information" (rather than "this function sometimes returns information, but this time, it didn't", which is more or less the semantics of returning null).


## Overloading

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


## Varargs and optional/named parameters

A function can take an arbitrary number of arguments, similarly to `*args` in Python, but they must all be of the same type. Unlike Python, you may declare other positional parameters after the variadic one, but there can be at most one variadic parameter. If its type is `X`, the type of the argument will be `XArray` if `X` is a primitive type and `Array<X>` if not.

```kotlin
fun countAndPrintArgs(vararg numbers: Int) {
    println(numbers.size)
    for (number in numbers) println(number)
}
```

There are no `**kwargs` in Kotlin, but you can define optional parameters with default values, and you may choose to name some or all of the parameters when you call the function (whether they've got default values or not). Like in Python, the named arguments can be reordered at will:

```kotlin
fun foo(decimal: Double, integer: Int, text: String = "Hello") { ... }

foo(3.14, text = "Bye", integer = 42)
foo(integer = 12, decimal = 3.4)
```

Unlike in Python, the expressions for the default values are evaluated at function invocation time, not at function definition time, which means that this classic Python trap is safe in Kotlin - every invocation will see a new, empty list:

```kotlin
fun tricky(x: Int, numbers: MutableList<Int> = mutableListOf()) {
    numbers.add(x)
    println(numbers)
}
```

You can call a variadic function with one array (but not a list or any other iterable) that contains all the variadic arguments, by _spreading_ it with the `*` operator (same syntax as Python):

```kotlin
val numbers = listOf(1, 2, 3)
countAndPrintArgs(*numbers.toIntArray())
```

Kotlin has inherited Java's fidgety array system, so primitive types have got their own array types and conversion functions, while any other type uses the generic `Array` type, to which you can convert with `.toTypedArray()`.

However, you can't spread a map into a function call and expect the values in the map to be passed to the parameters named by the keys - the names of the parameters must be known at compile time. If you need runtime-defined parameter names, your function must either take a map or take `vararg kwargs: Pair<String, X>` (where `X` is the "lowest common denominator" of the parameter types, in the worst case `Any?` - be prepared to have to typecast the parameter values, and note that you'll lose type safety). You can call such a function like this: `foo("bar" to 42, "test" to "hello")`, since `to` is an [infix function](classes.html#infix-functions) that creates a `Pair`.


