/* This class gets all information about the games on the system
 * 
 * Author: Mark Lumb 
 * 
 */

package StoreCombiner;

import java.io.*;
import java.util.*;

public class GamesLocator {
	private String[] games = new String[20];
	private int gamesPointer= 0;
	private int DRIVE_AMOUNT = 1;
	private LinkedList<String> gameNames[];
	private LinkedList<String> gameLocations[];
	private String[] drives;
	private String[][] folderLocations;
	private Boolean[][] folderOnDrive;
	private String[][] discLocations;
	private Boolean[][] discOnDrive;
	private String table = "";
	private String sortedAlphabet = "";

	public GamesLocator(txtFileManager fileImport) {		
		txtFileManager file = fileImport;
		DRIVE_AMOUNT = file.getDriveAmount();
		drives = file.getDrives();
		folderLocations = file.getFolderLocations();
		folderOnDrive = file.getFolderOnDrive();
		discLocations = file.getDiscLocations();
		discOnDrive = file.getDiscOnDrive();	
		// These must be imported from the txtFileManager class as they need to know the drive amount to create the 2d linked list and making 
		// them in the constructor only made them locally but they are needed to be fields for the class to use
		gameNames = file.getGameNames();
		gameLocations = file.getGameLocations();
		
		for (int i=0; i<DRIVE_AMOUNT; i++) {
			gameNames[i] = new LinkedList<String>();
			gameLocations[i] = new LinkedList<String>();
		}
	}
		
