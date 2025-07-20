import pygame

class Entity:
    def __init__(self, x, y, width, height, color, sprite_sheet_path=None, frame_width=None, frame_height=None, frame_count=4):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.frames = []
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.3  # Slower animation
        self.facing_right = True
        if sprite_sheet_path and frame_width and frame_height:
            try:
                sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
                for i in range(frame_count):
                    frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
                    self.frames.append(pygame.transform.scale(frame, (self.width, self.height)))
            except pygame.error as e:
                print(f"Warning: Could not load {sprite_sheet_path}: {e}")

    def update(self, actions, delta_time):
        self.velocity_x = 0
        self.velocity_y = 0
        if actions.get('left'):
            self.velocity_x = -self.speed
            self.facing_right = False
        if actions.get('right'):
            self.velocity_x = self.speed
            self.facing_right = True
        if actions.get('up'):
            self.velocity_y = -self.speed
        if actions.get('down'):
            self.velocity_y = self.speed
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Animation
        if self.frames:
            self.animation_timer += delta_time
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames)

    def render(self, surface, camera_x, camera_y):
        if self.frames:
            frame = self.frames[self.current_frame]
            if not self.facing_right:
                frame = pygame.transform.flip(frame, True, False)
            surface.blit(frame, (self.x - camera_x, self.y - camera_y))
        else:
            pygame.draw.rect(surface, self.color, (self.x - camera_x, self.y - camera_y, self.width, self.height))