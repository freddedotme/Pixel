import pygame


class System:

    setting_width = 1280
    setting_height = 720
    setting_size = (setting_width, setting_height)
    setting_fps = 60
    setting_circle_radius = 50
    setting_gravity = 8
    setting_velocity = 20
    setting_white = (255, 255, 255)
    setting_obstacle_speed = 5
    setting_difficulty = 0

    data_screen = pygame.display.set_mode(setting_size)
    data_clock = pygame.time.Clock()
    data_obstacles = []

    asset_example = ""

    event_obstacle_spawn = pygame.USEREVENT + 1
    event_obstacle_spawn_time = 2000
    event_difficulty = pygame.USEREVENT + 2
    pygame.time.set_timer(event_obstacle_spawn, event_obstacle_spawn_time)
    pygame.time.set_timer(event_difficulty, 10000)