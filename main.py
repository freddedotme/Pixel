import sys, pygame
from system import *
from player import *
from obstacle import *


def main():
    pygame.init()
    system = System
    player = Player(system)

    while 1:

        system.data_screen.fill(system.setting_white)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.jump()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()

        for e in pygame.event.get():

            if e.type == system.event_obstacle_spawn:
                obstacle = Obstacle(system)
                system.data_obstacles.append(obstacle)

            if e.type == system.event_difficulty:
                system.setting_difficulty += 1
                print(system.setting_difficulty)
                if system.setting_difficulty < 12:
                    system.setting_circle_radius -= 3
                    system.setting_velocity += 1
                    system.setting_gravity += 0.5
                    system.event_obstacle_spawn_time -= 100
                    pygame.time.set_timer(system.event_obstacle_spawn, system.event_obstacle_spawn_time)

            if e.type == pygame.QUIT:
                sys.exit()

        for obstacle in system.data_obstacles:
            if obstacle.has_collided(player): print("YOLO!")

        for obstacle in system.data_obstacles: obstacle.update()
        player.update()

        pygame.display.flip()
        system.data_clock.tick(system.setting_fps)


if __name__ == "__main__":
    main()
