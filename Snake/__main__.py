import constants 

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake())
    cast.add_actor("scores", Score())
  
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService(caption='Snake', width=900, height=600, cell_size=15, frame_rate=15)

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()