#pragma once
#include "ECS.h"
#include "../AssetManager.h"
#include "..//Game.h"
#include <SDL.h>
#include <SDL_ttf.h>
#include <string>

class UILabel : public Component {
private:
	SDL_Rect position;
	std::string labelText;
	std::string labelFont;
	SDL_Color textColour;
	SDL_Texture* labelTexture;

public:
	UILabel(int xPos, int yPos, std::string text, std::string font, SDL_Color& colour) : labelText(text), labelFont(font), textColour(colour) {
		position.x = xPos;
		position.y = yPos;

		SetLabelText(labelText, labelFont);
	}
	~UILabel() {}

	void SetLabelText(std::string text, std::string font) {
		SDL_Surface* surface = TTF_RenderText_Blended(Game::assets->GetFont(font), text.c_str(), textColour);
		labelTexture = SDL_CreateTextureFromSurface(Game::renderer, surface);
		SDL_FreeSurface(surface);

		SDL_QueryTexture(labelTexture, nullptr, nullptr, &position.w, &position.h);
	}
	void draw() override {
		SDL_RenderCopy(Game::renderer, labelTexture, nullptr, &position);
	}
};