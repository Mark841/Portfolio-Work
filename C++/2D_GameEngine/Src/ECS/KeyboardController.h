#pragma once

#include "..//Game.h"
#include "ECS.h"
#include "Components.h"

class KeyboardController : public Component {

private:

public:
	TransformComponent *transform;
	SpriteComponent* sprite;

	void init() override {
		transform = &entity->getComponent<TransformComponent>();
		sprite = &entity->getComponent<SpriteComponent>();
	}

	void update() override {
		// On key press
		if (Game::event.type == SDL_KEYDOWN) {
			switch (Game::event.key.keysym.sym) {
				// W
			case SDLK_w:
				transform->velocity.y = -1;
				sprite->play("Walking");
				break;
				// A
			case SDLK_a:
				transform->velocity.x = -1;
				sprite->play("Walking");
				sprite->spriteFlip = SDL_FLIP_HORIZONTAL;
				break;
				// S
			case SDLK_s:
				transform->velocity.y = 1;
				sprite->play("Walking");
				break;
				// D
			case SDLK_d:
				transform->velocity.x = 1;
				sprite->play("Walking");
				break;
			default:
				break;
			}
		}
		// On key release
		if (Game::event.type == SDL_KEYUP) {
			switch (Game::event.key.keysym.sym) {
				// W
			case SDLK_w:
				transform->velocity.y = 0;
				sprite->play("Idle");
				break;
				// A
			case SDLK_a:
				transform->velocity.x = 0;
				sprite->play("Idle");
				sprite->spriteFlip = SDL_FLIP_NONE;
				break;
				// S
			case SDLK_s:
				transform->velocity.y = 0;
				sprite->play("Idle");
				break;
				// D
			case SDLK_d:
				transform->velocity.x = 0;
				sprite->play("Idle");
				break;
			case SDLK_ESCAPE:
				Game::isRunning = false;
			default:
				break;
			}
		}
	}
};