import unittest
import random

import matplotlib.pyplot as plt
import networkx as nx

from tests.test_factory import TestFactory

from route_flow.road_network import RoadNetwork

__author__ = 'syadlowsky'

class TestRoadNetwork(unittest.TestCase):
    def setUp(self):
        from route_flow.origin import Origin

        network = nx.fast_gnp_random_graph(20, 0.1, directed=True)
        shortest_paths = nx.all_pairs_shortest_path_length(network)

        origins = set()
        od_pairs = []
        for r in shortest_paths:
            origins.add(r)
            for s in shortest_paths[r]:
                origins.add(s)
                od_pairs.append((Origin(r, r), Origin(s, s)))
        self.origins = list(origins)

        _, od_demand_dictionary = \
            TestFactory.create_od_demand_dictionary_from_connected_pairs(
                origins=self.origins, connected_pairs=od_pairs)
        _, _, self.od_demand = TestFactory.create_od_demand(origins,
                                                         od_demand_dictionary)

        self.subject = RoadNetwork(network, self.od_demand)

    def test_has_network(self):
        self.assertTrue(self.subject.network)

    def test_los_angeles(self):
        subject = RoadNetwork.los_angeles(2)
        self.assertTrue(subject)

    def test_los_angeles_origins_are_objects(self):
        from route_flow.origin import Origin
        subject = RoadNetwork.los_angeles(2)
        self.assertIsInstance(subject.od_demand.origins[0], Origin)

    def test_los_angeles_nodes_have_pos(self):
        subject = RoadNetwork.los_angeles(2)
        for node in subject.network.nodes():
            self.assertIn('pos', subject.network.node[node],
                          msg="Node (%s) doesn't have 'pos' value: %s" %
                          (node, subject.network.node[node]))

if __name__ == '__main__':
    unittest.main()
