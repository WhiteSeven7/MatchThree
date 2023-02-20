class Mover:
    def __init__(self, wall):
        self.wall = wall
        # 是否进行用户点击的移动，若是，阻止用户点击
        self.moving_stones = None
        # 若为真，执行exchange()函数
        self.need_exchange = False
        # 在两个stone发生exchange()后，打开
        self.check_stones = None
        # 防止反复打回的bug
        self.status = 'not_move'

    def set_moving(self, stone_1, stone_2, status, direction=None):
        """由用户和check_exchange()调用"""
        if direction is None:
            direction = stone_1.g_pos - stone_2.g_pos
        self.moving_stones = (stone_1, stone_2)
        stone_1.moving = -direction
        stone_2.moving = direction
        self.status = status

    def exchange(self):
        """进入标志: need_exchange，由stone.move()开启"""
        for stone in self.moving_stones:
            stone.move_recover()
            self.wall[stone.g_pos].contain(stone)
        self.need_exchange = False
        if self.status == 'swap':
            self.check_stones = self.moving_stones
        elif self.status == 'cancel':
            self.status = 'not_move'
        self.moving_stones = None

    def check_exchange(self):
        """进入标志: check_stones，由exchange()开启"""
        self.wall.get_three()
        if not self.wall.three_list:
            self.set_moving(self.check_stones[0], self.check_stones[1], 'cancel')
        else:
            self.status = 'not_move'
        self.check_stones = None

    # 让stone移动
    def stone_move(self):
        if self.moving_stones:
            for stone in self.moving_stones:
                if stone.moving is not None:
                    stone.move()
