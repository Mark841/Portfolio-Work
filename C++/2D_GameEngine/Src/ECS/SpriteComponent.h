#pragma once

#include "Components.h"
#include "SDL.h"
#include "..//TextureManager.h"
#include "Animation.h"
#include <map>
#include "../AssetManager.h"

class SpriteComponent : public Component {
public:

	int animIndex = 0;
	std::map<const char*, Animation> animations;
	SDL_RendererFlip spriteFlip = SDL_FLIP_NONE;

	SpriteComponent() = default;
	SpriteComponent(std::string id) {
		setTex(id);
	}
	SpriteComponent(std::string id, bool isAnimated) {
		animated = isAnimated;

		Animation idle = Animation(0, 3, 100);
		Animation walking = Animation(1, 8, 100);

		animations.emplace("Idle", idle);
		animations.emplace("Walking", walking);

		play("Idle");
		setTex(id);
	}

	~SpriteComponent() {
	}

	void setTex(std::string id) {
		texture = Game::assets->GetTexture(id);
	}

	void init() override {

		transform = &entity->getComponent<TransformComponent>();

		sourceRect.x = sourceRect.y = 0;
		sourceRect.w = transform->width;
		sourceRect.h = transform->height;
	}

	void update() override {

		if (animated) {
			sourceRect.x = sourceRect.w * static_cast<int>((SDL_GetTicks() / speed) % frames);
		}

		sourceRect.y = animIndex * transform->height;

		destinationRect.x = static_cast<int> (transform->position.x) - Game::camera.x;
		destinationRect.y = static_cast<int> (transform->position.y) - Game::camera.y;
		destinationRect.w = transform->width * transform->scale;
		destinationRect.h = transform->height * transform->scale;
	}

	void draw() override {
		TextureManager::Draw(texture, sourceRect, destinationRect, spriteFlip);
	}

	void play(const char* animName) {
		frames = animations[animName].frames;
		animIndex = animations[animName].index;
		speed = animations[animName].speed;
	}

private:
	TransformComponent* transform;
	SDL_Texture* texture;
	SDL_Rect sourceRect, destinationRect;

	bool animated = false;
	int frames = 0;
	// This speed is delay between frames in milliseconds
	int speed = 100;
};