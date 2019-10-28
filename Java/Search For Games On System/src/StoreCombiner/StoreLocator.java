/* This class contains all information about what stores and their locations are on the system.
 * It also contains the methods to open these stores.
 * 
 * Author: Mark Lumb 
 * 
 */

package StoreCombiner;

import java.io.*;

public class StoreLocator {
	private Boolean[][] storeOnDrive;
	private String[][] storeLocations;

	public StoreLocator(txtFileManager fileImport) {
		txtFileManager file = fileImport;
		storeOnDrive = file.getStoreOnDrive();
		storeLocations = file.getStoreLocations();
	}
	
	public void openSteam() {		
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			if (b[0]) {
				try {
					System.out.println("ATTEMPTING TO OPEN");
					File folder = new File(storeLocations[count][0]);
					Runtime.getRuntime().exec((storeLocations[count][0]+"\\Steam.exe"), null, folder);
				}
				catch (IOException e) {
					System.out.println("ERROR OPENING STORE");
				}
			}
			count++;
		}
	}
	public void openOrigin() {
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			if (b[1]) {
				try {
					System.out.println("ATTEMPTING TO OPEN");
					File folder = new File(storeLocations[count][1]);
					Runtime.getRuntime().exec((storeLocations[count][1]+"\\Origin.exe"), null, folder);
				}
				catch (IOException e) {
					System.out.println("ERROR OPENING STORE");
				}
			}
			count++;
		}
	}
	public void openUbisoft() {
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			if (b[2]) {
				try {
					System.out.println("ATTEMPTING TO OPEN");
					File folder = new File(storeLocations[count][2]);
					Runtime.getRuntime().exec((storeLocations[count][2]+"\\UbisoftGameLauncher.exe"), null, folder);
				}
				catch (IOException e) {
					System.out.println("ERROR OPENING STORE");
				}
			}
			count++;
		}
	}
	public void openEpic() {
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			if (b[3]) {
				try {
					System.out.println("ATTEMPTING TO OPEN");
					File folder = new File(storeLocations[count][3]);
					Runtime.getRuntime().exec((storeLocations[count][3]+"\\EpicGamesLauncher.exe"), null, folder);
				}
				catch (IOException e) {
					System.out.println("ERROR OPENING STORE");
				}
			}
			count++;
		}
	}
	

	public void openBlizzard() {
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			if (b[3]) {
				try {
					System.out.println("ATTEMPTING TO OPEN");
					File folder = new File(storeLocations[count][4]);
					Runtime.getRuntime().exec((storeLocations[count][4]+"\\Battle.net Launcher.exe"), null, folder);
				}
				catch (IOException e) {
					System.out.println("ERROR OPENING STORE");
				}
			}
			count++;
		}
	}
	public void openRockstar() {
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			if (b[3]) {
				try {
					System.out.println("ATTEMPTING TO OPEN");
					File folder = new File(storeLocations[count][5]);
					Runtime.getRuntime().exec((storeLocations[count][5]), null, folder);
				}
				catch (IOException e) {
					System.out.println("ERROR OPENING STORE");
				}
			}
			count++;
		}
	}
}
