The author strongly recommends that you use an IDE with Kotlin support, as the static typing allows an IDE to do reliable navigation and code completion. I recommend [IntelliJ IDEA](https://www.jetbrains.com/idea/), which is built by the same company that created Kotlin. The Community Edition is free; see [instructions for getting started](https://kotlinlang.org/docs/tutorials/getting-started.html) (it comes bundled with Kotlin, and you can run your program from the IDE).

If you insist on using a plain editor and the command line, see [these instructions instead](https://kotlinlang.org/docs/tutorials/command-line.html). In short, you need to _compile_ your Kotlin code before running it. Assuming that your Kotlin file is called `program.kt`:

```bash
kotlinc program.kt -include-runtime -d program.jar
```

By default, Kotlin compiles down to Java (so you have the entire Java Standard Library available to you, and interacting with Java libraries is a breeze), so you now have a Java Archive (`program.jar`) which includes the Java libraries that are necessary to support the Kotlin features (thanks to `-include-runtime`), and you can run it using an out-of-the-box Java runtime:

```bash
java -jar program.jar
```




---

[← Previous: Hello World](hello-world.html) | [Next: Declaring variables →](declaring-variables.html)


---

_This material was written by [Aasmund Eldhuset](https://eldhuset.net/); it is owned by [Khan Academy](https://www.khanacademy.org/) and is licensed for use under [CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). Please note that this is not a part of Khan Academy's official product offering._