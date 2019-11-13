/* This class contains the methods needed to read, write and create the text files needed for the 
 * program. It also contains methods that find the stores on the system if new ones have been added 
 * or for first time setup.
 * 
 * Author: Mark Lumb 
 * 
 */

package StoreCombiner;

import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class txtFileManager {
	private Boolean fileExists = false;
	private int driveAmount = 1;
	private String[] drives = new String[1];
	private int drivesPointer = 0;
	private int discAmount = 1;
	private int storeAmount = 5;
	private String location = "";
	// Layout of 2d arrays
	// [[STEAM],[ORIGIN],[UBISOFT],[EPIC],[ROCKSTAR],[BLIZZARD]]
	private String[][] folderLocations;
	private String[][] storeLocations;
	private Boolean[][] folderOnDrive;
	private Boolean[][] storeOnDrive;
	private int[] foldersOnDrive;
	private int[] storesOnDrive;
	private String[][] discLocations;
	private Boolean[][] discOnDrive;
	private String lastPlayed = "";
	
	public txtFileManager() {
		getAmountOfDrives();
		folderLocations = new String[driveAmount][storeAmount];
		folderOnDrive = new Boolean[driveAmount][storeAmount];
		storeLocations = new String[driveAmount][storeAmount];
		storeOnDrive = new Boolean[driveAmount][storeAmount];
		discLocations = new String[driveAmount][discAmount];
		discOnDrive = new Boolean[driveAmount][discAmount];
		storesOnDrive = new int[driveAmount];
		foldersOnDrive = new int[driveAmount];
		fillGenericOnDrive(storeOnDrive);
		fillGenericOnDrive(discOnDrive);
		fillGenericOnDrive(folderOnDrive);
		
		/*Boolean needToUpdate = checkIfNewStoreAdded();
		if (needToUpdate) {
			findStores();
			updateTxtFile();
		}
		else {
			loadTxtFile();
			if (!fileExists) {
				findStores();
				updateTxtFile();
			}
		}*/
		
		loadTxtFile();
		if (!fileExists) {
			findStores();
			updateTxtFile();
		}
	}
	
	/*public Boolean checkIfNewStoreAdded() {
		Boolean update = false;
		Scanner input = new Scanner(System.in);
		System.out.print("Have you installed a new store since last time (Y or N): ");
		String answer = input.next();
		if (answer.toLowerCase().equals("y") || answer.toLowerCase().equals("yes")) {
			update = true;
		}
		input.close();
		return update;
	}*/
	
	public void loadTxtFile() {
		try {
			FileReader file = new FileReader("C:\\GameStores\\storePaths.txt");
			Scanner source = new Scanner(file);
			source.useDelimiter(",");
			String store = "";
			for (int i=0; i<driveAmount; i++) {
				storesOnDrive[i] = Integer.parseInt(source.next().trim());
				for (int j=0; j<storesOnDrive[i]; j++) {
					store = source.next().trim();
					if (store.equals("Steam")) {
						storeLocations[i][0] = source.next().trim();
					}
					else if (store.equals("Origin")) {
						storeLocations[i][1] = source.next().trim();
					}
					else if (store.equals("Ubisoft")) {
						storeLocations[i][2] = source.next().trim();
					}
					else if (store.equals("Epic")) {
						storeLocations[i][3] = source.next().trim();
					}
					else if (store.equals("Blizzard")) {
						storeLocations[i][4] = source.next().trim();
					}
					else if (store.equals("Rockstar")) {
						storeLocations[i][5] = source.next().trim();
					}
				}
			}	
			
			String folder = "";
			for (int k=0; k<driveAmount; k++) {
				foldersOnDrive[k] = Integer.parseInt(source.next().trim());
				for (int j=0; j<foldersOnDrive[k]; j++) {
					folder = source.next().trim();
					if (folder.equals("Steam")) {
						folderLocations[k][0] = source.next().trim();
					}
					else if (folder.equals("Origin")) {
						folderLocations[k][1] = source.next().trim();
					}
					else if (folder.equals("Ubisoft")) {
						folderLocations[k][2] = source.next().trim();
					}
					else if (folder.equals("Epic")) {
						folderLocations[k][3] = source.next().trim();
					}
					else if (folder.equals("Blizzard")) {
						folderLocations[k][4] = source.next().trim();
					}
					else if (folder.equals("Rockstar")) {
						folderLocations[k][5] = source.next().trim();
					}
					else if (folder.equals("Disc")) {
						discLocations[k][0] = source.next().trim();
						discOnDrive[k][0] = true;
					}
				}
			}
			source.close();
			file.close();
						
			checkGenericFound(storeLocations, storeOnDrive);
			checkGenericFound(folderLocations, folderOnDrive);			
			fileExists = true;
		}
		catch (IOException e) {
			createTxtFile();
		}
	}
	public void checkGenericFound(String[][] array, Boolean[][] found) {
		int count1 = 0;
		int count2 = 0;
		for (String[] s: array) {
			for (String t: s) {
				if (t != null) {
					found[count1][count2] = true;
				}
				count2++;
			}
			count2 = 0;
			count1++;
		}
	}
	public void createTxtFile() {
		File folder = new File("C:\\GameStores"); 
		if (!folder.exists()) {
			folder.mkdir();
			System.out.println("FOLDER CREATED");
		}
		try {
			//FileOutputStream file = new FileOutputStream("C:\\GameStores\\storePaths.txt");
			//file.createNewFile();
			//file.close();
			String data = "Test data";
			Files.write(Paths.get("C:\\GameStores\\storePaths.txt"), data.getBytes());
			System.out.println("FILE CREATED");
		}
		catch (IOException f) {
			System.out.println("AN UNEXPECTED ERROR OCCURED");
		}
	}
	public void updateTxtFile() {
		try {
			FileWriter file = new FileWriter("C:\\GameStores\\storePaths.txt");
			// The folder locations for each store
			for (int i=0; i<driveAmount; i++) {
				file.write(storesOnDrive[i] + ",\n");				
				if (storeOnDrive[i][0]) {
					file.write("Steam," + storeLocations[i][0] + ",\n");
				}
				if (storeOnDrive[i][1]) {
					file.write("Origin," + storeLocations[i][1] + ",\n");
				}
				if (storeOnDrive[i][2]) {
					file.write("Ubisoft," + storeLocations[i][2] + ",\n");
				}
				if (storeOnDrive[i][3]) {
					file.write("Epic," + storeLocations[i][3] + ",\n");
				}
				if (storeOnDrive[i][4]) {
					file.write("Rockstar," + storeLocations[i][4] + ",\n");
				}
			}
			
			file.write("\n\n");
			// The folder locations for each library
			for (int j=0; j<driveAmount; j++) {
				if (discOnDrive[j][0]) {
					file.write((foldersOnDrive[j]+1) + ",\n");
				}
				else {
					file.write(foldersOnDrive[j] + ",\n");
				}
				if (folderOnDrive[j][0]) {
					file.write("Steam," + folderLocations[j][0] + ",\n");
				}
				if (folderOnDrive[j][1]) {
					file.write("Origin," + folderLocations[j][1] + ",\n");
				}
				if (folderOnDrive[j][2]) {
					file.write("Ubisoft," + folderLocations[j][2] + ",\n");
				}
				if (folderOnDrive[j][3]) {
					file.write("Epic," + folderLocations[j][3] + ",\n");
				}
				if (folderOnDrive[j][4]) {
					file.write("Rockstar," + folderLocations[j][4] + ",\n");
				}
				if (discOnDrive[j][0]) {
					file.write("Disc," + discLocations[j][0] + ",\n");
				}
			}
			file.close();
		}
		catch (IOException f) {
			System.out.println("An Unexpected Error Occured");
		}
	}
	
	public void loadLastPlayed() {
		try {
			FileReader file = new FileReader("C:\\GameStores\\lastPlayed.txt");
			Scanner source = new Scanner(file);
			lastPlayed = source.next();
			source.close();
			file.close();
		}
		catch (IOException e) {
			createLastPlayed();
		}
	}
	public void createLastPlayed() {
		try {
			String data = "Test data";
			Files.write(Paths.get("C:\\GameStores\\lastPlayed.txt"), data.getBytes());
			System.out.println("FILE CREATED");
		}
		catch (IOException f) {
			System.out.println("AN UNEXPECTED ERROR OCCURED");
		}
	}
	public void updateLastPlayed(String recentlyOpened) {
		try {
			FileWriter file = new FileWriter("C:\\GameStores\\lastPlayed.txt");
			file.write(recentlyOpened);
			file.close();
		}
		catch (IOException f) {
			System.out.println("AN UNEXPECTED ERROR OCCURED");
		}
	}
	
	public void getAmountOfDrives() {
		drivesPointer = 0;
		File[] paths = File.listRoots();
		for (File path: paths) {
			if (drivesPointer == driveAmount) {
				addAnotherDrive();
				driveAmount++;
			}
			drives[drivesPointer] = (path + "\\");
			drivesPointer++;
		}
	}
	public void addAnotherDrive() {
		String[] newDrives = new String[(drives.length+1)]; 
		int count = 0;
		// Replaces the existing entries in the drives
		for (String s: drives) {
			newDrives[count] = s;
			count ++;
		}
		drives = newDrives;
	}
	public Boolean[][] fillGenericOnDrive(Boolean[][] array) {
		int count1 = 0;
		int count2 = 0;
		for (Boolean[] b: array) {
			for (Boolean c: b) {
				array[count1][count2] = false;
				count2++;
			}
			count1++;
			count2=0;
		}
		return array;
	}
	
	public void findStores() {
		drivesPointer = 0;
		for (int i=0; i<driveAmount; i++) {
			steamStore(drives[i], drivesPointer);
			originStore(drives[i], drivesPointer);
			ubisoftStore(drives[i], drivesPointer);
			epicStore(drives[i], drivesPointer);
			//rockstarStore(drives[i], drivesPointer);
			disc(drives[i], drivesPointer);
			drivesPointer++;
		}
		int stores = 0;
		int count = 0;
		for (Boolean[] b: storeOnDrive) {
			for (Boolean c: b) {
				if (c) {
					stores++;
				}
			}
			storesOnDrive[count] = stores;
			stores = 0;
			count ++;
		}
		int folders = 0;
		count = 0;
		for (Boolean[] b: folderOnDrive) {
			for (Boolean c: b) {
				if (c) {
					folders++;
				}
			}
			foldersOnDrive[count] = folders;
			folders = 0;
			count ++;
		}
	}
	
	public void steamStore(String drive, int driveNumber) {
		findStore(drive, "Steam");
		findStore(drive, "SteamLibrary");
		if (!(location == "")) {
			folderLocations[driveNumber][0] = location;
			folderOnDrive[driveNumber][0] = true;
		}
		if (new File(location+"\\Steam.exe").exists()) {
			storeLocations[driveNumber][0] = location;
			storeOnDrive[driveNumber][0] = true;
		}
		location = "";
	}
	public void originStore(String drive, int driveNumber) {
		findStore(drive, "Origin");
		if (new File(location+"\\Origin.exe").exists()) {
			storeLocations[driveNumber][1] = location;
			storeOnDrive[driveNumber][1] = true;
		}
		else if (!(location == "")) {
			folderLocations[driveNumber][1] = location;
			folderOnDrive[driveNumber][1] = true;
		}
		location = "";
		findStore(drive, "Origin Games");
		if (!(location == "")) {
			folderLocations[driveNumber][1] = location;
			folderOnDrive[driveNumber][1] = true;
		}
		location = "";
	}
	public void ubisoftStore(String drive, int driveNumber) {
		findStore(drive, "Ubisoft");
		if (!(location == "")) {
			folderLocations[driveNumber][2] = location;
			folderOnDrive[driveNumber][2] = true;
		}
		if (new File(location+"\\Ubisoft Game Launcher\\UbisoftGameLauncher.exe").exists()) {
			storeLocations[driveNumber][2] = location+"\\Ubisoft Game Launcher";
			storeOnDrive[driveNumber][2] = true;
		}	
		location = "";
		/*findStore(drive, "Uplay Games");
		if (!(location == "")) {
			folderLocations[driveNumber][2] = location;
			folderOnDrive[driveNumber][2] = true;
		}
		location = "";*/
	}
	public void epicStore(String drive, int driveNumber) {
		findStore(drive, "Epic Games");
		if (!(location == "")) {
			folderLocations[driveNumber][3] = location;
			folderOnDrive[driveNumber][3] = true;
		}
		if (new File(location+"\\Launcher\\Engine\\Binaries\\Win64\\EpicGamesLauncher.exe").exists()) {
			storeLocations[driveNumber][3] = location+"\\Launcher\\Engine\\Binaries\\Win64";
			storeOnDrive[driveNumber][3] = true;
		}
		location = "";
	}
	public void disc(String drive, int driveNumber) {
		findStore(drive, "Disc Games");
		if (location.equals("")) {
			return;
		}
		discLocations[driveNumber][0] = location;
		discOnDrive[driveNumber][0] = true;
		location = "";
	}
	
	public void findStore(String loc, String store) {
		// Creates a list to hold all sub folders
		ArrayList<String> subFolders = new ArrayList<>();
		File folder = new File(loc);
		File[] files = folder.listFiles();
		// For each file in the folder
		if (files == null) {
			return;
		}
		for (File file: files) {
			// Checks if it is a folder
			if (file.isDirectory()) {
				// Checks if windows
				if (file.getName().equals("Windows")) {
					continue;
				}
				// Checks if program files
				if (file.getName().equals("ProgramData")) {
					continue;
				}
				// Checks if users
				if (file.getName().equals("Users")) {
					continue;
				}
				// Checks if recycle bin
				if (file.getName().equals("$Recycle.Bin")) {
					continue;
				}
				// Checks if the store was found
				if (file.getName().equals(store)) {
					location = loc + "\\" + file.getName();
					return;
				}
				// Adds each sub folder to a list
				subFolders.add(loc+"\\"+file.getName());
			}
		}
		// For each sub folder
		for (String sF: subFolders) {
			// Call the function again
			findStore(sF, store);
		}
		return;
	}

	public int getDriveAmount() {
		return driveAmount;
	}
	public String[] getDrives() {
		return drives;
	}
	public String[][] getStoreLocations() {
		return storeLocations;
	}
	public Boolean[][] getStoreOnDrive() {
		return storeOnDrive;
	}
	public String[][] getFolderLocations() {
		return folderLocations;
	}
	public Boolean[][] getFolderOnDrive() {
		return folderOnDrive;
	}
	public String[][] getDiscLocations() {
		return discLocations;
	}
	public Boolean[][] getDiscOnDrive() {
		return discOnDrive;
	}
	public LinkedList<String>[] getGameNames() {
		LinkedList<String> gameNames[] = new LinkedList[driveAmount];
		return gameNames;
	}
	public LinkedList<String>[] getGameLocations() {
		LinkedList<String> gameLocations[] = new LinkedList[driveAmount];
		return gameLocations;
	}
	public String getLastPlayedGame() {
		loadLastPlayed();
		return lastPlayed;
	}
}
