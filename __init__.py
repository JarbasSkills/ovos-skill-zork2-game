from pyfrotz.ovos import FrotzSkill


class Zork2Skill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="zork_2",
                         game_lang="en-us",
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         **kwargs)
