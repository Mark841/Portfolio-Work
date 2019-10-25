/*
This file is the map file which contains the items needed to load and draw the map onto the screen

Author: Mark Lumb
*/

#include "Map.h"
#include "Game.h"
#include <fstream>
#include "ECS/ECS.h"
#include "ECS/Components.h"

extern Manager manager;

Map::Map(std::string tID, int mScale, int tSize) : texID(tID), mapScale(mScale), tileSize(tSize) {
	scaledSize = (mScale * tSize);
}

Map::~Map() {
}

void Map::LoadMap(std::string path, int sizeX, int sizeY) {
	char c;
	std::fstream mapFile;
	mapFile.open(path);

	int srcX, srcY;

	// Code to parse the file
	for (int y = 0; y < sizeY; y++) {
		for (int x = 0; x < sizeX; x++) {
			mapFile.get(c);
			srcY = atoi(&c) * tileSize;
			mapFile.get(c);
			srcX = atoi(&c) * tileSize;
			AddTile(srcX, srcY, x * scaledSize, y * scaledSize);
			mapFile.ignore();
		}
	}

	// Ignores the blank line
	mapFile.ignore();
	for (int y = 0; y < sizeY; y ++) {
		for (int x = 0; x < sizeX; x++) {
			mapFile.get(c);
			if (c == '1') {
				auto& tcol(manager.addEntity());
				tcol.addComponent<ColliderComponent>("terrain", x * scaledSize, y * scaledSize, scaledSize);
				tcol.addGroup(Game::groupColliders);
			}
			mapFile.ignore();
		}
	}

	mapFile.close();
}

void Map::AddTile(int srcX, int srcY, int xPos, int yPos) {

	auto& tile(manager.addEntity());
	tile.addComponent<TileComponent>(srcX, srcY, xPos, yPos, tileSize, mapScale, texID);
	tile.addGroup(Game::groupMap);
}
