from global_vars import WIN_WIDTH, WIN_HEIGHT

def percent(percentage):
    return percentage / 100 * WIN_WIDTH

def item_on_screen(coordinates, dimensions):
    if(
        coordinates[0] > 0 - dimensions[0] and # has entered via left of window
        coordinates[0] < WIN_WIDTH and # has not left via right of window
        coordinates[1] > 0 - dimensions[1] and # has entered via top of window
        coordinates[1] < WIN_HEIGHT # had not left via bottom of window
    ):
        return True
    else:
        return False