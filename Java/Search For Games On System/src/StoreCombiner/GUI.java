/* This class contains all information needed for the GUI of the program
 * 
 * Author: Mark Lumb 
 * 
 */

package StoreCombiner;

import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.JTextPane;

public class GUI {
	private Font FONT = new Font("Arial", Font.PLAIN, 15);
	private JFrame frame;
	private JFrame loadingFrame;
	private GamesLocator games;
	private StoreLocator stores;
	private txtFileManager file;
	
	public GUI(txtFileManager fileImport) {
		file = fileImport;
		init(file);
	}
	
	public void init(txtFileManager file) {
		games = new GamesLocator(file);
		stores = new StoreLocator(file);
		newStoreMenu();
	}
	
	private void newStoreMenu() {
		// Adds a title to the window
    	frame = new JFrame("Store Manager");
		final JPanel panel = new JPanel();
		panel.setLayout(new GridLayout(3,1,5,5));
    	
    	// Creates the buttons that will be placed in the window
    	JRadioButton newStores = new JRadioButton("Yes");
    	JRadioButton noNewStores = new JRadioButton("No");
    	newStores.setFont(FONT);
    	noNewStores.setFont(FONT);
		panel.add(newStores);
		panel.add(noNewStores);
		panel.setBorder(BorderFactory.createTitledBorder(BorderFactory.createEtchedBorder(), "New stores installed since last time:"));
        
        // Sets what each button will do, they will go to new windows and close the main menu window when they do that
        newStores.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        	    createLoadingWindow();
        		file.findStores();
        		file.updateTxtFile();
        		closeLoadingWindow();
        		init(file);
        		mainMenu();
        	}
        });
        noNewStores.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        		mainMenu();
        	}
        });
        
        // Makes the window visible to the user and sets values to their preferred sizes using .pack()
        frame.add(panel); 
        frame.pack();
        frame.setSize(300, 120);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        
        // Sets what happens if the close button is pressed
        frame.addWindowListener(new WindowAdapter() {
        	public void windowClosing(WindowEvent e) { System.exit(0); }
    	});
    }
	
	private void createLoadingWindow() {
		loadingFrame = new JFrame("Loading");
        JLabel labelLoading = new JLabel("Please wait while loading");
        labelLoading.setBounds(10,10,10,10);
        loadingFrame.add(labelLoading); 
        loadingFrame.setSize(200,100);
        loadingFrame.pack();
        frame.setLocationRelativeTo(null);
        loadingFrame.setVisible(true);
	}
	private void closeLoadingWindow() {
		loadingFrame.dispose();
	}
	
	private void mainMenu() {
		// Adds a title to the window
    	frame = new JFrame("Main Menu");
    	
    	// Creates the buttons that will be placed in the window
    	JButton list = new JButton("List games on system");
    	JButton stores = new JButton("Open stores");
    	JButton recent = new JButton("Open last played game: " + file.getLastPlayedGame());
    	JButton search = new JButton("Search for a game on stores");
    	search.setFont(FONT);
    	stores.setFont(FONT);
    	list.setFont(FONT);
    	recent.setFont(FONT);
        
    	// Sets the layout of the window and puts the buttons on it
        Container contentPane = frame.getContentPane();
        contentPane.setLayout(new GridBagLayout());
		GridBagConstraints constraints = new GridBagConstraints();
        constraints.gridx = 0;
        constraints.gridy = 0;
        constraints.gridwidth = 1;
        constraints.fill = (GridBagConstraints.HORIZONTAL/2);
        contentPane.add(list, constraints);
        constraints.gridx = 1;
        contentPane.add(recent, constraints);
        constraints.gridx = 0;
        constraints.gridy = 1;
        contentPane.add(stores, constraints);
        constraints.gridx = 1;
        contentPane.add(search, constraints);
        
        // Sets what each button will do, they will go to new windows and close the main menu window when they do that
        list.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        		sortGamesPage();
        	}
        });
        stores.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        		openStore();
        	}
        });
        recent.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        		lastPlayedGame();
        	}
        });
        search.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        		searchForGame();
        	}
        });
        
        // Makes the window visible to the user and sets values to their preferred sizes using .pack()
        frame.pack();
        frame.setSize(500, 300);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        
        // Sets what happens if the close button is pressed
        frame.addWindowListener(new WindowAdapter() {
        	public void windowClosing(WindowEvent e) { System.exit(0); }
    	});
    }
	
	private void sortGamesPage() {
		frame = new JFrame("All Games on System");
		final JPanel panel = new JPanel();
		// Sets the layout of the window
		panel.setLayout(new GridBagLayout());
		GridBagConstraints constraints = new GridBagConstraints();
		
		// Creates the buttons for how the games should be laid out in the text box
		JLabel labelDescription = new JLabel("How to sort games:");
		labelDescription.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 0;
        panel.add(labelDescription, constraints);
        
		JRadioButton sortA = new JRadioButton("By Drive");
		JRadioButton sortB = new JRadioButton("By Store");
		JRadioButton sortC = new JRadioButton("Alphabetical Order");
		sortA.setFont(FONT);
		sortB.setFont(FONT);
		sortC.setFont(FONT);
		ButtonGroup bgroup = new ButtonGroup();
		bgroup.add(sortA);
		bgroup.add(sortB);
		bgroup.add(sortC);
        constraints.gridy = 1;
        constraints.gridwidth = 1;
        panel.add(sortA, constraints);
        constraints.gridx = 1;
        panel.add(sortB, constraints);
        constraints.gridx = 2;
        panel.add(sortC, constraints);
		
        JLabel labelSearch = new JLabel("All Games on The System:");
        labelSearch.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 2;
        panel.add(labelSearch, constraints);

		// Is a text box that fills the page
		final JTextPane text = new JTextPane();
        text.setFont(FONT);
        
        // Makes the text box to have a scroll bar if it needs one, but only if it needs one
        final JScrollPane scrollPane = new JScrollPane(text);
        scrollPane.setPreferredSize(new Dimension(650, 600));

        constraints.gridx = 0;
        constraints.gridy = 3;
        constraints.gridwidth = 3;
        panel.add(scrollPane, constraints);
        text.setEditable(false);
        
        // Is the back to menu button
        JButton returnButton = new JButton("Back To Menu");
        returnButton.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 4;
        constraints.gridwidth = 2;
        panel.add(returnButton, constraints);
        
        // Is the open game button
        JButton openGame = new JButton("Open Game");
        openGame.setFont(FONT);
        constraints.gridx = 2;
        constraints.gridy = 4;
        panel.add(openGame, constraints);

        sortA.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		text.setText("");
        		text.setText(games.getGamesByDrive());
        	}
        });
        sortB.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		text.setText("");
        		text.setText(games.getGamesByStore());
        	}
        });
        sortC.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		text.setText(games.getGamesByAlphabet());
        	}
        });
        	
        returnButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		frame.dispose();
        		mainMenu();
        	}
        });
        openGame.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
            	if (text.getSelectedText() != null) {
            		String chosenGame = text.getSelectedText();
            		file.updateLastPlayed(chosenGame);
            		games.launchGame(chosenGame);
            	}
            }
        });

        // Makes the window visible to the user and sets values to their preferred sizes using .pack()
		text.setText("");
        frame.add(panel); 
        frame.pack();
        frame.setSize(700, 740);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
	}
		
	private void openStore() {
		// Adds a title to the window
		frame = new JFrame("Open a Game Store");
		final JPanel panel = new JPanel();
		// Sets the layout of the window
		panel.setLayout(new GridBagLayout());
		GridBagConstraints constraints = new GridBagConstraints();
        
        // Is the Steam button
        JButton steam = new JButton("Steam Store");
        steam.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 0;
        constraints.gridwidth = 1;
        panel.add(steam, constraints);
        // Is the Origin button
        JButton origin = new JButton("Origin Store");
        origin.setFont(FONT);
        constraints.gridx = 1;
        constraints.gridy = 0;
        panel.add(origin, constraints);
        // Is the UPlay button
        JButton uplay = new JButton("UPlay Store");
        uplay.setFont(FONT);
        constraints.gridx = 2;
        constraints.gridy = 0;
        panel.add(uplay, constraints);
        // Is the Epic button
        JButton epic = new JButton("Epic Store");
        epic.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 1;
        panel.add(epic, constraints);
        // Is the Blizzard button
        JButton blizzard = new JButton("Blizzard Store");
        blizzard.setFont(FONT);
        constraints.gridx = 1;
        constraints.gridy = 1;
        panel.add(blizzard, constraints);
        // Is the Rockstar button
        JButton rockstar = new JButton("Rockstar Store");
        rockstar.setFont(FONT);
        constraints.gridx = 2;
        constraints.gridy = 1;
        panel.add(rockstar, constraints);
        
        // Is the back to menu button
        JButton backToMenu = new JButton("Back To Menu");
        backToMenu.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 3;
        panel.add(backToMenu, constraints);
      
        // States what happens when the steam button is pressed
        steam.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		stores.openSteam();
        	}
        });
        // States what happens when the origin button is pressed
        origin.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		stores.openOrigin();
        	}
        });
        // States what happens when the uplay button is pressed
        uplay.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		stores.openUbisoft();
        	}
        });
        // States what happens when the epic button is pressed
        epic.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		stores.openEpic();
        	}
        });
        // States what happens when the blizzard button is pressed
        blizzard.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		stores.openBlizzard();
        	}
        });
        // States what happens when the blizzard button is pressed
        rockstar.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		stores.openRockstar();
        	}
        });
        // States what happens when the back to menu button is pressed
        backToMenu.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		// closes this window and calls the main menu method
        		frame.dispose();
        		mainMenu();
        	}
        });

        // Makes the window visible to the user and sets values to their preferred sizes using .pack()
        frame.add(panel);
        frame.pack();
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
	}

	private void lastPlayedGame() {
		games.launchGame(file.getLastPlayedGame());
	}
	
	private void searchForGame() {
		// Adds a title to the window
		frame = new JFrame("Search For a Game on a Store");
		final JPanel panel = new JPanel();
		// Sets the layout of the window
		panel.setLayout(new GridBagLayout());
		GridBagConstraints constraints = new GridBagConstraints();
		
		// Is a text box that goes across the top of the page
		final JTextPane text = new JTextPane();
        text.setFont(FONT);
        text.setText("Here you can search for a particular game on any stores");
        constraints.fill = GridBagConstraints.HORIZONTAL;
        constraints.gridx = 0;
        constraints.gridy = 0;
        constraints.gridwidth = 2;
        constraints.insets = new Insets(5, 5, 5, 5);
        panel.add(text, constraints);
        
        // Is a label saying "Surname: " only on the left side of the window
        JLabel labelSearch = new JLabel("Search for Game:");
        labelSearch.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 1;
        constraints.gridwidth = 1;
        panel.add(labelSearch, constraints);
        // Is the entry field to go with the corresponding label, so is placed on the right side of the label
        JTextField fieldSearch = new JTextField(20);
        fieldSearch.setFont(FONT);
        constraints.gridx = 1;
        constraints.gridy = 1;
        panel.add(fieldSearch, constraints);
        
        final JTextPane textResult = new JTextPane();
        textResult.setFont(FONT);
        textResult.setText("Here you can see your search. \nNOTE: Origin store won't show as its website is difficult to search for games on");

        // Makes the text box to have a scroll bar if it needs one, but only if it needs one
        final JScrollPane scrollPane = new JScrollPane(textResult);
        scrollPane.setPreferredSize(new Dimension(350, 300));
        
        constraints.gridx = 0;
        constraints.gridy = 2;
        constraints.gridwidth = 2;
        constraints.insets = new Insets(5, 5, 5, 5);
        panel.add(textResult, constraints);

        
        // Is the back to menu button
        JButton backToMenu = new JButton("Back To Menu");
        backToMenu.setFont(FONT);
        constraints.gridx = 0;
        constraints.gridy = 3;
        constraints.gridwidth = 1;
        panel.add(backToMenu, constraints);
        
        // Is the button to add a user to the directory
        JButton searchButton = new JButton("Search for Game");
        searchButton.setFont(FONT);
        constraints.gridx = 1;
        constraints.gridy = 3;
        panel.add(searchButton, constraints);
        
        // States what happens when the search button is pressed
        searchButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		// closes this window and calls the main menu method
        		String returnSearch = "";
        		onlineSearch search = new onlineSearch();
        		returnSearch = search.steamSearch(fieldSearch.getText());
        		//returnSearch += search.originSearch(fieldSearch.getText());
        		returnSearch += search.ubisoftSearch(fieldSearch.getText());
        		returnSearch += search.epicSearch(fieldSearch.getText());
        		//returnSearch += search.rockstarSearch(fieldSearch.getText());
        		textResult.setText(returnSearch);
        		
        	}
        });
        // States what happens when the back to menu button is pressed
        backToMenu.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent event) {
        		// closes this window and calls the main menu method
        		frame.dispose();
        		mainMenu();
        	}
        });
        
        // Makes the window visible to the user and sets values to their preferred sizes using .pack()
        frame.add(panel);
        frame.pack();
        frame.setSize(500, 300);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
	}	
}