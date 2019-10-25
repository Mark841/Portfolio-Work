#pragma once

#include "ECS.h"
#include "Components.h"

class ProjectileComponent : public Component {
private:
	TransformComponent* transform;
	int range = 0;
	int speed = 0;
	int distance = 0;

public:
	ProjectileComponent(int rng, int spd) : range(rng), speed(spd) {}
	~ProjectileComponent();

	void init() override {
		transform = &entity->getComponent<TransformComponent>();
	}
	void update() override {
		distance += speed;
		if (distance > range) {
			entity->destroy();
		}
		else if (transform->position.x > Game::camera.x + Game::camera.w || 
			transform->position.x < Game::camera.x || 
			transform->position.y > Game::camera.y + Game::camera.h ||
			transform->position.y < Game::camera.y) {
			entity->destroy();
		}
	}
};