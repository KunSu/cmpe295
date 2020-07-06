import lgsvl
import os
import simulation.config as config

cf = config.Config()
sim = cf.Simulator()
cf.LoadOrResetScene(sim, "BorregasAve")

spawns = sim.get_spawn()

state = lgsvl.AgentState()
state.transform = spawns[0]

forward = lgsvl.utils.transform_to_forward(spawns[0])

# Agents can be spawned with a velocity. Default is to spawn with 0 velocity
state.velocity = 20 * forward
ego = sim.add_agent("Lincoln2017MKZ (Apollo 5.0)", lgsvl.AgentType.EGO, state)

ego.connect_bridge(os.environ.get("BRIDGE_HOST", "127.0.0.1"), 9090)
print("!!!Testing!!! ego.bridge_connected:", ego.bridge_connected)


# The bounding box of an agent are 2 points (min and max) such that the box formed from those 2 points completely encases the agent
# print("Vehicle bounding box =", ego.bounding_box)

# print("Current time = ", sim.current_time)
# print("Current frame = ", sim.current_frame)

# input("Press Enter to drive forward for 2 seconds")

# # The simulator can be run for a set amount of time. time_limit is optional and if omitted or set to 0, then the simulator will run indefinitely
# sim.run(time_limit = 2.0)

# print("Current time = ", sim.current_time)
# print("Current frame = ", sim.current_frame)

# input("Press Enter to continue driving for 2 seconds")

# sim.run(time_limit = 2.0)

# print("Current time = ", sim.current_time)
# print("Current frame = ", sim.current_frame)