	public void expandArray() {
		String[] newGames = new String[(games.length+1)]; 
		int count = 0;
		// Replaces the existing entries in the games
		for (String s: games) {
			newGames[count] = s;
			count ++;
		}
		games = newGames;
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
	
	public String getGamesByDrive() {
		table = "";
		int driveSearch = 0;
		for (String drive: drives) {
			table += drive.charAt(0) + " Drive:\n";
			if (folderOnDrive[driveSearch][0]) {
				steam(driveSearch);
			}
			if (folderOnDrive[driveSearch][1]) {
				origin(driveSearch);
			}
			if (folderOnDrive[driveSearch][2]) {
				ubisoft(driveSearch);
			}
			if (folderOnDrive[driveSearch][3]) {
				epic(driveSearch);
			}
			/*if (folderOnDrive[driveSearch][4]) {
				rockstar(drive, driveSearch);
			}
			if (folderOnDrive[driveSearch][5]) {
				blizzard(drive, driveSearch);
			}*/
			if (discOnDrive[driveSearch][0]) {
				disc(driveSearch);
			}
			//windows(drive, driveSearch);
			driveSearch++;
			table += "\n";
		}
		return table;
	}
	public String getGamesByStore() {
		table = "";
		Boolean outputName = false;
		int driveSearch = 0;
		for (String drive: drives) {
			if (folderOnDrive[driveSearch][0]) {
				if (!outputName) {
					table += "Steam:\n";
					outputName = true;
				}
				steam(driveSearch);
			}
			driveSearch++;
		}

		table += "\n";
		outputName = false;
		driveSearch = 0;
		for (String drive: drives) {
			if (folderOnDrive[driveSearch][1]) {
				if (!outputName) {
					table += "Origin:\n";
					outputName = true;
				}
				origin(driveSearch);
			}
			driveSearch++;
		}

		table += "\n";
		outputName = false;
		driveSearch = 0;
		for (String drive: drives) {
			if (folderOnDrive[driveSearch][2]) {
				if (!outputName) {
					table += "Ubisoft:\n";
					outputName = true;
				}
				ubisoft(driveSearch);
			}
			driveSearch++;
		}

		table += "\n";
		outputName = false;
		driveSearch = 0;
		for (String drive: drives) {
			if (folderOnDrive[driveSearch][3]) {
				if (!outputName) {
					table += "Epic:\n";
					outputName = true;
				}
				epic(driveSearch);
			}
			driveSearch++;
		}

		table += "\n";
		outputName = false;
		driveSearch = 0;
		for (String drive: drives) {
			if (discOnDrive[driveSearch][0]) {
				if (!outputName) {
					table += "Disc:\n";
					outputName = true;
				}
				disc(driveSearch);
			}
			driveSearch++;
		}
		return table;
	}
	public String getGamesByAlphabet() {
		if (sortedAlphabet.equals("")) {
			if (games[0] == null) {
				getGamesByDrive();	
			}	
			Arrays.sort(games);
			for (String game: games) {
				sortedAlphabet += game + "\n";
			}
		}
		return sortedAlphabet;
	}

	public void steam(int driveSearch) {
		String location = folderLocations[driveSearch][0];
		location += "\\steamapps\\common";
		File folder = new File(location);
		File[] listOfFiles = folder.listFiles();		
		if ((listOfFiles == null) || (listOfFiles.length==0)) {
			return;
		}
		ListIterator<String> iteratorName;
		ListIterator<String> iteratorLoc;
		for (int i = 0; i < listOfFiles.length; i++) {
			iteratorName = gameNames[driveSearch].listIterator();
			iteratorLoc = gameLocations[driveSearch].listIterator();
			if (listOfFiles[i].isDirectory()) {
				if (listOfFiles[i].getName().equals("Steamworks Shared")) {
					continue;
				}
				if (gamesPointer == games.length) {
					expandArray();
				}
				if (listOfFiles[i].getName().equals("insurgency2")) {
					games[gamesPointer] = "Insurgency";
					table += "Insurgency" + "\n";
				}
				else {
					games[gamesPointer] = listOfFiles[i].getName();
					table += listOfFiles[i].getName() + "\n";
				}
				gamesPointer++;
				while (iteratorName.hasNext()) {
					iteratorName.next();
					iteratorLoc.next();
				}
				iteratorName.add(listOfFiles[i].getName());
				iteratorLoc.add(location + "\\" + listOfFiles[i].getName());
			}
		}
	}
	public void origin(int driveSearch) {
		String location = folderLocations[driveSearch][1];
		File folder = new File(location);
		File[] listOfFiles = folder.listFiles();
		if ((listOfFiles == null) || (listOfFiles.length==0)) {
			return;
		}
		ListIterator<String> iteratorName;
		ListIterator<String> iteratorLoc;
		for (int i = 0; i < listOfFiles.length; i++) {
			iteratorName = gameNames[driveSearch].listIterator();
			iteratorLoc = gameLocations[driveSearch].listIterator();
			if (listOfFiles[i].isDirectory()) {
				table += listOfFiles[i].getName() + "\n";
				if (gamesPointer == games.length) {
					expandArray();
				}
				games[gamesPointer] = listOfFiles[i].getName();
				gamesPointer++;
				while (iteratorName.hasNext()) {
					iteratorName.next();
					iteratorLoc.next();
				}
				iteratorName.add(listOfFiles[i].getName());
				iteratorLoc.add(location + "\\" + listOfFiles[i].getName());
			}
		}
	}
	public void ubisoft(int driveSearch) {
		String location = folderLocations[driveSearch][2];
		location += "\\Ubisoft Game Launcher\\games";
		File folder = new File(location);
		File[] listOfFiles = folder.listFiles();
		if ((listOfFiles == null) || (listOfFiles.length==0)) {
			return;
		}
		ListIterator<String> iteratorName;
		ListIterator<String> iteratorLoc;
		for (int i = 0; i < listOfFiles.length; i++) {
			iteratorName = gameNames[driveSearch].listIterator();
			iteratorLoc = gameLocations[driveSearch].listIterator();
			if (listOfFiles[i].isDirectory()) {
				table += listOfFiles[i].getName() + "\n";
				if (gamesPointer == games.length) {
					expandArray();
				}
				games[gamesPointer] = listOfFiles[i].getName();
				gamesPointer++;
				while (iteratorName.hasNext()) {
					iteratorName.next();
					iteratorLoc.next();
				}
				iteratorName.add(listOfFiles[i].getName());
				iteratorLoc.add(location + "\\" + listOfFiles[i].getName());
			}
		}
	}
	public void epic(int driveSearch) {
		String location = folderLocations[driveSearch][3];
		File folder = new File(location);
		File[] listOfFiles = folder.listFiles();
		if ((listOfFiles == null) || (listOfFiles.length==0)) {
			return;
		}
		ListIterator<String> iteratorName;
		ListIterator<String> iteratorLoc;
		for (int i = 0; i < listOfFiles.length; i++) {
			iteratorName = gameNames[driveSearch].listIterator();
			iteratorLoc = gameLocations[driveSearch].listIterator();
			if (listOfFiles[i].getName().equals("DirectXRedist")) {
				continue;
			}
			if (listOfFiles[i].getName().equals("Launcher")) {
				continue;
			}
			if (listOfFiles[i].isDirectory()) {
				table += listOfFiles[i].getName() + "\n";
				if (gamesPointer == games.length) {
					expandArray();
				}
				games[gamesPointer] = listOfFiles[i].getName();
				gamesPointer++;
				while (iteratorName.hasNext()) {
					iteratorName.next();
					iteratorLoc.next();
				}
				iteratorName.add(listOfFiles[i].getName());
				iteratorLoc.add(location + "\\" + listOfFiles[i].getName());
			}
		}
	}
	public void disc(int driveSearch) {
		String location = discLocations[driveSearch][0];
		File folder = new File(location);
		File[] listOfFiles = folder.listFiles();
		if ((listOfFiles == null) || (listOfFiles.length==0)) {
			return;
		}
		ListIterator<String> iteratorName;
		ListIterator<String> iteratorLoc;
		
		for (int i = 0; i < listOfFiles.length; i++) {
			iteratorName = gameNames[driveSearch].listIterator();
			iteratorLoc = gameLocations[driveSearch].listIterator();
			if (listOfFiles[i].isDirectory()) {
				table += listOfFiles[i].getName() + "\n";
				if (gamesPointer == games.length) {
					expandArray();
				}
				games[gamesPointer] = listOfFiles[i].getName();
				gamesPointer++;
				while (iteratorName.hasNext()) {
					iteratorName.next();
					iteratorLoc.next();
				}
				iteratorName.add(listOfFiles[i].getName());
				iteratorLoc.add(location + "\\" + listOfFiles[i].getName());
			}
		}
	}	
		
	public void launchGame(String game) {
		if (game.equals("Insurgency")) {
			game = "insurgency2";
		}
		System.out.println("Selected Game: " + game);
		int gameIndex = 0;
		ListIterator<String> iteratorName;
		ListIterator<String> iteratorLoc;
		for (int i=0; i<DRIVE_AMOUNT; i++) {
			iteratorName = gameNames[i].listIterator();
			iteratorLoc = gameLocations[i].listIterator();
			while (iteratorName.hasNext()) {
				String name = iteratorName.next();
				// Checks if the game is found or not
				if (name.equals(game)) {
					for (int x=0; x<gameIndex; x++) {
						iteratorLoc.next();
					}
					String dir = iteratorLoc.next();
					File folder = new File(dir);
					File[] listOfFiles = folder.listFiles();					
					for (int z=0; z<listOfFiles.length; z++) {
						if (listOfFiles[z].getName().endsWith((".exe"))) {
							try {
								Runtime.getRuntime().exec((dir+"\\"+game), null, folder);
								System.out.println("RUNNING GAME");
							}
							catch (IOException e) {
								try {
									Runtime.getRuntime().exec((dir+"\\"+listOfFiles[z].getName()), null, folder);
									System.out.println("RUNNING GAME");
								}
								catch (IOException f) {
									System.out.println("ERROR");
								}
							}
						}
					}
				}
				gameIndex++;
			}
			gameIndex = 0;
		}
		System.out.println("NO .exe FILE WAS FOUND");
	}
}