import random

class TestFactory(object):
    @classmethod
    def create_origins(self):

        from route_flow.origin import Origin
        origins = []

        for i in xrange(5):
            vertices = [random.randint(1, 10),
                        random.randint(10, 20),
                        random.randint(20, 30)]
            origin = Origin(i, vertices)
            origins.append(origin)

        return origins

    @classmethod
    def create_od_demand_dictionary(self, origins=None):
        if origins is None:
            origins = self.create_origins()

        od_demand = {}
        for r in origins:
            od_demand[r] = {}
            for s in origins:
                od_demand[r][s] = (r, s, random.uniform(0, 100))

        return (origins, od_demand)

    @classmethod
    def create_od_demand(self, origins=None, od_demand_dictionary=None):
        from route_flow.od_demand import ODDemand

        if origins is None:
            origins = self.create_origins()

        if od_demand_dictionary is None:
            _, od_demand_dictionary = self.create_od_demand_dictionary(origins)

        return (origins, od_demand_dictionary,
                ODDemand(od_demand_dictionary))
