/**
 * Left-Right guessing game
 *
 *
 *
 *
 * This program randomly generates a number within the minimum
 * and maximum set values, it then prompts the user to make
 * a guess until they decide to quit or until they guess
 * correctly.
 * If the guess is incorrect, it will tell the user if the generated number is to the right
 * or the left of the guess.
 */

import java.util.Random;
import java.util.Scanner;

class LeftRightGuessingGame {
    public static void main(final String[] args) {
        // Initializing MAX and MIN set values for the randomly generated number.
        final int MAX = 50;
        final int MIN = -50;

        // Initializing scanner class
        final Scanner scanner = new Scanner(System.in);

        // Initializing variables for the user guess, random number and amount of guesses.
        int counter;
        int guess;
        int number;

        // Outer loop to play the game until the user decides to quit.
        do {
            // Generate random number
            number = new Random().nextInt(MIN, MAX);
            counter = 0;
            guess = -1000;
            System.out.println("Game start! Please enter a number between -50 and 50");
            System.out.println("Type 'quit' anytime to stop playing");

            // Loop to prompt the user for each guess.
            do {
                if (scanner.hasNextInt()) {
                    guess = scanner.nextInt();

                    if (guess > MAX || guess < MIN) {
                        System.out.println("The number should be between " + MIN + " and " + MAX + ".");
                    } else if (guess > number) {
                        System.out.println("Left.");
                        counter++;
                    } else if (guess < number) {
                        System.out.println("Right.");
                        counter++;
                    }
                } else if (scanner.hasNext("quit")) {
                    System.out.println("Thank you for playing.");
                    return;
                } else {  // Determines if the user entered a non integer character.
                    scanner.next();
                    System.out.println("Invalid input.");
                }
            } while (guess != number);

            counter++;
            System.out.println("Congrats! You have got the correct number in " + counter + " guesses!");
            System.out.println("Would you like to keep playing? yes/quit");
        } while (!scanner.next().equals("quit")); // Continues the loop if user input is not 'quit'.
    }

}