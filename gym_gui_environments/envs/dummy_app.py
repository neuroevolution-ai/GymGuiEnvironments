import gym


class DummyApp(gym.Env):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode="human"):
        pass
