/*
This file is the main game file contains the initialiser for the game and keeps it running

Author: Mark Lumb
*/

#include "Game.h"
#include "TextureManager.h"
#include "Map.h"
#include "ECS/Components.h"
#include "Vector2D.h"
#include "Collision.h"
#include "AssetManager.h"
#include <sstream>

Map* map;
Manager manager;

SDL_Renderer* Game::renderer = nullptr;
SDL_Event Game::event;

// Camera has default values 0,0 and then the same width as the screen of 800 and the height of 640
SDL_Rect Game::camera = { 0,0,6730,4670 };

AssetManager* Game::assets = new AssetManager(&manager);

bool Game::isRunning = false;

auto& player(manager.addEntity());
auto& label(manager.addEntity());

Game::Game() {
}

Game::~Game() {
}

void Game::init(const char* title, int xpos, int ypos, int width, int height, bool fullscreen) {

	int flags = 0;
	if (fullscreen) {
		flags = SDL_WINDOW_FULLSCREEN;
	}

	if (SDL_Init(SDL_INIT_EVERYTHING) == 0) {
		std::cout << "Subsystems Initialised!..." << std::endl;

		window = SDL_CreateWindow(title, xpos, ypos, width, height, flags);
		if (window) {
			std::cout << "Window Created!" << std::endl;
		}

		renderer = SDL_CreateRenderer(window, -1, 0);
		if (renderer) {
			SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
			std::cout << "Renderer Created!" << std::endl;
		}

		isRunning = true;
	}

	if (TTF_Init() == -1) {
		std::cout << "Error : SDL_TTF" << std::endl;
	}

	assets->AddTexture("terrain", "assets/terrain_texture.png");
	assets->AddTexture("player", "assets/player_anims.png");
	assets->AddTexture("projectile", "assets/projectile.png");
	assets->AddFont("arial", "assets/arial.ttf", 16);

	map = new Map("terrain", 3, 32);

	// ECS implementation 
	// The 30 and 20 is the amount of tiles that the map contains (map size)
	map->LoadMap("assets/map.map", 90, 60);

	player.addComponent<TransformComponent>(4);
	player.addComponent<SpriteComponent>("player", true);
	player.addComponent<KeyboardController>();
	player.addComponent<ColliderComponent>("player");
	player.addGroup(groupPlayers);

	SDL_Color white = { 255, 255, 255, 255 };
	label.addComponent<UILabel>(10, 10, "Test String", "arial", white);

	/*
	assets->CreateProjectile(Vector2D(300, 600), Vector2D(2, 0), 200, 2, "projectile");
	assets->CreateProjectile(Vector2D(250, 550), Vector2D(2, 0), 200, 2, "projectile");
	assets->CreateProjectile(Vector2D(200, 500), Vector2D(2, -1), 200, 2, "projectile");
	assets->CreateProjectile(Vector2D(150, 450), Vector2D(2, -1), 200, 2, "projectile");
	assets->CreateProjectile(Vector2D(100, 400), Vector2D(2, -2), 200, 2, "projectile");
	*/

}

auto& tiles(manager.getGroup(Game::groupMap));
auto& players(manager.getGroup(Game::groupPlayers));
auto& enemies(manager.getGroup(Game::groupEnemies));
auto& colliders(manager.getGroup(Game::groupColliders));
auto& projectiles(manager.getGroup(Game::groupProjectiles));

void Game::handleEvents() {
	
	SDL_PollEvent(&event);
	switch (event.type) {
	case SDL_QUIT:
		isRunning = false;
		break;
	default:
		break;
	}
}
void Game::update() {

	SDL_Rect playerCollider = player.getComponent<ColliderComponent>().collider;
	Vector2D playerPosition = player.getComponent<TransformComponent>().position;

	std::stringstream ss;
	ss << "Player position: " << playerPosition;
	label.getComponent<UILabel>().SetLabelText(ss.str(), "arial");

	manager.refresh();
	manager.update();

	for (auto& c : colliders) {
		SDL_Rect cCol = c->getComponent<ColliderComponent>().collider;
		if (Collision::AABB(cCol, playerCollider)) {
			// Pushes player back to previous position if they were walking into a collision point
			player.getComponent<TransformComponent>().position = playerPosition;
		}
	}

	for (auto& p : projectiles) {
		if (Collision::AABB(player.getComponent<ColliderComponent>().collider, p->getComponent<ColliderComponent>().collider)) {
			std::cout << "Player Hit" << std::endl;
			p->destroy();
		}
	}

	// Takes away half the screen to keep player central which is why the -400 and -320 are there
	camera.x = player.getComponent<TransformComponent>().position.x - 400;
	camera.y = player.getComponent<TransformComponent>().position.y - 320;

	// Checks bounds of the camera to not show tiles off screen (only shows the map)
	if (camera.x < 0) {
		camera.x = 0;
	}
	if (camera.y < 0) {
		camera.y = 0;
	}
	if (camera.x > camera.w) {
		camera.x = camera.w;
	}
	if (camera.y > camera.h) {
		camera.y = camera.h;
	}
}

void Game::render() {
	SDL_RenderClear(renderer);
	for (auto& t : tiles) {
		t->draw();
	}
	// To not show the collider yellow boxes
	for (auto& c : colliders) {
		c->draw();
	}
	//
	for (auto& p : players) {
		p->draw();
	}
	for (auto& p : projectiles) {
		p->draw();
	}
	for (auto& e : enemies) {
		e->draw();
	}

	label.draw();

	SDL_RenderPresent(renderer);
}
void Game::clean() {
	SDL_DestroyWindow(window);
	SDL_DestroyRenderer(renderer);
	SDL_Quit();
}