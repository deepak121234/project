/**
 * i deepak chander sharma, 000890413 certifies that this is my own work and I haven't allowed anybody to copy my code .
 * **/
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
/**this main class will basically read infomration from the icesheet and peroform task based on the info available.**/
public class Main {
    /**
     * this method is starting of the program
     * @param args
     * @throws FileNotFoundException if there is no file found
     */
    public static void main(String[] args) throws FileNotFoundException {
        /**
         * @param file contains the text file
         * @return  the given text file in the pdf
         */
        String file = "ICESHEETS.TXT";
        /**
         * @param fileScanner The scanner to read data from the file.
         * @ return information  about icesheet text file
         */
        Scanner fileScanner = new Scanner(new File(file));

        /**
         * @param numberoficesheet read input from file
         *@return the int value based omn calculation from the data given
         */
        int numbersofIceSheets = fileScanner.nextInt();
        /**
         * @param totoalcrackpts initialize it to 0
         * @return will return integer value
         */
        int totalcrackpts = 0;
        /**
         * @param maxfracturepts initialize it to 0
         * @return will return integer value
         */
        int maxfracturepts = 0;
        /**
         * @param sheetwithmaxfractures initialize it to 0
         * @return will return integer value
         */
        int sheetwithmaxfractures = 0;
        /**
         * @param totalfracturepts initiliaze it to 0
         * @return will return integer value
         */
        int totalfracturepts = 0;


        for (int sheet = 0; sheet < numbersofIceSheets; sheet++) {
            /**
             * @param rows read data from the file
             * @return  return the integer value
             */
            int rows = fileScanner.nextInt();
            /**
             * @param cols read data from the file
             * @return  return the integer value
             */
            int cols = fileScanner.nextInt();

            /**
             * @param icesheet a 2D array to store the ice sheet data
             * @ return a 2D array
             */

            int[][] iceSheet = new int[rows][cols];

            /**
             * @param fileScanner the Scanner to read information from the file.
             * @return A 2D array which represent the data sheet.
             * */
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    iceSheet[i][j] = fileScanner.nextInt();
                }
            }

            // Analyze the ice sheet
            int[] result = analyzeicesheet(iceSheet, sheet + 1); // Sheet numbers start from 1
            totalfracturepts += result[0];
            totalcrackpts += result[1];

            if (result[0] > maxfracturepts) {
                maxfracturepts = result[0];
                sheetwithmaxfractures = sheet + 1;
            }
        }

        fileScanner.close();

        System.out.println("the total number of fracture points in all sheets are : " + totalfracturepts);
        System.out.println("the total crack points in all sheets are : " + totalcrackpts);
        System.out.println("the sheet with the most fracture points is : " + sheetwithmaxfractures + " (Fracture points: " + maxfracturepts + ")");
        System.out.printf("The fraction of fracture points that are also crack points: %.3f\n", (totalcrackpts / (float) totalfracturepts));
    }

    /**
     * analyze icesheet for fracture and crack poiint
     * @param iceSheet is a 2d int array.
     * @param sheetNumber the number of icesheet
     * @return array of two int ( 1) fracture point, 2) crackpoint).
     */
    private static int[] analyzeicesheet(int[][] iceSheet, int sheetNumber) {
        int fracturePoints = 0;
        int crackPoints = 0;

        for (int i = 0; i < iceSheet.length; i++) {
            for (int j = 0; j < iceSheet[i].length; j++) {
                if (fracturepoint(iceSheet[i][j])) {
                    fracturePoints++;
                    if (crackpoint(iceSheet, i, j)) {
                        crackPoints++;
                        System.out.println("Sheet #" + sheetNumber + " Crack Point at: (" + i + ", " + j + ")");
                    }
                }
            }
        }

        System.out.println("Sheet #" + sheetNumber + " has " + fracturePoints + " fracture points.");
        return new int[]{fracturePoints, crackPoints};
    }

    /**
     * to determine whether the value in ice sheet is a fracture point\
     * @param value the value to be check
     * @return true if it is in fracture point and false if its not .
     */
    private static boolean fracturepoint(int value) {
        return value <= 200 && value % 50 == 0;
    }

    /**
     * to see if the value in  ice sheet is a crack point
     * @param iceSheet is 2d int array
     * @param row row index of the point to be check
     * @param col  col index of the point to be check
     * @return will show two value on true if it is crack point and fase if its not.
     */
    private static boolean crackpoint(int[][] iceSheet, int row, int col) {
        int rows = iceSheet.length;
        int cols = iceSheet[0].length;

        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                if (i == 0 && j == 0) continue;

                int newRow = row + i;
                int newCol = col + j;

                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
                    if (iceSheet[newRow][newCol] % 10 == 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}