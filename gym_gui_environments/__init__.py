from gym.envs.registration import register

register(
    id="PySideGUI-v0",
    entry_point="gym_gui_environments.pyside_gui_environments:GUIEnv"
)

register(
    id="PySideGUIRandomClick-v0",
    entry_point="gym_gui_environments.pyside_gui_environments:GUIEnvRandomClick"
)

register(
    id="PySideGUIRandomWidget-v0",
    entry_point="gym_gui_environments.pyside_gui_environments:GUIEnvRandomWidget"
)
