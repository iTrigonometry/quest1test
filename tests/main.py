import sys
sys.path.insert(0, sys.path[0][0:-5])
from characters import player as p, enemy as e # noqa


player = p.Player()
if __name__ == '__main__':
    player.set_name('zalupa')
    print(player.get_name())
