# Opanga Networks - Code Challenge
## Project Name
- opanga_configuration_parser
---

## Index

- [Problem Statement](#problem-statement)
- [Considerations](#considerations)
- [How to run the code?](#-how-to-run-the-code)
- [Notes](#notes)

## Problem statement
Write a program to parse configuration files made up of white space separated words and sections delimited by curly braces. Here is an example of the configuration file:

```properties
runtime {
    key1 value1
    key2 value2
    flag1

    system1 {
        prop1 value1
        prop1 value1
        ports 1234 5678 9102

        subsystem1 {
            prop3 value1 value2 value3
            flag2
        }
    }
    more stuff here
}
```

### Considerations:
- Save the parsed configuration in a data structure that allows querying for sections, subsections, key value pairs, and flags.
- Consider how to handle malformed configuration files.
- Write code to test your program, in the form of unit tests appropriate for the programming language of your choice.
- The code should compile and run, as well all the test cases should pass.
- Include in your solution all the instructions necessary to run the program, including how to set up the runtime environment with dependencies and requirements.
- Choose any one of the following programming languages: C, C++, Java, Python, JavaScript or Go.
- Let us know if you have any questions.
---

## How to run the code?
### Using Docker (recommended)
1. Install the latest version of Docker for your system.
2. Using the terminal, clone this repository to a folder of your preference.
3. Once positioned inside the cloned repository folder, build the Docker Image:
   ```bash
   docker build -t eddiejobs/opanga-code-challenge .
   ```
4. On the root repository path, create a new folder titled ```input```. Put here the configuration file you want to use to run the application.
5. Once built, you can run what you prefer:
   - Running test cases:
      ```bash
      docker run --rm -t eddiejobs/opanga-code-challenge pytest -v
      ```
   - Running the code using a file inside ```input``` folder:
      ```bash
      docker run --rm -t eddiejobs/opanga-code-challenge python src/app.py input/your-input.txt
      ```
---

## Notes
- In case anything is malfunctioning, please contact me as soon as possible, and I will be happy to assist you 😄.