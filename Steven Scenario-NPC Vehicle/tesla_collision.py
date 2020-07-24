#!/usr/bin/env python3
#
# Copyright (c) 2019 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import os
import lgsvl

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "BorregasAve":
  sim.reset()
else:
  sim.load("BorregasAve")

spawns = sim.get_spawn()

sx = spawns[0].position.x
sz = spawns[0].position.z
ry = spawns[0].rotation.y

forward = lgsvl.utils.transform_to_forward(spawns[0])
right = lgsvl.utils.transform_to_right(spawns[0])

# ego vehicle
state = lgsvl.AgentState()
state.transform = spawns[0]
state.velocity = 3 * forward
ego = sim.add_agent("Lincoln2017MKZ (Apollo 5.0)", lgsvl.AgentType.EGO, state)


# school bus, 20m ahead, perpendicular to road, stopped
state = lgsvl.AgentState()
state.transform.position = spawns[0].position + 40.0 * forward
state.transform.rotation.y = spawns[0].rotation.y + 270.0
state.transform.rotation.z = spawns[0].rotation.z + 90.0
#state.transform.rotation.x = spawns[0].rotation.x + 90.0
bus = sim.add_agent("SchoolBus", lgsvl.AgentType.NPC, state)

vehicles = {
  ego: "EGO",
  bus: "SchoolBus",
}

def on_collision(agent1, agent2, contact):
  name1 = vehicles[agent1]
  print("{} collided with at {}".format(name1, contact))

# The above on_collision function needs to be added to the callback list of each vehicle
ego.on_collision(on_collision)
bus.on_collision(on_collision)

input("Press Enter to run")

sim.run()