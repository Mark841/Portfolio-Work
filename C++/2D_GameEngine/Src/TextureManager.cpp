/*
This file is the file which holds information on how to load and draw the textures for everything to the screen

Author: Mark Lumb
*/

#include "TextureManager.h"

SDL_Texture* TextureManager::LoadTexture(const char* filename) {
	SDL_Surface* tempSurface = IMG_Load(filename);
	SDL_Texture* texture = SDL_CreateTextureFromSurface(Game::renderer, tempSurface);
	SDL_FreeSurface(tempSurface);

	return texture;
}

void TextureManager::Draw(SDL_Texture* tex, SDL_Rect src, SDL_Rect dest, SDL_RendererFlip flip) {
	SDL_RenderCopyEx(Game::renderer, tex, &src, &dest, NULL, NULL, flip);
}
