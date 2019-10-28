/* This file is the main file that runs the project
 * 
 * NOTE: For the program to work, the jsoup library must have a path built to it
 * 
 * Author: Mark Lumb 
 * 
 */

package StoreCombiner;

public class Main {
	public static void main(String[] args) {	
		txtFileManager file = new txtFileManager();
		new GUI(file);
	}
}