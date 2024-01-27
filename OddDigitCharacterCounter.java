/**
 * Odd Digit Character Counter
 *
 * 
 * 
 *
 * This program prompts the user to enter text, then reads it
 * to determine the total number of characters the user has entered
 * as well as the total number of each odd digit and then displays
 * them at the end.
 *
 *
 */

import java.util.Objects;
import java.util.Scanner;

public class OddDigitCharacterCounter {

    public static void main(String[] args) {

        // Initializing scanner class
        Scanner scanner = new Scanner(System.in);

        // Initializing user_confirmation as a string
        String user_confirmation;

        do {

            // counters for each odd number and the rest of the characters.
            int char_counter = 0;
            int counter_one = 0;
            int counter_three = 0;
            int counter_five = 0;
            int counter_seven = 0;
            int counter_nine = 0;

            // Asks the user to enter some text
            System.out.println("Enter text");

            String user_input = scanner.next();

            // For loop to go through the user input.
            for (int i = 0; i < user_input.length(); i++) {

                switch (user_input.charAt(i)) {
                    case '1':
                        counter_one++;
                        break;
                    case '3':
                        counter_three++;
                        break;
                    case '5':
                        counter_five++;
                        break;
                    case '7':
                        counter_seven++;
                        break;
                    case '9':
                        counter_nine++;
                        break;
                    default:
                        char_counter++;
                }
            }
            // if statements to determine which counter to print.
            if (counter_one > 0) {
                System.out.println("There are " + counter_one + " one(s) ");
            }

            if (counter_three > 0) {
                System.out.println("There are " + counter_three + " three(s) ");
            }

            if (counter_five > 0) {
                System.out.println("There are " + counter_five + " five(s) ");
            }

            if (counter_seven > 0) {
                System.out.println("There are " + counter_seven + " seven(s) ");
            }

            if (counter_nine > 0) {
                System.out.println("There are " + counter_nine + " nine(s) ");
            }

            if (char_counter > 0) {
                System.out.println("There are " + char_counter + " other characters ");
            }
            // Asks the user if they would like to continue and stores it in user_confirmation
            System.out.println("Would you like to continue? ");
            System.out.println(" (y) " + " (n) ");
            user_confirmation = scanner.next();

        }
        // Determines if the user_confirmation is y (yes)
        while (Objects.equals(user_confirmation, "y"));
    }
}


