#pragma once

#include "ECS.h"
#include "SDL.h"
#include "../Vector2D.h"
#include "../Game.h"
#include "../TextureManager.h"

class TileComponent : public Component {
	
public:

	SDL_Texture* texture;
	SDL_Rect srcRect, destRect;
	// This keeps track of where the tiles actually are and not where they're being drawn
	Vector2D position;

	TileComponent() = default;

	~TileComponent() {
		SDL_DestroyTexture(texture);
	}

	TileComponent(int srcX, int srcY, int xPos, int yPos, int tileSize, int tileScale, std::string id) {
		texture = Game::assets->GetTexture(id);


		srcRect.x = srcX;
		srcRect.y = srcY;
		srcRect.w = srcRect.h = tileSize;
		position.x = static_cast<float>(xPos);
		position.y = static_cast<float>(yPos);
		destRect.w = destRect.h = tileSize * tileScale;
	}

	void update() override {
		destRect.x = static_cast<int>(position.x - Game::camera.x);
		destRect.y = static_cast<int>(position.y - Game::camera.y);
	}

	void draw() override {
		TextureManager::Draw(texture, srcRect, destRect, SDL_FLIP_NONE);
	}
};