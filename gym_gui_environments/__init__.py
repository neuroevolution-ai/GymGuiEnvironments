from gym.envs.registration import register

register(
    id='DummyApp-v0',
    entry_point='gym_gui_environments.envs:DummyApp',
    timestep_limit=1000,
    reward_threshold=100.0,
    nondeterministic = True,
)
