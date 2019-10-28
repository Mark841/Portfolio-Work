/* This class contains the methods needed to search on the internet and get the data into the GUI.
 * 
 * NOTE: This program returns the first search result on each site, this is because the first result 
 * is normally the most relevant. At a later date I could use an algorithm to make it more accurate 
 * and find the most suitable result, but for the time being it is sufficient. The Epic store for some 
 * reason sometimes works and sometimes doesn't work, I have been unable to figure out why this occurs.
 * 
 * NOTE: The origin website does not allow me to query it, as the HTML appears hidden and I cannot 
 * access the contents of the page. It also is laid out over 3 different pages to get the price of 
 * the game and is very difficult to try and get. The blizzard store cannot be searched online, it 
 * is only through the store application and therefore no results can be used.
 * 
 * Rockstar store functionality will be added at a later date.
 * 
 * Author: Mark Lumb 
 * 
 */

package StoreCombiner;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class onlineSearch {
	public static final String STEAM_SEARCH_URL = "https://store.steampowered.com/search/?term=";
	public static final String ORIGIN_SEARCH_URL = "https://www.origin.com/gbr/en-us/search?searchString=";
	public static final String UBISOFT_SEARCH_URL = "https://store.ubi.com/uk/search?q=";
	public static final String UBISOFT_SEARCH_END_URL = "&prefn1=productTypeRefinementString&prefv1=games";
	public static final String EPIC_SEARCH_URL = "https://www.epicgames.com/store/en-US/store-search?q=";
	//public static final String ROCKSTAR_SEARCH_URL = "";
	
	
	public String steamSearch(String searchTerm) {
		String name = "";
		String price = "";
		try {
			org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(STEAM_SEARCH_URL+searchTerm).get();
			if (doc.select("div#search_resultsRows").select("[data-price-final]").select(":containsOwn(£)").first().hasText()) {
				name = doc.select("div#search_resultsRows").select("span.title").first().ownText();
				price = doc.select("div#search_resultsRows").select("[data-price-final]").select(":containsOwn(£)").first().ownText();
				return ("Steam has " + name + " for " + price + "\n");
			}
			else {
				return "Steam does not have this game\n";
			}
		}
		catch (IOException e) {
			return "Steam does not have this game\n";
		}
		catch (NullPointerException e) {
			return "Steam does not have this game\n";
		}
	}
	/*public String originSearch(String searchTerm) {
		String name = "";
		try {
			org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(ORIGIN_SEARCH_URL+searchTerm).get();
			
			// The website does not allow me to query it, as the HTML appears hidden and I cannot access the contents of the page
			System.out.println(doc.select("div#origin-content").select("div#content"));
		}
		catch (IOException e) {
		}
		return "Origin does not have this game\n";
	}*/
	public String ubisoftSearch(String searchTerm) {
		String name ="";
		String price = "";
		try {
			org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(UBISOFT_SEARCH_URL + searchTerm + UBISOFT_SEARCH_END_URL).get();
			if (doc.select("div.grid-x").hasText()) {
				name = doc.select("div.product-title-wrapper").select("h1[class*=\"product-name\"]").first().ownText();
				price = doc.select("div[class*=\"product-price\"]").select("span[class*=\"price-sales\"]").first().ownText();
				return ("Ubisoft has " + name + " for " + price + "\n");
			}
			else {
				return "1	Ubisoft does not have this game\n";
			}
		}
		catch (IOException e) {
			try {
				org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(UBISOFT_SEARCH_URL + searchTerm + UBISOFT_SEARCH_END_URL).get();
				if (doc.select("div.card-details-wrapper").first().hasText()) {
					name = doc.select("div.card-title").select("h2.prod-title").first().ownText();
					price = doc.select("div.card-info").select("div.card-price").select("span[class*=\"price-sales\"]").first().ownText();
					return ("Ubisoft has " + name + " for " + price + "\n");
				}
				else {
					return "2	Ubisoft does not have this game\n";
				}
			}
			catch (IOException except) {
				return "3	Ubisoft does not have this game\n";
			}
			catch (NullPointerException np) {
				return "4	Ubisoft does not have this game\n";
			}
		}
		catch (NullPointerException e) {
			try {
				org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(UBISOFT_SEARCH_URL + searchTerm + UBISOFT_SEARCH_END_URL).get();
				if (doc.select("div.card-details-wrapper").first().hasText()) {
					name = doc.select("div.card-title").select("h2.prod-title").first().ownText();
					price = doc.select("div.card-info").select("div.card-price").select("span[class*=\"price-sales\"]").first().ownText();
					return ("Ubisoft has " + name + " for " + price + "\n");
				}
				else {
					return "5	Ubisoft does not have this game\n";
				}
			}
			catch (IOException except) {
				return "6	Ubisoft does not have this game\n";
			}
			catch (NullPointerException np) {
				return "7	Ubisoft does not have this game\n";
			}
		}
	}
	public String epicSearch(String searchTerm) {
		String name = "";
		String price = "";
		try {
			org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(EPIC_SEARCH_URL+searchTerm).get();
			if (doc.select("[href]:has(div)").select("span[class*=\"StoreCard-details_\"]").first().hasText()) {
				name = doc.select("[href]:has(div)").select("span[class*=\"StoreCard-details_\"]").select("h3[class*=\"StoreCard-title\"]").first().ownText();
				price = doc.select("[href]:has(div)").select("span[class*=\"StoreCard-price\"]").select("span[class=\"\"]").select(":containsOwn(£)").first().ownText();
				return ("Epic has " + name + " for " + price + "\n");
			}
			else {
				return "Epic does not have this game\n";
			}
		}
		catch (IOException e) {	
			return "Epic does not have this game\n";
		}
		catch (NullPointerException e) {
			return "Epic does not have this game\n";
		}
	}
	/*
	public String rockstarSearch(String searchTerm) {
		String price = "";
		try {
			org.jsoup.nodes.Document doc = org.jsoup.Jsoup.connect(ROCKSTAR_SEARCH_URL+searchTerm).get();
			if (doc.select("div#search_resultsRows").select("[data-price-final]").select(":containsOwn(£)").first().hasText()) {
				price = doc.select("div#search_resultsRows").select("[data-price-final]").select(":containsOwn(£)").first().ownText();
				return ("Rockstar has " + searchTerm + " for " + price + "\n");
			}
		}
		catch (IOException e) {
		}
		return "Rockstar does not have this game";
	}*/
}
