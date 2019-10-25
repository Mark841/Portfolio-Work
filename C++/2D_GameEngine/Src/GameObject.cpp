/*
This file is the game object file which holds the class containing the elements of players and individuals in the game

Author: Mark Lumb
*/

#include "GameObject.h"
#include "TextureManager.h"

// This will scale the images on the screen
int scalar = 2;

GameObject::GameObject(const char* textureSheet, int x, int y) {
	// Calls the TextureManager class to load the players texture
	objTexture = TextureManager::LoadTexture(textureSheet);

	xpos = x;
	ypos = y;
}

void GameObject::Update() {
	xpos++;
	ypos++;

	sourceRectangle.h = 32;
	sourceRectangle.w = 32;
	sourceRectangle.x = 0;
	sourceRectangle.y = 0;

	destinationRectangle.x = xpos;
	destinationRectangle.y = ypos;
	destinationRectangle.w = sourceRectangle.w * scalar;
	destinationRectangle.h = sourceRectangle.h * scalar;
}

void GameObject::Render() {
	SDL_RenderCopy(Game::renderer, objTexture, &sourceRectangle, &destinationRectangle);
}