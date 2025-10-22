# Password Generator in Python

This project implements a **random password generator** in Python. It allows users to specify the length of the password and choose whether to include uppercase letters, numbers, and special characters. The tool generates secure, random passwords suitable for everyday use.

## Features

* Generate passwords with a customizable length.
* Option to include:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Secure, random password generation to ensure strong passwords.
* Command-line interface (CLI) for easy use.

## Installation

### Requirements:

* Python 3.x (No external libraries are required)

### Steps to Run Locally:

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/Kaushik4636/Password_Generator.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd password-generator
   ```

3. **Run the password generator**:

   ```bash
   python password_generator.py
   ```

   The script will prompt you for the desired password length and options to include various character types. It will then generate and display a random password based on your input.

## How to Use

1. **Run the program**: Execute the `password_generator.py` script to start the password generator.
2. **Enter the desired password length**: You’ll be prompted to input the number of characters for the password (recommendation: at least 8 characters).
3. **Choose which characters to include**:

   * You’ll be asked if you want to include uppercase letters, numbers, and special characters. Answer with `y` (yes) or `n` (no).
4. **Get your password**: The program will generate a random password based on your selections and display it.

### Example:

```
Welcome to the Password Generator!
Enter the desired password length: 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): n

Generated Password: Ab7Xn8KJ2pQz
```

## Code Overview

* **`generate_password()`**: This function takes the password length and user preferences as input, then constructs and returns a random password.
* **`main()`**: The main function interacts with the user, gets their input, and calls the `generate_password()` function to generate and display the password.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository, submit issues, or make pull requests. Contributions are welcome! If you have ideas for improving the project, I’d love to hear them.

## Contact

For any questions or feedback, reach out to me at:
madhavankaushik3@gmail.com

Let me know if you want to make any changes!
