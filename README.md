# Installation

Install directly from GitHub using `pip`:

```
pip install git+https://github.com/neuroevolution-ai/GymGuiEnvironments.git#egg=gym_gui_environments
```

# Usage

Import this package alongside `gym` and the environments are automatically registered and can be used with `gym.make`:

```python
import gym
import gym_gui_environments

env = gym.make("PySideGUI-v0")
env.reset()

# Alternative environment IDs: "PySideGUIRandomClick-v0", "PySideGUIRandomWidget-v0"
```

## Environment IDs

- `PySideGUI-v0`: Requires a tuple of integers as actions (x, y coordinates of a click)
- `PySideGUIRandomClick-v0`: Requires a boolean as action (which does nothing but is required because of the gym.Env
interface)
  - The environment clicks randomly in the SUT
- `PySideGUIRandomWidget-v0`, also requires a boolean as action
  - With a probability of 1/8, the environment does a random click in the SUT, while with a probability of 7/8 it
    selects a random widget in the SUT and clicks on a random position inside this widget
  - The probability of a random click can also be changed by setting `random_click_probability=PROB` in `gym.make`